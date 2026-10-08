"""Read STL without hiding defects; inspect geometry and render the exported mesh."""
from __future__ import annotations

from itertools import permutations
from pathlib import Path
import struct

import numpy as np
import trimesh

BUILD_VOLUME = np.array([256.0, 256.0, 256.0])


def load_stl(path: Path) -> trimesh.Trimesh:
    """Accept strict binary/ASCII STL, preserving degenerate and duplicate facets.

    Vertex merging rounds to 5 decimal places (mm) solely to reconstruct topology.
    No faces are removed, normals repaired, holes filled, or model units changed.
    """
    raw = path.read_bytes()
    if len(raw) >= 84 and 84 + 50 * struct.unpack_from("<I", raw, 80)[0] == len(raw):
        dtype = np.dtype([("normal", "<f4", (3,)), ("vertices", "<f4", (3, 3)),
                          ("attribute", "<u2")])
        triangles = np.frombuffer(raw, dtype=dtype, offset=84)["vertices"].astype(float)
    else:
        try:
            lines = [line.strip().split() for line in raw.decode("ascii").splitlines()
                     if line.strip()]
        except UnicodeDecodeError as exc:
            raise ValueError("Malformed/truncated binary STL or non-ASCII STL") from exc
        if not lines or lines[0][0].lower() != "solid" or lines[-1][0].lower() != "endsolid":
            raise ValueError("Malformed STL: binary length mismatch or missing ASCII solid markers")
        triangles_list = []
        index = 1
        while index < len(lines) - 1:
            block = lines[index:index + 7]
            if (len(block) != 7 or len(block[0]) != 5 or block[0][:2] != ["facet", "normal"]
                    or block[1] != ["outer", "loop"] or block[5] != ["endloop"]
                    or block[6] != ["endfacet"]
                    or any(len(line) != 4 or line[0] != "vertex" for line in block[2:5])):
                raise ValueError(f"Malformed ASCII STL near facet {len(triangles_list) + 1}")
            triangles_list.append([[float(v) for v in line[1:]] for line in block[2:5]])
            index += 7
        triangles = np.asarray(triangles_list, dtype=float).reshape((-1, 3, 3))
    if not len(triangles):
        raise ValueError("STL contains no triangles")
    if not np.isfinite(triangles).all():
        raise ValueError("STL contains NaN or infinite vertex coordinates")
    mesh = trimesh.Trimesh(vertices=triangles.reshape((-1, 3)),
                           faces=np.arange(len(triangles) * 3).reshape((-1, 3)),
                           process=False)
    mesh.merge_vertices(digits_vertex=5)
    return mesh


def surface_metrics(mesh: trimesh.Trimesh, angle: float = 45, bed_tolerance: float = 0.02) -> dict:
    """Local face-angle heuristic; does not prove bridge/overhang printability."""
    if not 0 < angle < 90 or bed_tolerance <= 0:
        raise ValueError("Overhang angle must be between 0 and 90; bed tolerance must be positive")
    bed_z = float(mesh.bounds[0, 2])
    on_bed = mesh.triangles[:, :, 2].max(axis=1) <= bed_z + bed_tolerance
    down = mesh.face_normals[:, 2] < -np.sin(np.deg2rad(angle)) - 1e-8
    risky = down & ~on_bed
    return {"overhang_angle_from_vertical_deg": angle,
            "candidate_overhang_area_mm2": float(mesh.area_faces[risky].sum()),
            "candidate_overhang_faces": int(risky.sum()),
            "bed_contact_area_mm2": float(mesh.area_faces[on_bed].sum()),
            "bed_reference_z_mm": bed_z}


def inspect_mesh(mesh: trimesh.Trimesh, *, path: Path | None = None, bed_margin: float = 2,
                 angle: float = 45, expected_shells: int | None = None) -> dict:
    if not 0 <= bed_margin < 128:
        raise ValueError("Bed margin must be >= 0 and < 128 mm per XY edge")
    if expected_shells is not None and expected_shells < 1:
        raise ValueError("Expected shell count must be positive")
    corners = mesh.triangles
    areas = np.linalg.norm(np.cross(corners[:, 1] - corners[:, 0],
                                   corners[:, 2] - corners[:, 0]), axis=1) / 2
    degenerate = int((areas <= 1e-12).sum())
    canonical = np.sort(mesh.faces, axis=1)
    duplicate = len(canonical) - len(np.unique(canonical, axis=0))
    edges = np.sort(mesh.edges, axis=1)
    unique_edges, counts = np.unique(edges, axis=0, return_counts=True)
    boundary = int((counts == 1).sum())
    nonmanifold = int((counts > 2).sum())
    components = trimesh.graph.connected_components(mesh.face_adjacency,
                                                    nodes=np.arange(len(mesh.faces)))
    shells = []
    # Edge-adjacency components which meet only at a point reveal pinched vertices.
    vertex_memberships = np.zeros(len(mesh.vertices), dtype=int)
    for component in components:
        face_ids = np.asarray(component, dtype=int)
        vertex_ids = np.unique(mesh.faces[face_ids])
        vertex_memberships[vertex_ids] += 1
        tris = corners[face_ids]
        shifted = tris - mesh.bounds[0]  # more stable signed volume for translated models
        signed_volume = np.einsum("ij,ij->i", shifted[:, 0],
                                   np.cross(shifted[:, 1], shifted[:, 2])).sum() / 6
        shells.append({"faces": len(face_ids), "signed_volume_mm3": float(signed_volume),
                       "min_z_mm": float(tris[:, :, 2].min())})
    pinched = int((vertex_memberships > 1).sum())
    extents = mesh.extents
    fit = bool(np.all(extents <= BUILD_VOLUME + 1e-5))
    usable = BUILD_VOLUME - [2 * bed_margin, 2 * bed_margin, 0]
    fits_margin = bool(np.all(extents <= usable + 1e-5))
    axis_options = [{"xyz_from_axes": "".join("XYZ"[i] for i in order),
                     "dimensions_mm": extents[list(order)].tolist()}
                    for order in permutations(range(3))
                    if np.all(extents[list(order)] <= usable + 1e-5)]
    metrics = surface_metrics(mesh, angle)
    volume = float(sum(shell["signed_volume_mm3"] for shell in shells))
    errors, warnings = [], []
    for condition, message in (
        (boundary > 0, f"{boundary} boundary edges: mesh is open"),
        (nonmanifold > 0, f"{nonmanifold} edges shared by more than two faces"),
        (pinched > 0, f"{pinched} vertices shared between separate surface shells"),
        (degenerate > 0, f"{degenerate} degenerate triangles"),
        (duplicate > 0, f"{duplicate} duplicate triangles"),
        (not mesh.is_winding_consistent, "Face winding is inconsistent"),
        (volume <= 0, "Total signed volume is zero or negative"),
        (not fit, "Bounding dimensions exceed the A1 build volume in this orientation"),
        (expected_shells is not None and len(shells) != expected_shells,
         f"Expected {expected_shells} surface shells, found {len(shells)}"),
    ):
        if condition:
            errors.append(message)
    if len(shells) > 1:
        warnings.append("Multiple surface shells: check intentional parts/cavities in the slicer")
    if any(shell["signed_volume_mm3"] < 0 for shell in shells):
        warnings.append("Negative-volume shells may be cavity surfaces; verify containment and winding")
    if not fits_margin and fit:
        warnings.append(f"Fits nominal A1 volume but not {bed_margin:g} mm XY margin per edge")
    if abs(float(mesh.bounds[0, 2])) > 0.02:
        warnings.append("Model base is not at Z=0; translate onto the plate before printing")
    if metrics["candidate_overhang_faces"]:
        warnings.append("Downward overhang candidates detected; inspect bridges and layer support")
    if metrics["bed_contact_area_mm2"] < 1:
        warnings.append("Little planar bed contact; consider reorientation or a brim")
    return {"file": str(path.resolve()) if path else None, "units_assumed": "mm",
            "passed": not errors, "errors": errors, "warnings": warnings,
            "triangles": len(mesh.faces), "vertices": len(mesh.vertices),
            "bounds_mm": mesh.bounds.tolist(), "dimensions_mm": extents.tolist(),
            "surface_area_mm2": float(areas.sum()), "signed_volume_mm3": volume,
            "watertight": bool(mesh.is_watertight),
            "winding_consistent": bool(mesh.is_winding_consistent),
            "boundary_edges": boundary, "nonmanifold_edges": nonmanifold,
            "pinched_vertices_between_shells": pinched,
            "degenerate_triangles": degenerate, "duplicate_triangles": duplicate,
            "surface_shell_count": len(shells), "surface_shells": shells,
            "a1_build_volume_mm": BUILD_VOLUME.tolist(), "fits_a1_current_orientation": fit,
            "bed_margin_per_xy_edge_mm": bed_margin, "fits_with_margin": fits_margin,
            "axis_permutations_fitting_margin": axis_options, **metrics,
            "limitations": ["STL is unitless; dimensions are interpreted as millimeters",
                            "Self-intersections, overlapping shells and local wall thickness are not tested",
                            "Shells count connected surfaces, not necessarily separate physical parts",
                            "Overhang areas are advisory, not a support or bridge simulation"]}


def orientation_candidates(mesh: trimesh.Trimesh, angle: float = 45, bed_margin: float = 2) -> list[dict]:
    rotations = {"original_Z_up": np.eye(4),
                 "Z_down": trimesh.transformations.rotation_matrix(np.pi, [1, 0, 0]),
                 "Y_up": trimesh.transformations.rotation_matrix(np.pi / 2, [1, 0, 0]),
                 "Y_down": trimesh.transformations.rotation_matrix(-np.pi / 2, [1, 0, 0]),
                 "X_up": trimesh.transformations.rotation_matrix(-np.pi / 2, [0, 1, 0]),
                 "X_down": trimesh.transformations.rotation_matrix(np.pi / 2, [0, 1, 0])}
    if not 0 <= bed_margin < 128:
        raise ValueError("Bed margin must be >= 0 and < 128 mm")
    result = []
    for name, transform in rotations.items():
        candidate = mesh.copy()
        candidate.apply_transform(transform)
        metrics = surface_metrics(candidate, angle)
        usable = BUILD_VOLUME - [2 * bed_margin, 2 * bed_margin, 0]
        result.append({"orientation": name, "rotation_matrix": transform.tolist(),
                       "dimensions_mm": candidate.extents.tolist(),
                       "fits_with_margin": bool(np.all(candidate.extents <= usable + 1e-5)),
                       **metrics})
    return sorted(result, key=lambda r: (not r["fits_with_margin"],
                                        r["candidate_overhang_area_mm2"],
                                        -r["bed_contact_area_mm2"], r["dimensions_mm"][2]))


def render_mesh(mesh: trimesh.Trimesh, output: Path, *, view: str = "iso",
                size: tuple[int, int] = (1200, 900), highlight_overhangs: bool = False,
                angle: float = 45, max_faces: int = 200_000) -> None:
    if min(size) <= 0:
        raise ValueError("Image dimensions must be positive")
    if len(mesh.faces) > max_faces:
        raise ValueError(f"{len(mesh.faces)} faces exceed --max-faces {max_faces}; "
                         "raise the limit or use the OpenSCAD rendering backend")
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d.art3d import Poly3DCollection

    camera = {"iso": (25, -55), "top": (90, -90), "front": (0, -90), "right": (0, 0)}
    if view not in camera:
        raise ValueError(f"Unknown view {view}")
    light = np.array([0.3, -0.5, 0.8])
    light /= np.linalg.norm(light)
    shade = 0.5 + 0.5 * np.maximum(0, mesh.face_normals @ light)
    colors = shade[:, None] * np.array([0.25, 0.62, 0.82])
    if highlight_overhangs:
        surface_metrics(mesh, angle)  # validates the requested threshold
        on_bed = mesh.triangles[:, :, 2].max(axis=1) <= mesh.bounds[0, 2] + 0.02
        risk = (mesh.face_normals[:, 2] < -np.sin(np.deg2rad(angle)) - 1e-8) & ~on_bed
        colors[risk] = [0.95, 0.25, 0.12]
    fig = plt.figure(figsize=(size[0] / 100, size[1] / 100), dpi=100)
    try:
        ax = fig.add_subplot(111, projection="3d")
        ax.add_collection3d(Poly3DCollection(mesh.triangles, facecolors=colors,
                                             edgecolors="none", linewidths=0))
        center = mesh.bounds.mean(axis=0)
        half = max(float(mesh.extents.max()), 0.1) * 0.58
        ax.set_xlim(center[0] - half, center[0] + half)
        ax.set_ylim(center[1] - half, center[1] + half)
        ax.set_zlim(center[2] - half, center[2] + half)
        ax.set_box_aspect([1, 1, 1])
        ax.set_proj_type("ortho")
        ax.view_init(*camera[view])
        ax.set_axis_off()
        ax.set_title(" × ".join(f"{v:.2f}" for v in mesh.extents) + " mm", fontsize=12)
        fig.subplots_adjust(left=0, right=1, bottom=0, top=0.94)
        output.parent.mkdir(parents=True, exist_ok=True)
        fig.savefig(output, dpi=100, facecolor="white")
    finally:
        plt.close(fig)

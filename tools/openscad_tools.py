#!/usr/bin/env python3
"""Reusable OpenSCAD/A1 tools. Run `python tools/openscad_tools.py --help`."""
from __future__ import annotations

import argparse
import hashlib
import importlib.metadata
import json
import os
from pathlib import Path
import re
import sys

from scad_runtime import BOSL2, DOCS, ROOT, export_scad, find_openscad, openscad_version


def write_json(path: Path | None, data: object) -> None:
    if path:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(data, indent=2, allow_nan=False) + "\n", encoding="utf-8")


def digest(path: Path) -> str:
    with path.open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest()


def show_check(report: dict) -> None:
    print(f"{'PASS' if report['passed'] else 'FAIL'}: {report['file']}")
    print("Dimensions (mm): " + " x ".join(f"{x:.3f}" for x in report["dimensions_mm"]))
    print(f"{report['triangles']:,} triangles; {report['surface_shell_count']} surface shells; "
          f"volume {report['signed_volume_mm3']:.2f} mm³")
    print(f"Overhang candidate area: {report['candidate_overhang_area_mm2']:.2f} mm²; "
          f"bed contact: {report['bed_contact_area_mm2']:.2f} mm²")
    for kind in ("errors", "warnings"):
        for message in report[kind]:
            print(f"{kind.upper()}: {message}")
    print("Advisory: self-intersections and wall thickness are not tested; inspect slicer layers.")


def mesh_report(args, path: Path) -> tuple[object, dict]:
    from mesh_tools import inspect_mesh, load_stl
    mesh = load_stl(path)
    return mesh, inspect_mesh(mesh, path=path, bed_margin=args.bed_margin,
                              angle=args.overhang_angle, expected_shells=args.expected_shells)


def doctor(args) -> int:
    versions = {}
    for name in ("numpy", "trimesh", "matplotlib", "Pillow"):
        try:
            versions[name] = importlib.metadata.version(name)
        except importlib.metadata.PackageNotFoundError:
            versions[name] = None
    data = {"python": sys.executable, "python_version": sys.version.split()[0],
            "packages": versions, "workspace": str(ROOT),
            "manual_exists": (DOCS / "OpenSCAD_User_Manual.md").is_file(),
            "bosl2_library_exists": (BOSL2 / "std.scad").is_file(),
            "bosl2_wiki_exists": (DOCS / "BOSL2-2.0.766-Wiki" / "Home.md").is_file()}
    try:
        executable = find_openscad(args.openscad)
        data.update(openscad=str(executable), openscad_version=openscad_version(executable))
    except (FileNotFoundError, RuntimeError, OSError) as exc:
        data["openscad_error"] = str(exc)
    print(json.dumps(data, indent=2))
    return int("openscad_error" in data or not all(versions.values()) or
               not data["manual_exists"] or not data["bosl2_library_exists"] or
               not data["bosl2_wiki_exists"])


def new_project(args) -> int:
    name = args.name.removeprefix("01_")
    if not re.fullmatch(r"[a-z][a-z0-9_-]*", name):
        raise ValueError("Project name must start with a lowercase letter and use a-z, 0-9, _ or -")
    parent = args.directory.resolve()
    directory = parent / f"01_{name}"
    entries = list(parent.iterdir()) if parent.exists() else []
    reserved = {entry.name.casefold() for entry in entries}
    if directory.name.casefold() in reserved or name.casefold() in reserved:
        raise FileExistsError(f"Project already exists; reuse its folder instead of creating it: {name}")
    reserved.add(directory.name.casefold())
    renames = []
    for previous in sorted(entries):
        if not previous.is_dir() or not previous.name.startswith("01_"):
            continue
        # Never move a junction/symlink target or anything outside this project parent.
        if previous.resolve().parent != parent:
            raise ValueError(f"Cannot rename a linked project outside {parent}: {previous}")
        base = previous.name
        while base.startswith("01_"):
            base = base[3:]
        if base in ("", ".", ".."):
            base = "archived_project"
        candidate, suffix = base, 2
        while candidate.casefold() in reserved:
            candidate = f"{base}_{suffix}"
            suffix += 1
        destination = parent / candidate
        if destination.resolve().parent != parent:
            raise ValueError(f"Rename destination must remain inside {parent}")
        reserved.add(candidate.casefold())
        renames.append((previous, destination))
    template_name = "clearance_coupon.scad" if args.template == "clearance" else (
        "bosl2_model.scad" if args.bosl2 else "model.scad")
    source = (ROOT / "tools" / "templates" / template_name).read_text(encoding="utf-8")
    source_path = directory / f"{name}.scad"
    readme_path = directory / "README.md"
    try:
        tool_path = Path(os.path.relpath(ROOT / "tools" / "openscad_tools.py", directory)).as_posix()
    except ValueError:
        tool_path = (ROOT / "tools" / "openscad_tools.py").as_posix()
    readme = (
        f"# {name}\n\nStatus: scaffold; replace the sample geometry before final delivery.\n\n"
        "Units: mm. Target: Bambu Lab A1; assumed 0.4 mm nozzle and 0.20 mm layers.\n"
        "Print orientation: as modeled, Z up and base at Z=0.\n"
        "Supports: design for none; review final slicer layers.\n\n"
        "Build from this project's folder (the command also works after removing its 01_ prefix):\n\n"
        f'```powershell\npython "{tool_path}" build "{name}.scad"\n```\n\n'
        "Keep all project-specific sources, exports, images and reports in this folder.\n"
        "Record final dimensions, material, tolerances, part exports and assembly instructions here.\n")
    completed_renames = []
    created = False
    try:
        for previous, destination in renames:
            previous.rename(destination)
            completed_renames.append((previous, destination))
        directory.mkdir(parents=True)
        created = True
        source_path.write_text(source, encoding="utf-8")
        readme_path.write_text(readme, encoding="utf-8")
    except Exception:
        for previous, destination in reversed(completed_renames):
            destination.rename(previous)
        if created:
            source_path.unlink(missing_ok=True)
            readme_path.unlink(missing_ok=True)
            directory.rmdir()
        raise
    for previous, destination in completed_renames:
        print(f"Previous working project: {previous.name} -> {destination.name}")
    print(f"Created {directory}; run build after completing the model to produce STL and PNG.")
    return 0


def export_command(args) -> int:
    output = args.output or args.source.with_suffix(".stl")
    if output.suffix.lower() != ".stl":
        raise ValueError("export requires an .stl output")
    result = export_scad(args.source, output, executable=find_openscad(args.openscad),
                         definitions=args.define, timeout=args.timeout,
                         allow_warnings=args.allow_warnings)
    print(json.dumps(result, indent=2))
    return 0


def render_command(args) -> int:
    from mesh_tools import load_stl, render_mesh
    output = args.output or args.source.with_suffix(".png")
    if output.suffix.lower() != ".png":
        raise ValueError("render requires a .png output")
    if args.backend == "openscad":
        export_scad(args.source, output, executable=find_openscad(args.openscad),
                    definitions=args.define, timeout=args.timeout, image_size=tuple(args.size),
                    allow_warnings=args.allow_warnings)
    else:
        if args.source.suffix.lower() != ".stl":
            raise ValueError("Mesh renderer requires STL; use --backend openscad for SCAD")
        render_mesh(load_stl(args.source), output, view=args.view, size=tuple(args.size),
                    highlight_overhangs=args.highlight_overhangs, angle=args.overhang_angle,
                    max_faces=args.max_faces)
    print(f"Rendered {output.resolve()}")
    return 0


def check_command(args) -> int:
    _, report = mesh_report(args, args.stl)
    write_json(args.json, report)
    show_check(report)
    return int(not report["passed"])


def build_command(args) -> int:
    output = (args.output_dir or args.source.resolve().parent).resolve()
    stem = args.source.stem
    stl, png = output / f"{stem}.stl", output / f"{stem}.png"
    # Invalidate the previous success manifest before any new build begins.
    manifest_path = output / f"{stem}.build.json"
    manifest = {"status": "building", "source": str(args.source.resolve()),
                "definitions": args.define, "bosl2_version": "2.0.766"}
    write_json(manifest_path, manifest)
    try:
        from mesh_tools import render_mesh
        executable = find_openscad(args.openscad)
        manifest.update(source_sha256=digest(args.source), openscad_version=openscad_version(executable))
        manifest["export"] = export_scad(args.source, stl, executable=executable,
                                          definitions=args.define, timeout=args.timeout,
                                          allow_warnings=args.allow_warnings)
        mesh, report = mesh_report(args, stl)
        write_json(output / f"{stem}.validation.json", report)
        if args.backend == "openscad":
            # Render the final STL, so PNG and mesh are always the same geometry.
            import tempfile
            with tempfile.TemporaryDirectory(prefix="scad-render-") as temp:
                wrapper = Path(temp) / "render.scad"
                wrapper.write_text(f"import({json.dumps(stl.as_posix())});\n", encoding="utf-8")
                export_scad(wrapper, png, executable=executable, timeout=args.timeout,
                            image_size=tuple(args.size), allow_warnings=args.allow_warnings)
        else:
            render_mesh(mesh, png, view=args.view, size=tuple(args.size),
                        highlight_overhangs=args.highlight_overhangs,
                        angle=args.overhang_angle, max_faces=args.max_faces)
        manifest.update(status="passed" if report["passed"] else "failed_validation",
                        stl_sha256=digest(stl), png_sha256=digest(png),
                        stl=str(stl), png=str(png), validation=str(output / f"{stem}.validation.json"))
        write_json(manifest_path, manifest)
        show_check(report)
        print(f"STL: {stl}\nPNG: {png}\nManifest: {manifest_path}")
        return int(not report["passed"])
    except Exception as exc:
        manifest.update(status="failed", error=str(exc))
        write_json(manifest_path, manifest)
        raise


def orient_command(args) -> int:
    from mesh_tools import load_stl, orientation_candidates
    result = orientation_candidates(load_stl(args.stl), args.overhang_angle, args.bed_margin)
    write_json(args.json, result)
    print("Six axis-aligned candidates; lower overhang area is a heuristic, not proof of printability.")
    for entry in result:
        print(f"{entry['orientation']:15} fit={entry['fits_with_margin']} "
              f"overhang={entry['candidate_overhang_area_mm2']:.2f} mm² "
              f"contact={entry['bed_contact_area_mm2']:.2f} mm²")
    print("No files were rotated. Apply the chosen rotation to the SCAD source, then rebuild.")
    return 0


def compare_command(args) -> int:
    from mesh_tools import load_stl
    import numpy as np
    if args.dimension_tolerance < 0 or args.volume_percent < 0:
        raise ValueError("Comparison tolerances must be nonnegative")
    old, new = load_stl(args.old), load_stl(args.new)
    change = new.extents - old.extents
    volume_change = abs(float(new.volume - old.volume)) / max(abs(float(old.volume)), 1e-12) * 100
    result = {"old": str(args.old.resolve()), "new": str(args.new.resolve()),
              "old_dimensions_mm": old.extents.tolist(), "new_dimensions_mm": new.extents.tolist(),
              "dimension_change_mm": change.tolist(), "volume_change_percent": volume_change,
              "dimension_tolerance_mm": args.dimension_tolerance,
              "volume_tolerance_percent": args.volume_percent,
              "within_summary_tolerances": bool(np.all(abs(change) <= args.dimension_tolerance)
                                                 and volume_change <= args.volume_percent),
              "limitations": "Compares dimensions/volume only; equal summaries do not imply equal shapes"}
    write_json(args.json, result)
    print(json.dumps(result, indent=2))
    return int(not result["within_summary_tolerances"])


def audit_command(args) -> int:
    if not args.directory.is_dir():
        raise ValueError(f"Project directory not found: {args.directory}")
    results = []
    excluded = {"tmp", ".git", "__pycache__", "SourceDocs"}
    for project in sorted(p for p in args.directory.iterdir() if p.is_dir() and not p.name.startswith(".")):
        files = [p for p in project.rglob("*") if p.is_file() and
                 not (set(p.relative_to(project).parts[:-1]) & excluded)]
        artifacts = {ext: [str(p.relative_to(project)) for p in files if p.suffix.lower() == ext]
                     for ext in (".scad", ".stl", ".png")}
        missing = [ext for ext, values in artifacts.items() if not values]
        entry = {"project": str(project.resolve()), "artifacts": artifacts, "missing": missing}
        if args.validate:
            from mesh_tools import inspect_mesh, load_stl
            from PIL import Image
            entry["stl_checks"] = []
            entry["png_errors"] = []
            for name in artifacts[".stl"]:
                try:
                    entry["stl_checks"].append(inspect_mesh(load_stl(project / name), path=project / name))
                except (ValueError, OSError) as exc:
                    entry["stl_checks"].append({"file": name, "passed": False, "errors": [str(exc)]})
            for name in artifacts[".png"]:
                try:
                    with Image.open(project / name) as img:
                        if img.format != "PNG":
                            raise ValueError("File is not PNG")
                        img.verify()
                except (OSError, ValueError) as exc:
                    entry["png_errors"].append({"file": name, "error": str(exc)})
        entry["passed"] = (not missing and not entry.get("png_errors") and
                           all(r["passed"] for r in entry.get("stl_checks", [])))
        results.append(entry)
        print(f"{'PASS' if entry['passed'] else 'FAIL'} {project.name}: "
              + ("missing " + ", ".join(missing) if missing else "SCAD/STL/PNG present")
              + ("; mesh/image validation performed" if args.validate else ""))
    write_json(args.json, results)
    if not results:
        print("No project subdirectories found.")
    return int(any(not entry["passed"] for entry in results))


def docs_command(args) -> int:
    paths = []
    if args.scope in ("all", "openscad"):
        paths.append(DOCS / "OpenSCAD_User_Manual.md")
    if args.scope in ("all", "bosl2"):
        paths.extend(sorted((DOCS / "BOSL2-2.0.766-Wiki").glob("*.md")))
    if args.scope in ("all", "source"):
        paths.extend(sorted(BOSL2.glob("*.scad")))
    if args.limit < 1:
        raise ValueError("Search limit must be positive")
    needle = args.query.casefold()
    matches = 0
    for path in paths:
        with path.open(encoding="utf-8-sig", errors="replace") as stream:
            for line_no, line in enumerate(stream, 1):
                if needle in line.casefold():
                    print(f"{path.relative_to(ROOT)}:{line_no}: {line.rstrip()[:500]}")
                    matches += 1
                    if matches >= args.limit:
                        return 0
    if not matches:
        print("No matches in local documentation.")
    return int(matches == 0)


def add_scad_flags(parser):
    parser.add_argument("--openscad", help="Executable path; otherwise OPENSCAD_EXE/PATH/Windows install")
    parser.add_argument("-D", "--define", action="append", default=[], metavar="NAME=VALUE",
                        help="Repeat for each OpenSCAD parameter; values use SCAD syntax")
    parser.add_argument("--timeout", type=float, default=300)
    parser.add_argument("--allow-warnings", action="store_true", help="Explicitly permit OpenSCAD warnings")


def add_check_flags(parser):
    parser.add_argument("--bed-margin", type=float, default=2, help="mm reserved per XY edge")
    parser.add_argument("--overhang-angle", type=float, default=45, help="degrees from vertical")
    parser.add_argument("--expected-shells", type=int, help="Require this connected SURFACE count")


def add_render_flags(parser):
    parser.add_argument("--backend", choices=("mesh", "openscad"), default="mesh")
    parser.add_argument("--view", choices=("iso", "top", "front", "right"), default="iso",
                        help="Mesh backend camera")
    parser.add_argument("--size", type=int, nargs=2, default=(1200, 900), metavar=("WIDTH", "HEIGHT"))
    parser.add_argument("--highlight-overhangs", action="store_true", help="Mesh backend: mark candidates red")
    parser.add_argument("--max-faces", type=int, default=200_000, help="Mesh backend resource guard")


def make_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    p = commands.add_parser("doctor", help="Check OpenSCAD, Python packages and local docs")
    p.add_argument("--openscad")
    p.set_defaults(func=doctor)
    p = commands.add_parser("new", help="Create the 01_ working project and unprefix previous folders")
    p.add_argument("name")
    p.add_argument("--directory", type=Path, default=ROOT / "projects")
    p.add_argument("--bosl2", action="store_true")
    p.add_argument("--template", choices=("model", "clearance"), default="model")
    p.set_defaults(func=new_project)
    p = commands.add_parser("export", help="Compile SCAD to binary STL, with captured logs")
    p.add_argument("source", type=Path)
    p.add_argument("-o", "--output", type=Path)
    add_scad_flags(p)
    p.set_defaults(func=export_command)
    p = commands.add_parser("render", help="Render STL to PNG, or SCAD via --backend openscad")
    p.add_argument("source", type=Path)
    p.add_argument("-o", "--output", type=Path)
    add_scad_flags(p)
    add_render_flags(p)
    p.add_argument("--overhang-angle", type=float, default=45)
    p.set_defaults(func=render_command)
    p = commands.add_parser("check", help="Check STL topology, volume, A1 fit and overhang candidates")
    p.add_argument("stl", type=Path)
    p.add_argument("--json", type=Path)
    add_check_flags(p)
    p.set_defaults(func=check_command)
    p = commands.add_parser("build", help="Export STL, validate, render PNG and record hashes")
    p.add_argument("source", type=Path)
    p.add_argument("--output-dir", type=Path)
    add_scad_flags(p)
    add_check_flags(p)
    add_render_flags(p)
    p.set_defaults(func=build_command)
    p = commands.add_parser("orient", help="Compare six orientations without modifying the model")
    p.add_argument("stl", type=Path)
    p.add_argument("--json", type=Path)
    p.add_argument("--bed-margin", type=float, default=2)
    p.add_argument("--overhang-angle", type=float, default=45)
    p.set_defaults(func=orient_command)
    p = commands.add_parser("compare", help="Compare dimensions and volume for mesh revisions")
    p.add_argument("old", type=Path)
    p.add_argument("new", type=Path)
    p.add_argument("--dimension-tolerance", type=float, default=0.1)
    p.add_argument("--volume-percent", type=float, default=1)
    p.add_argument("--json", type=Path)
    p.set_defaults(func=compare_command)
    p = commands.add_parser("audit", help="Read-only SCAD/STL/PNG inventory for existing projects")
    p.add_argument("directory", nargs="?", type=Path, default=ROOT / "projects")
    p.add_argument("--validate", action="store_true", help="Also check every STL and decode every PNG")
    p.add_argument("--json", type=Path)
    p.set_defaults(func=audit_command)
    p = commands.add_parser("docs", help="Search local OpenSCAD manual, BOSL2 wiki and source")
    p.add_argument("query")
    p.add_argument("--scope", choices=("all", "openscad", "bosl2", "source"), default="all")
    p.add_argument("--limit", type=int, default=20)
    p.set_defaults(func=docs_command)
    return parser


def main() -> int:
    parser = make_parser()
    args = parser.parse_args()
    try:
        return args.func(args)
    except ImportError as exc:
        print(f"Missing dependency: {exc}. Run python -m pip install -r tools/requirements.txt", file=sys.stderr)
        return 2
    except (OSError, ValueError, RuntimeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    # Windows redirected streams otherwise use a legacy code page. Keep paths,
    # units and documentation snippets readable for calling tools and scripts.
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    raise SystemExit(main())

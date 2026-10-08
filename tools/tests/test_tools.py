"""Geometry, CLI and real OpenSCAD regression tests; all mutations stay in temp dirs."""
from __future__ import annotations

import json
from pathlib import Path
import struct
import subprocess
import sys
import tempfile
import unittest
from unittest import mock

TOOLS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS))

import numpy as np
from PIL import Image
import trimesh

from mesh_tools import inspect_mesh, load_stl, orientation_candidates, render_mesh
from scad_runtime import export_scad, find_openscad, openscad_version


class MeshTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="openscad-tests-")
        self.directory = Path(self.temp.name)
        self.box = trimesh.creation.box(extents=[20, 30, 10])
        self.box.apply_translation([0, 0, 5])

    def tearDown(self):
        self.temp.cleanup()

    def save(self, mesh=None, filename="model.stl"):
        path = self.directory / filename
        path.write_bytes(trimesh.exchange.stl.export_stl(self.box if mesh is None else mesh))
        return path

    def test_valid_binary_and_ascii_have_same_dimensions(self):
        binary = self.save()
        ascii_path = self.directory / "ascii.stl"
        ascii_path.write_text(trimesh.exchange.stl.export_stl_ascii(self.box), encoding="ascii")
        for path in (binary, ascii_path):
            mesh = load_stl(path)
            report = inspect_mesh(mesh, path=path, expected_shells=1)
            self.assertTrue(report["passed"], report["errors"])
            np.testing.assert_allclose(report["dimensions_mm"], [20, 30, 10])
            self.assertAlmostEqual(report["signed_volume_mm3"], 6000)
            self.assertAlmostEqual(report["candidate_overhang_area_mm2"], 0)
            self.assertAlmostEqual(report["bed_contact_area_mm2"], 600)

    def test_binary_solid_header_is_not_misread_as_ascii(self):
        path = self.save()
        raw = bytearray(path.read_bytes())
        raw[:5] = b"solid"
        path.write_bytes(raw)
        self.assertEqual(len(load_stl(path).faces), 12)

    def test_truncated_binary_and_ascii_rejected(self):
        path = self.save()
        path.write_bytes(path.read_bytes()[:-1])
        with self.assertRaises(ValueError):
            load_stl(path)
        path.write_text("solid x\nfacet normal 0 0 1\nouter loop\nvertex 0 0 0\nendsolid x\n")
        with self.assertRaises(ValueError):
            load_stl(path)

    def test_empty_and_nonfinite_mesh_rejected(self):
        path = self.directory / "bad.stl"
        path.write_bytes(bytes(80) + struct.pack("<I", 0))
        with self.assertRaises(ValueError):
            load_stl(path)
        path = self.save()
        raw = bytearray(path.read_bytes())
        struct.pack_into("<f", raw, 96, float("nan"))
        path.write_bytes(raw)
        with self.assertRaises(ValueError):
            load_stl(path)

    def test_open_mesh_fails(self):
        mesh = trimesh.Trimesh(self.box.vertices, self.box.faces[:-1], process=False)
        report = inspect_mesh(mesh)
        self.assertFalse(report["passed"])
        self.assertEqual(report["boundary_edges"], 3)

    def test_duplicate_faces_preserved_and_detected(self):
        mesh = trimesh.Trimesh(self.box.vertices,
                               np.vstack([self.box.faces, self.box.faces[0]]), process=False)
        loaded = load_stl(self.save(mesh))
        report = inspect_mesh(loaded)
        self.assertEqual(len(loaded.faces), 13)
        self.assertEqual(report["duplicate_triangles"], 1)
        self.assertGreater(report["nonmanifold_edges"], 0)
        self.assertFalse(report["passed"])

    def test_degenerate_triangle_not_silently_removed(self):
        mesh = trimesh.Trimesh(self.box.vertices,
                               np.vstack([self.box.faces, [0, 0, 1]]), process=False)
        loaded = load_stl(self.save(mesh))
        self.assertEqual(len(loaded.faces), 13)
        self.assertEqual(inspect_mesh(loaded)["degenerate_triangles"], 1)

    def test_flipped_face_and_inverted_volume_fail(self):
        mesh = self.box.copy()
        mesh.faces[0] = mesh.faces[0][::-1]
        self.assertFalse(inspect_mesh(mesh)["winding_consistent"])
        mesh = self.box.copy()
        mesh.invert()
        report = inspect_mesh(mesh)
        self.assertFalse(report["passed"])
        self.assertLess(report["signed_volume_mm3"], 0)

    def test_legitimate_closed_cavity_can_pass(self):
        inner = trimesh.creation.box(extents=[10, 10, 4])
        inner.apply_translation([0, 0, 5])
        inner.invert()
        mesh = trimesh.util.concatenate([self.box, inner])
        report = inspect_mesh(mesh, expected_shells=2)
        self.assertTrue(report["passed"], report["errors"])
        self.assertEqual(report["surface_shell_count"], 2)
        self.assertAlmostEqual(report["signed_volume_mm3"], 5600)

    def test_point_contact_between_shells_fails(self):
        other = self.box.copy()
        other.apply_translation([20, 30, 10])
        mesh = load_stl(self.save(trimesh.util.concatenate([self.box, other])))
        report = inspect_mesh(mesh)
        self.assertGreater(report["pinched_vertices_between_shells"], 0)
        self.assertFalse(report["passed"])

    def test_a1_fit_margin_and_oversize(self):
        report = inspect_mesh(trimesh.creation.box(extents=[254, 30, 10]))
        self.assertTrue(report["passed"])
        self.assertTrue(report["fits_a1_current_orientation"])
        self.assertFalse(report["fits_with_margin"])
        report = inspect_mesh(trimesh.creation.box(extents=[257, 30, 10]))
        self.assertFalse(report["passed"])

    def test_expected_shells_mismatch_fails(self):
        self.assertFalse(inspect_mesh(self.box, expected_shells=2)["passed"])

    def test_six_rotations_preserve_geometry(self):
        original = self.box.vertices.copy()
        result = orientation_candidates(self.box)
        self.assertEqual(len(result), 6)
        for candidate in result:
            self.assertEqual(sorted(round(v, 5) for v in candidate["dimensions_mm"]), [10, 20, 30])
            self.assertAlmostEqual(candidate["candidate_overhang_area_mm2"], 0)
            rotation = np.array(candidate["rotation_matrix"])
            self.assertAlmostEqual(np.linalg.det(rotation[:3, :3]), 1)
        np.testing.assert_equal(self.box.vertices, original)

    def test_suspended_ceiling_is_overhang_candidate(self):
        floating = trimesh.creation.box(extents=[30, 30, 3])
        floating.apply_translation([0, 0, 20])
        mesh = trimesh.util.concatenate([self.box, floating])
        report = inspect_mesh(mesh)
        self.assertGreaterEqual(report["candidate_overhang_area_mm2"], 900)

    def test_render_creates_nonblank_png_at_requested_size(self):
        path = self.directory / "model.png"
        render_mesh(self.box, path, size=(640, 480))
        with Image.open(path) as image:
            self.assertEqual(image.size, (640, 480))
            self.assertGreater(float(np.asarray(image).std()), 5)

    def test_invalid_parameters_rejected(self):
        with self.assertRaises(ValueError):
            inspect_mesh(self.box, bed_margin=128)
        with self.assertRaises(ValueError):
            orientation_candidates(self.box, angle=90)
        with self.assertRaises(ValueError):
            render_mesh(self.box, self.directory / "out.png", max_faces=1)


class CLIFixture(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="openscad-cli-tests-")
        self.directory = Path(self.temp.name)

    def tearDown(self):
        self.temp.cleanup()

    def cli(self, *args):
        return subprocess.run([sys.executable, str(TOOLS / "openscad_tools.py"), *map(str, args)],
                              capture_output=True, text=True, encoding="utf-8", timeout=120)


class CLITests(CLIFixture):
    def test_scaffold_and_refuse_overwrite(self):
        result = self.cli("new", "sample", "--directory", self.directory, "--bosl2")
        self.assertEqual(result.returncode, 0, result.stderr)
        source = self.directory / "01_sample" / "sample.scad"
        original = source.read_bytes()
        result = self.cli("new", "sample", "--directory", self.directory)
        self.assertEqual(result.returncode, 2)
        self.assertEqual(source.read_bytes(), original)

    def test_switch_project_preserves_files_and_avoids_rename_collision(self):
        previous = self.directory / "01_old"
        previous.mkdir()
        (previous / "model.stl").write_bytes(b"old model sentinel")
        existing = self.directory / "old"
        existing.mkdir()
        (existing / "keep.txt").write_text("existing project sentinel")
        other_previous = self.directory / "01_second"
        other_previous.mkdir()
        (other_previous / "notes.txt").write_text("second project sentinel")
        result = self.cli("new", "current", "--directory", self.directory)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual((self.directory / "old_2" / "model.stl").read_bytes(), b"old model sentinel")
        self.assertEqual((existing / "keep.txt").read_text(), "existing project sentinel")
        self.assertEqual((self.directory / "second" / "notes.txt").read_text(), "second project sentinel")
        prefixed = [p.name for p in self.directory.iterdir() if p.is_dir() and p.name.startswith("01_")]
        self.assertEqual(prefixed, ["01_current"])

    def test_existing_unprefixed_project_refused_without_switching(self):
        (self.directory / "old").mkdir()
        (self.directory / "01_current").mkdir()
        result = self.cli("new", "old", "--directory", self.directory)
        self.assertEqual(result.returncode, 2, result.stderr)
        self.assertTrue((self.directory / "01_current").is_dir())
        self.assertFalse((self.directory / "01_old").exists())

    def test_prefixed_name_is_not_double_prefixed(self):
        result = self.cli("new", "01_sample", "--directory", self.directory)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertTrue((self.directory / "01_sample" / "sample.scad").is_file())
        self.assertFalse((self.directory / "01_01_sample").exists())

    def test_failed_scaffold_restores_previous_folder(self):
        import openscad_tools
        previous = self.directory / "01_old"
        previous.mkdir()
        (previous / "keep.txt").write_text("preserve me")
        args = openscad_tools.make_parser().parse_args(
            ["new", "current", "--directory", str(self.directory)])
        with mock.patch.object(Path, "write_text", side_effect=OSError("simulated write failure")):
            with self.assertRaisesRegex(OSError, "simulated write failure"):
                openscad_tools.new_project(args)
        self.assertEqual((previous / "keep.txt").read_text(), "preserve me")
        self.assertFalse((self.directory / "old").exists())
        self.assertFalse((self.directory / "01_current").exists())

    def test_check_failure_returns_nonzero_and_json(self):
        box = trimesh.creation.box()
        path = self.directory / "open.stl"
        path.write_bytes(trimesh.exchange.stl.export_stl(
            trimesh.Trimesh(box.vertices, box.faces[:-1], process=False)))
        output = self.directory / "report.json"
        result = self.cli("check", path, "--json", output)
        self.assertEqual(result.returncode, 1, result.stderr)
        self.assertFalse(json.loads(output.read_text())["passed"])

    def test_documentation_search(self):
        result = self.cli("docs", "cuboid(", "--scope", "bosl2", "--limit", 2)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(len(result.stdout.splitlines()), 2)

    def test_audit_reports_missing_deliverables(self):
        directory = self.directory / "unfinished"
        directory.mkdir()
        (directory / "unfinished.scad").write_text("cube(10);")
        report = self.directory / "audit.json"
        result = self.cli("audit", self.directory, "--json", report)
        self.assertEqual(result.returncode, 1, result.stderr)
        data = json.loads(report.read_text())
        self.assertEqual(data[0]["missing"], [".stl", ".png"])

    def test_missing_executable_invalidates_old_success_manifest(self):
        source = self.directory / "part.scad"
        source.write_text("cube(10);")
        manifest = source.with_suffix(".build.json")
        manifest.write_text('{"status":"passed"}')
        result = self.cli("build", source, "--openscad", self.directory / "missing.exe")
        self.assertEqual(result.returncode, 2, result.stderr)
        self.assertEqual(json.loads(manifest.read_text())["status"], "failed")


class RuntimeTests(unittest.TestCase):
    def test_version_timeout_is_actionable_runtime_error(self):
        with mock.patch("scad_runtime.subprocess.run",
                        side_effect=subprocess.TimeoutExpired(["openscad", "--version"], 20)):
            with self.assertRaisesRegex(RuntimeError, "version query timed out"):
                openscad_version(Path("openscad"))


class OpenSCADIntegration(CLIFixture):
    @classmethod
    def setUpClass(cls):
        try:
            cls.executable = find_openscad()
        except FileNotFoundError:
            raise unittest.SkipTest("OpenSCAD is not installed")

    def test_native_and_bosl2_build_create_three_artifacts(self):
        for name in ("model.scad", "bosl2_model.scad"):
            directory = self.directory / name.replace(".scad", "")
            directory.mkdir()
            source = directory / "sample.scad"
            source.write_bytes((TOOLS / "templates" / name).read_bytes())
            result = self.cli("build", source, "-D", "width=42", "--size", 640, 480)
            self.assertEqual(result.returncode, 0, result.stderr + result.stdout)
            self.assertTrue(source.is_file())
            stl, png = source.with_suffix(".stl"), source.with_suffix(".png")
            self.assertTrue(stl.is_file() and png.is_file())
            np.testing.assert_allclose(load_stl(stl).extents, [42, 30, 8], atol=0.02)
            report = json.loads(source.with_suffix(".validation.json").read_text())
            self.assertTrue(report["passed"])
            self.assertEqual(report["candidate_overhang_faces"], 0)
            manifest = json.loads(source.with_suffix(".build.json").read_text())
            self.assertEqual(manifest["status"], "passed")

    def test_compile_failure_preserves_old_mesh_and_invalidates_manifest(self):
        source, output = self.directory / "broken.scad", self.directory / "broken.stl"
        output.write_bytes(b"old mesh sentinel")
        manifest = self.directory / "broken.build.json"
        manifest.write_text('{"status":"passed"}')
        source.write_text("this is invalid OpenSCAD !")
        result = self.cli("build", source)
        self.assertEqual(result.returncode, 2, result.stderr)
        self.assertEqual(output.read_bytes(), b"old mesh sentinel")
        self.assertEqual(json.loads(manifest.read_text())["status"], "failed")
        self.assertTrue(output.with_suffix(".stl.openscad.log").is_file())

    def test_missing_include_fails_instead_of_exporting_partial_geometry(self):
        source, output = self.directory / "missing.scad", self.directory / "missing.stl"
        source.write_text("include <no_such_library_abc.scad>\ncube(10);\n")
        with self.assertRaises(RuntimeError):
            export_scad(source, output, executable=self.executable)
        self.assertFalse(output.exists())

    def test_clearance_coupon_build(self):
        source = self.directory / "coupon.scad"
        source.write_bytes((TOOLS / "templates" / "clearance_coupon.scad").read_bytes())
        result = self.cli("build", source, "--size", 640, 480)
        self.assertEqual(result.returncode, 0, result.stderr + result.stdout)
        report = json.loads(source.with_suffix(".validation.json").read_text())
        self.assertEqual(report["surface_shell_count"], 4)
        self.assertEqual(report["candidate_overhang_faces"], 0)

    def test_openscad_backend_build_renders_final_stl(self):
        source = self.directory / "render.scad"
        source.write_text("width=20; cube([width,15,5]);")
        result = self.cli("build", source, "--backend", "openscad", "-D", "width=25",
                          "--size", 640, 480)
        self.assertEqual(result.returncode, 0, result.stderr + result.stdout)
        np.testing.assert_allclose(load_stl(source.with_suffix(".stl")).extents, [25, 15, 5])
        with Image.open(source.with_suffix(".png")) as img:
            self.assertEqual(img.size, (640, 480))
            self.assertGreater(float(np.asarray(img).std()), 5)


if __name__ == "__main__":
    unittest.main()

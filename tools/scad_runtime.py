"""OpenSCAD discovery and atomic CLI exports. No shell or global configuration changes."""
from __future__ import annotations

import os
from pathlib import Path
import re
import shutil
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
BOSL2 = DOCS / "BOSL2-2.0.766"


def find_openscad(explicit: str | None = None) -> Path:
    """Prefer the Windows console executable so logs and exit codes are captured."""
    requested = explicit or os.environ.get("OPENSCAD_EXE")
    if requested:
        found = shutil.which(requested) or requested
        path = Path(found).expanduser().resolve()
        if not path.is_file():
            raise FileNotFoundError(f"OpenSCAD executable not found: {path}")
        return path
    candidates = [shutil.which(name) for name in ("openscad.com", "openscad", "openscad.exe")]
    if os.name == "nt":
        candidates += [str(Path(os.environ.get(env, default)) / "OpenSCAD" / name)
                       for env, default in (("ProgramFiles", "C:/Program Files"),
                                            ("ProgramFiles(x86)", "C:/Program Files (x86)"))
                       for name in ("openscad.com", "openscad.exe")]
    for candidate in candidates:
        if candidate and Path(candidate).is_file():
            return Path(candidate).resolve()
    raise FileNotFoundError("Install OpenSCAD or pass --openscad PATH / set OPENSCAD_EXE.")


def scad_environment() -> dict[str, str]:
    env = os.environ.copy()
    env["OPENSCADPATH"] = str(DOCS) + (os.pathsep + env["OPENSCADPATH"]
                                      if env.get("OPENSCADPATH") else "")
    return env


def openscad_version(executable: Path) -> str:
    try:
        result = subprocess.run([str(executable), "--version"], capture_output=True,
                                text=True, errors="replace", timeout=20, env=scad_environment())
    except subprocess.TimeoutExpired as exc:
        raise RuntimeError("OpenSCAD version query timed out after 20 seconds") from exc
    if result.returncode:
        raise RuntimeError(result.stderr or result.stdout or "OpenSCAD version query failed")
    return (result.stdout + result.stderr).strip()


def export_scad(source: Path, output: Path, *, executable: Path,
                definitions: list[str] | None = None, timeout: float = 300,
                image_size: tuple[int, int] = (1200, 900),
                allow_warnings: bool = False) -> dict:
    source, output = source.resolve(), output.resolve()
    if not source.is_file() or source.suffix.lower() != ".scad":
        raise ValueError(f"Expected an existing .scad source: {source}")
    if output.suffix.lower() not in (".stl", ".png"):
        raise ValueError("OpenSCAD export output must be .stl or .png")
    if timeout <= 0 or min(image_size) <= 0:
        raise ValueError("Timeout and image dimensions must be positive")
    for definition in definitions or []:
        if not re.fullmatch(r"[A-Za-z_$][A-Za-z0-9_$]*=.+", definition, re.DOTALL):
            raise ValueError(f"Use -D NAME=SCAD_EXPRESSION, got {definition!r}")
    output.parent.mkdir(parents=True, exist_ok=True)
    handle, tmp_name = tempfile.mkstemp(prefix=".openscad-", suffix=output.suffix,
                                        dir=output.parent)
    os.close(handle)
    tmp = Path(tmp_name)
    args = [str(executable), "-o", str(tmp)]
    if not allow_warnings:
        args += ["--hardwarnings"]
    if output.suffix.lower() == ".stl":
        args += ["--export-format", "binstl"]
    else:
        args += ["--render", "--autocenter", "--viewall", "--projection=o",
                 f"--imgsize={image_size[0]},{image_size[1]}", "--colorscheme=Tomorrow"]
    for definition in definitions or []:
        args += ["-D", definition]
    args.append(str(source))
    log = output.with_suffix(output.suffix + ".openscad.log")
    try:
        result = subprocess.run(args, cwd=source.parent, env=scad_environment(),
                                capture_output=True, text=True, errors="replace",
                                timeout=timeout)
        transcript = result.stdout + result.stderr
        log.write_text(transcript, encoding="utf-8")
        # Some OpenSCAD versions emit an ERROR while still returning zero.
        if result.returncode or re.search(r"^\s*ERROR:", transcript, re.MULTILINE):
            raise RuntimeError(f"OpenSCAD export failed; see {log}\n{transcript[-2000:]}")
        if not tmp.is_file() or tmp.stat().st_size == 0:
            raise RuntimeError(f"OpenSCAD produced no geometry; see {log}")
        tmp.replace(output)
        return {"source": str(source), "output": str(output), "definitions": definitions or [],
                "openscad": str(executable), "log": str(log), "bytes": output.stat().st_size}
    except subprocess.TimeoutExpired as exc:
        log.write_text(f"Export timed out after {timeout} seconds.\n" +
                       str(exc.stdout or "") + str(exc.stderr or ""), encoding="utf-8")
        raise RuntimeError(f"OpenSCAD timed out; see {log}") from exc
    finally:
        tmp.unlink(missing_ok=True)

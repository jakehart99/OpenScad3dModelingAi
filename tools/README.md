# Reusable OpenSCAD printing tools

Run commands from `C:\Users\jakeh\Documents\OpenSCAD_AI`. The scripts also resolve
the workspace/library location from their own paths, so they can be invoked
using an absolute script path from another working directory.

```powershell
python -m pip install -r tools/requirements.txt
python tools/openscad_tools.py doctor
python tools/openscad_tools.py --help
```

Requires Python 3.11+, OpenSCAD 2021.01+ for compilation, and the packages in
`requirements.txt` for mesh work. `new`, `docs`, and basic `audit` do not need
mesh packages. No slicer or GPU is required. OpenSCAD detection uses an explicit
`--openscad` path, `OPENSCAD_EXE`, PATH, then usual Windows installation paths.
On Windows it prefers `openscad.com` for synchronous command-line logs.

`scad_runtime.py` handles executable discovery, subprocess configuration and
exports. `mesh_tools.py` handles STL reading, inspection, orientation analysis
and mesh rendering. `openscad_tools.py` supplies the command-line workflow.
`templates/` contains plain OpenSCAD, BOSL2 and clearance-coupon starters.

## Start and build a project

```powershell
python tools/openscad_tools.py new bracket --bosl2
# Replace the starter geometry with the desired design.
python tools/openscad_tools.py build projects/01_bracket/bracket.scad
```

`build` creates `<stem>.stl`, `<stem>.png`, `<stem>.validation.json`,
`<stem>.build.json`, and `<stem>.stl.openscad.log` beside the source. The manifest
records SCAD/STL/PNG SHA-256 hashes, OpenSCAD version, local BOSL2 version and
parameter overrides. The hash covers the main source only; included-file changes
are not automatically tracked. Always rebuild after changing any dependency.
`--output-dir PATH` changes the artifact directory. Keep the required source and
final artifacts together for delivery. The manifest is invalidated on a new build
and records failed builds, so old output files are not mistaken for new success.

`new bracket` creates `projects/01_bracket/`. Only the current working project
has the `01_` prefix. When starting a new project, the tool removes this prefix
from older working folders and preserves their contents. If the destination
name already exists, it adds a numeric suffix (`bracket_2`, etc.) instead of
overwriting or merging folders. Renames stay inside the selected project parent.
An existing prefixed or unprefixed project with the requested name is refused;
reuse/rename that folder when continuing it. `new 01_bracket` also accepts an
already prefixed name without adding the prefix twice. `--directory PATH` uses
the same convention in that parent folder. Generated project README build commands
run from inside the project and remain valid after the folder's prefix is removed.
All project-specific files belong inside the project folder; keep final exports
easy to find and separate reference assets or temporary work into subfolders.

Both a native and a pinned BOSL2 sample can be used. The tools set `OPENSCADPATH`
to the local `docs/` folder **only for the child process**; the versioned include is:

```openscad
include <BOSL2-2.0.766/std.scad>
```

See [AGENTS.md](../AGENTS.md) for GUI setup, BOSL2 selection and print design rules.
`examples/bosl2_plate/` contains a working source plus its exported STL, mesh PNG,
OpenSCAD PNG, validation report and build manifest for reference.

## Individual commands

```powershell
# Export final evaluated geometry; parameters are OpenSCAD expressions.
python tools/openscad_tools.py export projects/01_bracket/bracket.scad -D 'height=12'
python tools/openscad_tools.py export projects/01_bracket/bracket.scad -D 'part="base"' -o projects/01_bracket/base.stl

# Preserve the mesh while inspecting it.
python tools/openscad_tools.py check projects/01_bracket/base.stl --json projects/01_bracket/base.validation.json
python tools/openscad_tools.py check projects/01_bracket/base.stl --bed-margin 5 --expected-shells 1

# Render actual exported facets; no decimation or invented geometry.
python tools/openscad_tools.py render projects/01_bracket/base.stl -o projects/01_bracket/base.png
python tools/openscad_tools.py render projects/01_bracket/base.stl --view front --size 1600 1200 -o projects/01_bracket/base_front.png
python tools/openscad_tools.py render projects/01_bracket/base.stl --highlight-overhangs -o projects/01_bracket/base_overhangs.png

# OpenSCAD's own fully evaluated PNG renderer requires OpenGL availability.
python tools/openscad_tools.py render projects/01_bracket/bracket.scad --backend openscad -o projects/01_bracket/scad_view.png
python tools/openscad_tools.py build projects/01_bracket/bracket.scad --backend openscad

# Rank six rotations, then apply the chosen rotation in SCAD and rebuild.
python tools/openscad_tools.py orient projects/01_bracket/base.stl --json projects/01_bracket/orientations.json

# Summary comparison only; does not establish equal shape.
python tools/openscad_tools.py compare projects/01_bracket/base_old.stl projects/01_bracket/base.stl --dimension-tolerance 0.1 --volume-percent 1

# Inventory existing project folders without modifying their contents.
python tools/openscad_tools.py audit
python tools/openscad_tools.py audit --validate --json tools/project_audit.json

# Literal, case-insensitive search of the local documentation/source.
python tools/openscad_tools.py docs "path_sweep(" --scope bosl2 --limit 10
python tools/openscad_tools.py docs "OPENSCADPATH" --scope openscad
python tools/openscad_tools.py docs "module threaded_rod" --scope source
```

`render` defaults to a 1200 × 900 PNG. Mesh views: `iso`, `top`, `front`, `right`.
The mesh renderer uses a CPU Matplotlib backend and works without an OpenGL
window. It refuses meshes larger than 200,000 faces by default to bound resource
use; raise `--max-faces` or use the OpenSCAD backend for larger models. It never
silently drops faces. `--view` and `--highlight-overhangs` affect the mesh backend.
An OpenSCAD-backed `build` renders an imported final STL to keep artifacts matched.

Exports use argument lists rather than shell commands, temporary output files,
a 300-second configurable `--timeout`, and warning failures by default.
Successful export replaces the target; compile failure leaves an existing target
unchanged and writes a log. Use `--allow-warnings` only after understanding the
warning. Exports do not imply mesh verification; use `check` or `build`.

## Fit-test coupon

```powershell
python tools/openscad_tools.py new fit_coupon --template clearance
python tools/openscad_tools.py build projects/01_fit_coupon/fit_coupon.scad
```

The coupon has a through-hole bar and separate pegs with small flat bases.
Default peg diameter: 6 mm. Default **radial** clearances: 0.15, 0.25, 0.35 mm,
giving hole diameters 6.30, 6.50, 6.70 mm. Labels show radial clearance.
Edit `clearances` and the dimensions, or pass `-D 'clearances=[0.1,0.2,0.3]'`.
Use `-D 'part="holes"'` or `-D 'part="pegs"'` with separate output names to export
components individually. Print with the target material/profile and transfer
the observed fit to the functional design. This is a fit test, not automatic
dimensional compensation for every feature.

## Checks, meaning, and limitations

STL reading accepts ASCII and binary, including binary headers starting with
`solid`. It rejects empty, malformed/truncated and nonfinite-coordinate meshes.
Topology reconstruction merges vertex positions rounded to 5 decimal places
(0.00001 mm grid); it preserves faces. Reports include dimensions/bounds,
triangle count, area, signed volume, winding, boundary/non-manifold edges,
duplicate/degenerate triangles and connected surface shells. Point contacts
between otherwise separate shells are flagged. No repairs are applied.

The A1 fit test uses 256 mm in each axis. A configurable XY margin defaults
to 2 mm per edge. Exceeding the nominal envelope fails; fitting the envelope
without the requested margin produces a warning. The plate can be translated
in the slicer; the report warns when the source base is not Z=0.

Multiple surfaces are not necessarily multiple physical parts: a fully enclosed
cavity creates an inward-facing surface shell. Negative shell volumes are
reported for review, while total volume must be positive. `--expected-shells`
means **connected surface shells**. Cavity containment is not verified.

Overhang candidates are downward faces exceeding a configurable angle **from
vertical** (45° default), excluding faces at the lowest bed plane. This does not
trace support below a face, analyze layers, distinguish bridges from ceilings,
or account for cooling/material. Zero candidates does not guarantee support-free
printing. Orientation ranking only considers six axis-aligned directions and
does not weigh load direction, cosmetic requirements or per-part orientations.

**Self-intersections, overlapping solids, local wall thickness, full vertex-link
manifoldness and slicer toolpaths are not tested.** Preview the actual PNG and
review slicing before calling a design print-ready. Equal volume/dimensions in
`compare` can describe different shapes.

`audit` groups immediate project subdirectories and finds required extensions
recursively, excluding `tmp`, `.git`, `__pycache__`, and `SourceDocs` folders.
It checks presence, not source-to-mesh provenance or whether an image depicts
the correct model. `--validate` adds STL checks and PNG decoding, but visual
review and a current build are still required.

Exit codes: **0** success; **1** failed validation, missing deliverables,
comparison outside tolerances, unavailable doctor requirements or no search
matches; **2** invalid invocation, compile failure, malformed input or runtime
error. Advisory warnings alone do not fail mesh checks. Inspect JSON for details.

## Verify the toolkit

```powershell
python -m unittest discover -s tools/tests -v
```

Tests use temporary directories and generated meshes. OpenSCAD integration
checks are skipped if no executable is available; they check native and pinned
BOSL2 exports, matched PNGs, coupon generation, and compile failure behavior.
No existing project models are rewritten.

# OpenSCAD models for the Bambu Lab A1

## Purpose and required deliverables

In this directory, create editable, parametric **OpenSCAD 3D models optimized for
3D printing on a Bambu Lab A1**. Prefer designs that print **without supports**.
Use supports only when geometry, function, or surface quality makes them
absolutely necessary after considering orientation, chamfers, bridges, or
splitting the model into separately printable parts. Explain any necessary
supports and identify the affected regions.

Start every requested model or project by creating its project folder inside
`projects/`, before creating any project files. Name the working folder
`projects/01_<project_name>/`, using a clear, descriptive project name. Every completed project
must contain at least these **three real, nonempty files**:

1. One or more `.scad` files containing the editable 3D model.
2. One or more `.stl` files exported from that model, ready for slicing.
3. One or more `.png` images showing the actual final model clearly.

The three file types are a minimum, not a limit. Use matching stems where
possible, for example `bracket.scad`, `bracket.stl`, and `bracket.png`.
For assemblies, retain a master SCAD file, export every separately printable
part as its own STL, and provide a useful assembly image as well as part views
when needed. A `.3mf`, `.blend`, render of unrelated geometry, screenshot of code,
or placeholder file does not replace a required file. A new scaffold is unfinished
until its model is designed and its STL and PNG are generated and checked.

Add a short project `README.md` documenting dimensions, material assumptions,
nozzle/layer settings, bed orientation, supports (normally none), fit clearances,
part selection parameters, build commands, and assembly instructions as relevant.
Regenerate STL and PNG after every final geometry change. Preserve existing
projects and documentation unless the current task calls for changing them.

## Project folders and the working-project prefix

Use **`01_` as a prefix at the beginning of the working project's folder name**
(for example, `projects/01_tablet_stand/`) so it sorts near the top. Only the
project currently being worked on may have this prefix.

When starting a different project, inspect the immediate folders in `projects/`
and remove the leading `01_` from every other project's folder name. For example,
rename `01_tablet_stand` to `tablet_stand` before creating `01_cable_holder`.
Preserve each renamed folder and all its contents. If the unprefixed destination
already exists, choose a distinct name such as `tablet_stand_2`; never overwrite,
delete, or merge an existing project to remove the prefix. After switching, verify
that exactly one project folder has `01_`, belonging to the current project.

When continuing an existing project, reuse its folder and add the `01_` prefix
if needed, removing the prefix from any other project folders. Do not create a
duplicate project or add the prefix twice. Keep the current folder prefixed until
work switches to another project.

Keep **all project-specific files inside that project's folder**: SCAD sources,
STLs, PNGs, README, validation reports, build logs, reference assets and assembly
files. Keep filenames descriptive and the folder organized. Use subfolders such
as `references/`, `renders/`, or `tmp/` when helpful; remove disposable temporary
files after verification and make the final SCAD/STL/PNG deliverables easy to find.
Shared reusable tools belong in `tools/`, and shared documentation belongs in
`docs/`. Update paths in project instructions or source files when a folder rename
affects them.

The `new` tool creates `projects/01_<name>/` and removes `01_` from previous
working-project folders, preserving their files and avoiding name collisions.
For an existing project, rename/reuse its folder instead of running `new` again.

## Printer and design conventions

- Use **millimeters** throughout. STL is unitless; the tools and slicer must
  interpret coordinates as mm.
- The A1 has a nominal **256 × 256 × 256 mm** build volume and an included
  **0.4 mm nozzle**, according to [Bambu Lab's A1 specifications](https://bambulab.com/en/a1/tech-specs).
  Do not confuse it with the A1 mini. Unless the user specifies otherwise, assume
  a 0.4 mm nozzle and use 0.20 mm layers as a working design assumption.
- Fit the model in its intended print orientation. Reserve space for brims and
  other slicer features; the tools use a configurable 2 mm margin per XY edge
  as an initial check. Nominal volume fit alone does not establish plate layout
  or sequential-print clearance.
- Put the intended bottom at **Z=0**, with positive Z above the bed. Provide
  adequate planar bed contact. Orient for layer strength and functional load,
  as well as low support use. Consider a brim for a small footprint or tall part.
- Prefer vertical walls, flat bases, bottom chamfers, self-supporting tapers,
  and teardrop/diamond profiles for horizontal holes when appropriate.
  Avoid broad unsupported ceilings, floating islands, and inaccessible supports.
  Inspect any proposed bridges in the actual slicer profile. A 45° overhang
  threshold measured from vertical is a conservative starting heuristic, not
  a universal printer or material guarantee.
- Make wall thickness, clearance, hole sizes and critical dimensions explicit
  parameters. As initial design choices for a 0.4 mm nozzle, consider roughly
  1.2–1.6 mm walls for ordinary parts, thicker walls/ribs for loads, and clearances
  calibrated with a coupon. These are design starting points, not machine specs.
  Match final thicknesses to the slicer's actual extrusion widths.
- Distinguish **radial/per-side clearance** from **diametral/total clearance**.
  For a shaft of diameter D and radial clearance C, its hole diameter is D+2*C.
  Calibrate fits for material, orientation, and actual printer/slicer settings.
- Keep models manifold and closed. Avoid zero-thickness walls, coplanar cutters,
  edge/point-only unions, duplicate solids and accidental disconnected pieces.
  Extend boolean cutters slightly past their target and overlap joined solids
  by a small deliberate epsilon. Do not silently repair an STL instead of
  correcting the SCAD source.
- Use named parameters, reusable modules, and `assert()` for invalid dimensions.
  Separate printable parts from assembly/exploded views with a `part` or `mode`
  parameter. Use `$fa`/`$fs` or an appropriate `$fn` to balance smooth surfaces
  with mesh size; distinguish `$preview` quality from final export quality.

## Local OpenSCAD documentation

The complete local OpenSCAD manual is:

`C:\Users\jakeh\Documents\OpenSCAD_AI\docs\OpenSCAD_User_Manual.md`

Use this Markdown manual as the primary OpenSCAD reference. It covers the
language, geometry, transformations, booleans, extrusion, import/export,
rendering, CLI usage, and library paths. Related images are in
`docs/OpenSCAD_User_Manual_assets/`. Search the relevant sections rather than
guessing syntax. Some sections describe historical versions; compare CLI flags
with the installed executable's `--help` and version reported by `doctor`.
Full STL export evaluates geometry; an F5/OpenCSG preview alone is insufficient.
Use full evaluation (`--render`) when rendering PNGs through OpenSCAD.

```powershell
python tools/openscad_tools.py docs "linear_extrude" --scope openscad
python tools/openscad_tools.py doctor
```

## Local BOSL2 library and wiki: what they are

- **`docs/BOSL2-2.0.766/` is executable library source**, the Belfry OpenSCAD
  Library v2, pinned here to **2.0.766** (confirmed in `version.scad`). It contains
  `.scad` implementations, `README.md`, `examples/`, `tests/`, and development
  scripts. It extends OpenSCAD with shapes, attachment-based positioning,
  rounding/chamfers, paths/regions, sweeps, math, and mechanical parts. Its README
  requires OpenSCAD **2021.01 or later** and describes BOSL2 as beta; BOSL v1 code
  is not interchangeable with BOSL2. Preserve the pinned source tree.
- **`docs/BOSL2-2.0.766-Wiki/` is its local Markdown documentation**, not another
  library to include. Start with `Home.md`, `Tutorials.md`, `CheatSheet.md`,
  `TOC.md` (file index), `AlphaIndex.md` (symbol index), and `Topics.md`.
  Individual API pages such as `shapes3d.scad.md` and `threading.scad.md` document
  signatures, argument conventions, examples and limitations. The
  `Tutorial-*.md` pages teach usage; `images/` contains supporting illustrations.
  Cross-check wiki examples against the pinned source when anything disagrees.

Use native OpenSCAD primitives and booleans when they express a simple model
clearly. Use BOSL2 when it reduces custom geometry code, improves positioning,
or provides a tested shape or mechanical feature needed by the design.

| Need | Useful BOSL2 files / local wiki pages |
| --- | --- |
| Rounded/chamfered boxes, cylinders, tubes, prisms | `shapes3d.scad`; `Tutorial-Shapes3d.md`, `Tutorial-Rounding_the_Cube.md` |
| Position parts relative to faces, edges or anchors | `attachments.scad`; `Tutorial-Attachment-Overview.md`, positioning/attach/align tutorials |
| Subtract attached children, edge masks/profiles | `attachments.scad`, `masks.scad`; attachment tags and edge profiling tutorials |
| Repeated features and readable transformations | `distributors.scad`, `transforms.scad`; their tutorials |
| Rounded outlines, extrusions and filleted connections | `rounding.scad`, `paths.scad`, `regions.scad`; rounding API and paths tutorial |
| Loft cross-sections or sweep a profile along a path | `skin.scad`, `beziers.scad`, `vnf.scad`; skinning and VNF tutorials |
| Generic or standardized threads, screws, nut pockets | `threading.scad`, `screws.scad`, `screw_drive.scad` |
| Dovetails, clips, hinges, separately printed connections | `joiners.scad`, `hinges.scad`, `sliders.scad`, `partitions.scad` |
| Cross-braced walls or lightweight structural panels | `walls.scad` (`sparse_wall`, `sparse_cuboid`, `hex_panel`); `cubetruss.scad` |
| Gears/racks/worms or bottle interfaces | `gears.scad`, `bottlecaps.scad` |

BOSL2 features do not automatically make a design support-free or a fit accurate.
For example, rounding a bottom edge can reduce bed contact or introduce an
overhang; rounding only vertical edges preserves a flat base. Printed threads,
clips and hinges need appropriate wall thickness, clearance and test prints.
For lightweight supports and frames, consult `walls.scad.md`: its cross-braced
wall tools expose parameters such as `maxang` and `max_bridge` to control
overhangs and bridge lengths. Choose these for the actual print orientation and
material; the library's default bridge length is not a tested A1 capability.

### Includes and library resolution

The shared Python tools prepend this workspace's `docs/` to **the OpenSCAD child
process's** `OPENSCADPATH`. This supports a version-specific include without
copying, renaming, or modifying the bundled library:

```openscad
include <BOSL2-2.0.766/std.scad>
// Add only the specialty files actually required:
// include <BOSL2-2.0.766/threading.scad>
// include <BOSL2-2.0.766/screws.scad>
// include <BOSL2-2.0.766/gears.scad>
// include <BOSL2-2.0.766/walls.scad>

$fa = $preview ? 8 : 3;
$fs = $preview ? 1 : 0.35;
cuboid([40, 30, 8], rounding=3, edges="Z", anchor=BOTTOM);
```

`std.scad` already includes the common geometry, attachment, transform,
distribution, path, region, rounding, skin and math modules. Specialty parts
such as screws, threads, gears, joiners and hinges need their documented extra
includes. Use **`include`**, rather than substituting `use`, so BOSL2 constants,
configuration and dependencies are initialized.

Wiki examples often say `include <BOSL2/std.scad>` because their installation
uses a folder named `BOSL2`. This workspace's folder has a versioned name; adapt
those include paths. For the GUI, launch OpenSCAD from PowerShell with the same
library root (adjust executable path if necessary):

```powershell
$env:OPENSCADPATH = (Resolve-Path docs).Path + [IO.Path]::PathSeparator + $env:OPENSCADPATH
& 'C:\Program Files\OpenSCAD\openscad.exe' 'projects\my_part\my_part.scad'
```

Alternatively, a source directly inside `projects/01_<name>/` can use
`include <../../docs/BOSL2-2.0.766/std.scad>`; adjust relative depth if relocated.
Do not assume the Python tool's process environment also configures an already
running GUI.

### Attachment rules worth remembering

- BOSL2 shapes support `anchor`, `spin`, and `orient`; they apply in that order.
  `cuboid()` is centered by default; use `anchor=BOTTOM` for a bed-aligned part.
- `position()` places children relative to a parent's anchors; `attach()` can
  also align a child's anchor and orientation. Look up its exact arguments.
- `diff()`/`tag()` support subtractive geometry within attachment hierarchies.
  Tags inherit through children; explicitly manage tags when nesting parts.
- Native extrusions, imported meshes and other non-attachable objects require
  the documented attachable alternative, `attachable()` wrapper, or
  `force_tag()` for tagged operations as appropriate. Do not assume every native
  module supports BOSL2 attachments. Consult the local tutorials and source.

```powershell
python tools/openscad_tools.py docs "cuboid(" --scope bosl2
python tools/openscad_tools.py docs "threaded_rod" --scope source
```

## Shared Python tools and completion workflow

**Always inspect `tools/README.md` and reuse the Python tools in `tools/`** for
OpenSCAD exports, STL verification, model images and other repeatable work.
Extend these tools when a generally useful capability is missing; avoid copying
project-specific mesh-check scripts into each new project. Keep changes
documented and test meaningful geometry/failure cases when tool behavior changes.

The entry point is `python tools/openscad_tools.py`:

| Command | Purpose |
| --- | --- |
| `doctor` | Discover OpenSCAD, dependencies, manual and BOSL2 |
| `new <name> [--bosl2]` | Create `projects/01_<name>/` with a starter SCAD and README; unprefix previous working folders |
| `new <name> --template clearance` | Create a hole/peg coupon for radial fit testing |
| `export <source.scad>` | Export binary STL atomically and capture OpenSCAD logs |
| `check <model.stl> [--json report.json]` | Check topology, winding, volume, dimensions, A1 fit and overhang candidates |
| `render <model.stl>` | Create PNG directly from the exported mesh; optional orthographic views/overhang coloring |
| `build <source.scad>` | Export STL, check it, create PNG and write validation/provenance JSON |
| `orient <model.stl>` | Compare six axis-aligned orientations without modifying files |
| `compare <old.stl> <new.stl>` | Compare dimensions/volume for unintended size changes |
| `audit [projects_dir] [--validate]` | Read-only project deliverable inventory; optional mesh/PNG checks |
| `docs <query>` | Search the local manual, BOSL2 wiki and source |

Typical workflow from the workspace root:

```powershell
python tools/openscad_tools.py doctor
python tools/openscad_tools.py new my_part --bosl2
# Design/edit projects/01_my_part/my_part.scad, then:
python tools/openscad_tools.py build projects/01_my_part/my_part.scad
python tools/openscad_tools.py orient projects/01_my_part/my_part.stl
python tools/openscad_tools.py render projects/01_my_part/my_part.stl --view top -o projects/01_my_part/my_part_top.png
```

For named parts, use repeatable `-D` definitions and distinct output names:

```powershell
python tools/openscad_tools.py export projects/01_my_part/my_part.scad -D 'part="base"' -o projects/01_my_part/base.stl
python tools/openscad_tools.py check projects/01_my_part/base.stl --json projects/01_my_part/base.validation.json
python tools/openscad_tools.py render projects/01_my_part/base.stl -o projects/01_my_part/base.png
```

Before declaring a project complete:

1. Fully export the final SCAD and address OpenSCAD errors/warnings. Warnings
   fail by default; use `--allow-warnings` only for an understood, documented warning.
2. Check each STL. Fix open/non-manifold edges, pinched shells, inconsistent
   winding, duplicate/degenerate triangles, nonpositive volume, or oversize geometry.
   Review multiple shells: separate parts and enclosed cavity surfaces can be
   intentional. `--expected-shells` counts connected surfaces, not physical parts.
3. Open and visually inspect the final PNG; verify orientation, holes, proportions,
   and visible details. Provide additional views for hidden functional features.
4. When slicer access is available, inspect the STL in Bambu Studio with the
   actual A1 nozzle/material profile. Review layer islands, bridges, wall paths,
   bed adhesion and support requirements. Record any unresolved slicer checks
   instead of claiming they passed.
5. Confirm matching `.scad`, `.stl`, `.png` deliverables and update the README.

The mesh tools reconstruct topology by merging vertex coordinates at five
decimal places in mm. They preserve faces and do not silently repair meshes.
Their checks do **not** prove absence of self-intersections, overlapping shells,
thin walls, or support needs. Orientation rankings and colored overhangs are
heuristics; dimensions/volume comparison does not prove two shapes are identical.
Use geometric reasoning, images, slicer review and fit tests to finish validation.

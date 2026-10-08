# Verified BOSL2 plate example

An example of local BOSL2 inclusion and the export/check/render workflow.
Dimensions: 40 × 30 × 8 mm. Flat bottom at Z=0; only vertical edges are rounded.
Intended orientation: as modeled. Supports: none expected; inspect final slicing.
Working assumptions: 0.4 mm nozzle, 0.20 mm layers, PLA. No mating clearances.

From the workspace root:

```powershell
python tools/openscad_tools.py build tools/examples/bosl2_plate/bosl2_plate.scad
```

The `.stl` and `.png` are generated from this source. The validation JSON records
mesh checks; the build manifest records hashes and the installed OpenSCAD version.
This example demonstrates the tools; it has not been physically test printed.

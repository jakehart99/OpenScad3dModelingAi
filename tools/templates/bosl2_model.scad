// Pinned local BOSL2. tools/openscad_tools.py sets OPENSCADPATH to the docs folder.
include <BOSL2-2.0.766/std.scad>
// Replace the sample with the requested model. Units: mm. Bottom stays flat.
width = 40;
depth = 30;
height = 8;
corner_radius = 3;
$fa = $preview ? 8 : 3;
$fs = $preview ? 1 : 0.35;
assert(corner_radius >= 0 && width > 2*corner_radius && depth > 2*corner_radius && height > 0);

module model() {
    cuboid([width, depth, height], rounding=corner_radius,
           edges="Z", anchor=BOTTOM);
}
model();

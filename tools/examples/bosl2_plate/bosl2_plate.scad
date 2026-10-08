// Working pinned BOSL2 example: flat-bottomed plate with vertical rounded edges.
include <BOSL2-2.0.766/std.scad>
width = 40;
depth = 30;
height = 8;
corner_radius = 3;
$fa = $preview ? 8 : 3;
$fs = $preview ? 1 : 0.35;
assert(corner_radius >= 0 && width > 2*corner_radius && depth > 2*corner_radius && height > 0);
cuboid([width,depth,height], rounding=corner_radius, edges="Z", anchor=BOTTOM);

// Replace this sample with the requested model. All dimensions are millimeters.
// Base at Z=0; export the printable geometry, not an exploded assembly.
width = 40;
depth = 30;
height = 8;
corner_radius = 3;
$fa = $preview ? 8 : 3;
$fs = $preview ? 1 : 0.35;
assert(corner_radius >= 0 && width > 2*corner_radius && depth > 2*corner_radius && height > 0);

module model() {
    // Round the XY outline only, preserving a flat, support-free bottom.
    linear_extrude(height)
        offset(r=corner_radius)
            square([width-2*corner_radius, depth-2*corner_radius], center=true);
}
model();

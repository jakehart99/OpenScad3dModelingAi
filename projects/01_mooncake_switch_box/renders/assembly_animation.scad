// Assembly animation scene. Uses the exported STLs (already fully evaluated) and
// takes positions from the master model. Driven by $t in [0, 1]; frames are made
// by make_assembly_video.py. Display only - nothing here is printed.
include <../mooncake_switch_box.scad>
part = "none";             // suppress the master model's own output

designs_shown = ["smiley", "zhong", "qiu", "yue"];
c_base   = "#d9bf94";
c_insert = "#e8a923";
c_cake   = "#a8652f";
c_red    = "#b5332b";
c_yellow = "#f0b52a";
c_cream  = "#fbf7ef";
c_white  = "#f4f4f2";
c_clear  = [0.80, 0.88, 1.00, 0.45];
c_stem   = "#2f7de1";

function clamp01(x) = min(1, max(0, x));
function ease(x) = let(u = clamp01(x)) u * u * (3 - 2 * u);
function seg(a, b) = ease(($t - a) / (b - a));
function drop(a, b, h) = h * (1 - seg(a, b));
function visible(a) = $t >= a;
// Short press pulse for key i (0..1 of key_travel).
function press(i) = let(c = 0.53 + i * 0.045, w = 0.022, d = abs($t - c) / w) d < 1 ? 1 - d * d : 0;

// MX-clone switch with plate top at z=0 (bottom housing, clear top, blue stem).
module show_switch(p) {
    color(c_white) {
        translate([-7, -7, -5]) cube([14, 14, 5]);
        translate([0, 0, -8]) cylinder(d = 4, h = 3.01);
        for (x = [-3.8, 2.5]) translate([x, 2.5 * sign(x), -8.3]) cylinder(d = 1, h = 3.4);
    }
    color(c_stem) {
        translate([-3.5, -3, 3.5 - p]) cube([7, 6, 4.5]);
        translate([0, 0, 8 - p + 1.8]) {
            cube([4.0, 1.2, 3.6], center = true);
            cube([1.2, 4.0, 3.6], center = true);
        }
    }
    color(c_clear) hull() {
        linear_extrude(0.01) square(15.5, center = true);
        translate([0, 0, 6.6]) linear_extrude(0.01) square(10.5, center = true);
    }
}

module scene() {
    color(c_base) translate([0, 0, drop(0.0, 0.07, 30)]) import("../base.stl");
    if (visible(0.07))
        color(c_insert) translate([0, 0, shelf_z + drop(0.07, 0.17, 35)]) import("../insert.stl");
    for (i = [0:3]) let(c = cell_centers[i], p = press(i) * key_travel) {
        a = 0.18 + i * 0.035;
        if (visible(a)) translate([c.x, c.y, plate_top_z + drop(a, a + 0.07, 30)]) show_switch(p);
        b = 0.34 + i * 0.035;
        if (visible(b))
            color(c_cake) translate([c.x, c.y, plate_top_z + cap_rest - p + drop(b, b + 0.07, 30)])
                import(str("../keycaps/keycap_", designs_shown[i], ".stl"));
    }
    if (visible(0.74))
        translate([0, 0, lip_z + lid_h + drop(0.74, 0.86, 35)]) rotate([0, 180, 0]) {
            color(c_base) import("../lid.stl");
            for (c = [["red", c_red], ["yellow", c_yellow], ["white", c_cream]])
                color(c[1]) translate([0, 0, -0.02]) import(str("../lid_inlay_", c[0], ".stl"));
        }
}

// Slow turntable that settles facing the camera, then tilts to show off the lid art.
translate([0, 0, 18]) rotate([28 * seg(0.86, 0.97), 0, 0]) translate([0, 0, -18]) rotate([0, 0, -200 * (1 - ease($t / 0.92))]) scene();

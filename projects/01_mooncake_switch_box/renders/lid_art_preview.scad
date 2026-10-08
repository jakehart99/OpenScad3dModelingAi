// Flat colour preview of the lid artwork as it reads on the finished box.
include <../mooncake_switch_box.scad>
part = "none";
color("#d9bf94") translate([0, 0, -1]) linear_extrude(1) rsq(base_outer, base_r);
for (c = [["red", "#b5332b"], ["yellow", "#f0b52a"], ["white", "#fbf7ef"]])
    color(c[1]) linear_extrude(0.6) mirror([1, 0]) lid_art2d(c[0]);

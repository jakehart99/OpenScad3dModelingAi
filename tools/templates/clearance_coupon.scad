// Print the hole bar and removable pegs as separate pieces, with no supports.
// Values are RADIAL clearances: hole diameter = peg diameter + 2*clearance.
// Start here, then calibrate for the actual material, nozzle and slicer profile.
clearances = [0.15, 0.25, 0.35];
peg_diameter = 6;
plate_thickness = 3;
peg_height = 8;
spacing = 18;
part = "all"; // [all,holes,pegs]
$fa = 3;
$fs = 0.3;
assert(len(clearances)>0 && peg_diameter>0 && plate_thickness>0 && peg_height>0);
assert(min(clearances)>=0 && spacing>peg_diameter+2*max(clearances)+4);
assert(part=="all" || part=="holes" || part=="pegs");

module hole_bar() {
    difference() {
        translate([-spacing/2,-8,0]) cube([len(clearances)*spacing,16,plate_thickness]);
        for(i=[0:len(clearances)-1])
            translate([i*spacing,0,-0.1])
                cylinder(d=peg_diameter+2*clearances[i],h=plate_thickness+0.2);
    }
    for(i=[0:len(clearances)-1])
        translate([i*spacing,5,plate_thickness-0.01])
            linear_extrude(0.41) text(str(clearances[i]),size=2.5,halign="center",valign="center");
}
module pegs() {
    for(i=[0:len(clearances)-1]) translate([i*spacing,22,0]) {
        cylinder(d=peg_diameter+5,h=2);
        translate([0,0,1.9]) cylinder(d=peg_diameter,h=peg_height+0.1);
    }
}
if(part=="all" || part=="holes") hole_bar();
if(part=="all" || part=="pegs") pegs();

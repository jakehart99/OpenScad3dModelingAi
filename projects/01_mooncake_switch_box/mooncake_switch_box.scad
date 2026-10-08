// Mooncake fidget switch box: 2x2 "mooncake" keycaps on MX-style switches,
// in a mooncake-gift-box style base, tray insert and friction lid.
// Units: mm. Every printable part is modelled in its print orientation (Z=0 = bed).
// Pinned local BOSL2. tools/openscad_tools.py sets OPENSCADPATH to the docs folder.
include <BOSL2-2.0.766/std.scad>

/* [Part selection] */
// assembly / exploded are display-only views (include dummy switches).
part = "assembly"; // [none, assembly, exploded, keycap, insert, insert_single, base, lid, lid_inlay, fit_coupon]
// Keycap face design (used when part = "keycap").
design = "smiley"; // [smiley, zhong, qiu, yue, man, jia, le, yuan, fu, blank]
// Lid artwork colour (used when part = "lid_inlay").
inlay_color = "red"; // [red, yellow, white]

/* [Mooncake keycap] */
cake_d = 32;              // tip-to-tip diameter of the scalloped outline
cake_lobes = 14;          // number of scallops
cake_lobe_depth = 1.5;    // radial depth of the scallop valleys
cake_valley_round = 0.6;  // fillet radius in the valleys
cake_h = 12;              // body height (relief adds relief_h on top)
cake_top_round = 1.6;     // rounded top edge radius
cake_bottom_chamfer = 0.4;// elephant-foot chamfer on the bed edge
relief_h = 0.6;           // raised pattern / character height (3 layers @ 0.2)
deboss_depth = 0.8;       // smiley eyes and mouth depth
cavity_d = 23;            // underside pocket that clears the switch housing
cavity_h = 5;             // pocket depth = stem post length
stem_d = 5.6;             // keycap stem post diameter
cross_h = [4.15, 1.35];   // horizontal slot of the MX "+" socket [x, y]
cross_v = [1.25, 4.15];   // vertical slot of the MX "+" socket [x, y]
stem_slop = 0.0;          // added to every socket slot width (tune with fit_coupon)
socket_depth = 3.8;       // MX cross is ~3.6 tall
socket_flare = 0.2;       // first-layer flare of the socket (elephant-foot relief)
char_font = "Microsoft YaHei:style=Bold";
char_size = 8.4;
char_bold = 0.12;         // outward offset that thickens thin glyph strokes

/* [MX switch interface] */
plate_t = 1.5;            // MX clips need a 1.5 mm plate
plate_hole = 14.0;        // MX plate cut-out (square)
housing_w = 15.6;         // MX top-housing footprint
frame_clear = 0.2;        // per-side clearance between housing and locating frame
frame_wall = 1.2;
frame_h = 2.0;
cap_rest = 8.0;           // keycap bottom above plate top when the key is up
key_travel = 4.0;
switch_gap = 8.5;         // free space below the plate bottom: MX-clone body ~3.5 + centre post/pins ~3.3 => ~6.8 needed

/* [Tray insert] */
cell_w = 35.5;            // inner size of each mooncake cell
cell_r = 7;               // cell corner radius
div_t = 2.0;              // divider wall between cells
insert_wall = 1.8;        // insert outer wall
insert_wall_h = 13;       // cell wall height above the plate
flute_pitch = 2.6;        // spacing of the vertical cupcake-liner flutes
flute_amp = 0.35;         // flute amplitude (+/-)
insert_fit = 0.3;         // per-side clearance insert -> base
single_wall = 1.6;        // wall of the single-cell cups
single_gap = 0.4;         // gap between the four single cups

/* [Base] */
base_wall = 3.2;
base_floor = 2.0;
shelf_w = 2.5;            // ledge the insert rests on
rib_w = 2.0;              // centre cross ribs under the insert dividers
base_h = 28;
lip_h = 6;                // height of the lid-engagement lip

/* [Lid] */
lid_wall = 1.4;
lid_fit = 0.2;            // per-side clearance lid skirt -> base lip
lid_top = 1.6;
lid_headroom = 1.0;       // gap between keycap tops and lid ceiling
inlay_depth = 0.6;        // lid artwork recess / inlay thickness
notch_w = 14;             // fingernail notches in the skirt edge
notch_d = 1.5;

/* [Hidden] */
$fa = $preview ? 8 : 3;
$fs = $preview ? 0.6 : 0.3;
eps = 0.01;

designs = [
    ["smiley", ""],  ["zhong", "中"], ["qiu", "秋"], ["yue", "月"], ["man", "满"],
    ["jia", "家"],   ["le", "乐"],    ["yuan", "圆"], ["fu", "福"], ["blank", ""]
];
function design_char(d) = [for (x = designs) if (x[0] == d) x[1]][0];

// ---------- Derived dimensions ----------
cell_pitch   = cell_w + div_t;
cell_centers = [for (x = [-1, 1], y = [-1, 1]) [x, y] * cell_pitch / 2];
insert_outer = 2 * cell_w + div_t + 2 * insert_wall;
insert_r     = cell_r + insert_wall;
insert_h     = plate_t + insert_wall_h;
single_outer = (insert_outer - single_gap) / 2;
single_cell  = single_outer - 2 * single_wall;
single_pitch = single_outer + single_gap;
base_inner   = insert_outer + 2 * insert_fit;
base_inner_r = insert_r + insert_fit;
base_outer   = base_inner + 2 * base_wall;
base_r       = base_inner_r + base_wall;
shelf_z      = base_floor + switch_gap;
plate_top_z  = shelf_z + plate_t;
cap_full_h   = cake_h + relief_h;
cap_top_z    = plate_top_z + cap_rest + cap_full_h;
lip_z        = base_h - lip_h;
lip_outer    = base_outer - 2 * (lid_wall + lid_fit);
lip_r        = base_r - (lid_wall + lid_fit);
lid_inner_h  = max(lip_h, cap_top_z + lid_headroom - lip_z);
lid_h        = lid_top + lid_inner_h;
frame_in     = housing_w + 2 * frame_clear;
cake_valley_r = cake_d / 2 - cake_lobe_depth;

assert(!is_undef(design_char(design)), str("Unknown design: ", design));
assert(cavity_d > housing_w * sqrt(2) + 0.5, "cavity must clear the switch housing diagonal");
assert(cavity_d / 2 + 2.5 < cake_valley_r, "keycap skirt too thin");
assert(socket_depth < cavity_h + cake_h - 2, "socket too deep");
assert(cap_rest - key_travel > frame_h + 0.5, "keycap would hit the locating frame at bottom-out");
assert(cake_d + 2 <= min(cell_w, single_cell), "mooncake needs >= 1 mm clearance in its cell");
assert(frame_in + 2 * frame_wall < cell_w, "frame larger than cell");
assert((lip_outer - base_inner) / 2 >= 1.2, "base lip wall too thin");
assert(shelf_z + insert_h <= base_h, "insert sticks out of the base");
assert(cell_pitch / 2 - plate_hole / 2 > rib_w / 2 + 1, "switch bodies would hit the centre ribs");

// ---------- 2D helpers ----------
module rsq(w, r) { offset(r = r) square(w - 2 * r, center = true); }
module ring(r_out, w) { difference() { circle(r_out); circle(r_out - w); } }

function cake_path_raw(R = cake_d / 2) =
    let(n = cake_lobes * 24)
    [for (i = [0:n - 1]) let(a = 360 * i / n)
        (R - cake_lobe_depth * (1 - abs(cos(cake_lobes * a / 2)))) * [cos(a), sin(a)]];
// Dilate then erode: fillets the cusp valleys, leaves the lobes untouched.
function cake_path() =
    offset(offset(cake_path_raw(), r = cake_valley_round, closed = true),
           r = -cake_valley_round, closed = true);

cake_pts = cake_path();   // computed once; BOSL2 path offsets are slow
module cake2d() { polygon(cake_pts); }

module smiley2d(s = 1) {
    scale(s) {
        for (x = [-2.6, 2.6]) translate([x, 1.3]) circle(r = 0.8);
        // smile: arc stroked with round caps
        pts = [for (a = [212:8:328]) [0, 1.0] + 2.6 * [cos(a), sin(a)]];
        for (i = [0:len(pts) - 2]) hull() {
            translate(pts[i]) circle(r = 0.42);
            translate(pts[i + 1]) circle(r = 0.42);
        }
    }
}

// Raised lace pattern on the mooncake face (border, petal ring, centre ring).
module cake_lace2d() {
    difference() { offset(r = -1.9) cake2d(); offset(r = -2.6) cake2d(); }
    petal_r = 10.1;
    for (i = [0:cake_lobes - 1]) {
        rotate(360 * i / cake_lobes) translate([petal_r, 0]) ring(1.5, 0.65);
        rotate(360 * (i + 0.5) / cake_lobes) translate([petal_r, 0]) circle(d = 1.0);
    }
    ring(8.05, 0.7);
}

module cake_motif2d(d) {
    ch = design_char(d);
    if (ch != "")
        offset(r = char_bold)
            text(ch, size = char_size, font = char_font, halign = "center", valign = "center");
}

// ---------- Keycap ----------
module mx_socket2d(slop, extra = 0) {
    square(cross_h + [1, 1] * (slop + extra), center = true);
    square(cross_v + [1, 1] * (slop + extra), center = true);
}

module stem_socket(slop = stem_slop) {
    translate([0, 0, -1]) linear_extrude(socket_depth + 1) mx_socket2d(slop);
    translate([0, 0, -1]) linear_extrude(1 + 0.2) mx_socket2d(slop, 2 * socket_flare);
}

module keycap(d = design) {
    difference() {
        union() {
            offset_sweep(cake_pts, height = cake_h,
                         bottom = os_chamfer(width = cake_bottom_chamfer),
                         top = os_circle(r = cake_top_round, steps = 8), steps = 8);
            translate([0, 0, cake_h - eps]) linear_extrude(relief_h + eps) {
                cake_lace2d();
                cake_motif2d(d);
            }
        }
        // Underside pocket around the stem post (bridged ceiling, ~8.7 mm span).
        translate([0, 0, -1]) linear_extrude(cavity_h + 1)
            difference() { circle(d = cavity_d); circle(d = stem_d); }
        stem_socket();
        if (d == "smiley")
            translate([0, 0, cake_h - deboss_depth]) linear_extrude(deboss_depth + 1) smiley2d();
    }
}

// ---------- Tray insert ----------
function fluted_path(w, r) =
    let(p = [for (q = rect([w, w], rounding = r, $fn = 72)) q],
        nf = max(8, round(path_length(p, closed = true) / flute_pitch)),
        rp = resample_path(p, n = nf * 8, closed = true),
        nr = path_normals(rp, closed = true))
    [for (i = idx(rp)) rp[i] + flute_amp * cos(360 * nf * i / len(rp)) * nr[i]];

module switch_mount() {
    // Locating frame around the switch top housing, standing on the plate.
    translate([0, 0, plate_t - eps]) linear_extrude(frame_h + eps)
        difference() { square(frame_in + 2 * frame_wall, center = true); square(frame_in, center = true); }
}

module plate_cutout() { translate([0, 0, -1]) linear_extrude(plate_t + 2) square(plate_hole, center = true); }

module cup_body(outer, outer_r, pocket, centers) {
    difference() {
        linear_extrude(insert_h) rsq(outer, outer_r);
        for (c = centers) translate([c.x, c.y, plate_t]) linear_extrude(insert_h)
            polygon(fluted_path(pocket, cell_r));
        for (c = centers) translate(c) plate_cutout();
    }
    for (c = centers) translate(c) switch_mount();
}

module insert() { cup_body(insert_outer, insert_r, cell_w, cell_centers); }

// One of four single-cell cups that together replace the 2x2 insert.
module insert_single() { cup_body(single_outer, cell_r + single_wall, single_cell, [[0, 0]]); }

// ---------- Base ----------
module base() {
    difference() {
        union() {
            linear_extrude(lip_z) rsq(base_outer, base_r);
            translate([0, 0, lip_z - eps]) linear_extrude(lip_h + eps) rsq(lip_outer, lip_r);
        }
        translate([0, 0, shelf_z]) linear_extrude(base_h) rsq(base_inner, base_inner_r);
        translate([0, 0, base_floor]) linear_extrude(switch_gap + eps)
            difference() {
                rsq(base_inner - 2 * shelf_w, base_inner_r - shelf_w);
                square([rib_w, base_outer], center = true);
                square([base_outer, rib_w], center = true);
            }
    }
}

// ---------- Lid (modelled upside down: decorated top face on the bed) ----------
// Gift-box artwork as flush inlays in three colours over the lid colour:
// red outlines/text, yellow moon/mooncakes, white bunny/clouds. Shapes are painted
// back-to-front; each layer is cut by every later layer so colour regions never overlap.
art_font = "Segoe UI Black";
art_cakes = [[-5, -5], [-17, -14], [17, -14], [0, -18]];   // back to front
art_names = concat(
    ["border", "yline", "moon", "spark", "clover", "text",
     "cloudL_o", "cloudL_f", "cloudL_d", "cloudR_o", "cloudR_f", "cloudR_d",
     "bun_o", "bun_f", "bun_d"],
    [for (i = [0:3], l = ["o", "f", "r", "d"]) str("cake", i, "_", l)]);
function art_color(name) =
    let(t = name[len(name) - 1])
    name == "yline" || name == "moon" || name == "spark" ? "yellow"
    : name == "border" || name == "clover" || name == "text" ? "red"
    : t == "o" || t == "d" || t == "r" ? "red"
    : (name[0] == "c" && name[1] == "a") ? "yellow" : "white";

module ellipse(rx, ry) { scale([rx, ry]) circle(1, $fn = 64); }
module arc_stroke(r, a0, a1, w, step = 10) {
    pts = [for (a = [a0:step:a1]) r * [cos(a), sin(a)]];
    for (i = [0:len(pts) - 2]) hull() { translate(pts[i]) circle(d = w); translate(pts[i + 1]) circle(d = w); }
}
module sparkle(s) { scale(s) polygon([[0, 1], [0.22, 0.22], [1, 0], [0.22, -0.22], [0, -1], [-0.22, -0.22], [-1, 0], [-0.22, 0.22]]); }
module clover(r = 1.3) { difference() { for (a = [0:90:270]) rotate(a + 45) translate([r, 0]) circle(r); circle(0.6); } }

module art_text() {
    // Arched "MOONCAKE", letters placed along a circle of radius R.
    letters = ["M", "O", "O", "N", "C", "A", "K", "E"];
    adv = [9.6, 8.0, 8.0, 8.0, 7.0, 8.0, 7.8, 6.4];
    R = 85; yc = 26;
    total = sum(adv);
    for (i = [0:7]) let(sx = sum([for (j = [0:i]) adv[j]]) - adv[i] / 2 - total / 2, th = sx / R * 180 / PI)
        translate([R * sin(th), yc - R * (1 - cos(th))]) rotate(-th)
            offset(r = 0.3) text(letters[i], size = 7.6, font = art_font, halign = "center", valign = "center");
}

module cloud_sil() {
    translate([0, 1]) circle(3);
    translate([3.6, 0.2]) circle(2.3);
    translate([-3.8, 0]) circle(2.2);
    translate([-6, -2.3]) offset(r = 1) offset(delta = -1) square([12.5, 2.8]);
}
module cloud_detail() { translate([-0.3, 1]) arc_stroke(1.5, -60, 230, 0.75); }

module bun_sil() {
    ellipse(7, 6);
    translate([2, 9]) rotate(-15) ellipse(2.6, 7.5);
    translate([6.5, 6.5]) rotate(-48) ellipse(2.5, 7);
    translate([1.5, -7]) ellipse(7, 6.5);
}
module bun_detail() {
    for (x = [-3.4, 1.0]) translate([x, -0.3]) arc_stroke(1.0, 200, 340, 0.7, 20);   // happy closed eyes
    translate([-1.2, -3]) circle(d = 0.9);
    translate([2, 9]) rotate(-15) translate([0, 1.2]) ellipse(0.8, 4.2);              // inner ear
}

module cake_top() { scale([0.5, 0.5 * 0.45]) cake2d(); }
module cake_sil() { hull() { cake_top(); translate([0, -7]) cake_top(); } }
module cake_face() {
    for (x = [-2.3, 2.3]) translate([x, -5.9]) circle(r = 0.7);
    translate([0, -6.3]) arc_stroke(1.4, 205, 335, 0.75, 13);
    for (x = [-5.8, 5.8]) translate([x, -5.0]) hull() { circle(d = 0.7); translate([0, -4.0]) circle(d = 0.7); }
}

module art_layer(name) {
    if (name == "border") difference() { rsq(base_outer - 3, base_r - 1.5); rsq(base_outer - 7.4, base_r - 3.7); }
    else if (name == "yline") difference() { rsq(base_outer - 10, base_r - 5); rsq(base_outer - 11.6, base_r - 5.8); }
    else if (name == "moon") translate([-14, 8]) circle(8.5);
    else if (name == "spark") for (p = [[-3, 15.5], [31, 10], [-32, -10], [27, -24]]) translate(p) sparkle(1.8);
    else if (name == "clover") for (x = [-1, 1], y = [-1, 1]) translate([31 * x, y > 0 ? 31.5 : -30.5]) clover();
    else if (name == "text") art_text();
    else if (name == "cloudL_o") translate([-24, 4]) offset(r = 0.9) cloud_sil();
    else if (name == "cloudL_f") translate([-24, 4]) cloud_sil();
    else if (name == "cloudL_d") translate([-24, 4]) cloud_detail();
    else if (name == "cloudR_o") translate([27, -3]) mirror([1, 0]) scale(0.9) offset(r = 1.0) cloud_sil();
    else if (name == "cloudR_f") translate([27, -3]) mirror([1, 0]) scale(0.9) cloud_sil();
    else if (name == "cloudR_d") translate([27, -3]) mirror([1, 0]) scale(0.9) cloud_detail();
    else if (name == "bun_o") translate([11, 1]) offset(r = 0.9) bun_sil();
    else if (name == "bun_f") translate([11, 1]) bun_sil();
    else if (name == "bun_d") translate([11, 1]) bun_detail();
    else for (i = [0:3]) if (name == str("cake", i, "_o")) translate(art_cakes[i]) offset(r = 0.9) cake_sil();
        else if (name == str("cake", i, "_f")) translate(art_cakes[i]) cake_sil();
        else if (name == str("cake", i, "_r")) translate(art_cakes[i]) difference() { cake_top(); offset(r = -0.7) cake_top(); }
        else if (name == str("cake", i, "_d")) translate(art_cakes[i]) cake_face();
}

// One colour's visible regions (view orientation, i.e. not yet mirrored).
module art_color2d(c) {
    n = len(art_names);
    for (k = [0:n - 1]) if (art_color(art_names[k]) == c)
        difference() {
            art_layer(art_names[k]);
            if (k < n - 1) for (j = [k + 1:n - 1]) if (art_color(art_names[j]) != c) art_layer(art_names[j]);
        }
}

// Mirrored so the art reads correctly after the printed lid is flipped over.
module lid_art2d(c = "all") {
    mirror([1, 0])
        if (c == "all") for (k = [0:len(art_names) - 1]) art_layer(art_names[k]);
        else art_color2d(c);
}

module lid() {
    difference() {
        linear_extrude(lid_h) rsq(base_outer, base_r);
        translate([0, 0, lid_top]) linear_extrude(lid_h) rsq(lip_outer + 2 * lid_fit, lip_r + lid_fit);
        for (s = [-1, 1]) translate([0, s * base_outer / 2, lid_h])
            cube([notch_w, 4 * lid_wall + 2, 2 * notch_d], center = true);
        translate([0, 0, -1]) linear_extrude(1 + inlay_depth) lid_art2d();
    }
}

// Inlay for one filament colour; load lid + the three inlays as one multi-part object.
module lid_inlay(c = inlay_color) { linear_extrude(inlay_depth) lid_art2d(c); }

// ---------- Fit coupon: three plate holes + three stem sockets ----------
module fit_coupon() {
    holes = [plate_hole - 0.1, plate_hole, plate_hole + 0.1];
    slops = [stem_slop, stem_slop + 0.1, stem_slop + 0.2];
    sp = frame_in + 2 * frame_wall + 1.2;
    w = 3 * sp + 2;
    difference() {
        union() {
            translate([-w / 2, 0, 0]) cube([w, sp + 1, plate_t]);
            translate([-w / 2, -12, 0]) cube([w, 12 + eps, 6]);
        }
        for (i = [0:2]) {
            translate([(i - 1) * sp, sp / 2 + 0.5, -1]) linear_extrude(plate_t + 2) square(holes[i], center = true);
            translate([(i - 1) * sp, -6, 0]) stem_socket(slops[i]);
            // i+1 dots identify the variant (hole and socket in the same column)
            for (k = [0:i]) translate([(i - 1) * sp + (k - i / 2) * 2.2, -10, 6 - 0.6])
                cylinder(d = 1.2, h = 1);
        }
    }
    for (i = [0:2]) translate([(i - 1) * sp, sp / 2 + 0.5, 0]) switch_mount();
}

// ---------- Display-only ----------
module dummy_switch() {
    // MX switch envelope relative to the plate top: housing, stem, bottom body.
    translate([0, 0, -5]) linear_extrude(5) square(13.9, center = true);
    hull() {
        linear_extrude(0.01) square(housing_w, center = true);
        translate([0, 0, 6.6 - 0.01]) linear_extrude(0.01) square(10.5, center = true);
    }
    translate([0, 0, 6.6]) cylinder(d = 5, h = cap_rest - 6.6 + 1);
}

assembly_designs = ["smiley", "zhong", "qiu", "yue"];
module assembly(explode = 0) {
    base();
    translate([0, 0, shelf_z + explode * 1.0]) insert();
    for (i = [0:3]) let(c = cell_centers[i]) {
        translate([c.x, c.y, plate_top_z + explode * 1.5]) dummy_switch();
        translate([c.x, c.y, plate_top_z + cap_rest + explode * 2.5]) keycap(assembly_designs[i]);
    }
    translate([0, 0, lip_z + lid_h + 18 + explode * 3.5]) rotate([0, 180, 0]) lid();
}

if (part == "keycap") keycap();
else if (part == "insert") insert();
else if (part == "insert_single") insert_single();
else if (part == "base") base();
else if (part == "lid") lid();
else if (part == "lid_inlay") lid_inlay();
else if (part == "fit_coupon") fit_coupon();
else if (part == "exploded") assembly(explode = 14);
else if (part != "none") assembly();

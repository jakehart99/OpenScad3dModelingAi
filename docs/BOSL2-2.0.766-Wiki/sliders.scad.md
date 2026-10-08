# LibFile: sliders.scad

Simple V-groove based sliders and rails.

To use, add the following lines to the beginning of your file:

    include <BOSL2/std.scad>
    include <BOSL2/sliders.scad>

## File Contents

1. [Section: Modules](#section-modules)
    - [`slider()`](#module-slider) – Creates a V-groove slider. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
    - [`rail()`](#module-rail) – Creates a V-groove rail. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>


## Section: Modules


### Module: slider()

**Synopsis:** Creates a V-groove slider. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>

**Topics:** [Parts](Topics#parts), [Sliders](Topics#sliders)

**See Also:** [rail()](#module-rail)

**Usage:** 

- slider(l, w, h, [base=], [wall=], [ang=], [$slop=]) [ATTACHMENTS];

**Description:** 

Creates a slider to match a V-groove rail.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`l`                  | Length (long axis) of slider.  Default: 30
`w`                  | Width of slider.  Default: 10
`h`                  | Height of slider.  Default: 10

<abbr title="These args must be used by name, ie: name=value">By&nbsp;Name</abbr> | What it does
-------------------- | ------------
`base`               | Height of slider base.  Default: 10
`wall`               | Width of wall behind each side of the slider.  Default: 5
`ang`                | Overhang angle measured down from vertical, matching the rail.  Default: 30
`chamfer`            | Size of chamfer. Default: 2.
`anchor`             | Translate so anchor point is at origin (0,0,0).  See [anchor](attachments.scad#subsection-anchor).  Default: `BOTTOM`
`spin`               | Rotate this many degrees around the Z axis after anchor.  See [spin](attachments.scad#subsection-spin).  Default: `0`
`orient`             | Vector to rotate top towards, after spin.  See [orient](attachments.scad#subsection-orient).  Default: `UP`
`$slop`              | The printer-specific slop value to make parts fit just right.

**Example 1:** 

<img align="left" alt="slider() Example 1" src="images/sliders/slider.png" width="320" height="240">

    include <BOSL2/std.scad>
    include <BOSL2/sliders.scad>
    slider(l=30, base=10, wall=4, $slop=0.2);

<br clear="all" /><br/>

**Example 2:** Vertically centered anchors are aligned with the slider V tips.

<img align="left" alt="slider() Example 2" src="images/sliders/slider_2.png" width="320" height="240">

    include <BOSL2/std.scad>
    include <BOSL2/sliders.scad>
    slider(l=30, base=10, wall=4) show_anchors();

<br clear="all" /><br/>

---

### Module: rail()

**Synopsis:** Creates a V-groove rail. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>

**Topics:** [Parts](Topics#parts), [Sliders](Topics#sliders)

**See Also:** [slider()](#module-slider)

**Usage:** 

- rail(l, w, h, [chamfer=], [ang=]) [ATTACHMENTS];

**Description:** 

Creates a V-groove rail.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`l`                  | Length (long axis) of the rail.  Default: 30
`w`                  | Width of the rail.  Default: 10
`h`                  | Height of the rail.  Default: 10
`chamfer`            | Size of chamfer at end of rail.  Default: 1
`ang`                | Overhang angle measured down from vertical.  Default: 30

<abbr title="These args must be used by name, ie: name=value">By&nbsp;Name</abbr> | What it does
-------------------- | ------------
`anchor`             | Translate so anchor point is at origin (0,0,0).  See [anchor](attachments.scad#subsection-anchor).  Default: `BOTTOM`
`spin`               | Rotate this many degrees around the Z axis after anchor.  See [spin](attachments.scad#subsection-spin).  Default: `0`
`orient`             | Vector to rotate top towards, after spin.  See [orient](attachments.scad#subsection-orient).  Default: `UP`

**Example 1:** 

<img align="left" alt="rail() Example 1" src="images/sliders/rail.png" width="320" height="240">

    include <BOSL2/std.scad>
    include <BOSL2/sliders.scad>
    rail(l=100, w=10, h=10);

<br clear="all" /><br/>

**Example 2:** Anchors

<img align="left" alt="rail() Example 2" src="images/sliders/rail_2.png" width="320" height="240">

    include <BOSL2/std.scad>
    include <BOSL2/sliders.scad>
    rail(l=100, w=10, h=10) show_anchors();

<br clear="all" /><br/>

---


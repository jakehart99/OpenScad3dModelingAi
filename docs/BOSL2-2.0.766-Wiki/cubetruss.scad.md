# LibFile: cubetruss.scad

Parts for making modular open-frame cross-braced trusses and connectors.

To use, add the following lines to the beginning of your file:

    include <BOSL2/std.scad>
    include <BOSL2/cubetruss.scad>

## File Contents

1. [Section: Cube Trusses](#section-cube-trusses)
    - [`cubetruss()`](#module-cubetruss) – Creates a multi-cube straight cubetruss shape. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
    - [`cubetruss_corner()`](#module-cubetruss_corner) – Creates a multi-cube corner cubetruss shape. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
    - [`cubetruss_support()`](#module-cubetruss_support) – Creates a cubetruss support structure shape. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>

2. [Section: Cubetruss Support](#section-cubetruss-support)
    - [`cubetruss_foot()`](#module-cubetruss_foot) – Creates a foot that can connect two cubetrusses. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
    - [`cubetruss_joiner()`](#module-cubetruss_joiner) – Creates a joiner that can connect two cubetrusses end-to-end. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
    - [`cubetruss_uclip()`](#module-cubetruss_uclip) – Creates a joiner that can connect two cubetrusses end-to-end. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>

3. [Section: Cubetruss Primitives](#section-cubetruss-primitives)
    - [`cubetruss_segment()`](#module-cubetruss_segment) – Creates a single cubetruss cube. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
    - [`cubetruss_clip()`](#module-cubetruss_clip) – Creates a clip for the end of a cubetruss to snap-lock it to another cubetruss. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
    - [`cubetruss_dist()`](#function-cubetruss_dist) – Returns the length of a cubetruss truss.


## Section: Cube Trusses


### Module: cubetruss()

**Synopsis:** Creates a multi-cube straight cubetruss shape. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>

**Topics:** [Trusses](Topics#trusses), [CubeTruss](Topics#cubetruss), [FDM Optimized](Topics#fdm-optimized), [Parts](Topics#parts)

**See Also:** [cubetruss\_segment()](#module-cubetruss_segment), [cubetruss\_support()](#module-cubetruss_support), [cubetruss\_corner()](#module-cubetruss_corner)

**Usage:** 

- cubetruss(extents, [clips=], [bracing=], [size=], [strut=], [clipthick=], ...) [ATTACHMENTS];

**Description:** 

Creates a cubetruss truss, assembled out of one or more cubical segments.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`extents`            | Scalar length in cubes of the truss, or for a vector, 2- or 3-vector of cube counts.  An omitted Z count is 1.  Default: 6
`clips`              | A side direction or list of side directions to add clips to.  Default: []
`bracing`            | If true, adds internal cross-braces.  Default: `$cubetruss_bracing` (usually true)
`size`               | The length of each side of the cubetruss cubes.  Default: `$cubetruss_size` (usually 30)
`strut`              | The width of the struts on the cubetruss cubes.  Default: `$cubetruss_strut_size` (usually 4)
`clipthick`          | The thickness of the clips.  Default: `$cubetruss_clip_thickness` (usually 1.6)

<abbr title="These args must be used by name, ie: name=value">By&nbsp;Name</abbr> | What it does
-------------------- | ------------
`anchor`             | Translate so anchor point is at origin (0,0,0).  See [anchor](attachments.scad#subsection-anchor).  Default: `CENTER`
`spin`               | Rotate this many degrees around the Z axis.  See [spin](attachments.scad#subsection-spin).  Default: `0`
`orient`             | Vector to rotate top towards.  See [orient](attachments.scad#subsection-orient).  Default: `UP`

**Example 1:** 

<img align="left" alt="cubetruss() Example 1" src="images/cubetruss/cubetruss.png" width="320" height="240">

    include <BOSL2/std.scad>
    include <BOSL2/cubetruss.scad>
    cubetruss(extents=3);

<br clear="all" /><br/>

**Example 2:** 

<img align="left" alt="cubetruss() Example 2" src="images/cubetruss/cubetruss_2.png" width="320" height="240">

    include <BOSL2/std.scad>
    include <BOSL2/cubetruss.scad>
    cubetruss(extents=3, clips=FRONT);

<br clear="all" /><br/>

**Example 3:** 

<img align="left" alt="cubetruss() Example 3" src="images/cubetruss/cubetruss_3.png" width="320" height="240">

    include <BOSL2/std.scad>
    include <BOSL2/cubetruss.scad>
    cubetruss(extents=3, clips=[FRONT,BACK]);

<br clear="all" /><br/>

**Example 4:** 

<img align="left" alt="cubetruss() Example 4" src="images/cubetruss/cubetruss_4.png" width="320" height="240">

    include <BOSL2/std.scad>
    include <BOSL2/cubetruss.scad>
    cubetruss(extents=[2,3]);

<br clear="all" /><br/>

**Example 5:** 

<img align="left" alt="cubetruss() Example 5" src="images/cubetruss/cubetruss_5.png" width="320" height="240">

    include <BOSL2/std.scad>
    include <BOSL2/cubetruss.scad>
    cubetruss(extents=[1,4,2]);

<br clear="all" /><br/>

**Example 6:** 

<img align="left" alt="cubetruss() Example 6" src="images/cubetruss/cubetruss_6.png" width="320" height="240">

    include <BOSL2/std.scad>
    include <BOSL2/cubetruss.scad>
    cubetruss(extents=[1,4,2], bracing=false);

<br clear="all" /><br/>

---

### Module: cubetruss\_corner()

**Synopsis:** Creates a multi-cube corner cubetruss shape. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>

**Topics:** [Trusses](Topics#trusses), [CubeTruss](Topics#cubetruss), [FDM Optimized](Topics#fdm-optimized), [Parts](Topics#parts)

**See Also:** [cubetruss\_segment()](#module-cubetruss_segment), [cubetruss\_support()](#module-cubetruss_support), [cubetruss()](#module-cubetruss)

**Usage:** 

- cubetruss_corner(h, extents, [bracing=], [size=], [strut=], [clipthick=]);

**Description:** 

Creates a corner cubetruss with extents jutting out in one or more directions.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`h`                  | The number of cubes high to make the base and horizontal extents.  Default: 1
`extents`            | Cube counts extending right, back, left, front, and up from the corner.  A vector may omit trailing zero counts.  A scalar extends right, back, and up equally.  Default: [1,1,0,0,1]
`bracing`            | If true, adds internal cross-braces.  Default: `$cubetruss_bracing` (usually true)
`size`               | The length of each side of the cubetruss cubes.  Default: `$cubetruss_size` (usually 30)
`strut`              | The width of the struts on the cubetruss cubes.  Default: `$cubetruss_strut_size` (usually 4)
`clipthick`          | The thickness of the clips.  Default: `$cubetruss_clip_thickness` (usually 1.6)

<abbr title="These args must be used by name, ie: name=value">By&nbsp;Name</abbr> | What it does
-------------------- | ------------
`anchor`             | Translate so anchor point is at origin (0,0,0).  See [anchor](attachments.scad#subsection-anchor).  Default: `CENTER`
`spin`               | Rotate this many degrees around the Z axis.  See [spin](attachments.scad#subsection-spin).  Default: `0`
`orient`             | Vector to rotate top towards.  See [orient](attachments.scad#subsection-orient).  Default: `UP`

**Example 1:** 

<img align="left" alt="cubetruss\_corner() Example 1" src="images/cubetruss/cubetruss_corner.png" width="320" height="240">

    include <BOSL2/std.scad>
    include <BOSL2/cubetruss.scad>
    cubetruss_corner(extents=2);

<br clear="all" /><br/>

**Example 2:** 

<img align="left" alt="cubetruss\_corner() Example 2" src="images/cubetruss/cubetruss_corner_2.png" width="320" height="240">

    include <BOSL2/std.scad>
    include <BOSL2/cubetruss.scad>
    cubetruss_corner(extents=2, h=2);

<br clear="all" /><br/>

**Example 3:** 

<img align="left" alt="cubetruss\_corner() Example 3" src="images/cubetruss/cubetruss_corner_3.png" width="320" height="240">

    include <BOSL2/std.scad>
    include <BOSL2/cubetruss.scad>
    cubetruss_corner(extents=[3,3,0,0,2]);

<br clear="all" /><br/>

**Example 4:** 

<img align="left" alt="cubetruss\_corner() Example 4" src="images/cubetruss/cubetruss_corner_4.png" width="320" height="240">

    include <BOSL2/std.scad>
    include <BOSL2/cubetruss.scad>
    cubetruss_corner(extents=[3,0,3,0,2]);

<br clear="all" /><br/>

**Example 5:** 

<img align="left" alt="cubetruss\_corner() Example 5" src="images/cubetruss/cubetruss_corner_5.png" width="320" height="240">

    include <BOSL2/std.scad>
    include <BOSL2/cubetruss.scad>
    cubetruss_corner(extents=[3,3,3,3,2]);

<br clear="all" /><br/>

---

### Module: cubetruss\_support()

**Synopsis:** Creates a cubetruss support structure shape. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>

**Topics:** [Trusses](Topics#trusses), [CubeTruss](Topics#cubetruss), [FDM Optimized](Topics#fdm-optimized), [Parts](Topics#parts)

**See Also:** [cubetruss\_segment()](#module-cubetruss_segment), [cubetruss()](#module-cubetruss), [cubetruss\_corner()](#module-cubetruss_corner)

**Usage:** 

- cubetruss_support([size=], [strut=], [extents=]) [ATTACHMENTS];

**Description:** 

Creates a single cubetruss support.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`size`               | The length of each side of the cubetruss cubes.  Default: `$cubetruss_size` (usually 30)
`strut`              | The width of the struts on the cubetruss cubes.  Default: `$cubetruss_strut_size` (usually 4)
`extents`            | If given as an integer, specifies the number of vertical segments for the support.  If given as a list of 3 integers, specifies the number of segments in the X, Y, and Z directions.  Default: 1.

<abbr title="These args must be used by name, ie: name=value">By&nbsp;Name</abbr> | What it does
-------------------- | ------------
`anchor`             | Translate so anchor point is at origin (0,0,0).  See [anchor](attachments.scad#subsection-anchor).  Default: `CENTER`
`spin`               | Rotate this many degrees around the Z axis.  See [spin](attachments.scad#subsection-spin).  Default: `0`
`orient`             | Vector to rotate top towards.  See [orient](attachments.scad#subsection-orient).  Default: `UP`

**Example 1:** 

<img align="left" alt="cubetruss\_support() Example 1" src="images/cubetruss/cubetruss_support.png" width="320" height="240">

    include <BOSL2/std.scad>
    include <BOSL2/cubetruss.scad>
    cubetruss_support();

<br clear="all" /><br/>

**Example 2:** 

<img align="left" alt="cubetruss\_support() Example 2" src="images/cubetruss/cubetruss_support_2.png" width="320" height="240">

    include <BOSL2/std.scad>
    include <BOSL2/cubetruss.scad>
    cubetruss_support(extents=2);

<br clear="all" /><br/>

**Example 3:** 

<img align="left" alt="cubetruss\_support() Example 3" src="images/cubetruss/cubetruss_support_3.png" width="320" height="240">

    include <BOSL2/std.scad>
    include <BOSL2/cubetruss.scad>
    cubetruss_support(extents=3);

<br clear="all" /><br/>

**Example 4:** 

<img align="left" alt="cubetruss\_support() Example 4" src="images/cubetruss/cubetruss_support_4.png" width="320" height="240">

    include <BOSL2/std.scad>
    include <BOSL2/cubetruss.scad>
    cubetruss_support(extents=[2,2,3]);

<br clear="all" /><br/>

**Example 5:** 

<img align="left" alt="cubetruss\_support() Example 5" src="images/cubetruss/cubetruss_support_5.png" width="320" height="240">

    include <BOSL2/std.scad>
    include <BOSL2/cubetruss.scad>
    cubetruss_support(strut=4);

<br clear="all" /><br/>

**Example 6:** 

<img align="left" alt="cubetruss\_support() Example 6" src="images/cubetruss/cubetruss_support_6.png" width="320" height="240">

    include <BOSL2/std.scad>
    include <BOSL2/cubetruss.scad>
    cubetruss_support(extents=2) show_anchors();

<br clear="all" /><br/>

---

## Section: Cubetruss Support


### Module: cubetruss\_foot()

**Synopsis:** Creates a foot that can connect two cubetrusses. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>

**Topics:** [Trusses](Topics#trusses), [CubeTruss](Topics#cubetruss), [FDM Optimized](Topics#fdm-optimized), [Parts](Topics#parts)

**See Also:** [cubetruss\_segment()](#module-cubetruss_segment), [cubetruss\_support()](#module-cubetruss_support), [cubetruss()](#module-cubetruss), [cubetruss\_corner()](#module-cubetruss_corner)

**Usage:** 

- cubetruss_foot(w, [size=], [strut=], [clipthick=]) [ATTACHMENTS];

**Description:** 

Creates a foot that can be clipped onto the bottom of a truss for support.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`w`                  | The number of cube segments to span between the clips.  Default: 1
`size`               | The length of each side of the cubetruss cubes.  Default: `$cubetruss_size` (usually 30)
`strut`              | The width of the struts on the cubetruss cubes.  Default: `$cubetruss_strut_size` (usually 4)
`clipthick`          | The thickness of the clips.  Default: `$cubetruss_clip_thickness` (usually 1.6)

<abbr title="These args must be used by name, ie: name=value">By&nbsp;Name</abbr> | What it does
-------------------- | ------------
`$slop`              | make fit looser to allow for printer overextrusion
`anchor`             | Translate so anchor point is at origin (0,0,0).  See [anchor](attachments.scad#subsection-anchor).  Default: `CENTER`
`spin`               | Rotate this many degrees around the Z axis.  See [spin](attachments.scad#subsection-spin).  Default: `0`
`orient`             | Vector to rotate top towards.  See [orient](attachments.scad#subsection-orient).  Default: `UP`

**Example 1:** 

<img align="left" alt="cubetruss\_foot() Example 1" src="images/cubetruss/cubetruss_foot.png" width="320" height="240">

    include <BOSL2/std.scad>
    include <BOSL2/cubetruss.scad>
    cubetruss_foot(w=1);

<br clear="all" /><br/>

**Example 2:** 

<img align="left" alt="cubetruss\_foot() Example 2" src="images/cubetruss/cubetruss_foot_2.png" width="320" height="240">

    include <BOSL2/std.scad>
    include <BOSL2/cubetruss.scad>
    cubetruss_foot(w=3);

<br clear="all" /><br/>

---

### Module: cubetruss\_joiner()

**Synopsis:** Creates a joiner that can connect two cubetrusses end-to-end. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>

**Topics:** [Trusses](Topics#trusses), [CubeTruss](Topics#cubetruss), [FDM Optimized](Topics#fdm-optimized), [Parts](Topics#parts)

**See Also:** [cubetruss\_segment()](#module-cubetruss_segment), [cubetruss\_support()](#module-cubetruss_support), [cubetruss()](#module-cubetruss), [cubetruss\_corner()](#module-cubetruss_corner)

**Usage:** 

- cubetruss_joiner([w=], [vert=], [size=], [strut=], [clipthick=]) [ATTACHMENTS];

**Description:** 

Creates a part to join two cubetruss trusses end-to-end.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`w`                  | The number of cube segments to span between the clips.  Default: 1
`vert`               | If true, add vertical risers to clip to the ends of the cubetruss trusses.  Default: true
`size`               | The length of each side of the cubetruss cubes.  Default: `$cubetruss_size` (usually 30)
`strut`              | The width of the struts on the cubetruss cubes.  Default: `$cubetruss_strut_size` (usually 4)
`clipthick`          | The thickness of the clips.  Default: `$cubetruss_clip_thickness` (usually 1.6)

<abbr title="These args must be used by name, ie: name=value">By&nbsp;Name</abbr> | What it does
-------------------- | ------------
`$slop`              | Make fit looser by this amount to allow for printer overextrusion
`anchor`             | Translate so anchor point is at origin (0,0,0).  See [anchor](attachments.scad#subsection-anchor).  Default: `CENTER`
`spin`               | Rotate this many degrees around the Z axis.  See [spin](attachments.scad#subsection-spin).  Default: `0`
`orient`             | Vector to rotate top towards.  See [orient](attachments.scad#subsection-orient).  Default: `UP`

**Example 1:** 

<img align="left" alt="cubetruss\_joiner() Example 1" src="images/cubetruss/cubetruss_joiner.png" width="320" height="240">

    include <BOSL2/std.scad>
    include <BOSL2/cubetruss.scad>
    cubetruss_joiner(w=1, vert=false);

<br clear="all" /><br/>

**Example 2:** 

<img align="left" alt="cubetruss\_joiner() Example 2" src="images/cubetruss/cubetruss_joiner_2.png" width="320" height="240">

    include <BOSL2/std.scad>
    include <BOSL2/cubetruss.scad>
    cubetruss_joiner(w=1, vert=true);

<br clear="all" /><br/>

**Example 3:** 

<img align="left" alt="cubetruss\_joiner() Example 3" src="images/cubetruss/cubetruss_joiner_3.png" width="320" height="240">

    include <BOSL2/std.scad>
    include <BOSL2/cubetruss.scad>
    cubetruss_joiner(w=2, vert=true, anchor=BOT);

<br clear="all" /><br/>

---

### Module: cubetruss\_uclip()

**Synopsis:** Creates a joiner that can connect two cubetrusses end-to-end. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>

**Topics:** [Trusses](Topics#trusses), [CubeTruss](Topics#cubetruss), [FDM Optimized](Topics#fdm-optimized), [Parts](Topics#parts)

**See Also:** [cubetruss\_segment()](#module-cubetruss_segment), [cubetruss\_support()](#module-cubetruss_support), [cubetruss()](#module-cubetruss), [cubetruss\_corner()](#module-cubetruss_corner)

**Usage:** 

- cubetruss_uclip(dual, [size=], [strut=], [clipthick=]) [ATTACHMENTS];

**Description:** 

Creates a small clip that can snap around one or two adjacent struts.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`dual`               | If true, create a clip to clip around two adjacent struts.  If false, just fit around one strut.  Default: true
`size`               | The length of each side of the cubetruss cubes.  Default: `$cubetruss_size` (usually 30)
`strut`              | The width of the struts on the cubetruss cubes.  Default: `$cubetruss_strut_size` (usually 4)
`clipthick`          | The thickness of the clips.  Default: `$cubetruss_clip_thickness` (usually 1.6)

<abbr title="These args must be used by name, ie: name=value">By&nbsp;Name</abbr> | What it does
-------------------- | ------------
`$slop`              | Make fit looser by this amount
`anchor`             | Translate so anchor point is at origin (0,0,0).  See [anchor](attachments.scad#subsection-anchor).  Default: `CENTER`
`spin`               | Rotate this many degrees around the Z axis.  See [spin](attachments.scad#subsection-spin).  Default: `0`
`orient`             | Vector to rotate top towards.  See [orient](attachments.scad#subsection-orient).  Default: `UP`

**Example 1:** 

<img align="left" alt="cubetruss\_uclip() Example 1" src="images/cubetruss/cubetruss_uclip.png" width="320" height="240">

    include <BOSL2/std.scad>
    include <BOSL2/cubetruss.scad>
    cubetruss_uclip(dual=false);

<br clear="all" /><br/>

**Example 2:** 

<img align="left" alt="cubetruss\_uclip() Example 2" src="images/cubetruss/cubetruss_uclip_2.png" width="320" height="240">

    include <BOSL2/std.scad>
    include <BOSL2/cubetruss.scad>
    cubetruss_uclip(dual=true);

<br clear="all" /><br/>

---

## Section: Cubetruss Primitives


### Module: cubetruss\_segment()

**Synopsis:** Creates a single cubetruss cube. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>

**Topics:** [Trusses](Topics#trusses), [CubeTruss](Topics#cubetruss), [FDM Optimized](Topics#fdm-optimized), [Parts](Topics#parts)

**See Also:** [cubetruss\_support()](#module-cubetruss_support), [cubetruss()](#module-cubetruss), [cubetruss\_corner()](#module-cubetruss_corner)

**Usage:** 

- cubetruss_segment([size=], [strut=], [bracing=]);

**Description:** 

Creates a single cubetruss cube segment.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`size`               | The length of each side of the cubetruss cubes.  Default: `$cubetruss_size` (usually 30)
`strut`              | The width of the struts on the cubetruss cubes.  Default: `$cubetruss_strut_size` (usually 4)
`bracing`            | If true, adds internal cross-braces.  Default: `$cubetruss_bracing` (usually true)

<abbr title="These args must be used by name, ie: name=value">By&nbsp;Name</abbr> | What it does
-------------------- | ------------
`anchor`             | Translate so anchor point is at origin (0,0,0).  See [anchor](attachments.scad#subsection-anchor).  Default: `CENTER`
`spin`               | Rotate this many degrees around the Z axis.  See [spin](attachments.scad#subsection-spin).  Default: `0`
`orient`             | Vector to rotate top towards.  See [orient](attachments.scad#subsection-orient).  Default: `UP`

**Example 1:** 

<img align="left" alt="cubetruss\_segment() Example 1" src="images/cubetruss/cubetruss_segment.png" width="320" height="240">

    include <BOSL2/std.scad>
    include <BOSL2/cubetruss.scad>
    cubetruss_segment(bracing=false);

<br clear="all" /><br/>

**Example 2:** 

<img align="left" alt="cubetruss\_segment() Example 2" src="images/cubetruss/cubetruss_segment_2.png" width="320" height="240">

    include <BOSL2/std.scad>
    include <BOSL2/cubetruss.scad>
    cubetruss_segment(bracing=true);

<br clear="all" /><br/>

**Example 3:** 

<img align="left" alt="cubetruss\_segment() Example 3" src="images/cubetruss/cubetruss_segment_3.png" width="320" height="240">

    include <BOSL2/std.scad>
    include <BOSL2/cubetruss.scad>
    cubetruss_segment(strut=4);

<br clear="all" /><br/>

**Example 4:** 

<img align="left" alt="cubetruss\_segment() Example 4" src="images/cubetruss/cubetruss_segment_4.png" width="320" height="240">

    include <BOSL2/std.scad>
    include <BOSL2/cubetruss.scad>
    cubetruss_segment(size=40);

<br clear="all" /><br/>

---

### Module: cubetruss\_clip()

**Synopsis:** Creates a clip for the end of a cubetruss to snap-lock it to another cubetruss. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>

**Topics:** [Trusses](Topics#trusses), [CubeTruss](Topics#cubetruss), [FDM Optimized](Topics#fdm-optimized), [Parts](Topics#parts)

**See Also:** [cubetruss\_segment()](#module-cubetruss_segment), [cubetruss\_support()](#module-cubetruss_support), [cubetruss()](#module-cubetruss), [cubetruss\_corner()](#module-cubetruss_corner)

**Usage:** 

- cubetruss_clip(extents, [size=], [strut=], [clipthick=]) [ATTACHMENTS];

**Description:** 

Creates a pair of clips to add onto the end of a truss.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`extents`            | How many cubes to separate the clips by.  Default: 1
`size`               | The length of each side of the cubetruss cubes.  Default: `$cubetruss_size` (usually 30)
`strut`              | The width of the struts on the cubetruss cubes.  Default: `$cubetruss_strut_size` (usually 4)
`clipthick`          | The thickness of the clip.  Default: `$cubetruss_clip_thickness` (usually 1.6)

<abbr title="These args must be used by name, ie: name=value">By&nbsp;Name</abbr> | What it does
-------------------- | ------------
`$slop`              | allowance for printer overextrusion
`anchor`             | Translate so anchor point is at origin (0,0,0).  See [anchor](attachments.scad#subsection-anchor).  Default: `CENTER`
`spin`               | Rotate this many degrees around the Z axis.  See [spin](attachments.scad#subsection-spin).  Default: `0`
`orient`             | Vector to rotate top towards.  See [orient](attachments.scad#subsection-orient).  Default: `UP`

**Example 1:** 

<img align="left" alt="cubetruss\_clip() Example 1" src="images/cubetruss/cubetruss_clip.png" width="320" height="240">

    include <BOSL2/std.scad>
    include <BOSL2/cubetruss.scad>
    cubetruss_clip(extents=2);

<br clear="all" /><br/>

**Example 2:** 

<img align="left" alt="cubetruss\_clip() Example 2" src="images/cubetruss/cubetruss_clip_2.png" width="320" height="240">

    include <BOSL2/std.scad>
    include <BOSL2/cubetruss.scad>
    cubetruss_clip(extents=1);

<br clear="all" /><br/>

**Example 3:** 

<img align="left" alt="cubetruss\_clip() Example 3" src="images/cubetruss/cubetruss_clip_3.png" width="320" height="240">

    include <BOSL2/std.scad>
    include <BOSL2/cubetruss.scad>
    cubetruss_clip(clipthick=2.5);

<br clear="all" /><br/>

---

### Function: cubetruss\_dist()

**Synopsis:** Returns the length of a cubetruss truss.

**Topics:** [Trusses](Topics#trusses), [CubeTruss](Topics#cubetruss), [FDM Optimized](Topics#fdm-optimized), [Parts](Topics#parts)

**See Also:** [cubetruss\_segment()](#module-cubetruss_segment), [cubetruss\_support()](#module-cubetruss_support), [cubetruss()](#module-cubetruss), [cubetruss\_corner()](#module-cubetruss_corner)

**Usage:** 

- length = cubetruss_dist(cubes, [gaps], [size=], [strut=]);

**Description:** 

Function to calculate the length of a cubetruss truss.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`cubes`              | The number of cubes along the truss's length.  Default: 0
`gaps`               | The number of extra strut widths to add in, corresponding to each time a truss butts up against another.  Default: 0
`size`               | The length of each side of the cubetruss cubes.  Default: `$cubetruss_size` (usually 30)
`strut`              | The width of the struts on the cubetruss cubes.  Default: `$cubetruss_strut_size` (usually 4)

---


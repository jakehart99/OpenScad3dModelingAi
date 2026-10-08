![BOSL2 Logo](https://raw.githubusercontent.com/BelfrySCAD/BOSL2/master/images/BOSL2logo.png)

# Belfry OpenSCAD Library v2

## Documentation Indices

- [Index by File (Table of Contents)](TOC)
- [Index by Function/Module Name](AlphaIndex)
- [Index by Topic](Topics)
- [Usage Cheat Sheet](CheatSheet)
- [List of Tutorials](Tutorials)

## Overview

The BOSL2 library is an enormous library that provides many different kinds of capabilities to simplify the development of models in OpenSCAD, and to make things possible that are difficult in native OpenSCAD.  Some of the things BOSL2 provides are:

* **Shorthands.** The shorthands make your code a little shorter, and more importantly, they can make it significantly easier to read.  Compare `up(x)` to `translate([0,0,x])`.  The shorthands include operations for creating [copies of objects](https://github.com/BelfrySCAD/BOSL2/wiki/distributors.scad) and for applying [transformations](https://github.com/BelfrySCAD/BOSL2/wiki/transforms.scad) to objects, including [rot()](https://github.com/BelfrySCAD/BOSL2/wiki/transforms.scad#functionmodule-rot) which extends rotate in some useful ways that are not easy to do directly. 
* **Attachments.**  Unless you make models containing just one object the attachments features can revolutionize your modeling.  They let you position components of a model relative to other components so you don't have to keep track of the positions and orientations of parts of the model.  You can instead place an something on the TOP of something else, perhaps aligned to the RIGHT.  For a full introduction to attachments, consult the [Attachments Tutorial.](https://github.com/BelfrySCAD/BOSL2/wiki/Tutorial-Attachment-Overview)
* **Rounding and filleting.**  Rounding and filleting is hard in OpenSCAD.  The library provides modules like [cuboid()](https://github.com/BelfrySCAD/BOSL2/wiki/shapes3d.scad#module-cuboid) to make a cube with any of the edges rounded, [offset_sweep()](https://github.com/BelfrySCAD/BOSL2/wiki/rounding.scad#functionmodule-offset_sweep) to round the ends of a linear extrusion, and [prism_connector()](https://github.com/BelfrySCAD/BOSL2/wiki/rounding.scad#module-prism_connector) which works with the attachments feature to create filleted prisms between a variety of objects, or even rounded holes through a single object.  You can also use [edge_profile()](https://github.com/BelfrySCAD/BOSL2/wiki/attachments.scad#module-edge_profile) to apply a variety of different mask profiles to chosen edges of a cubic shape, or you can directly subtract 3d mask shapes from an edge of objects that are not cubes. 
* **Complex object support.**  The [path_sweep()](https://github.com/BelfrySCAD/BOSL2/wiki/skin.scad#functionmodule-path_sweep) function/module takes a 2d polygon moves it through space along a path and sweeps out a 3d shape as it moves.  You can link together a series of arbitrary polygons with [skin()](https://github.com/BelfrySCAD/BOSL2/wiki/skin.scad#functionmodule-skin) or [vnf_vertex_array().](https://github.com/BelfrySCAD/BOSL2/wiki/vnf.scad#functionmodule-vnf_vertex_array)  Support for [beziers](https://github.com/BelfrySCAD/BOSL2/wiki/beziers.scad) and [NURBS](https://github.com/BelfrySCAD/BOSL2/wiki/nurbs.scad) can help you construct the building blocks you need.  [Metaballs](https://github.com/BelfrySCAD/BOSL2/wiki/isosurface.scad#functionmodule-metaballs) can create organic surfaces that blend shapes together.  
* **Building Blocks.** OpenSCAD provides cubes, cones and spheres.  The BOSL2 library extends this to provide different kinds of prisms, tubes, and other abstract geometrical building blocks. In many cases the BOSL2 objects include options to round their edges.  Basic objects have extensions like the ability to specify the **inner** radius of a circle to create holes with a guaranteed minimum size.  
* **Texturing.**  Many kinds of objects can be created with [textures](https://github.com/BelfrySCAD/BOSL2/wiki/skin.scad#section-texturing) applied.  This can create knurling, but it can do much more than that.  A texture can be any repeating pattern, and applying a texture can actually replace the base object with something different based on repeating copies of the texture element.  A texture can also be an image; using texturing you can emboss an arbitrary image onto your model. 
* **Parts library.**  The parts library includes many useful specific functional parts including [gears](https://github.com/BelfrySCAD/BOSL2/wiki/gears.scad), generic [threading](https://github.com/BelfrySCAD/BOSL2/wiki/threading.scad#section-generic-threading), and specific threading to match plastic [bottles](https://github.com/BelfrySCAD/BOSL2/wiki/bottlecaps.scad), [pipe fittings](https://github.com/BelfrySCAD/BOSL2/wiki/threading.scad#module-npt_threaded_rod), or standard [screws.](https://github.com/BelfrySCAD/BOSL2/wiki/screws.scad)  Also included are [clips](https://github.com/BelfrySCAD/BOSL2/wiki/joiners.scad#section-tension-clips), [hinges](https://github.com/BelfrySCAD/BOSL2/wiki/hinges.scad), and [dovetail joints.](https://github.com/BelfrySCAD/BOSL2/wiki/joiners.scad#section-dovetails)
* **Geometrical operations on data.**  In OpenSCAD, geometrical operations happen on geometry, and information can never be extracted from geometry.  The BOLS2 library provides operations on 2d point lists (called "paths" or "regions") to make [rounded paths](https://github.com/BelfrySCAD/BOSL2/wiki/rounding.scad#function-round_corners) from ones with corners or do operations like [intersection](https://github.com/BelfrySCAD/BOSL2/wiki/regions.scad#functionmodule-intersection) and [offset](https://github.com/BelfrySCAD/BOSL2/wiki/regions.scad#function-offset).  It can also do some limited operations on three dimensional data.
* **Programming aids.** The library provides basic [mathematical operations](https://github.com/BelfrySCAD/BOSL2/wiki/math.scad) including solutions to [linear systems of equations](https://github.com/BelfrySCAD/BOSL2/wiki/linalg.scad#function-linear_solve) and [generic](https://github.com/BelfrySCAD/BOSL2/wiki/math.scad#function-root_find) and [polynomial](https://github.com/BelfrySCAD/BOSL2/wiki/math.scad#function-real_roots) numerical root finding.  It provides [geometrical operations](https://github.com/BelfrySCAD/BOSL2/wiki/geometry.scad) like [line intersection](https://github.com/BelfrySCAD/BOSL2/wiki/geometry.scad#function-line_intersection) or [circle intersection](https://github.com/BelfrySCAD/BOSL2/wiki/geometry.scad#function-circle_circle_intersection), [coordinate transformations](https://github.com/BelfrySCAD/BOSL2/wiki/coords.scad), [string manipulation,](https://github.com/BelfrySCAD/BOSL2/wiki/strings.scad) and [list processing](https://github.com/BelfrySCAD/BOSL2/wiki/lists.scad).   

## Installation

1. Download the .zip or .tar.gz release file for this library.  Currently you should be able to find this at https://github.com/BelfrySCAD/BOSL2/archive/refs/heads/master.zip
2. Unpack it. Make sure that you unpack the whole file structure. Some zipfile unpackers call this option "Use folder names". It should create either a `BOSL-v2.0` or `BOSL2-master` directory with the library files within it.  You should see "examples", "scripts", "tests", and other subdirectories.
3. Rename the unpacked main directory to `BOSL2`.
4. Move the `BOSL2` directory into the apropriate OpenSCAD library directory.  The library directory may be on the list below, but for SNAP or other prepackaged installations, it is probably somewhere else.  To find it, run OpenSCAD and select Help&rarr;Library Info, and look for the entry that says "User Library Path".  This is your default library directory.  You may choose to change it to something more convenient by setting the environment variable OPENSCADPATH.  Using this variable also means that all versions of OpenSCAD you install will look for libraries in the same location.  
    - Windows: `My Documents\OpenSCAD\libraries\`
    - Linux: `$HOME/.local/share/OpenSCAD/libraries/`
    - Mac OS X: `$HOME/Documents/OpenSCAD/libraries/`
5. Restart OpenSCAD.


## Other Libraries that Synergize with BOSL2

- [Pathbuilder](https://github.com/dinther/pathbuilder) – SVG path string parsing.
- [Attachable Text3d](https://github.com/jon-gilbert/openscad_attachable_text3d) - FontMetrics aware attachable text for BOSL2.
- [JL_SCAD](https://github.com/lijon/jl_scad) - A Library to make enclosures for electronics projects, with BOSL2.

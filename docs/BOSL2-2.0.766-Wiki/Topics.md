# Topic Index

An index of topics, with related functions, modules, and constants.

**A**: [Affine](#affine), [Angle](#angle), [Area](#area), [Argument Handling](#argument-handling), [Arrays](#arrays), [Attachable](#attachable), [Attachment](#attachment), [Attachments](#attachments)

**B**: [Bearings](#bearings), [Bezier Curves](#bezier-curves), [Bezier Patches](#bezier-patches), [Bezier Paths](#bezier-paths), [Boolean Operations](#boolean-operations), [Boolean Testing](#boolean-testing), [Bottles](#bottles), [Bounding Boxes](#bounding-boxes), [Bounds](#bounds)

**C**: [Calculus](#calculus), [Centroid](#centroid), [Chamfers](#chamfers), [Circles](#circles), [Clockwise](#clockwise), [Closest](#closest), [Collinearity](#collinearity), [Collision](#collision), [Colors](#colors), [Colorspace](#colorspace), [Comparators](#comparators), [Comparison](#comparison), [Comparisons](#comparisons), [Complex Numbers](#complex-numbers), [Constants](#constants), [Contours](#contours), [Convexity](#convexity), [Coordinates](#coordinates), [Copiers](#copiers), [Coplanarity](#coplanarity), [CubeTruss](#cubetruss), [Cylinders](#cylinders)

**D**: [Data Structures](#data-structures), [Debugging](#debugging), [Descriptions](#descriptions), [Dictionaries](#dictionaries), [Distance](#distance), [Distributors](#distributors), [Drawing Tools](#drawing-tools)

**E**: [Error Checking](#error-checking), [Extrusion](#extrusion), [Extrusions](#extrusions)

**F**: [FDM Optimized](#fdm-optimized), [Filters](#filters), [Function Literals](#function-literals), [Function Plotting](#function-plotting)

**G**: [Gears](#gears), [Geometry](#geometry)

**H**: [Hashing](#hashing), [Hinges](#hinges), [Hulling](#hulling)

**I**: [Indexing](#indexing), [Interpolation](#interpolation), [Intersection](#intersection), [Isosurfaces](#isosurfaces), [Iteration](#iteration)

**J**: [Joiners](#joiners)

**L**: [Linear Algebra](#linear-algebra), [Lines](#lines), [List Handling](#list-handling), [Lists](#lists), [Logic](#logic), [Looping](#looping)

**M**: [Masking](#masking), [Masks](#masks), [Masks (2D)](#masks-2d), [Math](#math), [Math Operators](#math-operators), [Matrices](#matrices), [Metaballs](#metaballs), [Mini-Language](#mini-language), [Mirroring](#mirroring), [Miscellaneous](#miscellaneous), [Modifiers](#modifiers), [Modular Hose](#modular-hose), [Motors](#motors)

**N**: [NURBS](#nurbs), [NURBS Curves](#nurbs-curves), [NURBS Patches](#nurbs-patches), [NURBS Surfaces](#nurbs-surfaces)

**O**: [Offsets](#offsets)

**P**: [Partitions](#partitions), [Parts](#parts), [Path Generators](#path-generators), [Path Generators (2D)](#path-generators-2d), [Path Generators (3D)](#path-generators-3d), [Path Subdivision](#path-subdivision), [Paths](#paths), [Paths (2D)](#paths-2d), [Paths (3D)](#paths-3d), [Planes](#planes), [Points](#points), [Polygon](#polygon), [Polygons](#polygons), [Polyhedra](#polyhedra), [Projection](#projection)

**Q**: [Quantization](#quantization)

**R**: [Random](#random), [Reflection](#reflection), [Regions](#regions), [Revolution](#revolution), [Rotation](#rotation), [Rounding](#rounding)

**S**: [Scaling](#scaling), [Screws](#screws), [Search](#search), [Searching](#searching), [Segments](#segments), [Set Handling](#set-handling), [Shapes](#shapes), [Shapes (2D)](#shapes-2d), [Shapes (3D)](#shapes-3d), [Shapes2D](#shapes2d), [Shapes3D](#shapes3d), [Shearing](#shearing), [Shell](#shell), [Skewing](#skewing), [Skin](#skin), [Skinning](#skinning), [Sliders](#sliders), [Slop](#slop), [Spheres](#spheres), [Spiral](#spiral), [Statistics](#statistics), [String Operators](#string-operators), [Strings](#strings), [Sweep](#sweep)

**T**: [Tangents](#tangents), [Test](#test), [Testing](#testing), [Text](#text), [Textures](#textures), [Threading](#threading), [Transformations](#transformations), [Transforms](#transforms), [Translation](#translation), [Triangles](#triangles), [Triangulation](#triangulation), [Trigonometry](#trigonometry), [Trusses](#trusses), [Type Checking](#type-checking), [Type Conversion](#type-conversion), [Type Queries](#type-queries)

**U**: [Undef Handling](#undef-handling)

**V**: [VNF Generators](#vnf-generators), [VNF Manipulation](#vnf-manipulation), [Vectors](#vectors), [Versioning](#versioning), [versioning](#versioning)

**W**: [Walls](#walls), [Wiring](#wiring)

### Affine

- [`apply()`](transforms.scad#function-apply) Func – Applies a transformation matrix to a point, list of points, array of points, or a VNF. <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return a transformation matrix.">[<abbr>Mat</abbr>]</sup>
- [`back()`](transforms.scad#functionmodule-back) Func/Mod – Translates children backward (Y+). <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return a transformation matrix.">[<abbr>Mat</abbr>]</sup>
- [`diagonal_matrix()`](linalg.scad#function-diagonal_matrix) Func – Make a diagonal matrix.
- [`down()`](transforms.scad#functionmodule-down) Func/Mod – Translates children downward (Z-). <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return a transformation matrix.">[<abbr>Mat</abbr>]</sup>
- [`frame_map()`](transforms.scad#functionmodule-frame_map) Func/Mod – Rotates and possibly skews children from one frame of reference to another. <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return a transformation matrix.">[<abbr>Mat</abbr>]</sup>
- [`fwd()`](transforms.scad#functionmodule-fwd) Func/Mod – Translates children forward (Y-). <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return a transformation matrix.">[<abbr>Mat</abbr>]</sup>
- [`IDENT`](constants.scad#constant-ident) Const – A constant, the 3D identity transformation matrix. <sup title="Can return a transformation matrix.">[<abbr>Mat</abbr>]</sup>
- [`ident()`](linalg.scad#function-ident) Func – Return identity matrix.
- [`is_rotation()`](linalg.scad#function-is_rotation) Func – Check if a transformation matrix represents a rotation.
- [`left()`](transforms.scad#functionmodule-left) Func/Mod – Translates children leftward (X-). <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return a transformation matrix.">[<abbr>Mat</abbr>]</sup>
- [`mirror()`](transforms.scad#functionmodule-mirror) Func/Mod – Reflects children across an arbitrary plane. <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return a transformation matrix.">[<abbr>Mat</abbr>]</sup> <sup title="Extends the OpenScad keyword of the same name.">[<abbr>Ext</abbr>]</sup>
- [`move()`](transforms.scad#functionmodule-move) Func/Mod – Translates children in an arbitrary direction. <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return a transformation matrix.">[<abbr>Mat</abbr>]</sup>
- [`right()`](transforms.scad#functionmodule-right) Func/Mod – Translates children rightward (X+). <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return a transformation matrix.">[<abbr>Mat</abbr>]</sup>
- [`rot()`](transforms.scad#functionmodule-rot) Func/Mod – Rotates children in various ways. <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return a transformation matrix.">[<abbr>Mat</abbr>]</sup>
- [`rot_decode()`](geometry.scad#function-rot_decode) Func – Extract axis and rotation angle from a rotation matrix.
- [`rot_inverse()`](linalg.scad#function-rot_inverse) Func – Invert 2d or 3d rotation transformations.
- [`scale()`](transforms.scad#functionmodule-scale) Func/Mod – Scales children arbitrarily. <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return a transformation matrix.">[<abbr>Mat</abbr>]</sup> <sup title="Extends the OpenScad keyword of the same name.">[<abbr>Ext</abbr>]</sup>
- [`skew()`](transforms.scad#functionmodule-skew) Func/Mod – Skews (or shears) children along various axes. <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return a transformation matrix.">[<abbr>Mat</abbr>]</sup>
- [`tilt()`](transforms.scad#functionmodule-tilt) Func/Mod – Tilts children toward a direction <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return a transformation matrix.">[<abbr>Mat</abbr>]</sup>
- [`move()`](transforms.scad#functionmodule-move) Func/Mod – Translates children in an arbitrary direction. <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return a transformation matrix.">[<abbr>Mat</abbr>]</sup>
- [`up()`](transforms.scad#functionmodule-up) Func/Mod – Translates children upward (Z+). <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return a transformation matrix.">[<abbr>Mat</abbr>]</sup>
- [`xflip()`](transforms.scad#functionmodule-xflip) Func/Mod – Reflects children across the YZ plane. <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return a transformation matrix.">[<abbr>Mat</abbr>]</sup>
- [`right()`](transforms.scad#functionmodule-right) Func/Mod – Translates children rightward (X+). <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return a transformation matrix.">[<abbr>Mat</abbr>]</sup>
- [`xrot()`](transforms.scad#functionmodule-xrot) Func/Mod – Rotates children around the X axis using the right-hand rule. <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return a transformation matrix.">[<abbr>Mat</abbr>]</sup>
- [`xscale()`](transforms.scad#functionmodule-xscale) Func/Mod – Scales children along the X axis. <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return a transformation matrix.">[<abbr>Mat</abbr>]</sup>
- [`yflip()`](transforms.scad#functionmodule-yflip) Func/Mod – Reflects children across the XZ plane. <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return a transformation matrix.">[<abbr>Mat</abbr>]</sup>
- [`back()`](transforms.scad#functionmodule-back) Func/Mod – Translates children backward (Y+). <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return a transformation matrix.">[<abbr>Mat</abbr>]</sup>
- [`yrot()`](transforms.scad#functionmodule-yrot) Func/Mod – Rotates children around the Y axis using the right-hand rule. <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return a transformation matrix.">[<abbr>Mat</abbr>]</sup>
- [`yscale()`](transforms.scad#functionmodule-yscale) Func/Mod – Scales children along the Y axis. <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return a transformation matrix.">[<abbr>Mat</abbr>]</sup>
- [`zflip()`](transforms.scad#functionmodule-zflip) Func/Mod – Reflects children across the XY plane. <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return a transformation matrix.">[<abbr>Mat</abbr>]</sup>
- [`up()`](transforms.scad#functionmodule-up) Func/Mod – Translates children upward (Z+). <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return a transformation matrix.">[<abbr>Mat</abbr>]</sup>
- [`zrot()`](transforms.scad#functionmodule-zrot) Func/Mod – Rotates children around the Z axis using the right-hand rule. <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return a transformation matrix.">[<abbr>Mat</abbr>]</sup>
- [`zscale()`](transforms.scad#functionmodule-zscale) Func/Mod – Scales children along the Z axis. <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return a transformation matrix.">[<abbr>Mat</abbr>]</sup>

### Angle

- [`plane_line_angle()`](geometry.scad#function-plane_line_angle) Func – Returns the angle between a plane and a 3d line.

### Area

- [`polygon_area()`](geometry.scad#function-polygon_area) Func – Calculate area of a 2d or 3d polygon.
- [`region_area()`](regions.scad#function-region_area) Func – Computes the area of the specified valid [region](Glossary#region).

### Argument Handling

- [`get_anchor()`](utility.scad#function-get_anchor) Func – Returns the correct anchor from `anchor` and `center`.
- [`get_radius()`](utility.scad#function-get_radius) Func – Given various radii and diameters, returns the most specific radius.
- [`scalar_vec3()`](utility.scad#function-scalar_vec3) Func – Expands a scalar or a list with length less than 3 to a length 3 vector.

### Arrays

- [`block_matrix()`](linalg.scad#function-block_matrix) Func – Make a new matrix from a block of matrices.
- [`column()`](linalg.scad#function-column) Func – Extract a column from a matrix.
- [`hstack()`](linalg.scad#function-hstack) Func – Make a new matrix by stacking matrices horizontally.
- [`submatrix()`](linalg.scad#function-submatrix) Func – Extract a submatrix from a matrix
- [`submatrix_set()`](linalg.scad#function-submatrix_set) Func – Takes a matrix as input and change values in a submatrix.

### Attachable

- [`cube()`](shapes3d.scad#functionmodule-cube) Func/Mod – Creates a cube with anchors for attaching children. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Extends the OpenScad keyword of the same name.">[<abbr>Ext</abbr>]</sup>
- [`cuboid()`](shapes3d.scad#module-cuboid) Mod – Creates a cube with chamfering and roundovers. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`cylinder()`](shapes3d.scad#functionmodule-cylinder) Func/Mod – Creates an attachable cylinder. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Extends the OpenScad keyword of the same name.">[<abbr>Ext</abbr>]</sup>
- [`egg()`](shapes2d.scad#functionmodule-egg) Func/Mod – Creates an egg-shaped 2d object. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`ellipse()`](shapes2d.scad#functionmodule-ellipse) Func/Mod – Creates the approximation of an ellipse or a circle. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`fillet()`](shapes3d.scad#module-fillet) Mod – Creates a smooth fillet between two faces. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup>
- [`glued_circles()`](shapes2d.scad#functionmodule-glued_circles) Func/Mod – Creates a shape of two circles joined by a curved waist. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`hemicyl()`](shapes3d.scad#module-hemicyl) Mod – Creates a half cylinder, with optional rounding or chamfers on the flat face.
- [`hexagon()`](shapes2d.scad#functionmodule-hexagon) Func/Mod – Creates a regular hexagon. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`keyhole()`](shapes2d.scad#functionmodule-keyhole) Func/Mod – Creates a 2D keyhole shape. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`mask2d_chamfer()`](masks.scad#functionmodule-mask2d_chamfer) Func/Mod – Produces a 2D chamfer mask shape. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`mask2d_cove()`](masks.scad#functionmodule-mask2d_cove) Func/Mod – Creates a 2D cove (quarter-round) mask shape. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`mask2d_dovetail()`](masks.scad#functionmodule-mask2d_dovetail) Func/Mod – Creates a 2D dovetail mask shape. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`mask2d_ogee()`](masks.scad#functionmodule-mask2d_ogee) Func/Mod – Creates a 2D ogee mask shape. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`mask2d_rabbet()`](masks.scad#functionmodule-mask2d_rabbet) Func/Mod – Creates a rabbet mask shape. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`mask2d_roundover()`](masks.scad#functionmodule-mask2d_roundover) Func/Mod – Creates a circular mask shape for rounding edges or beading. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`mask2d_smooth()`](masks.scad#functionmodule-mask2d_smooth) Func/Mod – Creates a continuous curvature mask for rounding edges. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`mask2d_teardrop()`](masks.scad#functionmodule-mask2d_teardrop) Func/Mod – Creates a 2D teardrop shape with specified max angle from vertical. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`octagon()`](shapes2d.scad#functionmodule-octagon) Func/Mod – Creates a regular octagon. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`octahedron()`](shapes3d.scad#functionmodule-octahedron) Func/Mod – Creates an octahedron with axis-aligned points. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup>
- [`onion()`](shapes3d.scad#functionmodule-onion) Func/Mod – Creates an attachable onion-like shape. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup>
- [`pentagon()`](shapes2d.scad#functionmodule-pentagon) Func/Mod – Creates a regular pentagon. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`pie_slice()`](shapes3d.scad#functionmodule-pie_slice) Func/Mod – Creates a pie slice shape. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup>
- [`prismoid()`](shapes3d.scad#functionmodule-prismoid) Func/Mod – Creates a rectangular prismoid shape with optional roundovers and chamfering. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup>
- [`rect()`](shapes2d.scad#functionmodule-rect) Func/Mod – Creates a 2d rectangle with optional corner rounding. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`rect_tube()`](shapes3d.scad#module-rect_tube) Mod – Creates a rectangular tube. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`regular_ngon()`](shapes2d.scad#functionmodule-regular_ngon) Func/Mod – Creates a regular N-sided polygon. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`regular_prism()`](shapes3d.scad#functionmodule-regular_prism) Func/Mod – Creates a regular prism with roundovers and chamfering <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup>
- [`reuleaux_polygon()`](shapes2d.scad#functionmodule-reuleaux_polygon) Func/Mod – Creates a constant-width shape that is not circular. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`right_triangle()`](shapes2d.scad#functionmodule-right_triangle) Func/Mod – Creates a right triangle. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`ring()`](shapes2d.scad#functionmodule-ring) Func/Mod – Draws a 2D ring or partial ring or returns a region or path <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Region.">[<abbr>Region</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`semicircle()`](shapes2d.scad#functionmodule-semicircle) Func/Mod – Creates a semicircle with optional roundings or chamfers <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`sphere()`](shapes3d.scad#functionmodule-sphere) Func/Mod – Creates an attachable spherical object. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Extends the OpenScad keyword of the same name.">[<abbr>Ext</abbr>]</sup>
- [`spheroid()`](shapes3d.scad#functionmodule-spheroid) Func/Mod – Creates an attachable spherical object with controllable triangulation. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup>
- [`squircle()`](shapes2d.scad#functionmodule-squircle) Func/Mod – Creates a shape between a circle and a square. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`star()`](shapes2d.scad#functionmodule-star) Func/Mod – Creates a star-shaped polygon or returns a star-shaped region. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`supershape()`](shapes2d.scad#functionmodule-supershape) Func/Mod – Creates a 2D [Superformula](https://en.wikipedia.org/wiki/Superformula) shape. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`teardrop()`](shapes3d.scad#functionmodule-teardrop) Func/Mod – Creates a teardrop shape. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup>
- [`teardrop2d()`](shapes2d.scad#functionmodule-teardrop2d) Func/Mod – Creates a 2D teardrop shape. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`textured_tile()`](shapes3d.scad#functionmodule-textured_tile) Func/Mod – Creates a cube or trapezoidal prism with a textured top face for attaching to objects. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup>
- [`torus()`](shapes3d.scad#functionmodule-torus) Func/Mod – Creates an attachable torus. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup>
- [`trapezoid()`](shapes2d.scad#functionmodule-trapezoid) Func/Mod – Creates a trapezoid with parallel top and bottom sides. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`tube()`](shapes3d.scad#module-tube) Mod – Creates a cylindrical or conical tube. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`wedge()`](shapes3d.scad#functionmodule-wedge) Func/Mod – Creates a 3d triangular wedge. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup>

### Attachment

- [`attach_part()`](attachments.scad#module-attach_part) Mod – Select a named attachable part for subsequent attachment operations
- [`desc_dir()`](attachments.scad#function-desc_dir) Func – Computes the direction in the current context of a direction or anchor in a description's context
- [`EDGE()`](constants.scad#function-edge) Func – Named edge anchor constants
- [`FACE()`](constants.scad#function-face) Func – Named face anchor constants

### Attachments

- [`align()`](attachments.scad#module-align) Mod – Position children with alignment to parent edges. <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup>
- [`anchor_arrow()`](attachments.scad#module-anchor_arrow) Mod – Shows a 3d anchor orientation arrow. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`anchor_arrow2d()`](attachments.scad#module-anchor_arrow2d) Mod – Shows a 2d anchor orientation arrow. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`attach()`](attachments.scad#module-attach) Mod – Attaches children to a parent object at an anchor point and with anchor orientation. <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup>
- [`attach_geom()`](attachments.scad#function-attach_geom) Func – Returns the internal geometry description of an attachable object.
- [`attachable()`](attachments.scad#module-attachable) Mod – Manages the anchoring, spin, orientation, and attachments for an object.
- [`change_anchors()`](attachments.scad#module-change_anchors) Mod – Changes the named anchors inherited from the parent
- [`color_this()`](color.scad#module-color_this) Mod – Sets the color for attachable children at the current level only. <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup>
- [`conv_hull()`](attachments.scad#module-conv_hull) Mod – Performs a hull operation on the children using tags to determine what happens.
- [`corner_mask()`](masks.scad#module-corner_mask) Mod – Attaches a 3d mask shape to the given corners of the parent. <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup>
- [`corner_profile()`](masks.scad#module-corner_profile) Mod – Rotationally extrudes a 2d edge profile into corner mask on the given corners of the parent. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`default_tag()`](attachments.scad#module-default_tag) Mod – Conditionally set a default tag for all children.
- [`define_part()`](attachments.scad#function-define_part) Func – Creates an attachable part data structure.
- [`desc_dist()`](attachments.scad#function-desc_dist) Func – Computes the distance between two points specified by attachable descriptions
- [`desc_point()`](attachments.scad#function-desc_point) Func – Computes the location in the current context of an anchor point from an attachable description
- [`diff()`](attachments.scad#module-diff) Mod – Performs a differencing operation using tags rather than hierarchy to control what happens.
- [`edge_mask()`](masks.scad#module-edge_mask) Mod – Attaches a 3D mask shape to the given edges of the parent. <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup>
- [`edge_profile()`](masks.scad#module-edge_profile) Mod – Extrudes a 2d edge profile into a mask on edges of the parent cuboid, prismoid or cone. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`edge_profile_asym()`](masks.scad#module-edge_profile_asym) Mod – Extrudes an asymmetric 2D profile into a mask on edges and corners of the parent cuboid. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`expose_anchors()`](attachments.scad#module-expose_anchors) Mod – Used to show a transparent object with solid color anchor arrows.
- [`face_mask()`](masks.scad#module-face_mask) Mod – Ataches a 3d mask shape to the given faces of the parent. <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup>
- [`face_profile()`](masks.scad#module-face_profile) Mod – Extrudes a 2D edge profile into a mask for all edges and corners of the given faces on the parent. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`force_tag()`](attachments.scad#module-force_tag) Mod – Assigns a tag to a non-attachable object.
- [`frame_ref()`](attachments.scad#module-frame_ref) Mod – Shows axis orientation arrows. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`generic_airplane()`](attachments.scad#module-generic_airplane) Mod – Shows a generic airplane shape, useful for viewing orientations. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`ghost()`](color.scad#module-ghost) Mod – Sets % modifier for attachable children and their descendants. <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup>
- [`ghost_this()`](color.scad#module-ghost_this) Mod – Apply % modifier to children at a single level. <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup>
- [`hide()`](attachments.scad#module-hide) Mod – Hides attachable children with the given tags.
- [`hide_this()`](attachments.scad#module-hide_this) Mod – Hides attachable children at the current level
- [`highlight()`](color.scad#module-highlight) Mod – Sets # modifier for attachable children and their descendants. <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup>
- [`highlight_this()`](color.scad#module-highlight_this) Mod – Apply # modifier to children at a single level. <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup>
- [`intersect()`](attachments.scad#module-intersect) Mod – Perform an intersection operation on children using tags rather than hierarchy to control what happens.
- [`named_anchor()`](attachments.scad#function-named_anchor) Func – Creates an anchor data structure.
- [`orient()`](attachments.scad#module-orient) Mod – Orients children's tops in the directon of the specified anchor. <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup>
- [`parent()`](attachments.scad#function-parent) Func – Returns a description (transformation state and attachment geometry) of the parent
- [`parent_part()`](attachments.scad#function-parent_part) Func – Returns a description (transformation state and attachment geometry) of a part defined by the parent
- [`position()`](attachments.scad#module-position) Mod – Attaches children to a parent object at an anchor point. <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup>
- [`recolor()`](color.scad#module-recolor) Mod – Sets the color for attachable children and their descendants. <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup>
- [`reorient()`](attachments.scad#function-reorient) Func – Calculates the transformation matrix needed to reorient an object. <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup>
- [`restore()`](attachments.scad#module-restore) Mod – Restores transformation state and attachment geometry from a description
- [`show_all()`](attachments.scad#module-show_all) Mod – Shows all children and clears tags.
- [`show_anchors()`](attachments.scad#module-show_anchors) Mod – Shows anchors for the parent object. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`show_int()`](attachments.scad#module-show_int) Mod – Shows children with the listed tags that were already shown in the parent context.
- [`show_only()`](attachments.scad#module-show_only) Mod – Show only the children with the listed tags.
- [`show_transform_list()`](attachments.scad#module-show_transform_list) Mod – Shows a list of transforms and how they connect. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`tag()`](attachments.scad#module-tag) Mod – Assigns a tag to an object
- [`tag_conv_hull()`](attachments.scad#module-tag_conv_hull) Mod – Performs a [`conv_hull()`](#module-conv\_hull) and then sets a tag on the result.
- [`tag_diff()`](attachments.scad#module-tag_diff) Mod – Performs a [`diff()`](#module-diff) and then sets a tag on the result.
- [`tag_intersect()`](attachments.scad#module-tag_intersect) Mod – Performs an [`intersect()`](#module-intersect) and then tags the result.
- [`tag_scope()`](attachments.scad#module-tag_scope) Mod – Creates a new tag scope.
- [`tag_this()`](attachments.scad#module-tag_this) Mod – Assigns a tag to an object at the current level only.
- [`text()`](shapes2d.scad#module-text) Mod – Creates an attachable block of text. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`text3d()`](shapes3d.scad#module-text3d) Mod – Creates an attachable 3d text block. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`transform_desc()`](attachments.scad#function-transform_desc) Func – Applies a transformation matrix to a description

### Bearings

- [`ball_bearing()`](ball_bearings.scad#module-ball_bearing) Mod – Creates a standardized ball bearing assembly. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`ball_bearing_info()`](ball_bearings.scad#function-ball_bearing_info) Func – Returns dimensional and feature information for a standardized ball bearing assembly.
- [`linear_bearing()`](linear_bearings.scad#module-linear_bearing) Mod – Creates a generic linear bearing cartridge. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`linear_bearing_housing()`](linear_bearings.scad#module-linear_bearing_housing) Mod – Creates a generic linear bearing mount clamp. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`lmXuu_bearing()`](linear_bearings.scad#module-lmxuu_bearing) Mod – Creates a standardized LM*UU linear bearing cartridge. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`lmXuu_housing()`](linear_bearings.scad#module-lmxuu_housing) Mod – Creates a standardized LM*UU linear bearing mount clamp. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`lmXuu_info()`](linear_bearings.scad#function-lmxuu_info) Func – Returns the sizes of a standard LM*UU linear bearing cartridge.

### Bezier Curves

- [`bezier_closest_point()`](beziers.scad#function-bezier_closest_point) Func – Finds the closest position on a bezier curve to a given point.
- [`bezier_curvature()`](beziers.scad#function-bezier_curvature) Func – Returns the curvature at one or more given positions along a bezier curve.
- [`bezier_curve()`](beziers.scad#function-bezier_curve) Func – Computes a specified number of points on a bezier curve. <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`bezier_derivative()`](beziers.scad#function-bezier_derivative) Func – Evaluates the derivative of the bezier curve at the given point or points.
- [`bezier_length()`](beziers.scad#function-bezier_length) Func – Approximate the length of part of a bezier curve.
- [`bezier_line_intersection()`](beziers.scad#function-bezier_line_intersection) Func – Calculates where a bezier curve intersects a line.
- [`bezier_points()`](beziers.scad#function-bezier_points) Func – Computes one or more specified points along a bezier curve. <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`bezier_sweep()`](beziers.scad#functionmodule-bezier_sweep) Func/Mod – Sweep a 2d polygon path along a bezier with exact tangents <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`bezier_tangent()`](beziers.scad#function-bezier_tangent) Func – Calculates unit tangent vectors along the bezier curve at one or more given positions.
- [`bezpath_sweep()`](beziers.scad#functionmodule-bezpath_sweep) Func/Mod – Sweep a 2d polygon path along a bezier path with exact tangents <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>

### Bezier Patches

- [`bezier_patch_flat()`](beziers.scad#function-bezier_patch_flat) Func – Creates a flat bezier patch.
- [`bezier_patch_normals()`](beziers.scad#function-bezier_patch_normals) Func – Computes surface normals for one or more places on a bezier surface patch.
- [`bezier_patch_points()`](beziers.scad#function-bezier_patch_points) Func – Computes one or more specified points across a bezier surface patch.
- [`bezier_patch_reverse()`](beziers.scad#function-bezier_patch_reverse) Func – Reverses the orientation of a bezier patch.
- [`bezier_sheet()`](beziers.scad#function-bezier_sheet) Func – Creates a thin sheet from a bezier patch by extruding in normal to the patch <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup>
- [`bezier_vnf()`](beziers.scad#function-bezier_vnf) Func – Generates a (probably non-manifold) VNF for one or more bezier surface patches. <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup>
- [`bezier_vnf_degenerate_patch()`](beziers.scad#function-bezier_vnf_degenerate_patch) Func – Generates a VNF for a degenerate bezier surface patch. <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup>
- [`debug_bezier_patches()`](beziers.scad#module-debug_bezier_patches) Mod – Shows a bezier surface patch and its associated control points. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`is_bezier_patch()`](beziers.scad#function-is_bezier_patch) Func – Returns true if the given item is a bezier patch.

### Bezier Paths

- [`bez_begin()`](beziers.scad#function-bez_begin) Func – Calculates starting bezier path control points.
- [`bez_end()`](beziers.scad#function-bez_end) Func – Calculates ending bezier path control points.
- [`bez_joint()`](beziers.scad#function-bez_joint) Func – Calculates control points for a disjointed corner bezier path joint.
- [`bez_tang()`](beziers.scad#function-bez_tang) Func – Calculates control points for a smooth bezier path joint.
- [`bezpath_close_to_axis()`](beziers.scad#function-bezpath_close_to_axis) Func – Closes a 2D bezier path to the specified axis. <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`bezpath_closest_point()`](beziers.scad#function-bezpath_closest_point) Func – Finds the closest point on a bezier path to a given point.
- [`bezpath_curve()`](beziers.scad#function-bezpath_curve) Func – Converts bezier path into a path of points. <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`bezpath_length()`](beziers.scad#function-bezpath_length) Func – Approximate the length of a bezier path.
- [`bezpath_offset()`](beziers.scad#function-bezpath_offset) Func – Forms a closed bezier path loop with a translated and reversed copy of itself. <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`bezpath_points()`](beziers.scad#function-bezpath_points) Func – Computes one or more specified points along a bezier path. <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`debug_bezier()`](beziers.scad#module-debug_bezier) Mod – Shows a bezier path and its associated control points. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`path_to_bezpath()`](beziers.scad#function-path_to_bezpath) Func – Generates a bezier path that passes through all points in a given linear path. <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>

### Boolean Operations

- [`difference()`](regions.scad#functionmodule-difference) Func/Mod – Performs a Boolean difference operation. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Region.">[<abbr>Region</abbr>]</sup>
- [`exclusive_or()`](regions.scad#functionmodule-exclusive_or) Func/Mod – Performs a Boolean exclusive-or operation. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Region.">[<abbr>Region</abbr>]</sup>
- [`f_and()`](fnliterals.scad#function-f_and) Func – Returns a function to check if both `a` and `b` are true.
- [`f_nand()`](fnliterals.scad#function-f_nand) Func – Returns a function to check if `a` and `b` are not both true.
- [`f_nor()`](fnliterals.scad#function-f_nor) Func – Returns a function to check if neither `a` nor `b` are true.
- [`f_not()`](fnliterals.scad#function-f_not) Func – Returns a function to check if `a` is not true.
- [`f_or()`](fnliterals.scad#function-f_or) Func – Returns a function to check if either `a` or `b` is true.
- [`f_xor()`](fnliterals.scad#function-f_xor) Func – Returns a function to check if either `a` or `b`, but not both, are true.
- [`intersection()`](regions.scad#functionmodule-intersection) Func/Mod – Performs a Boolean intersection operation. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Region.">[<abbr>Region</abbr>]</sup>
- [`union()`](regions.scad#functionmodule-union) Func/Mod – Performs a Boolean union operation. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Region.">[<abbr>Region</abbr>]</sup>

### Boolean Testing

- [`is_bool_list()`](utility.scad#function-is_bool_list) Func – Returns true if the argument list contains only booleans.
- [`num_true()`](utility.scad#function-num_true) Func – Returns the number of true entries in the arguemnt list.

### Bottles

- [`bottle_adapter_cap_to_cap()`](bottlecaps.scad#module-bottle_adapter_cap_to_cap) Mod – Creates a generic adaptor between a cap and a cap. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`bottle_adapter_neck_to_cap()`](bottlecaps.scad#module-bottle_adapter_neck_to_cap) Mod – Creates a generic adapter between a neck and a cap. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`bottle_adapter_neck_to_neck()`](bottlecaps.scad#module-bottle_adapter_neck_to_neck) Mod – Creates a generic adaptor between a neck and a neck. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`generic_bottle_cap()`](bottlecaps.scad#module-generic_bottle_cap) Mod – Creates a generic cap for a bottle. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`generic_bottle_neck()`](bottlecaps.scad#module-generic_bottle_neck) Mod – Creates a generic neck for a bottle. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`mason_cap()`](bottlecaps.scad#module-mason_cap) Mod – Creates a threaded mason jar cap. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`mason_neck()`](bottlecaps.scad#module-mason_neck) Mod – Creates a threaded glass mason jar neck. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`pco1810_cap()`](bottlecaps.scad#module-pco1810_cap) Mod – Creates a cap for a PCO1810 standard bottle. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`pco1810_neck()`](bottlecaps.scad#module-pco1810_neck) Mod – Creates a neck for a PCO1810 standard bottle. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`pco1881_cap()`](bottlecaps.scad#module-pco1881_cap) Mod – Creates a cap for a PCO1881 standard bottle. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`pco1881_neck()`](bottlecaps.scad#module-pco1881_neck) Mod – Creates a neck for a PCO1881 standard bottle. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`sp_cap()`](bottlecaps.scad#module-sp_cap) Mod – Creates an SPI threaded bottle cap. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`sp_diameter()`](bottlecaps.scad#function-sp_diameter) Func – Returns the base diameter of an SPI bottle neck from the nominal diameter and type number.
- [`sp_neck()`](bottlecaps.scad#module-sp_neck) Mod – Creates an SPI threaded bottle neck. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>

### Bounding Boxes

- [`bounding_box()`](miscellaneous.scad#module-bounding_box) Mod – Creates the smallest bounding box that contains all the children. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`fit_to_box()`](vectors.scad#function-fit_to_box) Func – Scale the x, y, and/or z coordinates of a list of points to span a range.
- [`pointlist_bounds()`](vectors.scad#function-pointlist_bounds) Func – Returns the min and max bounding coordinates for the given list of points.
- [`vnf_bounds()`](vnf.scad#function-vnf_bounds) Func – Returns the min and max bounding coordinates for the VNF.

### Bounds

- [`bounding_box()`](miscellaneous.scad#module-bounding_box) Mod – Creates the smallest bounding box that contains all the children. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`fit_to_box()`](vectors.scad#function-fit_to_box) Func – Scale the x, y, and/or z coordinates of a list of points to span a range.
- [`fit_to_range()`](math.scad#function-fit_to_range) Func – Scale the values in an array to span a range.
- [`pointlist_bounds()`](vectors.scad#function-pointlist_bounds) Func – Returns the min and max bounding coordinates for the given list of points.
- [`vnf_bounds()`](vnf.scad#function-vnf_bounds) Func – Returns the min and max bounding coordinates for the VNF.

### Calculus

- [`deriv()`](math.scad#function-deriv) Func – Returns the first derivative estimate of a list of data.
- [`deriv2()`](math.scad#function-deriv2) Func – Returns the second derivative estimate of a list of data.
- [`deriv3()`](math.scad#function-deriv3) Func – Returns the third derivative estimate of a list of data.

### Centroid

- [`centroid()`](geometry.scad#function-centroid) Func – Compute centroid of a 2d or 3d polygon or a VNF.

### Chamfers

- [`chamfer_corner_mask()`](masks.scad#module-chamfer_corner_mask) Mod – Creates a shape to chamfer a 90° corner. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`chamfer_cylinder_mask()`](masks.scad#module-chamfer_cylinder_mask) Mod – Creates a shape to chamfer the end of a cylinder. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`chamfer_edge_mask()`](masks.scad#module-chamfer_edge_mask) Mod – Creates a shape to chamfer a 90° edge. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`cyl()`](shapes3d.scad#functionmodule-cyl) Func/Mod – Creates an attachable cylinder with roundovers, chamfering or texturing. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup>
- [`hemicyl()`](shapes3d.scad#module-hemicyl) Mod – Creates a half cylinder, with optional rounding or chamfers on the flat face.
- [`regular_prism()`](shapes3d.scad#functionmodule-regular_prism) Func/Mod – Creates a regular prism with roundovers and chamfering <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup>
- [`semicircle()`](shapes2d.scad#functionmodule-semicircle) Func/Mod – Creates a semicircle with optional roundings or chamfers <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`xcyl()`](shapes3d.scad#functionmodule-xcyl) Func/Mod – Creates a cylinder oriented along the X axis. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup>
- [`ycyl()`](shapes3d.scad#functionmodule-ycyl) Func/Mod – Creates a cylinder oriented along the y axis. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup>
- [`zcyl()`](shapes3d.scad#module-zcyl) Mod – Creates a cylinder oriented along the y axis. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup>

### Circles

- [`circle_2tangents()`](geometry.scad#function-circle_2tangents) Func – Given two 2d or 3d rays, find a circle tangent to both.
- [`circle_3points()`](geometry.scad#function-circle_3points) Func – Find a circle passing through three 2d or 3d points.
- [`circle_circle_intersection()`](geometry.scad#function-circle_circle_intersection) Func – Find the intersection points of two 2d circles.
- [`circle_circle_tangents()`](geometry.scad#function-circle_circle_tangents) Func – Find tangents to a pair of circles in 2d.
- [`circle_line_intersection()`](geometry.scad#function-circle_line_intersection) Func – Find the intersection points between a 2d circle and a line, ray or segment.
- [`circle_point_tangents()`](geometry.scad#function-circle_point_tangents) Func – Given a circle and point, find tangents to circle passing through the point.

### Clockwise

- [`ccw_polygon()`](geometry.scad#function-ccw_polygon) Func – Return counter-clockwise version of a polygon.
- [`clockwise_polygon()`](geometry.scad#function-clockwise_polygon) Func – Return clockwise version of a polygon.
- [`is_polygon_clockwise()`](geometry.scad#function-is_polygon_clockwise) Func – Determine if a 2d polygon winds clockwise.
- [`reverse_polygon()`](geometry.scad#function-reverse_polygon) Func – Reverse winding direction of polygon.

### Closest

- [`vector_nearest()`](vectors.scad#function-vector_nearest) Func – Finds the `k` nearest points in a list to a given point.
- [`vector_search()`](vectors.scad#function-vector_search) Func – Finds points in a list that are close to a given point.
- [`vector_search_tree()`](vectors.scad#function-vector_search_tree) Func – Makes a distance search tree for a list of points.

### Collinearity

- [`is_collinear()`](geometry.scad#function-is_collinear) Func – Determine if points are collinear.

### Collision

- [`convex_collision()`](geometry.scad#function-convex_collision) Func – Check whether the convex hulls of two point lists intersect.

### Colors

- [`color_this()`](color.scad#module-color_this) Mod – Sets the color for attachable children at the current level only. <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup>
- [`hsl()`](color.scad#functionmodule-hsl) Func/Mod – Converts HSL to RGB or colors children with an HSL color. <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup>
- [`hsv()`](color.scad#functionmodule-hsv) Func/Mod – Converts HSV to RGB or colors children with an HSV color. <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup>
- [`lch()`](color.scad#functionmodule-lch) Func/Mod – Converts D65 CIE LCh to sRGB or colors children with an LCh color. <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup>
- [`rainbow()`](color.scad#module-rainbow) Mod – Iterates through a list, displaying children in different colors. <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup>
- [`recolor()`](color.scad#module-recolor) Mod – Sets the color for attachable children and their descendants. <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup>

### Colorspace

- [`hsl()`](color.scad#functionmodule-hsl) Func/Mod – Converts HSL to RGB or colors children with an HSL color. <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup>
- [`hsv()`](color.scad#functionmodule-hsv) Func/Mod – Converts HSV to RGB or colors children with an HSV color. <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup>
- [`lch()`](color.scad#functionmodule-lch) Func/Mod – Converts D65 CIE LCh to sRGB or colors children with an LCh color. <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup>

### Comparators

- [`are_polygons_equal()`](geometry.scad#function-are_polygons_equal) Func – Check if two polygons (not necessarily in the same point order) are equal.
- [`f_approx()`](fnliterals.scad#function-f_approx) Func – Returns a function to compare if `a` is approximately equal to `b`.
- [`f_cmp()`](fnliterals.scad#function-f_cmp) Func – Returns a function to compare values.
- [`f_eq()`](fnliterals.scad#function-f_eq) Func – Returns a function to compare if `a` is exactly equal to `b`.
- [`f_gt()`](fnliterals.scad#function-f_gt) Func – Returns a function to compare if `a` is greater than `b`.
- [`f_gte()`](fnliterals.scad#function-f_gte) Func – Returns a function to compare if `a` is greater than or equal to `b`.
- [`f_lt()`](fnliterals.scad#function-f_lt) Func – Returns a function to compare if `a` is less than `b`.
- [`f_lte()`](fnliterals.scad#function-f_lte) Func – Returns a function to compare if `a` is less than or equal to `b`.
- [`f_napprox()`](fnliterals.scad#function-f_napprox) Func – Returns a function to compare if `a` is not approximately equal to `b`.
- [`f_neq()`](fnliterals.scad#function-f_neq) Func – Returns a function to compare if `a` is not exactly equal to `b`.

### Comparison

- [`are_regions_equal()`](regions.scad#function-are_regions_equal) Func – Returns true if given regions are the same polygons.
- [`point_in_region()`](regions.scad#function-point_in_region) Func – Tests if a point is inside, outside, or on the border of a [region](Glossary#region).

### Comparisons

- [`all_equal()`](comparisons.scad#function-all_equal) Func – Returns true if all items in a list are approximately equal to each other.
- [`all_negative()`](comparisons.scad#function-all_negative) Func – Returns true if the value(s) given are less than zero.
- [`all_nonnegative()`](comparisons.scad#function-all_nonnegative) Func – Returns true if the value(s) given are greater than or equal to zero.
- [`all_nonpositive()`](comparisons.scad#function-all_nonpositive) Func – Returns true if the value(s) given are less than or equal to zero.
- [`all_nonzero()`](comparisons.scad#function-all_nonzero) Func – Returns true if the value(s) given are not approximately zero.
- [`all_positive()`](comparisons.scad#function-all_positive) Func – Returns true if the value(s) given are greater than zero.
- [`all_zero()`](comparisons.scad#function-all_zero) Func – Returns true if the value(s) given are approximately zero.
- [`approx()`](comparisons.scad#function-approx) Func – Returns true if two values are equal to within a small epsilon value.
- [`are_ends_equal()`](comparisons.scad#function-are_ends_equal) Func – Returns true if the first and last items in a list are approximately equal.
- [`compare_lists()`](comparisons.scad#function-compare_lists) Func – Compares two lists of values, possibly of different type.
- [`compare_vals()`](comparisons.scad#function-compare_vals) Func – Compares two values, possibly of different type.
- [`is_decreasing()`](comparisons.scad#function-is_decreasing) Func – Returns true if every item in a list is less than the previous item.
- [`is_increasing()`](comparisons.scad#function-is_increasing) Func – Returns true if every item in a list is greater than the previous item.
- [`unique_approx()`](comparisons.scad#function-unique_approx) Func – Returns a subset whose retained items are pairwise separated by a tolerance.
- [`unique_approx_indexed()`](comparisons.scad#function-unique_approx_indexed) Func – Returns indices of a subset whose retained items are separated by more than a tolerance.

### Complex Numbers

- [`c_conj()`](math.scad#function-c_conj) Func – Returns the complex conjugate of the input.
- [`c_div()`](math.scad#function-c_div) Func – Divides two complex numbers.
- [`c_ident()`](math.scad#function-c_ident) Func – Returns an n by n complex identity matrix.
- [`c_imag()`](math.scad#function-c_imag) Func – Returns the imaginary part of a complex number, vector or matrix..
- [`c_mul()`](math.scad#function-c_mul) Func – Multiplies two complex numbers.
- [`c_norm()`](math.scad#function-c_norm) Func – Returns the norm of a complex number or vector.
- [`c_real()`](math.scad#function-c_real) Func – Returns the real part of a complex number, vector or matrix..
- [`complex()`](math.scad#function-complex) Func – Replaces scalars in a list or matrix with complex number 2-vectors.
- [`poly_roots()`](math.scad#function-poly_roots) Func – Returns all complex valued roots of the given real polynomial.
- [`polynomial()`](math.scad#function-polynomial) Func – Evaluate a polynomial at a real or complex value.
- [`quadratic_roots()`](math.scad#function-quadratic_roots) Func – Computes roots for the quadratic equation.
- [`real_roots()`](math.scad#function-real_roots) Func – Returns all real roots of the given real polynomial.

### Constants

- [`$slop`](constants.scad#constant-slop) Const – The slop amount to make printed items fit closely. `0.0` by default.
- [`BACK`](constants.scad#constant-back) Const – The backwards (Y+) direction vector constant `[0,1,0]`.
- [`BOTTOM`](constants.scad#constant-bottom) Const – The down-wards (Z-) direction vector constant `[0,0,-1]`.
- [`BOTTOM`](constants.scad#constant-bottom) Const – The down-wards (Z-) direction vector constant `[0,0,-1]`.
- [`CENTER`](constants.scad#constant-center) Const – The center vector constant `[0,0,0]`.
- [`CENTER`](constants.scad#constant-center) Const – The center vector constant `[0,0,0]`.
- [`CENTER`](constants.scad#constant-center) Const – The center vector constant `[0,0,0]`.
- [`BOTTOM`](constants.scad#constant-bottom) Const – The down-wards (Z-) direction vector constant `[0,0,-1]`.
- [`EDGE()`](constants.scad#function-edge) Func – Named edge anchor constants
- [`EPSILON`](math.scad#constant-epsilon) Const – A tiny value to compare floating point values.  1e-9
- [`FACE()`](constants.scad#function-face) Func – Named face anchor constants
- [`FRONT`](constants.scad#constant-front) Const – The front-wards (Y-) direction vector constant `[0,-1,0]`.
- [`FRONT`](constants.scad#constant-front) Const – The front-wards (Y-) direction vector constant `[0,-1,0]`.
- [`FRONT`](constants.scad#constant-front) Const – The front-wards (Y-) direction vector constant `[0,-1,0]`.
- [`IDENT`](constants.scad#constant-ident) Const – A constant, the 3D identity transformation matrix. <sup title="Can return a transformation matrix.">[<abbr>Mat</abbr>]</sup>
- [`INCH`](constants.scad#constant-inch) Const – A constant, the  number of millimeters in an inch. `25.4`
- [`INF`](math.scad#constant-inf) Const – The floating point value for Infinite.
- [`LEFT`](constants.scad#constant-left) Const – The left-wards (X-) direction vector constant `[-1,0,0]`.
- [`LINE`](constants.scad#constant-line) Const – A constant for specifying an unbounded line in various geometry.scad functions.  `[false,false]`
- [`NAN`](math.scad#constant-nan) Const – The floating point value for Not a Number.
- [`PHI`](math.scad#constant-phi) Const – The golden ratio φ (phi).  Approximately 1.6180339887
- [`RAY`](constants.scad#constant-ray) Const – A constant for specifying a ray line in various geometry.scad functions.  `[true,false]`
- [`RIGHT`](constants.scad#constant-right) Const – The right-wards (X+) direction vector constant `[1,0,0]`.
- [`SEGMENT`](constants.scad#constant-segment) Const – A constant for specifying a line segment in various geometry.scad functions.  `[true,true]`
- [`TOP`](constants.scad#constant-top) Const – The top-wards (Z+) direction vector constant `[0,0,1]`.
- [`TOP`](constants.scad#constant-top) Const – The top-wards (Z+) direction vector constant `[0,0,1]`.

### Contours

- [`contour()`](isosurface.scad#functionmodule-contour) Func/Mod – Creates a 2D contour from a function or array of values. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup> <sup title="Can return a Region.">[<abbr>Region</abbr>]</sup>
- [`metaballs2d()`](isosurface.scad#functionmodule-metaballs2d) Func/Mod – Creates a group of 2D metaballs (smoothly connected blobs). <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Region.">[<abbr>Region</abbr>]</sup>

### Convexity

- [`convex_collision()`](geometry.scad#function-convex_collision) Func – Check whether the convex hulls of two point lists intersect.
- [`convex_distance()`](geometry.scad#function-convex_distance) Func – Compute distance between convex hull of two point lists.
- [`is_polygon_convex()`](geometry.scad#function-is_polygon_convex) Func – Check if a polygon is convex.

### Coordinates

- [`altaz_to_xyz()`](coords.scad#function-altaz_to_xyz) Func – Convert altitude/azimuth/range to 3D cartesian coordinates. <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`cylindrical_to_xyz()`](coords.scad#function-cylindrical_to_xyz) Func – Convert cylindrical coordinates to cartesian coordinates. <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`lift_plane()`](coords.scad#function-lift_plane) Func – Map a list of 2D points onto a plane in 3D. <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`path2d()`](coords.scad#function-path2d) Func – Convert a path to 2D. <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`path3d()`](coords.scad#function-path3d) Func – Convert a path to 3D. <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`path4d()`](coords.scad#function-path4d) Func – Convert a path to 4d. <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`point2d()`](coords.scad#function-point2d) Func – Convert a vector to 2D.
- [`point3d()`](coords.scad#function-point3d) Func – Convert a vector to 3D.
- [`point4d()`](coords.scad#function-point4d) Func – Convert a vector to 4d.
- [`polar_to_xy()`](coords.scad#function-polar_to_xy) Func – Convert 2D polar coordinates to cartesian coordinates. <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`project_plane()`](coords.scad#function-project_plane) Func – Project a set of points onto a specified plane, returning 2D points. <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`spherical_to_xyz()`](coords.scad#function-spherical_to_xyz) Func – Convert spherical coordinates to 3D cartesian coordinates. <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`xy_to_polar()`](coords.scad#function-xy_to_polar) Func – Convert 2D cartesian coordinates to polar coordinates (radius and angle)
- [`xyz_to_altaz()`](coords.scad#function-xyz_to_altaz) Func – Convert 3D cartesian coordinates to [altitude,azimuth,range].
- [`xyz_to_cylindrical()`](coords.scad#function-xyz_to_cylindrical) Func – Convert 3D cartesian coordinates to cylindrical coordinates.
- [`xyz_to_spherical()`](coords.scad#function-xyz_to_spherical) Func – Convert 3D cartesian coordinates to spherical coordinates.

### Copiers

- [`arc_copies()`](distributors.scad#functionmodule-arc_copies) Func/Mod – Distributes duplicates of children along an arc. <sup title="Can return a list of transformation matrices.">[<abbr>MatList</abbr>]</sup> <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup>
- [`desc_copies()`](attachments.scad#module-desc_copies) Mod – Places copies according to a list of transformation matrices and supplies descriptions for the copies. <sup title="Can return a list of transformation matrices.">[<abbr>MatList</abbr>]</sup> <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup>
- [`grid_copies()`](distributors.scad#functionmodule-grid_copies) Func/Mod – Places copies of children in an [X,Y] grid. <sup title="Can return a list of transformation matrices.">[<abbr>MatList</abbr>]</sup> <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup>
- [`line_copies()`](distributors.scad#functionmodule-line_copies) Func/Mod – Places copies of children along an arbitrary line. <sup title="Can return a list of transformation matrices.">[<abbr>MatList</abbr>]</sup> <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup>
- [`mirror_copy()`](distributors.scad#functionmodule-mirror_copy) Func/Mod – Makes a copy of children mirrored across a given plane. <sup title="Can return a list of transformation matrices.">[<abbr>MatList</abbr>]</sup> <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup>
- [`move_copies()`](distributors.scad#functionmodule-move_copies) Func/Mod – Translates copies of all children. <sup title="Can return a list of transformation matrices.">[<abbr>MatList</abbr>]</sup> <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup>
- [`path_copies()`](distributors.scad#functionmodule-path_copies) Func/Mod – Uniformly distributes copies of children along a path. <sup title="Can return a list of transformation matrices.">[<abbr>MatList</abbr>]</sup> <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup>
- [`rot_copies()`](distributors.scad#functionmodule-rot_copies) Func/Mod – Rotates copies of children. <sup title="Can return a list of transformation matrices.">[<abbr>MatList</abbr>]</sup> <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup>
- [`sphere_copies()`](distributors.scad#functionmodule-sphere_copies) Func/Mod – Distributes copies of children over the surface of a sphere. <sup title="Can return a list of transformation matrices.">[<abbr>MatList</abbr>]</sup> <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup>
- [`xcopies()`](distributors.scad#functionmodule-xcopies) Func/Mod – Places copies of children along the X axis. <sup title="Can return a list of transformation matrices.">[<abbr>MatList</abbr>]</sup> <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup>
- [`xflip_copy()`](distributors.scad#functionmodule-xflip_copy) Func/Mod – Makes a copy of children mirrored across the X axis. <sup title="Can return a list of transformation matrices.">[<abbr>MatList</abbr>]</sup> <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup>
- [`xrot_copies()`](distributors.scad#functionmodule-xrot_copies) Func/Mod – Rotates copies of children around the X axis. <sup title="Can return a list of transformation matrices.">[<abbr>MatList</abbr>]</sup> <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup>
- [`ycopies()`](distributors.scad#functionmodule-ycopies) Func/Mod – Places copies of children along the Y axis. <sup title="Can return a list of transformation matrices.">[<abbr>MatList</abbr>]</sup> <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup>
- [`yflip_copy()`](distributors.scad#functionmodule-yflip_copy) Func/Mod – Makes a copy of children mirrored across the Y axis. <sup title="Can return a list of transformation matrices.">[<abbr>MatList</abbr>]</sup> <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup>
- [`yrot_copies()`](distributors.scad#functionmodule-yrot_copies) Func/Mod – Rotates copies of children around the Y axis. <sup title="Can return a list of transformation matrices.">[<abbr>MatList</abbr>]</sup> <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup>
- [`zcopies()`](distributors.scad#functionmodule-zcopies) Func/Mod – Places copies of children along the Z axis. <sup title="Can return a list of transformation matrices.">[<abbr>MatList</abbr>]</sup> <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup>
- [`zflip_copy()`](distributors.scad#functionmodule-zflip_copy) Func/Mod – Makes a copy of children mirrored across the Z axis. <sup title="Can return a list of transformation matrices.">[<abbr>MatList</abbr>]</sup> <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup>
- [`zrot_copies()`](distributors.scad#functionmodule-zrot_copies) Func/Mod – Rotates copies of children around the Z axis. <sup title="Can return a list of transformation matrices.">[<abbr>MatList</abbr>]</sup> <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup>

### Coplanarity

- [`is_coplanar()`](geometry.scad#function-is_coplanar) Func – Check if 3d points are coplanar and not collinear.

### CubeTruss

- [`cubetruss()`](cubetruss.scad#module-cubetruss) Mod – Creates a multi-cube straight cubetruss shape. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`cubetruss_clip()`](cubetruss.scad#module-cubetruss_clip) Mod – Creates a clip for the end of a cubetruss to snap-lock it to another cubetruss. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`cubetruss_corner()`](cubetruss.scad#module-cubetruss_corner) Mod – Creates a multi-cube corner cubetruss shape. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`cubetruss_dist()`](cubetruss.scad#function-cubetruss_dist) Func – Returns the length of a cubetruss truss.
- [`cubetruss_foot()`](cubetruss.scad#module-cubetruss_foot) Mod – Creates a foot that can connect two cubetrusses. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`cubetruss_joiner()`](cubetruss.scad#module-cubetruss_joiner) Mod – Creates a joiner that can connect two cubetrusses end-to-end. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`cubetruss_segment()`](cubetruss.scad#module-cubetruss_segment) Mod – Creates a single cubetruss cube. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`cubetruss_support()`](cubetruss.scad#module-cubetruss_support) Mod – Creates a cubetruss support structure shape. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`cubetruss_uclip()`](cubetruss.scad#module-cubetruss_uclip) Mod – Creates a joiner that can connect two cubetrusses end-to-end. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>

### Cylinders

- [`chamfer_cylinder_mask()`](masks.scad#module-chamfer_cylinder_mask) Mod – Creates a shape to chamfer the end of a cylinder. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`cyl()`](shapes3d.scad#functionmodule-cyl) Func/Mod – Creates an attachable cylinder with roundovers, chamfering or texturing. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup>
- [`hemicyl()`](shapes3d.scad#module-hemicyl) Mod – Creates a half cylinder, with optional rounding or chamfers on the flat face.
- [`rounding_cylinder_mask()`](masks.scad#module-rounding_cylinder_mask) Mod – Creates a shape to round the end of a cylinder. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`xcyl()`](shapes3d.scad#functionmodule-xcyl) Func/Mod – Creates a cylinder oriented along the X axis. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup>
- [`ycyl()`](shapes3d.scad#functionmodule-ycyl) Func/Mod – Creates a cylinder oriented along the y axis. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup>
- [`zcyl()`](shapes3d.scad#module-zcyl) Mod – Creates a cylinder oriented along the y axis. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup>

### Data Structures

- [`binsearch()`](fnliterals.scad#function-binsearch) Func – Does a binary search of a sorted list to find the index of a given value.
- [`echo_struct()`](structs.scad#functionmodule-echo_struct) Func/Mod – Echoes the struct to the console in a formatted manner.
- [`hashmap()`](fnliterals.scad#function-hashmap) Func – Creates a hashmap manipulation function.
- [`is_struct()`](structs.scad#function-is_struct) Func – Returns true if the value is a struct.
- [`simple_hash()`](fnliterals.scad#function-simple_hash) Func – Returns an integer hash of a given value.
- [`struct_keys()`](structs.scad#function-struct_keys) Func – Returns a list of keys for a struct.
- [`struct_remove()`](structs.scad#function-struct_remove) Func – Removes one or more keys from a struct.
- [`struct_set()`](structs.scad#function-struct_set) Func – Sets one or more key-value pairs in a struct.
- [`struct_val()`](structs.scad#function-struct_val) Func – Returns the value for an key in a struct.

### Debugging

- [`anchor_arrow()`](attachments.scad#module-anchor_arrow) Mod – Shows a 3d anchor orientation arrow. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`anchor_arrow2d()`](attachments.scad#module-anchor_arrow2d) Mod – Shows a 2d anchor orientation arrow. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`assert_approx()`](utility.scad#module-assert_approx) Mod – Assert that a value is approximately what was expected.
- [`assert_equal()`](utility.scad#module-assert_equal) Mod – Assert that a value is expected.
- [`color_overlaps()`](color.scad#module-color_overlaps) Mod – Shows ghostly children, with overlaps highlighted in color. <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup>
- [`debug_bezier()`](beziers.scad#module-debug_bezier) Mod – Shows a bezier path and its associated control points. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`debug_bezier_patches()`](beziers.scad#module-debug_bezier_patches) Mod – Shows a bezier surface patch and its associated control points. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`debug_nurbs()`](nurbs.scad#module-debug_nurbs) Mod – Shows a NURBS curve and its control points, knots and weights <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`debug_nurbs_interp()`](nurbs.scad#module-debug_nurbs_interp) Mod – Interpolates a NURBS using [`nurbs_interp()`](#function-nurbs\_interp) and displays the curve with informative overlays.
- [`debug_polygon()`](drawing.scad#module-debug_polygon) Mod – Draws an annotated polygon. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`debug_region()`](regions.scad#module-debug_region) Mod – Draws an annotated [region](Glossary#region). <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`debug_vnf()`](vnf.scad#module-debug_vnf) Mod – A replacement for `vnf_polyhedron()` to help with debugging. <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup>
- [`expose_anchors()`](attachments.scad#module-expose_anchors) Mod – Used to show a transparent object with solid color anchor arrows.
- [`frame_ref()`](attachments.scad#module-frame_ref) Mod – Shows axis orientation arrows. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`generic_airplane()`](attachments.scad#module-generic_airplane) Mod – Shows a generic airplane shape, useful for viewing orientations. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`ghost()`](color.scad#module-ghost) Mod – Sets % modifier for attachable children and their descendants. <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup>
- [`ghost_this()`](color.scad#module-ghost_this) Mod – Apply % modifier to children at a single level. <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup>
- [`highlight()`](color.scad#module-highlight) Mod – Sets # modifier for attachable children and their descendants. <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup>
- [`highlight_this()`](color.scad#module-highlight_this) Mod – Apply # modifier to children at a single level. <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup>
- [`rainbow()`](color.scad#module-rainbow) Mod – Iterates through a list, displaying children in different colors. <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup>
- [`shape_compare()`](utility.scad#module-shape_compare) Mod – Compares two child shapes. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`show_anchors()`](attachments.scad#module-show_anchors) Mod – Shows anchors for the parent object. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`show_plane()`](geometry.scad#module-show_plane) Mod – Display (part of) a plane <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`show_transform_list()`](attachments.scad#module-show_transform_list) Mod – Shows a list of transforms and how they connect. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`vnf_validate()`](vnf.scad#module-vnf_validate) Mod – Echos non-manifold VNF errors to the console. <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup>

### Descriptions

- [`desc_copies()`](attachments.scad#module-desc_copies) Mod – Places copies according to a list of transformation matrices and supplies descriptions for the copies. <sup title="Can return a list of transformation matrices.">[<abbr>MatList</abbr>]</sup> <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup>
- [`desc_dir()`](attachments.scad#function-desc_dir) Func – Computes the direction in the current context of a direction or anchor in a description's context
- [`desc_dist()`](attachments.scad#function-desc_dist) Func – Computes the distance between two points specified by attachable descriptions
- [`desc_point()`](attachments.scad#function-desc_point) Func – Computes the location in the current context of an anchor point from an attachable description
- [`is_description()`](attachments.scad#function-is_description) Func – Check if its argument is a description
- [`parent()`](attachments.scad#function-parent) Func – Returns a description (transformation state and attachment geometry) of the parent
- [`parent_part()`](attachments.scad#function-parent_part) Func – Returns a description (transformation state and attachment geometry) of a part defined by the parent
- [`prism_connector()`](rounding.scad#module-prism_connector) Mod – Construct a filleted prism that connects objects <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`restore()`](attachments.scad#module-restore) Mod – Restores transformation state and attachment geometry from a description
- [`transform_desc()`](attachments.scad#function-transform_desc) Func – Applies a transformation matrix to a description

### Dictionaries

- [`echo_struct()`](structs.scad#functionmodule-echo_struct) Func/Mod – Echoes the struct to the console in a formatted manner.
- [`is_struct()`](structs.scad#function-is_struct) Func – Returns true if the value is a struct.
- [`struct_keys()`](structs.scad#function-struct_keys) Func – Returns a list of keys for a struct.
- [`struct_remove()`](structs.scad#function-struct_remove) Func – Removes one or more keys from a struct.
- [`struct_set()`](structs.scad#function-struct_set) Func – Sets one or more key-value pairs in a struct.
- [`struct_val()`](structs.scad#function-struct_val) Func – Returns the value for an key in a struct.

### Distance

- [`closest_point()`](vectors.scad#function-closest_point) Func – Finds the closest point in a list of points.
- [`convex_distance()`](geometry.scad#function-convex_distance) Func – Compute distance between convex hull of two point lists.
- [`furthest_point()`](vectors.scad#function-furthest_point) Func – Finds the furthest point in a list of points.
- [`line_closest_point()`](geometry.scad#function-line_closest_point) Func – Find point on given line, segment or ray that is closest to a given point.
- [`point_line_distance()`](geometry.scad#function-point_line_distance) Func – Find shortest distance from point to a line, segment or ray.
- [`point_plane_distance()`](geometry.scad#function-point_plane_distance) Func – Determine distance between a point and plane.
- [`ruler()`](shapes3d.scad#module-ruler) Mod – Creates a ruler. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`segment_distance()`](geometry.scad#function-segment_distance) Func – Find smallest distance between two line semgnets.

### Distributors

- [`arc_copies()`](distributors.scad#functionmodule-arc_copies) Func/Mod – Distributes duplicates of children along an arc. <sup title="Can return a list of transformation matrices.">[<abbr>MatList</abbr>]</sup> <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup>
- [`desc_copies()`](attachments.scad#module-desc_copies) Mod – Places copies according to a list of transformation matrices and supplies descriptions for the copies. <sup title="Can return a list of transformation matrices.">[<abbr>MatList</abbr>]</sup> <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup>
- [`grid_copies()`](distributors.scad#functionmodule-grid_copies) Func/Mod – Places copies of children in an [X,Y] grid. <sup title="Can return a list of transformation matrices.">[<abbr>MatList</abbr>]</sup> <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup>
- [`line_copies()`](distributors.scad#functionmodule-line_copies) Func/Mod – Places copies of children along an arbitrary line. <sup title="Can return a list of transformation matrices.">[<abbr>MatList</abbr>]</sup> <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup>
- [`mirror_copy()`](distributors.scad#functionmodule-mirror_copy) Func/Mod – Makes a copy of children mirrored across a given plane. <sup title="Can return a list of transformation matrices.">[<abbr>MatList</abbr>]</sup> <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup>
- [`move_copies()`](distributors.scad#functionmodule-move_copies) Func/Mod – Translates copies of all children. <sup title="Can return a list of transformation matrices.">[<abbr>MatList</abbr>]</sup> <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup>
- [`path_copies()`](distributors.scad#functionmodule-path_copies) Func/Mod – Uniformly distributes copies of children along a path. <sup title="Can return a list of transformation matrices.">[<abbr>MatList</abbr>]</sup> <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup>
- [`rot_copies()`](distributors.scad#functionmodule-rot_copies) Func/Mod – Rotates copies of children. <sup title="Can return a list of transformation matrices.">[<abbr>MatList</abbr>]</sup> <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup>
- [`sphere_copies()`](distributors.scad#functionmodule-sphere_copies) Func/Mod – Distributes copies of children over the surface of a sphere. <sup title="Can return a list of transformation matrices.">[<abbr>MatList</abbr>]</sup> <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup>
- [`xcopies()`](distributors.scad#functionmodule-xcopies) Func/Mod – Places copies of children along the X axis. <sup title="Can return a list of transformation matrices.">[<abbr>MatList</abbr>]</sup> <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup>
- [`xflip_copy()`](distributors.scad#functionmodule-xflip_copy) Func/Mod – Makes a copy of children mirrored across the X axis. <sup title="Can return a list of transformation matrices.">[<abbr>MatList</abbr>]</sup> <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup>
- [`xrot_copies()`](distributors.scad#functionmodule-xrot_copies) Func/Mod – Rotates copies of children around the X axis. <sup title="Can return a list of transformation matrices.">[<abbr>MatList</abbr>]</sup> <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup>
- [`ycopies()`](distributors.scad#functionmodule-ycopies) Func/Mod – Places copies of children along the Y axis. <sup title="Can return a list of transformation matrices.">[<abbr>MatList</abbr>]</sup> <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup>
- [`yflip_copy()`](distributors.scad#functionmodule-yflip_copy) Func/Mod – Makes a copy of children mirrored across the Y axis. <sup title="Can return a list of transformation matrices.">[<abbr>MatList</abbr>]</sup> <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup>
- [`yrot_copies()`](distributors.scad#functionmodule-yrot_copies) Func/Mod – Rotates copies of children around the Y axis. <sup title="Can return a list of transformation matrices.">[<abbr>MatList</abbr>]</sup> <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup>
- [`zcopies()`](distributors.scad#functionmodule-zcopies) Func/Mod – Places copies of children along the Z axis. <sup title="Can return a list of transformation matrices.">[<abbr>MatList</abbr>]</sup> <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup>
- [`zflip_copy()`](distributors.scad#functionmodule-zflip_copy) Func/Mod – Makes a copy of children mirrored across the Z axis. <sup title="Can return a list of transformation matrices.">[<abbr>MatList</abbr>]</sup> <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup>
- [`zrot_copies()`](distributors.scad#functionmodule-zrot_copies) Func/Mod – Rotates copies of children around the Z axis. <sup title="Can return a list of transformation matrices.">[<abbr>MatList</abbr>]</sup> <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup>

### Drawing Tools

- [`dashed_stroke()`](drawing.scad#functionmodule-dashed_stroke) Func/Mod – Draws a dashed line along a path or region boundary. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a list of Paths.">[<abbr>PathList</abbr>]</sup>
- [`helix()`](drawing.scad#function-helix) Func – Creates a 3D helical path, including flat spirals. <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`stroke()`](drawing.scad#module-stroke) Mod – Draws a line along a path or region boundary. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>

### Error Checking

- [`assert_approx()`](utility.scad#module-assert_approx) Mod – Assert that a value is approximately what was expected.
- [`assert_equal()`](utility.scad#module-assert_equal) Mod – Assert that a value is expected.
- [`deprecate()`](utility.scad#module-deprecate) Mod – Display a console note that a module is deprecated and suggest a replacement.
- [`no_children()`](utility.scad#module-no_children) Mod – Assert that the calling module does not support children.
- [`no_function()`](utility.scad#function-no_function) Func – Assert that the argument exists only as a module and not as a function.
- [`no_module()`](utility.scad#module-no_module) Mod – Assert that the argument exists only as a function and not as a module.
- [`req_children()`](utility.scad#module-req_children) Mod – Assert that the calling module requires children.
- [`shape_compare()`](utility.scad#module-shape_compare) Mod – Compares two child shapes. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>

### Extrusion

- [`associate_vertices()`](skin.scad#function-associate_vertices) Func – Create vertex association to control how [`skin()`](#functionmodule-skin) links vertices. <sup title="Can return a list of Paths.">[<abbr>PathList</abbr>]</sup>
- [`attach_prism()`](rounding.scad#module-attach_prism) Mod – Attach a filleted prism with optional rounded end <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`bezier_sweep()`](beziers.scad#functionmodule-bezier_sweep) Func/Mod – Sweep a 2d polygon path along a bezier with exact tangents <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`bezpath_sweep()`](beziers.scad#functionmodule-bezpath_sweep) Func/Mod – Sweep a 2d polygon path along a bezier path with exact tangents <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`cylindrical_extrude()`](miscellaneous.scad#module-cylindrical_extrude) Mod – Extrudes 2D children outwards around a cylinder. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`extrude_from_to()`](miscellaneous.scad#module-extrude_from_to) Mod – Extrudes 2D children between two points in 3D space. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`linear_sweep()`](skin.scad#functionmodule-linear_sweep) Func/Mod – Create a linear extrusion from a path, with optional texturing. <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`path_extrude()`](miscellaneous.scad#module-path_extrude) Mod – Extrudes 2D children along a 3D path. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`path_extrude2d()`](miscellaneous.scad#module-path_extrude2d) Mod – Extrudes 2D children along a 2D path. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`path_sweep()`](skin.scad#functionmodule-path_sweep) Func/Mod – Sweep a 2d polygon path along a 2d or 3d path. <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`path_sweep2d()`](skin.scad#functionmodule-path_sweep2d) Func/Mod – Sweep a 2d polygon path along a 2d path allowing self-intersection. <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`prism_connector()`](rounding.scad#module-prism_connector) Mod – Construct a filleted prism that connects objects <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`rotate_sweep()`](skin.scad#functionmodule-rotate_sweep) Func/Mod – Create a surface of revolution from a path with optional texturing. <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`skin()`](skin.scad#functionmodule-skin) Func/Mod – Connect a sequence of arbitrary polygons into a 3D object. <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`spiral_sweep()`](skin.scad#functionmodule-spiral_sweep) Func/Mod – Sweep a path along a helix. <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`sweep()`](skin.scad#functionmodule-sweep) Func/Mod – Construct a 3d object from arbitrary transformations of a 2d polygon path. <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`sweep_attach()`](skin.scad#module-sweep_attach) Mod – Attach children to sides of a path\_sweep parent object <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`texture()`](skin.scad#function-texture) Func – Produce a standard texture.

### Extrusions

- [`jittered_poly()`](shapes2d.scad#module-jittered_poly) Mod – Creates a polygon with extra points for smoother twisted extrusions. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>

### FDM Optimized

- [`corrugated_wall()`](walls.scad#module-corrugated_wall) Mod – Makes a corrugated rectangular wall. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`cubetruss()`](cubetruss.scad#module-cubetruss) Mod – Creates a multi-cube straight cubetruss shape. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`cubetruss_clip()`](cubetruss.scad#module-cubetruss_clip) Mod – Creates a clip for the end of a cubetruss to snap-lock it to another cubetruss. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`cubetruss_corner()`](cubetruss.scad#module-cubetruss_corner) Mod – Creates a multi-cube corner cubetruss shape. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`cubetruss_dist()`](cubetruss.scad#function-cubetruss_dist) Func – Returns the length of a cubetruss truss.
- [`cubetruss_foot()`](cubetruss.scad#module-cubetruss_foot) Mod – Creates a foot that can connect two cubetrusses. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`cubetruss_joiner()`](cubetruss.scad#module-cubetruss_joiner) Mod – Creates a joiner that can connect two cubetrusses end-to-end. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`cubetruss_segment()`](cubetruss.scad#module-cubetruss_segment) Mod – Creates a single cubetruss cube. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`cubetruss_support()`](cubetruss.scad#module-cubetruss_support) Mod – Creates a cubetruss support structure shape. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`cubetruss_uclip()`](cubetruss.scad#module-cubetruss_uclip) Mod – Creates a joiner that can connect two cubetrusses end-to-end. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`hex_panel()`](walls.scad#module-hex_panel) Mod – Create a hexagon braced panel of any shape <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`mask2d_teardrop()`](masks.scad#functionmodule-mask2d_teardrop) Func/Mod – Creates a 2D teardrop shape with specified max angle from vertical. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`narrowing_strut()`](walls.scad#module-narrowing_strut) Mod – Makes a strut like an extruded baseball home plate. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`onion()`](shapes3d.scad#functionmodule-onion) Func/Mod – Creates an attachable onion-like shape. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup>
- [`sparse_cuboid()`](walls.scad#module-sparse_cuboid) Mod – Makes an open cross-braced cuboid <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`sparse_wall()`](walls.scad#module-sparse_wall) Mod – Makes an open cross-braced rectangular wall. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`sparse_wall2d()`](walls.scad#module-sparse_wall2d) Mod – Makes an open cross-braced rectangular wall. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`teardrop()`](shapes3d.scad#functionmodule-teardrop) Func/Mod – Creates a teardrop shape. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup>
- [`teardrop_corner_mask()`](masks.scad#module-teardrop_corner_mask) Mod – Creates a shape to round a 90° corner but limit the angle of overhang. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`teardrop_edge_mask()`](masks.scad#module-teardrop_edge_mask) Mod – Creates a shape to round an edge while limiting the angle of overhang. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`thinning_triangle()`](walls.scad#module-thinning_triangle) Mod – Makes a triangular wall with a thin middle. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`thinning_wall()`](walls.scad#module-thinning_wall) Mod – Makes a rectangular wall with a thin middle. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>

### Filters

- [`filter()`](fnliterals.scad#function-filter) Func – Returns just the list items which the given function returns true for.
- [`find_all()`](fnliterals.scad#function-find_all) Func – Returns the indices of all items in a list that a given function returns true for.

### Function Literals

- [`accumulate()`](fnliterals.scad#function-accumulate) Func – Applies a 2-arg function cumulatively to the items of a list, returning a list of every result.
- [`binsearch()`](fnliterals.scad#function-binsearch) Func – Does a binary search of a sorted list to find the index of a given value.
- [`f_1arg()`](fnliterals.scad#function-f_1arg) Func – Creates a factory for a 2-arg function literal, where you can optionally pre-fill the arg.
- [`f_2arg()`](fnliterals.scad#function-f_2arg) Func – Creates a factory for a 2-arg function literal, where you can optionally pre-fill the args.
- [`f_2arg_simple()`](fnliterals.scad#function-f_2arg_simple) Func – Creates a factory for a 2-arg function literal, where you can optionally pre-fill the args.
- [`f_3arg()`](fnliterals.scad#function-f_3arg) Func – Creates a factory for a 3-arg function literal, where you can optionally pre-fill the args.
- [`f_abs()`](fnliterals.scad#function-f_abs) Func – Returns a function to calculate the absolute value of a given number.
- [`f_acos()`](fnliterals.scad#function-f_acos) Func – Returns a function to calculate the arccosine of a value.
- [`f_add()`](fnliterals.scad#function-f_add) Func – Returns a function to add `a` and `b`.
- [`f_and()`](fnliterals.scad#function-f_and) Func – Returns a function to check if both `a` and `b` are true.
- [`f_approx()`](fnliterals.scad#function-f_approx) Func – Returns a function to compare if `a` is approximately equal to `b`.
- [`f_asin()`](fnliterals.scad#function-f_asin) Func – Returns a function to calculate the arcsine of a value.
- [`f_atan()`](fnliterals.scad#function-f_atan) Func – Returns a function to calculate the arctangent of a value.
- [`f_atan2()`](fnliterals.scad#function-f_atan2) Func – Returns a function to calculate the arctangent of `y` and `x`
- [`f_ceil()`](fnliterals.scad#function-f_ceil) Func – Returns a function to calculate the integer ceiling of a given number.
- [`f_chr()`](fnliterals.scad#function-f_chr) Func – Returns a function to get a string character from its ordinal number.
- [`f_cmp()`](fnliterals.scad#function-f_cmp) Func – Returns a function to compare values.
- [`f_cos()`](fnliterals.scad#function-f_cos) Func – Returns a function to calculate the cosine of a value.
- [`f_cross()`](fnliterals.scad#function-f_cross) Func – Returns a function to calculate the norm of a given vector.
- [`f_div()`](fnliterals.scad#function-f_div) Func – Returns a function to divide `a` by `b`.
- [`f_eq()`](fnliterals.scad#function-f_eq) Func – Returns a function to compare if `a` is exactly equal to `b`.
- [`f_even()`](fnliterals.scad#function-f_even) Func – Returns a function to check if `a` is an even number.
- [`f_exp()`](fnliterals.scad#function-f_exp) Func – Returns a function to calculate the natural exponent of a given number.
- [`f_floor()`](fnliterals.scad#function-f_floor) Func – Returns a function to calculate the integer floor of a given number.
- [`f_gt()`](fnliterals.scad#function-f_gt) Func – Returns a function to compare if `a` is greater than `b`.
- [`f_gte()`](fnliterals.scad#function-f_gte) Func – Returns a function to compare if `a` is greater than or equal to `b`.
- [`f_is_bezier_patch()`](fnliterals.scad#function-f_is_bezier_patch) Func – Returns a function to determine if a value is a Bezier Patch structure.
- [`f_is_bool()`](fnliterals.scad#function-f_is_bool) Func – Returns a function to determine if a value is a boolean.
- [`f_is_def()`](fnliterals.scad#function-f_is_def) Func – Returns a function to determine if a value is not `undef`.
- [`f_is_finite()`](fnliterals.scad#function-f_is_finite) Func – Returns a function to determine if a value is a number type that is finite.
- [`f_is_function()`](fnliterals.scad#function-f_is_function) Func – Returns a function to determine if a value is a function literal.
- [`f_is_int()`](fnliterals.scad#function-f_is_int) Func – Returns a function to determine if a value is an integer number.
- [`f_is_list()`](fnliterals.scad#function-f_is_list) Func – Returns a function to determine if a value is a list.
- [`f_is_nan()`](fnliterals.scad#function-f_is_nan) Func – Returns a function to determine if a value is a number type that is Not a Number (NaN).
- [`f_is_num()`](fnliterals.scad#function-f_is_num) Func – Returns a function to determine if a value is a number.
- [`f_is_path()`](fnliterals.scad#function-f_is_path) Func – Returns a function to determine if a value is a Path (a list of points).
- [`f_is_range()`](fnliterals.scad#function-f_is_range) Func – Returns a function to determine if a value is a range.
- [`f_is_region()`](fnliterals.scad#function-f_is_region) Func – Returns a function to determine if a value is a Region (a list of Paths).
- [`f_is_string()`](fnliterals.scad#function-f_is_string) Func – Returns a function to determine if a value is a string.
- [`f_is_undef()`](fnliterals.scad#function-f_is_undef) Func – Returns a function to determine if a value is `undef`.
- [`f_is_vector()`](fnliterals.scad#function-f_is_vector) Func – Returns a function to determine if a value is a list of numbers.
- [`f_is_vnf()`](fnliterals.scad#function-f_is_vnf) Func – Returns a function to determine if a value is a VNF structure.
- [`f_len()`](fnliterals.scad#function-f_len) Func – Returns a function to calculate the length of a string or list.
- [`f_ln()`](fnliterals.scad#function-f_ln) Func – Returns a function to calculate the natural logarithm of a given number.
- [`f_log()`](fnliterals.scad#function-f_log) Func – Returns a function to calculate the base 10 logarithm of a given number.
- [`f_lt()`](fnliterals.scad#function-f_lt) Func – Returns a function to compare if `a` is less than `b`.
- [`f_lte()`](fnliterals.scad#function-f_lte) Func – Returns a function to compare if `a` is less than or equal to `b`.
- [`f_max()`](fnliterals.scad#function-f_max) Func – Returns a function to calculate the maximum value of a list.
- [`f_max2()`](fnliterals.scad#function-f_max2) Func – Returns a function to calculate the maximum of two values.
- [`f_max3()`](fnliterals.scad#function-f_max3) Func – Returns a function to calculate the maximum of three values.
- [`f_min()`](fnliterals.scad#function-f_min) Func – Returns a function to calculate the minimum value of a list.
- [`f_min2()`](fnliterals.scad#function-f_min2) Func – Returns a function to calculate the minimum of two values.
- [`f_min3()`](fnliterals.scad#function-f_min3) Func – Returns a function to calculate the minimum of three values.
- [`f_mod()`](fnliterals.scad#function-f_mod) Func – Returns a function to calculate the modulo of `a` divided by `b`.
- [`f_mul()`](fnliterals.scad#function-f_mul) Func – Returns a function to multiply `a` by `b`.
- [`f_nand()`](fnliterals.scad#function-f_nand) Func – Returns a function to check if `a` and `b` are not both true.
- [`f_napprox()`](fnliterals.scad#function-f_napprox) Func – Returns a function to compare if `a` is not approximately equal to `b`.
- [`f_neg()`](fnliterals.scad#function-f_neg) Func – Returns a function to calculate `-a`
- [`f_neq()`](fnliterals.scad#function-f_neq) Func – Returns a function to compare if `a` is not exactly equal to `b`.
- [`f_nor()`](fnliterals.scad#function-f_nor) Func – Returns a function to check if neither `a` nor `b` are true.
- [`f_norm()`](fnliterals.scad#function-f_norm) Func – Returns a function to calculate the norm of a given vector.
- [`f_not()`](fnliterals.scad#function-f_not) Func – Returns a function to check if `a` is not true.
- [`f_odd()`](fnliterals.scad#function-f_odd) Func – Returns a function to check if `a` is an odd number.
- [`f_or()`](fnliterals.scad#function-f_or) Func – Returns a function to check if either `a` or `b` is true.
- [`f_ord()`](fnliterals.scad#function-f_ord) Func – Returns a function to get the ordinal number of a string character.
- [`f_pow()`](fnliterals.scad#function-f_pow) Func – Returns a function to calculate `a` to the power of `b`.
- [`f_round()`](fnliterals.scad#function-f_round) Func – Returns a function to calculate the integer rounding of a given number.
- [`f_sign()`](fnliterals.scad#function-f_sign) Func – Returns a function to calculate the sign of a given number.
- [`f_sin()`](fnliterals.scad#function-f_sin) Func – Returns a function to calculate the sine of a value.
- [`f_sqr()`](fnliterals.scad#function-f_sqr) Func – Returns a function to calculate the square of a given number.
- [`f_sqrt()`](fnliterals.scad#function-f_sqrt) Func – Returns a function to calculate the square root of a given number.
- [`f_str()`](fnliterals.scad#function-f_str) Func – Returns a function to get the string representation of an arbitrary value.
- [`f_str2()`](fnliterals.scad#function-f_str2) Func – Returns a function to concatenate the string representations of two arbitrary values.
- [`f_str3()`](fnliterals.scad#function-f_str3) Func – Returns a function to concatenate the string representations of three arbitrary values.
- [`f_sub()`](fnliterals.scad#function-f_sub) Func – Returns a function to subtract `a` from `b`.
- [`f_tan()`](fnliterals.scad#function-f_tan) Func – Returns a function to calculate the tangent of a value.
- [`f_xor()`](fnliterals.scad#function-f_xor) Func – Returns a function to check if either `a` or `b`, but not both, are true.
- [`filter()`](fnliterals.scad#function-filter) Func – Returns just the list items which the given function returns true for.
- [`find_all()`](fnliterals.scad#function-find_all) Func – Returns the indices of all items in a list that a given function returns true for.
- [`find_first()`](fnliterals.scad#function-find_first) Func – Returns the index of the first item in a list, after `start`, that a given function returns true for.
- [`for_n()`](fnliterals.scad#function-for_n) Func – Iteratively calls a work function `n` times, returning the final result.
- [`hashmap()`](fnliterals.scad#function-hashmap) Func – Creates a hashmap manipulation function.
- [`is_func()`](utility.scad#function-is_func) Func – Returns true if the argument is a function literal.
- [`ival()`](fnliterals.scad#function-ival) Func – Generates a function with signature `(i,x)` that calls `func(i)`
- [`map()`](fnliterals.scad#function-map) Func – Applies a function to each item in a list.
- [`reduce()`](fnliterals.scad#function-reduce) Func – Applies a 2-arg function cumulatively to the items of a list, returning the final result.
- [`simple_hash()`](fnliterals.scad#function-simple_hash) Func – Returns an integer hash of a given value.
- [`while()`](fnliterals.scad#function-while) Func – While a `cond` function returns true, iteratively calls a work function, returning the final result.
- [`xval()`](fnliterals.scad#function-xval) Func – Generates a function with signature `(i,x)` that calls `func(x)`

### Function Plotting

- [`plot3d()`](shapes3d.scad#functionmodule-plot3d) Func/Mod – Generates a surface by evaluating a function on a 2D grid <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup>
- [`plot_revolution()`](shapes3d.scad#functionmodule-plot_revolution) Func/Mod – Generates a surface by evaluating a of z and theta and putting the result on a surface of revolution <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup>

### Gears

- [`auto_profile_shift()`](gears.scad#function-auto_profile_shift) Func – Returns the recommended profile shift for a gear.
- [`bevel_gear()`](gears.scad#functionmodule-bevel_gear) Func/Mod – Creates a straight, zerol, or spiral bevel gear. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup>
- [`bevel_pitch_angle()`](gears.scad#function-bevel_pitch_angle) Func – Returns the pitch cone angle for a bevel gear.
- [`circular_pitch()`](gears.scad#function-circular_pitch) Func – Returns tooth density expressed as "circular pitch".
- [`crown_gear()`](gears.scad#functionmodule-crown_gear) Func/Mod – Creates a crown gear that can mesh with a spur gear. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup>
- [`diametral_pitch()`](gears.scad#function-diametral_pitch) Func – Returns tooth density expressed as "diametral pitch".
- [`enveloping_worm()`](gears.scad#functionmodule-enveloping_worm) Func/Mod – Creates a double-enveloping worm that will mate with a worm gear. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup>
- [`gear_dist()`](gears.scad#function-gear_dist) Func – Returns the distance between two gear centers for spur gears or parallel axis helical gears.
- [`gear_dist_skew()`](gears.scad#function-gear_dist_skew) Func – Returns the distance between two helical gear centers with skew axes.
- [`module_value()`](gears.scad#function-module_value) Func – Returns tooth density expressed as "module"
- [`outer_radius()`](gears.scad#function-outer_radius) Func – Returns the outer radius for a gear.
- [`pitch_radius()`](gears.scad#function-pitch_radius) Func – Returns the pitch radius for a gear.
- [`rack()`](gears.scad#functionmodule-rack) Func/Mod – Creates a straight or helical gear rack. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup>
- [`rack2d()`](gears.scad#functionmodule-rack2d) Func/Mod – Creates a 2D gear rack. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`ring_gear()`](gears.scad#module-ring_gear) Mod – Creates a 3D ring gear. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`ring_gear2d()`](gears.scad#module-ring_gear2d) Mod – Creates a 2D ring gear. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`root_radius()`](gears.scad#function-root_radius) Func – Returns the radius of the roots of the teeth
- [`spur_gear()`](gears.scad#functionmodule-spur_gear) Func/Mod – Creates a spur gear, helical gear, or internal ring gear. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup>
- [`spur_gear2d()`](gears.scad#functionmodule-spur_gear2d) Func/Mod – Creates a 2D spur gear or internal ring gear. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Region.">[<abbr>Region</abbr>]</sup>
- [`worm()`](gears.scad#functionmodule-worm) Func/Mod – Creates a worm that will mate with a worm gear. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup>
- [`worm_dist()`](gears.scad#function-worm_dist) Func – Returns the distance between a worm and a worm gear
- [`worm_gear()`](gears.scad#functionmodule-worm_gear) Func/Mod – Creates a worm gear that will mate with a worm. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup>
- [`worm_gear_thickness()`](gears.scad#function-worm_gear_thickness) Func – Returns the thickness for a worm gear.

### Geometry

- [`adj_ang_to_hyp()`](trigonometry.scad#function-adj_ang_to_hyp) Func – Returns the hypotenuse length from the length of the adjacent side and the reference reference angle.
- [`adj_ang_to_opp()`](trigonometry.scad#function-adj_ang_to_opp) Func – Returns the opposite side length from the length of the adjacent side and the reference reference angle.
- [`adj_hyp_to_ang()`](trigonometry.scad#function-adj_hyp_to_ang) Func – Returns the reference angle from the lengths of the adjacent side and the hypotenuse.
- [`adj_hyp_to_opp()`](trigonometry.scad#function-adj_hyp_to_opp) Func – Returns the opposite side length from the lengths of the adjacent side and the hypotenuse.
- [`adj_opp_to_ang()`](trigonometry.scad#function-adj_opp_to_ang) Func – Returns the reference angle from the lengths of the adjacent and opposite sides.
- [`adj_opp_to_hyp()`](trigonometry.scad#function-adj_opp_to_hyp) Func – Returns the hypotenuse length from the lengths of the adjacent and opposite sides.
- [`align_polygon()`](geometry.scad#function-align_polygon) Func – Find best alignment of a 2d polygon to a reference 2d polygon over a set of transformations.
- [`ang_adj_to_hyp()`](trigonometry.scad#function-ang_adj_to_hyp) Func – Returns the hypotenuse length from the reference reference angle and length of the adjacent side.
- [`ang_adj_to_opp()`](trigonometry.scad#function-ang_adj_to_opp) Func – Returns the opposite side length from the reference reference angle and the length of the adjacent side.
- [`ang_hyp_to_adj()`](trigonometry.scad#function-ang_hyp_to_adj) Func – Returns the adjacent side length from the reference reference angle and the length of the hypotenuse.
- [`ang_hyp_to_opp()`](trigonometry.scad#function-ang_hyp_to_opp) Func – Returns the opposite side length from the reference reference angle and the length of the hypotenuse.
- [`ang_opp_to_adj()`](trigonometry.scad#function-ang_opp_to_adj) Func – Returns the adjacent side length from the reference reference angle and the length of the opposite side.
- [`ang_opp_to_hyp()`](trigonometry.scad#function-ang_opp_to_hyp) Func – Returns the hypotenuse length from the reference reference angle and the length of the opposite side.
- [`are_points_on_plane()`](geometry.scad#function-are_points_on_plane) Func – Determine if all of the listed points are on a plane.
- [`are_polygons_equal()`](geometry.scad#function-are_polygons_equal) Func – Check if two polygons (not necessarily in the same point order) are equal.
- [`bezier_line_intersection()`](beziers.scad#function-bezier_line_intersection) Func – Calculates where a bezier curve intersects a line.
- [`ccw_polygon()`](geometry.scad#function-ccw_polygon) Func – Return counter-clockwise version of a polygon.
- [`centroid()`](geometry.scad#function-centroid) Func – Compute centroid of a 2d or 3d polygon or a VNF.
- [`circle_2tangents()`](geometry.scad#function-circle_2tangents) Func – Given two 2d or 3d rays, find a circle tangent to both.
- [`circle_3points()`](geometry.scad#function-circle_3points) Func – Find a circle passing through three 2d or 3d points.
- [`circle_circle_intersection()`](geometry.scad#function-circle_circle_intersection) Func – Find the intersection points of two 2d circles.
- [`circle_circle_tangents()`](geometry.scad#function-circle_circle_tangents) Func – Find tangents to a pair of circles in 2d.
- [`circle_line_intersection()`](geometry.scad#function-circle_line_intersection) Func – Find the intersection points between a 2d circle and a line, ray or segment.
- [`circle_point_tangents()`](geometry.scad#function-circle_point_tangents) Func – Given a circle and point, find tangents to circle passing through the point.
- [`clockwise_polygon()`](geometry.scad#function-clockwise_polygon) Func – Return clockwise version of a polygon.
- [`closest_point()`](vectors.scad#function-closest_point) Func – Finds the closest point in a list of points.
- [`convex_collision()`](geometry.scad#function-convex_collision) Func – Check whether the convex hulls of two point lists intersect.
- [`convex_distance()`](geometry.scad#function-convex_distance) Func – Compute distance between convex hull of two point lists.
- [`fit_to_box()`](vectors.scad#function-fit_to_box) Func – Scale the x, y, and/or z coordinates of a list of points to span a range.
- [`furthest_point()`](vectors.scad#function-furthest_point) Func – Finds the furthest point in a list of points.
- [`hull()`](geometry.scad#function-hull) Func – Convex hull of a list of 2d or 3d points. <sup title="Extends the OpenScad keyword of the same name.">[<abbr>Ext</abbr>]</sup>
- [`hull2d_path()`](geometry.scad#function-hull2d_path) Func – Convex hull of a list of 2d points.
- [`hull3d_faces()`](geometry.scad#function-hull3d_faces) Func – Convex hull of a list of 3d points.
- [`hull_points()`](geometry.scad#module-hull_points) Mod – Convex hull of a list of 2d or 3d points.
- [`hyp_adj_to_ang()`](trigonometry.scad#function-hyp_adj_to_ang) Func – Returns the reference reference angle from the lengths of the hypotenuse and the adjacent side.
- [`hyp_adj_to_opp()`](trigonometry.scad#function-hyp_adj_to_opp) Func – Returns the opposite side length from the lengths of the hypotenuse and the adjacent side.
- [`hyp_ang_to_adj()`](trigonometry.scad#function-hyp_ang_to_adj) Func – Returns the adjacent side length from the length of the hypotenuse and the reference reference angle.
- [`hyp_ang_to_opp()`](trigonometry.scad#function-hyp_ang_to_opp) Func – Returns the opposite side length from the length of the hypotenuse and the reference reference angle.
- [`hyp_opp_to_adj()`](trigonometry.scad#function-hyp_opp_to_adj) Func – Returns the adjacent side length from the lengths of the hypotenuse and the opposite side.
- [`hyp_opp_to_ang()`](trigonometry.scad#function-hyp_opp_to_ang) Func – Returns the reference reference angle from the lengths of the hypotenuse and the opposite side.
- [`is_collinear()`](geometry.scad#function-is_collinear) Func – Determine if points are collinear.
- [`is_coplanar()`](geometry.scad#function-is_coplanar) Func – Check if 3d points are coplanar and not collinear.
- [`is_point_on_line()`](geometry.scad#function-is_point_on_line) Func – Determine if a point is on a line, ray or segment.
- [`is_polygon_clockwise()`](geometry.scad#function-is_polygon_clockwise) Func – Determine if a 2d polygon winds clockwise.
- [`is_polygon_convex()`](geometry.scad#function-is_polygon_convex) Func – Check if a polygon is convex.
- [`law_of_cosines()`](trigonometry.scad#function-law_of_cosines) Func – Applies the Law of Cosines for an arbitrary triangle.
- [`law_of_sines()`](trigonometry.scad#function-law_of_sines) Func – Applies the Law of Sines for an arbitrary triangle.
- [`line_closest_point()`](geometry.scad#function-line_closest_point) Func – Find point on given line, segment or ray that is closest to a given point.
- [`line_from_points()`](geometry.scad#function-line_from_points) Func – Given a list of collinear points, return the line they define.
- [`line_intersection()`](geometry.scad#function-line_intersection) Func – Compute intersection of two lines, segments or rays.
- [`line_normal()`](geometry.scad#function-line_normal) Func – Return normal vector to given line.
- [`opp_adj_to_ang()`](trigonometry.scad#function-opp_adj_to_ang) Func – Returns the reference reference angle from the lengths of the opposite and adjacent sides.
- [`opp_adj_to_hyp()`](trigonometry.scad#function-opp_adj_to_hyp) Func – Returns the hypotenuse length from the lengths of the opposite and adjacent sides.
- [`opp_ang_to_adj()`](trigonometry.scad#function-opp_ang_to_adj) Func – Returns the adjacent side length from the length of the opposite side and the reference reference angle.
- [`opp_ang_to_hyp()`](trigonometry.scad#function-opp_ang_to_hyp) Func – Returns the hypotenuse length from the length of the opposite side and the reference reference angle.
- [`opp_hyp_to_adj()`](trigonometry.scad#function-opp_hyp_to_adj) Func – Returns the adjacent side length from the lengths of the opposite side and the hypotenuse.
- [`opp_hyp_to_ang()`](trigonometry.scad#function-opp_hyp_to_ang) Func – Returns the reference reference angle from the lengths of the opposite side and the hypotenuse.
- [`plane3pt()`](geometry.scad#function-plane3pt) Func – Return a plane from 3 points.
- [`plane3pt_indexed()`](geometry.scad#function-plane3pt_indexed) Func – Given list of 3d points and 3 indices, return the plane they define.
- [`plane_closest_point()`](geometry.scad#function-plane_closest_point) Func – Returns the orthogonal projection of points onto a plane.
- [`plane_from_normal()`](geometry.scad#function-plane_from_normal) Func – Return plane defined by normal vector and a point.
- [`plane_from_points()`](geometry.scad#function-plane_from_points) Func – Return plane defined by a set of 3D points, with arbitrary normal direction.
- [`plane_from_polygon()`](geometry.scad#function-plane_from_polygon) Func – Given a 3d planar polygon, returns directed plane.
- [`plane_intersection()`](geometry.scad#function-plane_intersection) Func – Returns the intersection of two or three planes.
- [`plane_line_angle()`](geometry.scad#function-plane_line_angle) Func – Returns the angle between a plane and a 3d line.
- [`plane_line_intersection()`](geometry.scad#function-plane_line_intersection) Func – Returns the intersection of a plane and 3d line, segment or ray.
- [`plane_normal()`](geometry.scad#function-plane_normal) Func – Returns the normal vector to a plane.
- [`plane_offset()`](geometry.scad#function-plane_offset) Func – Returns the signed offset of the plane from the origin.
- [`point_in_polygon()`](geometry.scad#function-point_in_polygon) Func – Checks if a 2d point is inside or on the boundary of a 2d polygon.
- [`point_line_distance()`](geometry.scad#function-point_line_distance) Func – Find shortest distance from point to a line, segment or ray.
- [`point_plane_distance()`](geometry.scad#function-point_plane_distance) Func – Determine distance between a point and plane.
- [`pointlist_bounds()`](vectors.scad#function-pointlist_bounds) Func – Returns the min and max bounding coordinates for the given list of points.
- [`polygon_area()`](geometry.scad#function-polygon_area) Func – Calculate area of a 2d or 3d polygon.
- [`polygon_line_intersection()`](geometry.scad#function-polygon_line_intersection) Func – Find intersection between 2d or 3d polygon and a line, segment or ray.
- [`polygon_normal()`](geometry.scad#function-polygon_normal) Func – Return normal to a polygon.
- [`polygon_triangulate()`](geometry.scad#function-polygon_triangulate) Func – Divide a polygon into triangles.
- [`quadratic_roots()`](math.scad#function-quadratic_roots) Func – Computes roots for the quadratic equation.
- [`reindex_polygon()`](geometry.scad#function-reindex_polygon) Func – Adjust point indexing of polygon to minimize pointwise distance to a reference polygon.
- [`reverse_polygon()`](geometry.scad#function-reverse_polygon) Func – Reverse winding direction of polygon.
- [`segment_distance()`](geometry.scad#function-segment_distance) Func – Find smallest distance between two line semgnets.
- [`segs()`](utility.scad#function-segs) Func – Returns the number of sides for a circle given `$fn`, `$fa`, and `$fs`.
- [`sphere_line_intersection()`](geometry.scad#function-sphere_line_intersection) Func – Find intersection between a sphere and line, ray or segment.
- [`surface_normals()`](paths.scad#function-surface_normals) Func – Estimates the normals to a surface defined by a [point](Glossary#point) array

### Hashing

- [`hashmap()`](fnliterals.scad#function-hashmap) Func – Creates a hashmap manipulation function.
- [`simple_hash()`](fnliterals.scad#function-simple_hash) Func – Returns an integer hash of a given value.

### Hinges

- [`apply_folding_hinges_and_snaps()`](hinges.scad#module-apply_folding_hinges_and_snaps) Mod – Adds snap shapes and removes living hinges from a child shape. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`knuckle_hinge()`](hinges.scad#module-knuckle_hinge) Mod – Creates a knuckle-hinge shape. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`living_hinge_mask()`](hinges.scad#module-living_hinge_mask) Mod – Creates a mask to make a folding "living" hinge. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`snap_lock()`](hinges.scad#module-snap_lock) Mod – Creates a snap-lock shape. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`snap_socket()`](hinges.scad#module-snap_socket) Mod – Creates a snap-lock socket shape. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>

### Hulling

- [`conv_hull()`](attachments.scad#module-conv_hull) Mod – Performs a hull operation on the children using tags to determine what happens.
- [`hull()`](geometry.scad#function-hull) Func – Convex hull of a list of 2d or 3d points. <sup title="Extends the OpenScad keyword of the same name.">[<abbr>Ext</abbr>]</sup>
- [`hull2d_path()`](geometry.scad#function-hull2d_path) Func – Convex hull of a list of 2d points.
- [`hull3d_faces()`](geometry.scad#function-hull3d_faces) Func – Convex hull of a list of 3d points.
- [`hull_points()`](geometry.scad#module-hull_points) Mod – Convex hull of a list of 2d or 3d points.

### Indexing

- [`count()`](math.scad#function-count) Func – Creates a list of incrementing numbers.

### Interpolation

- [`bilerp()`](math.scad#function-bilerp) Func – Bi-linear interpolation between four values
- [`debug_nurbs_interp()`](nurbs.scad#module-debug_nurbs_interp) Mod – Interpolates a NURBS using [`nurbs_interp()`](#function-nurbs\_interp) and displays the curve with informative overlays.
- [`lerp()`](math.scad#function-lerp) Func – Linearly interpolates between two values.
- [`lerpn()`](math.scad#function-lerpn) Func – Returns exactly `n` values, linearly interpolated between `a` and `b`.
- [`nurbs_interp()`](nurbs.scad#function-nurbs_interp) Func – Finds a NURBS curve passing through a point list with optional derivative constraints.
- [`nurbs_interp_surface()`](nurbs.scad#functionmodule-nurbs_interp_surface) Func/Mod – Returns a NURBS surface that passes through a grid of 3D data points. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`rot_resample()`](skin.scad#function-rot_resample) Func – Resample a list of rotation operators. <sup title="Can return a list of transformation matrices.">[<abbr>MatList</abbr>]</sup>
- [`slerp()`](math.scad#function-slerp) Func – Spherical lerp(), great-circle interpolation on a unit sphere.
- [`slerpn()`](math.scad#function-slerpn) Func – Spherical lerpn(), returns exactly `n` vectors interpolated on a great circle.

### Intersection

- [`bezier_line_intersection()`](beziers.scad#function-bezier_line_intersection) Func – Calculates where a bezier curve intersects a line.
- [`circle_line_intersection()`](geometry.scad#function-circle_line_intersection) Func – Find the intersection points between a 2d circle and a line, ray or segment.
- [`convex_collision()`](geometry.scad#function-convex_collision) Func – Check whether the convex hulls of two point lists intersect.
- [`plane_intersection()`](geometry.scad#function-plane_intersection) Func – Returns the intersection of two or three planes.
- [`plane_line_intersection()`](geometry.scad#function-plane_line_intersection) Func – Returns the intersection of a plane and 3d line, segment or ray.
- [`polygon_line_intersection()`](geometry.scad#function-polygon_line_intersection) Func – Find intersection between 2d or 3d polygon and a line, segment or ray.
- [`sphere_line_intersection()`](geometry.scad#function-sphere_line_intersection) Func – Find intersection between a sphere and line, ray or segment.

### Isosurfaces

- [`isosurface()`](isosurface.scad#functionmodule-isosurface) Func/Mod – Creates a 3D isosurface (a 3D contour) from a function or array of values. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup>
- [`metaballs()`](isosurface.scad#functionmodule-metaballs) Func/Mod – Creates a group of 3D metaballs (smoothly connected blobs). <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup>

### Iteration

- [`combinations()`](lists.scad#function-combinations) Func – Returns a list of all combinations of the list entries.
- [`for_n()`](fnliterals.scad#function-for_n) Func – Iteratively calls a work function `n` times, returning the final result.
- [`idx()`](lists.scad#function-idx) Func – Returns a range useful for iterating over a list.
- [`loop_done()`](utility.scad#function-loop_done) Func – Returns true if the argument indicates the current C-style loop is finishing.
- [`loop_while()`](utility.scad#function-loop_while) Func – Returns true if both arguments indicate the current C-style loop should continue.
- [`looping()`](utility.scad#function-looping) Func – Returns true if the argument indicates the current C-style loop should continue.
- [`pair()`](lists.scad#function-pair) Func – Returns a list of overlapping consecutive pairs in a list.
- [`permutations()`](lists.scad#function-permutations) Func – Returns a list of all permutations of the list entries.
- [`triplet()`](lists.scad#function-triplet) Func – Returns a list of overlapping consecutive triplets in a list.
- [`while()`](fnliterals.scad#function-while) Func – While a `cond` function returns true, iteratively calls a work function, returning the final result.

### Joiners

- [`dovetail()`](joiners.scad#module-dovetail) Mod – Creates a possibly tapered dovetail shape. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`half_joiner()`](joiners.scad#functionmodule-half_joiner) Func/Mod – Creates a half-joiner shape to mate with a [`half_joiner2()`](#functionmodule-half\_joiner2) shape.. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup>
- [`half_joiner2()`](joiners.scad#functionmodule-half_joiner2) Func/Mod – Creates a half\_joiner2 shape to mate with a [`half_joiner()`](#functionmodule-half\_joiner) shape.. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup>
- [`half_joiner_clear()`](joiners.scad#functionmodule-half_joiner_clear) Func/Mod – Creates a mask to clear space for a [`half_joiner()`](#functionmodule-half\_joiner). <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup>
- [`joiner()`](joiners.scad#module-joiner) Mod – Creates a joiner shape that can mate with another rotated joiner shape. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`joiner_clear()`](joiners.scad#module-joiner_clear) Mod – Creates a mask to clear space for a [`joiner()`](#module-joiner) shape. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`rabbit_clip()`](joiners.scad#module-rabbit_clip) Mod – Creates a rabbit-eared clip that can snap into a slot. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`snap_pin()`](joiners.scad#module-snap_pin) Mod – Creates a snap-pin that can slot into a [`snap_pin_socket()`](#module-snap\_pin\_socket) to join two parts. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`snap_pin_socket()`](joiners.scad#module-snap_pin_socket) Mod – Creates a snap-pin socket for a [`snap_pin()`](#module-snap\_pin) to slot into. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>

### Linear Algebra

- [`back_substitute()`](linalg.scad#function-back_substitute) Func – Solve an upper triangular system, Rx=b.
- [`cholesky()`](linalg.scad#function-cholesky) Func – Compute the Cholesky factorization of a matrix.
- [`det2()`](linalg.scad#function-det2) Func – Compute determinant of 2x2 matrix.
- [`det3()`](linalg.scad#function-det3) Func – Compute determinant of 3x3 matrix.
- [`det4()`](linalg.scad#function-det4) Func – Compute determinant of 4x4 matrix.
- [`determinant()`](linalg.scad#function-determinant) Func – compute determinant of an arbitrary square matrix.
- [`linear_solve()`](linalg.scad#function-linear_solve) Func – Solve Ax=b or, for overdetermined case, solve the least square problem.
- [`linear_solve3()`](linalg.scad#function-linear_solve3) Func – Fast solution to Ax=b where A is 3x3.
- [`lu_factor()`](linalg.scad#function-lu_factor) Func – Compute LU factorization of a matrix with pivoting.
- [`matrix_inverse()`](linalg.scad#function-matrix_inverse) Func – General matrix inverse.
- [`matrix_trace()`](linalg.scad#function-matrix_trace) Func – Compute the trace of a square matrix.
- [`norm_fro()`](linalg.scad#function-norm_fro) Func – Compute Frobenius norm of a matrix
- [`null_space()`](linalg.scad#function-null_space) Func – Return basis for the null space of A.
- [`outer_product()`](linalg.scad#function-outer_product) Func – Compute the outer product of two vectors.
- [`qr_factor()`](linalg.scad#function-qr_factor) Func – Compute QR factorization of a matrix.
- [`rot_inverse()`](linalg.scad#function-rot_inverse) Func – Invert 2d or 3d rotation transformations.
- [`swap_columns()`](linalg.scad#function-swap_columns) Func – Swap two columns of a matrix
- [`transpose()`](linalg.scad#function-transpose) Func – Transpose a matrix

### Lines

- [`circle_line_intersection()`](geometry.scad#function-circle_line_intersection) Func – Find the intersection points between a 2d circle and a line, ray or segment.
- [`LINE`](constants.scad#constant-line) Const – A constant for specifying an unbounded line in various geometry.scad functions.  `[false,false]`
- [`line_closest_point()`](geometry.scad#function-line_closest_point) Func – Find point on given line, segment or ray that is closest to a given point.
- [`line_from_points()`](geometry.scad#function-line_from_points) Func – Given a list of collinear points, return the line they define.
- [`line_intersection()`](geometry.scad#function-line_intersection) Func – Compute intersection of two lines, segments or rays.
- [`line_normal()`](geometry.scad#function-line_normal) Func – Return normal vector to given line.
- [`plane_line_angle()`](geometry.scad#function-plane_line_angle) Func – Returns the angle between a plane and a 3d line.
- [`plane_line_intersection()`](geometry.scad#function-plane_line_intersection) Func – Returns the intersection of a plane and 3d line, segment or ray.
- [`point_line_distance()`](geometry.scad#function-point_line_distance) Func – Find shortest distance from point to a line, segment or ray.
- [`polygon_line_intersection()`](geometry.scad#function-polygon_line_intersection) Func – Find intersection between 2d or 3d polygon and a line, segment or ray.
- [`RAY`](constants.scad#constant-ray) Const – A constant for specifying a ray line in various geometry.scad functions.  `[true,false]`
- [`SEGMENT`](constants.scad#constant-segment) Const – A constant for specifying a line segment in various geometry.scad functions.  `[true,true]`
- [`sphere_line_intersection()`](geometry.scad#function-sphere_line_intersection) Func – Find intersection between a sphere and line, ray or segment.

### List Handling

- [`all_equal()`](comparisons.scad#function-all_equal) Func – Returns true if all items in a list are approximately equal to each other.
- [`all_negative()`](comparisons.scad#function-all_negative) Func – Returns true if the value(s) given are less than zero.
- [`all_nonnegative()`](comparisons.scad#function-all_nonnegative) Func – Returns true if the value(s) given are greater than or equal to zero.
- [`all_nonpositive()`](comparisons.scad#function-all_nonpositive) Func – Returns true if the value(s) given are less than or equal to zero.
- [`all_nonzero()`](comparisons.scad#function-all_nonzero) Func – Returns true if the value(s) given are not approximately zero.
- [`all_positive()`](comparisons.scad#function-all_positive) Func – Returns true if the value(s) given are greater than zero.
- [`all_zero()`](comparisons.scad#function-all_zero) Func – Returns true if the value(s) given are approximately zero.
- [`are_ends_equal()`](comparisons.scad#function-are_ends_equal) Func – Returns true if the first and last items in a list are approximately equal.
- [`bselect()`](lists.scad#function-bselect) Func – Select list items using boolean index list.
- [`column()`](linalg.scad#function-column) Func – Extract a column from a matrix.
- [`combinations()`](lists.scad#function-combinations) Func – Returns a list of all combinations of the list entries.
- [`compare_lists()`](comparisons.scad#function-compare_lists) Func – Compares two lists of values, possibly of different type.
- [`compare_vals()`](comparisons.scad#function-compare_vals) Func – Compares two values, possibly of different type.
- [`deduplicate()`](comparisons.scad#function-deduplicate) Func – Returns a list with all consecutive duplicate values removed.
- [`deduplicate_indexed()`](comparisons.scad#function-deduplicate_indexed) Func – Takes a list of indices into a list of values, and returns a list of indices whose values are not consecutively the same.
- [`find_approx()`](comparisons.scad#function-find_approx) Func – Finds the indexes of the item(s) in the given list that are approximately the given value.
- [`flatten()`](lists.scad#function-flatten) Func – Flattens a list of sublists into a single list.
- [`force_list()`](lists.scad#function-force_list) Func – Coerces non-list values into a list.
- [`force_region()`](regions.scad#function-force_region) Func – Given a polygon returns a region. <sup title="Can return a Region.">[<abbr>Region</abbr>]</sup>
- [`full_flatten()`](lists.scad#function-full_flatten) Func – Recursively flattens nested sublists into a single list of non-list values.
- [`group_data()`](comparisons.scad#function-group_data) Func – Groups list data by integer group numbers.
- [`group_sort()`](comparisons.scad#function-group_sort) Func – Returns a sorted list of groups of values.
- [`idx()`](lists.scad#function-idx) Func – Returns a range useful for iterating over a list.
- [`in_list()`](lists.scad#function-in_list) Func – Returns true if a value is in a list.
- [`is_decreasing()`](comparisons.scad#function-is_decreasing) Func – Returns true if every item in a list is less than the previous item.
- [`is_homogeneous()`](lists.scad#function-is_homogeneous) Func – Returns true if all members of a list are of the same type.
- [`is_homogeneous()`](lists.scad#function-is_homogeneous) Func – Returns true if all members of a list are of the same type.
- [`is_increasing()`](comparisons.scad#function-is_increasing) Func – Returns true if every item in a list is greater than the previous item.
- [`is_region()`](regions.scad#function-is_region) Func – Returns true if the input appears to be a [region](Glossary#region).
- [`is_region_simple()`](regions.scad#function-is_region_simple) Func – Returns true if the input is a region with no corner contact.
- [`is_valid_region()`](regions.scad#function-is_valid_region) Func – Returns true if the input is a valid [region](Glossary#region).
- [`last()`](lists.scad#function-last) Func – Returns the last item of a list.
- [`list()`](lists.scad#function-list) Func – Expands a range into a full list.
- [`list_bset()`](lists.scad#function-list_bset) Func – Returns a list where values are spread to locations indicated by a boolean index list.
- [`list_head()`](lists.scad#function-list_head) Func – Returns the elements at the beginning of a list.
- [`list_insert()`](lists.scad#function-list_insert) Func – Inserts values into the middle of a list.
- [`list_largest()`](comparisons.scad#function-list_largest) Func – Returns the `k` largest values in the list, in arbitrary order.
- [`list_pad()`](lists.scad#function-list_pad) Func – Extend list to specified length.
- [`list_remove()`](lists.scad#function-list_remove) Func – Removes items by index from a list.
- [`list_remove_values()`](lists.scad#function-list_remove_values) Func – Removes items by value from a list.
- [`list_rotate()`](lists.scad#function-list_rotate) Func – Rotates the ordering of a list.
- [`list_set()`](lists.scad#function-list_set) Func – Sets the value of specific list items.
- [`list_shape()`](lists.scad#function-list_shape) Func – Returns the dimensions of an array.
- [`list_smallest()`](comparisons.scad#function-list_smallest) Func – Returns the `k` smallest values in the list, in arbitrary order.
- [`list_swap()`](lists.scad#function-list_swap) Func – Swaps two items in a list by index
- [`list_tail()`](lists.scad#function-list_tail) Func – Returns the elements at the end of a list.
- [`list_to_matrix()`](lists.scad#function-list_to_matrix) Func – Groups items in a list into sublists.
- [`list_unwrap()`](comparisons.scad#function-list_unwrap) Func – Removes the last item of a list if its first and last values are equal.
- [`list_wrap()`](comparisons.scad#function-list_wrap) Func – Returns a list whose last value is the same as the first.
- [`make_region()`](regions.scad#function-make_region) Func – Converts lists of intersecting [polygons](Glossary#polygon) into valid [regions](Glossary#region). <sup title="Can return a Region.">[<abbr>Region</abbr>]</sup>
- [`max_index()`](comparisons.scad#function-max_index) Func – Returns the index of the maximum value in the given list.
- [`max_length()`](lists.scad#function-max_length) Func – Given a list of sublists, returns the length of the longest sublist.
- [`min_index()`](comparisons.scad#function-min_index) Func – Returns the index of the minimum value in the given list.
- [`min_length()`](lists.scad#function-min_length) Func – Given a list of sublists, returns the length of the shortest sublist.
- [`pair()`](lists.scad#function-pair) Func – Returns a list of overlapping consecutive pairs in a list.
- [`permutations()`](lists.scad#function-permutations) Func – Returns a list of all permutations of the list entries.
- [`rainbow()`](color.scad#module-rainbow) Mod – Iterates through a list, displaying children in different colors. <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup>
- [`region()`](regions.scad#module-region) Mod – Creates the 2D [polygons](Glossary#polygon) described by the given [region](Glossary#region) or list of polygons. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`region_parts()`](regions.scad#function-region_parts) Func – Splits a [region](Glossary#region) into a list of connected regions. <sup title="Can return a list of Regions.">[<abbr>RegList</abbr>]</sup>
- [`repeat()`](lists.scad#function-repeat) Func – Returns a list of repeated copies of a value.
- [`repeat_entries()`](lists.scad#function-repeat_entries) Func – Repeats list entries (as uniformly as possible) to make list of specified length.
- [`reverse()`](lists.scad#function-reverse) Func – Reverses the elements of a list.
- [`select()`](lists.scad#function-select) Func – Returns one or more items from a list, with wrapping.
- [`set_difference()`](lists.scad#function-set_difference) Func – Returns a list of unique items that are in list A, but not in list B.
- [`set_intersection()`](lists.scad#function-set_intersection) Func – Returns a list of unique items that are in both given lists.
- [`set_union()`](lists.scad#function-set_union) Func – Merges two lists, returning a list of unique items.
- [`shuffle()`](lists.scad#function-shuffle) Func – Randomizes the order of a list.
- [`slice()`](lists.scad#function-slice) Func – Returns part of a list without wrapping.
- [`sort()`](comparisons.scad#function-sort) Func – Returns a sorted list.
- [`sortidx()`](comparisons.scad#function-sortidx) Func – Returns a list of sorted indices into a list.
- [`split_region_at_region_crossings()`](regions.scad#function-split_region_at_region_crossings) Func – Splits [regions](Glossary#region) where [polygons](Glossary#polygon) touch and at intersections.
- [`triplet()`](lists.scad#function-triplet) Func – Returns a list of overlapping consecutive triplets in a list.
- [`unique()`](comparisons.scad#function-unique) Func – Returns a sorted list with all duplicates removed.
- [`unique_approx()`](comparisons.scad#function-unique_approx) Func – Returns a subset whose retained items are pairwise separated by a tolerance.
- [`unique_approx_indexed()`](comparisons.scad#function-unique_approx_indexed) Func – Returns indices of a subset whose retained items are separated by more than a tolerance.
- [`unique_count()`](comparisons.scad#function-unique_count) Func – Returns a sorted list of unique items with counts.

### Lists

- [`vnf_from_polygons()`](vnf.scad#function-vnf_from_polygons) Func – Returns a VNF from a list of 3D polygons. <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup>
- [`vnf_from_region()`](vnf.scad#function-vnf_from_region) Func – Returns a 3D VNF given a 2D region. <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup>
- [`vnf_join()`](vnf.scad#function-vnf_join) Func – Returns a single VNF structure from a list of VNF structures. <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup>
- [`vnf_tri_array()`](vnf.scad#functionmodule-vnf_tri_array) Func/Mod – Returns a VNF from an array of points. The array need not be rectangular. <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup>
- [`vnf_vertex_array()`](vnf.scad#functionmodule-vnf_vertex_array) Func/Mod – Returns a VNF structure from a rectangular vertex list. <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>

### Logic

- [`f_and()`](fnliterals.scad#function-f_and) Func – Returns a function to check if both `a` and `b` are true.
- [`f_nand()`](fnliterals.scad#function-f_nand) Func – Returns a function to check if `a` and `b` are not both true.
- [`f_nor()`](fnliterals.scad#function-f_nor) Func – Returns a function to check if neither `a` nor `b` are true.
- [`f_not()`](fnliterals.scad#function-f_not) Func – Returns a function to check if `a` is not true.
- [`f_or()`](fnliterals.scad#function-f_or) Func – Returns a function to check if either `a` or `b` is true.
- [`f_xor()`](fnliterals.scad#function-f_xor) Func – Returns a function to check if either `a` or `b`, but not both, are true.

### Looping

- [`accumulate()`](fnliterals.scad#function-accumulate) Func – Applies a 2-arg function cumulatively to the items of a list, returning a list of every result.
- [`filter()`](fnliterals.scad#function-filter) Func – Returns just the list items which the given function returns true for.
- [`find_all()`](fnliterals.scad#function-find_all) Func – Returns the indices of all items in a list that a given function returns true for.
- [`for_n()`](fnliterals.scad#function-for_n) Func – Iteratively calls a work function `n` times, returning the final result.
- [`map()`](fnliterals.scad#function-map) Func – Applies a function to each item in a list.
- [`reduce()`](fnliterals.scad#function-reduce) Func – Applies a 2-arg function cumulatively to the items of a list, returning the final result.
- [`while()`](fnliterals.scad#function-while) Func – While a `cond` function returns true, iteratively calls a work function, returning the final result.

### Masking

- [`back_half()`](partitions.scad#functionmodule-back_half) Func/Mod – Masks the front half of an object along the X-Z plane, leaving the back half. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup> <sup title="Can return a Region.">[<abbr>Region</abbr>]</sup>
- [`bottom_half()`](partitions.scad#functionmodule-bottom_half) Func/Mod – Masks the top half of an object along the X-Y plane, leaving the bottom half. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup> <sup title="Can return a Region.">[<abbr>Region</abbr>]</sup>
- [`chamfer_corner_mask()`](masks.scad#module-chamfer_corner_mask) Mod – Creates a shape to chamfer a 90° corner. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`chamfer_cylinder_mask()`](masks.scad#module-chamfer_cylinder_mask) Mod – Creates a shape to chamfer the end of a cylinder. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`chamfer_edge_mask()`](masks.scad#module-chamfer_edge_mask) Mod – Creates a shape to chamfer a 90° edge. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`corner_mask()`](masks.scad#module-corner_mask) Mod – Attaches a 3d mask shape to the given corners of the parent. <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup>
- [`corner_profile()`](masks.scad#module-corner_profile) Mod – Rotationally extrudes a 2d edge profile into corner mask on the given corners of the parent. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`edge_mask()`](masks.scad#module-edge_mask) Mod – Attaches a 3D mask shape to the given edges of the parent. <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup>
- [`edge_profile()`](masks.scad#module-edge_profile) Mod – Extrudes a 2d edge profile into a mask on edges of the parent cuboid, prismoid or cone. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`edge_profile_asym()`](masks.scad#module-edge_profile_asym) Mod – Extrudes an asymmetric 2D profile into a mask on edges and corners of the parent cuboid. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`face_mask()`](masks.scad#module-face_mask) Mod – Ataches a 3d mask shape to the given faces of the parent. <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup>
- [`face_profile()`](masks.scad#module-face_profile) Mod – Extrudes a 2D edge profile into a mask for all edges and corners of the given faces on the parent. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`front_half()`](partitions.scad#functionmodule-front_half) Func/Mod – Masks the back half of an object along the X-Z plane, leaving the front half. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup> <sup title="Can return a Region.">[<abbr>Region</abbr>]</sup>
- [`half_of()`](partitions.scad#functionmodule-half_of) Func/Mod – Masks half of an object at a cut plane. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup> <sup title="Can return a Region.">[<abbr>Region</abbr>]</sup>
- [`left_half()`](partitions.scad#functionmodule-left_half) Func/Mod – Masks the right half of an object along the Y-Z plane, leaving the left half. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup> <sup title="Can return a Region.">[<abbr>Region</abbr>]</sup>
- [`partition()`](partitions.scad#module-partition) Mod – Cuts an object in two with matched joining edges, then separates the parts. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup> <sup title="Can return a Region.">[<abbr>Region</abbr>]</sup>
- [`partition_cut_mask()`](partitions.scad#module-partition_cut_mask) Mod – Creates a mask to cut an object into two subparts that can be reassembled. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`partition_mask()`](partitions.scad#module-partition_mask) Mod – Creates a mask to remove half an object with the remaining half suitable for reassembly. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`partition_path()`](partitions.scad#module-partition_path) Mod – Creates a partition path from a path description. <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`right_half()`](partitions.scad#functionmodule-right_half) Func/Mod – Masks the left half of an object along the Y-Z plane, leaving the right half. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup> <sup title="Can return a Region.">[<abbr>Region</abbr>]</sup>
- [`rounding_corner_mask()`](masks.scad#module-rounding_corner_mask) Mod – Creates a shape to round 90° corners. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`rounding_cylinder_mask()`](masks.scad#module-rounding_cylinder_mask) Mod – Creates a shape to round the end of a cylinder. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`rounding_hole_mask()`](masks.scad#module-rounding_hole_mask) Mod – Creates a shape to round the edge of a round hole. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`teardrop_corner_mask()`](masks.scad#module-teardrop_corner_mask) Mod – Creates a shape to round a 90° corner but limit the angle of overhang. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`teardrop_edge_mask()`](masks.scad#module-teardrop_edge_mask) Mod – Creates a shape to round an edge while limiting the angle of overhang. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`top_half()`](partitions.scad#functionmodule-top_half) Func/Mod – Masks the bottom half of an object along the X-Y plane, leaving the top half. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup> <sup title="Can return a Region.">[<abbr>Region</abbr>]</sup>

### Masks

- [`hex_drive_mask()`](screw_drive.scad#module-hex_drive_mask) Mod – Creates a mask for a hex drive recess. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`phillips_depth()`](screw_drive.scad#function-phillips_depth) Func – Returns the depth a phillips recess needs to be for a given diameter.
- [`phillips_diam()`](screw_drive.scad#function-phillips_diam) Func – Returns the diameter of a phillips recess of a given depth.
- [`phillips_mask()`](screw_drive.scad#module-phillips_mask) Mod – Creates a mask for a Philips screw drive. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`polygon_edge_mask()`](masks.scad#module-polygon_edge_mask) Mod – Extrudes a 2d mask polygon to an edge mask with a correct corner anchor <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`robertson_mask()`](screw_drive.scad#module-robertson_mask) Mod – Creates a mask for a Robertson/Square drive recess. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`rounding_edge_mask()`](masks.scad#module-rounding_edge_mask) Mod – Creates a shape to round an arbitrary 3d edge. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`torx_depth()`](screw_drive.scad#function-torx_depth) Func – Returns the typical depth of a torx drive recess.
- [`torx_diam()`](screw_drive.scad#function-torx_diam) Func – Returns the diameter of a torx drive.
- [`torx_info()`](screw_drive.scad#function-torx_info) Func – Returns the dimensions of a torx drive.
- [`torx_mask()`](screw_drive.scad#module-torx_mask) Mod – Creates a mask for a torx drive recess. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`torx_mask2d()`](screw_drive.scad#module-torx_mask2d) Mod – Creates the 2D cross section for a torx drive recess. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>

### Masks (2D)

- [`mask2d_chamfer()`](masks.scad#functionmodule-mask2d_chamfer) Func/Mod – Produces a 2D chamfer mask shape. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`mask2d_cove()`](masks.scad#functionmodule-mask2d_cove) Func/Mod – Creates a 2D cove (quarter-round) mask shape. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`mask2d_dovetail()`](masks.scad#functionmodule-mask2d_dovetail) Func/Mod – Creates a 2D dovetail mask shape. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`mask2d_ogee()`](masks.scad#functionmodule-mask2d_ogee) Func/Mod – Creates a 2D ogee mask shape. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`mask2d_rabbet()`](masks.scad#functionmodule-mask2d_rabbet) Func/Mod – Creates a rabbet mask shape. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`mask2d_roundover()`](masks.scad#functionmodule-mask2d_roundover) Func/Mod – Creates a circular mask shape for rounding edges or beading. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`mask2d_smooth()`](masks.scad#functionmodule-mask2d_smooth) Func/Mod – Creates a continuous curvature mask for rounding edges. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`mask2d_teardrop()`](masks.scad#functionmodule-mask2d_teardrop) Func/Mod – Creates a 2D teardrop shape with specified max angle from vertical. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>

### Math

- [`acosh()`](math.scad#function-acosh) Func – Returns the hyperbolic arc-cosine of the given value.
- [`add_scalar()`](vectors.scad#function-add_scalar) Func – Adds a scalar value to every item in a vector.
- [`asinh()`](math.scad#function-asinh) Func – Returns the hyperbolic arc-sine of the given value.
- [`atanh()`](math.scad#function-atanh) Func – Returns the hyperbolic arc-tangent of the given value.
- [`bilerp()`](math.scad#function-bilerp) Func – Bi-linear interpolation between four values
- [`binomial()`](math.scad#function-binomial) Func – Returns the binomial coefficients of the integer `n`.
- [`binomial_coefficient()`](math.scad#function-binomial_coefficient) Func – Returns the `k`-th binomial coefficient of the integer `n`.
- [`c_conj()`](math.scad#function-c_conj) Func – Returns the complex conjugate of the input.
- [`c_div()`](math.scad#function-c_div) Func – Divides two complex numbers.
- [`c_ident()`](math.scad#function-c_ident) Func – Returns an n by n complex identity matrix.
- [`c_imag()`](math.scad#function-c_imag) Func – Returns the imaginary part of a complex number, vector or matrix..
- [`c_mul()`](math.scad#function-c_mul) Func – Multiplies two complex numbers.
- [`c_norm()`](math.scad#function-c_norm) Func – Returns the norm of a complex number or vector.
- [`c_real()`](math.scad#function-c_real) Func – Returns the real part of a complex number, vector or matrix..
- [`complex()`](math.scad#function-complex) Func – Replaces scalars in a list or matrix with complex number 2-vectors.
- [`constrain()`](math.scad#function-constrain) Func – Limit (clamp) a number or array of numbers to a specified range of values.
- [`convolve()`](math.scad#function-convolve) Func – Returns the convolution of `p` and `q`.
- [`cosh()`](math.scad#function-cosh) Func – Returns the hyperbolic cosine of the given value.
- [`count()`](math.scad#function-count) Func – Creates a list of incrementing numbers.
- [`cumprod()`](math.scad#function-cumprod) Func – Returns the running cumulative product of a list of values.
- [`cumsum()`](math.scad#function-cumsum) Func – Returns the running cumulative sum of a list of values.
- [`deltas()`](math.scad#function-deltas) Func – Returns the deltas between a list of values.
- [`deriv()`](math.scad#function-deriv) Func – Returns the first derivative estimate of a list of data.
- [`deriv2()`](math.scad#function-deriv2) Func – Returns the second derivative estimate of a list of data.
- [`deriv3()`](math.scad#function-deriv3) Func – Returns the third derivative estimate of a list of data.
- [`EPSILON`](math.scad#constant-epsilon) Const – A tiny value to compare floating point values.  1e-9
- [`factorial()`](math.scad#function-factorial) Func – Returns the factorial of the given integer.
- [`fit_to_range()`](math.scad#function-fit_to_range) Func – Scale the values in an array to span a range.
- [`gcd()`](math.scad#function-gcd) Func – Returns the Greatest Common Divisor/Factor of two integers.
- [`hypot()`](math.scad#function-hypot) Func – Returns the hypotenuse length of a 2D or 3D triangle.
- [`INF`](math.scad#constant-inf) Const – The floating point value for Infinite.
- [`is_vector()`](vectors.scad#function-is_vector) Func – Returns true if the given value is a vector.
- [`lcm()`](math.scad#function-lcm) Func – Returns the Least Common Multiple of two or more integers.
- [`lerp()`](math.scad#function-lerp) Func – Linearly interpolates between two values.
- [`lerpn()`](math.scad#function-lerpn) Func – Returns exactly `n` values, linearly interpolated between `a` and `b`.
- [`log2()`](math.scad#function-log2) Func – Returns the log base 2 of the given value.
- [`mean()`](math.scad#function-mean) Func – Returns the mean value of a list of values.
- [`mean_angle()`](math.scad#function-mean_angle) Func – Returns the mean angle of two angles
- [`median()`](math.scad#function-median) Func – Returns the median value of a list of values.
- [`modang()`](math.scad#function-modang) Func – Returns an angle normalized to between -180º and 180º.
- [`NAN`](math.scad#constant-nan) Const – The floating point value for Not a Number.
- [`PHI`](math.scad#constant-phi) Const – The golden ratio φ (phi).  Approximately 1.6180339887
- [`poly_add()`](math.scad#function-poly_add) Func – Returns the polynomial sum of adding two polynomials.
- [`poly_div()`](math.scad#function-poly_div) Func – Returns the polynomial quotient and remainder results of dividing two polynomials.
- [`poly_mult()`](math.scad#function-poly_mult) Func – Compute product of two polynomials, returning a polynomial.
- [`poly_roots()`](math.scad#function-poly_roots) Func – Returns all complex valued roots of the given real polynomial.
- [`polynomial()`](math.scad#function-polynomial) Func – Evaluate a polynomial at a real or complex value.
- [`posmod()`](math.scad#function-posmod) Func – Returns the positive modulo of a value.
- [`product()`](math.scad#function-product) Func – Returns the multiplicative product of a list of values.
- [`quadratic_roots()`](math.scad#function-quadratic_roots) Func – Computes roots for the quadratic equation.
- [`quant()`](math.scad#function-quant) Func – Returns `x` quantized to the nearest integer multiple of `y`.
- [`quantdn()`](math.scad#function-quantdn) Func – Returns `x` quantized down to an integer multiple of `y`.
- [`quantup()`](math.scad#function-quantup) Func – Returns `x` quantized uo to an integer multiple of `y`.
- [`real_roots()`](math.scad#function-real_roots) Func – Returns all real roots of the given real polynomial.
- [`root_find()`](math.scad#function-root_find) Func – Finds a root of the given continuous function.
- [`sinh()`](math.scad#function-sinh) Func – Returns the hyperbolic sine of the given value.
- [`slerp()`](math.scad#function-slerp) Func – Spherical lerp(), great-circle interpolation on a unit sphere.
- [`slerpn()`](math.scad#function-slerpn) Func – Spherical lerpn(), returns exactly `n` vectors interpolated on a great circle.
- [`sqr()`](math.scad#function-sqr) Func – Returns the square of the given value.
- [`sum()`](math.scad#function-sum) Func – Returns the sum of a list of values.
- [`sum_of_sines()`](math.scad#function-sum_of_sines) Func – Returns the sum of one or more sine waves at a given angle.
- [`surface_normals()`](paths.scad#function-surface_normals) Func – Estimates the normals to a surface defined by a [point](Glossary#point) array
- [`tanh()`](math.scad#function-tanh) Func – Returns the hyperbolic tangent of the given value.
- [`unit()`](vectors.scad#function-unit) Func – Returns the unit length of a given vector.
- [`v_abs()`](vectors.scad#function-v_abs) Func – Returns the absolute values of the given vector.
- [`v_ceil()`](vectors.scad#function-v_ceil) Func – Returns the values of the given vector, rounded up.
- [`v_div()`](vectors.scad#function-v_div) Func – Returns the element-wise division of two equal-length vectors.
- [`v_floor()`](vectors.scad#function-v_floor) Func – Returns the values of the given vector, rounded down.
- [`v_lookup()`](vectors.scad#function-v_lookup) Func – Like `lookup()`, but it can interpolate between vector results.
- [`v_mul()`](vectors.scad#function-v_mul) Func – Returns the element-wise multiplication of two equal-length vectors.
- [`v_round()`](vectors.scad#function-v_round) Func – Returns the values of the given vector, rounded to the nearest whole number.
- [`v_theta()`](vectors.scad#function-v_theta) Func – Returns the angle counter-clockwise from X+ on the XY plane.
- [`vector_angle()`](vectors.scad#function-vector_angle) Func – Returns the minor angle between two vectors.
- [`vector_axis()`](vectors.scad#function-vector_axis) Func – Returns the perpendicular axis between two vectors.
- [`vector_bisect()`](vectors.scad#function-vector_bisect) Func – Returns the vector that bisects two vectors.
- [`vector_perp()`](vectors.scad#function-vector_perp) Func – Returns component of a vector perpendicular to a second vector

### Math Operators

- [`f_abs()`](fnliterals.scad#function-f_abs) Func – Returns a function to calculate the absolute value of a given number.
- [`f_acos()`](fnliterals.scad#function-f_acos) Func – Returns a function to calculate the arccosine of a value.
- [`f_add()`](fnliterals.scad#function-f_add) Func – Returns a function to add `a` and `b`.
- [`f_asin()`](fnliterals.scad#function-f_asin) Func – Returns a function to calculate the arcsine of a value.
- [`f_atan()`](fnliterals.scad#function-f_atan) Func – Returns a function to calculate the arctangent of a value.
- [`f_atan2()`](fnliterals.scad#function-f_atan2) Func – Returns a function to calculate the arctangent of `y` and `x`
- [`f_ceil()`](fnliterals.scad#function-f_ceil) Func – Returns a function to calculate the integer ceiling of a given number.
- [`f_cos()`](fnliterals.scad#function-f_cos) Func – Returns a function to calculate the cosine of a value.
- [`f_div()`](fnliterals.scad#function-f_div) Func – Returns a function to divide `a` by `b`.
- [`f_even()`](fnliterals.scad#function-f_even) Func – Returns a function to check if `a` is an even number.
- [`f_exp()`](fnliterals.scad#function-f_exp) Func – Returns a function to calculate the natural exponent of a given number.
- [`f_floor()`](fnliterals.scad#function-f_floor) Func – Returns a function to calculate the integer floor of a given number.
- [`f_ln()`](fnliterals.scad#function-f_ln) Func – Returns a function to calculate the natural logarithm of a given number.
- [`f_log()`](fnliterals.scad#function-f_log) Func – Returns a function to calculate the base 10 logarithm of a given number.
- [`f_max()`](fnliterals.scad#function-f_max) Func – Returns a function to calculate the maximum value of a list.
- [`f_max2()`](fnliterals.scad#function-f_max2) Func – Returns a function to calculate the maximum of two values.
- [`f_max3()`](fnliterals.scad#function-f_max3) Func – Returns a function to calculate the maximum of three values.
- [`f_min()`](fnliterals.scad#function-f_min) Func – Returns a function to calculate the minimum value of a list.
- [`f_min2()`](fnliterals.scad#function-f_min2) Func – Returns a function to calculate the minimum of two values.
- [`f_min3()`](fnliterals.scad#function-f_min3) Func – Returns a function to calculate the minimum of three values.
- [`f_mod()`](fnliterals.scad#function-f_mod) Func – Returns a function to calculate the modulo of `a` divided by `b`.
- [`f_mul()`](fnliterals.scad#function-f_mul) Func – Returns a function to multiply `a` by `b`.
- [`f_neg()`](fnliterals.scad#function-f_neg) Func – Returns a function to calculate `-a`
- [`f_odd()`](fnliterals.scad#function-f_odd) Func – Returns a function to check if `a` is an odd number.
- [`f_pow()`](fnliterals.scad#function-f_pow) Func – Returns a function to calculate `a` to the power of `b`.
- [`f_round()`](fnliterals.scad#function-f_round) Func – Returns a function to calculate the integer rounding of a given number.
- [`f_sign()`](fnliterals.scad#function-f_sign) Func – Returns a function to calculate the sign of a given number.
- [`f_sin()`](fnliterals.scad#function-f_sin) Func – Returns a function to calculate the sine of a value.
- [`f_sqr()`](fnliterals.scad#function-f_sqr) Func – Returns a function to calculate the square of a given number.
- [`f_sqrt()`](fnliterals.scad#function-f_sqrt) Func – Returns a function to calculate the square root of a given number.
- [`f_str3()`](fnliterals.scad#function-f_str3) Func – Returns a function to concatenate the string representations of three arbitrary values.
- [`f_sub()`](fnliterals.scad#function-f_sub) Func – Returns a function to subtract `a` from `b`.
- [`f_tan()`](fnliterals.scad#function-f_tan) Func – Returns a function to calculate the tangent of a value.

### Matrices

- [`apply()`](transforms.scad#function-apply) Func – Applies a transformation matrix to a point, list of points, array of points, or a VNF. <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return a transformation matrix.">[<abbr>Mat</abbr>]</sup>
- [`back()`](transforms.scad#functionmodule-back) Func/Mod – Translates children backward (Y+). <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return a transformation matrix.">[<abbr>Mat</abbr>]</sup>
- [`back_substitute()`](linalg.scad#function-back_substitute) Func – Solve an upper triangular system, Rx=b.
- [`block_matrix()`](linalg.scad#function-block_matrix) Func – Make a new matrix from a block of matrices.
- [`cholesky()`](linalg.scad#function-cholesky) Func – Compute the Cholesky factorization of a matrix.
- [`column()`](linalg.scad#function-column) Func – Extract a column from a matrix.
- [`det2()`](linalg.scad#function-det2) Func – Compute determinant of 2x2 matrix.
- [`det3()`](linalg.scad#function-det3) Func – Compute determinant of 3x3 matrix.
- [`det4()`](linalg.scad#function-det4) Func – Compute determinant of 4x4 matrix.
- [`determinant()`](linalg.scad#function-determinant) Func – compute determinant of an arbitrary square matrix.
- [`diagonal_matrix()`](linalg.scad#function-diagonal_matrix) Func – Make a diagonal matrix.
- [`down()`](transforms.scad#functionmodule-down) Func/Mod – Translates children downward (Z-). <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return a transformation matrix.">[<abbr>Mat</abbr>]</sup>
- [`echo_matrix()`](linalg.scad#functionmodule-echo_matrix) Func/Mod – Print a matrix neatly to the console.
- [`flatten()`](lists.scad#function-flatten) Func – Flattens a list of sublists into a single list.
- [`frame_map()`](transforms.scad#functionmodule-frame_map) Func/Mod – Rotates and possibly skews children from one frame of reference to another. <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return a transformation matrix.">[<abbr>Mat</abbr>]</sup>
- [`full_flatten()`](lists.scad#function-full_flatten) Func – Recursively flattens nested sublists into a single list of non-list values.
- [`fwd()`](transforms.scad#functionmodule-fwd) Func/Mod – Translates children forward (Y-). <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return a transformation matrix.">[<abbr>Mat</abbr>]</sup>
- [`hstack()`](linalg.scad#function-hstack) Func – Make a new matrix by stacking matrices horizontally.
- [`IDENT`](constants.scad#constant-ident) Const – A constant, the 3D identity transformation matrix. <sup title="Can return a transformation matrix.">[<abbr>Mat</abbr>]</sup>
- [`ident()`](linalg.scad#function-ident) Func – Return identity matrix.
- [`is_matrix()`](linalg.scad#function-is_matrix) Func – Check if input is a numeric matrix or tensor, optionally of specified size
- [`is_matrix_symmetric()`](linalg.scad#function-is_matrix_symmetric) Func – Checks if matrix is symmetric
- [`is_rotation()`](linalg.scad#function-is_rotation) Func – Check if a transformation matrix represents a rotation.
- [`left()`](transforms.scad#functionmodule-left) Func/Mod – Translates children leftward (X-). <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return a transformation matrix.">[<abbr>Mat</abbr>]</sup>
- [`linear_solve()`](linalg.scad#function-linear_solve) Func – Solve Ax=b or, for overdetermined case, solve the least square problem.
- [`linear_solve3()`](linalg.scad#function-linear_solve3) Func – Fast solution to Ax=b where A is 3x3.
- [`list_shape()`](lists.scad#function-list_shape) Func – Returns the dimensions of an array.
- [`list_to_matrix()`](lists.scad#function-list_to_matrix) Func – Groups items in a list into sublists.
- [`lu_factor()`](linalg.scad#function-lu_factor) Func – Compute LU factorization of a matrix with pivoting.
- [`matrix_inverse()`](linalg.scad#function-matrix_inverse) Func – General matrix inverse.
- [`matrix_trace()`](linalg.scad#function-matrix_trace) Func – Compute the trace of a square matrix.
- [`mirror()`](transforms.scad#functionmodule-mirror) Func/Mod – Reflects children across an arbitrary plane. <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return a transformation matrix.">[<abbr>Mat</abbr>]</sup> <sup title="Extends the OpenScad keyword of the same name.">[<abbr>Ext</abbr>]</sup>
- [`move()`](transforms.scad#functionmodule-move) Func/Mod – Translates children in an arbitrary direction. <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return a transformation matrix.">[<abbr>Mat</abbr>]</sup>
- [`norm_fro()`](linalg.scad#function-norm_fro) Func – Compute Frobenius norm of a matrix
- [`null_space()`](linalg.scad#function-null_space) Func – Return basis for the null space of A.
- [`outer_product()`](linalg.scad#function-outer_product) Func – Compute the outer product of two vectors.
- [`qr_factor()`](linalg.scad#function-qr_factor) Func – Compute QR factorization of a matrix.
- [`right()`](transforms.scad#functionmodule-right) Func/Mod – Translates children rightward (X+). <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return a transformation matrix.">[<abbr>Mat</abbr>]</sup>
- [`rot()`](transforms.scad#functionmodule-rot) Func/Mod – Rotates children in various ways. <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return a transformation matrix.">[<abbr>Mat</abbr>]</sup>
- [`rot_decode()`](geometry.scad#function-rot_decode) Func – Extract axis and rotation angle from a rotation matrix.
- [`rot_inverse()`](linalg.scad#function-rot_inverse) Func – Invert 2d or 3d rotation transformations.
- [`rot_resample()`](skin.scad#function-rot_resample) Func – Resample a list of rotation operators. <sup title="Can return a list of transformation matrices.">[<abbr>MatList</abbr>]</sup>
- [`scale()`](transforms.scad#functionmodule-scale) Func/Mod – Scales children arbitrarily. <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return a transformation matrix.">[<abbr>Mat</abbr>]</sup> <sup title="Extends the OpenScad keyword of the same name.">[<abbr>Ext</abbr>]</sup>
- [`skew()`](transforms.scad#functionmodule-skew) Func/Mod – Skews (or shears) children along various axes. <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return a transformation matrix.">[<abbr>Mat</abbr>]</sup>
- [`submatrix()`](linalg.scad#function-submatrix) Func – Extract a submatrix from a matrix
- [`submatrix_set()`](linalg.scad#function-submatrix_set) Func – Takes a matrix as input and change values in a submatrix.
- [`swap_columns()`](linalg.scad#function-swap_columns) Func – Swap two columns of a matrix
- [`tilt()`](transforms.scad#functionmodule-tilt) Func/Mod – Tilts children toward a direction <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return a transformation matrix.">[<abbr>Mat</abbr>]</sup>
- [`move()`](transforms.scad#functionmodule-move) Func/Mod – Translates children in an arbitrary direction. <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return a transformation matrix.">[<abbr>Mat</abbr>]</sup>
- [`transpose()`](linalg.scad#function-transpose) Func – Transpose a matrix
- [`up()`](transforms.scad#functionmodule-up) Func/Mod – Translates children upward (Z+). <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return a transformation matrix.">[<abbr>Mat</abbr>]</sup>
- [`xflip()`](transforms.scad#functionmodule-xflip) Func/Mod – Reflects children across the YZ plane. <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return a transformation matrix.">[<abbr>Mat</abbr>]</sup>
- [`right()`](transforms.scad#functionmodule-right) Func/Mod – Translates children rightward (X+). <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return a transformation matrix.">[<abbr>Mat</abbr>]</sup>
- [`xrot()`](transforms.scad#functionmodule-xrot) Func/Mod – Rotates children around the X axis using the right-hand rule. <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return a transformation matrix.">[<abbr>Mat</abbr>]</sup>
- [`xscale()`](transforms.scad#functionmodule-xscale) Func/Mod – Scales children along the X axis. <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return a transformation matrix.">[<abbr>Mat</abbr>]</sup>
- [`yflip()`](transforms.scad#functionmodule-yflip) Func/Mod – Reflects children across the XZ plane. <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return a transformation matrix.">[<abbr>Mat</abbr>]</sup>
- [`back()`](transforms.scad#functionmodule-back) Func/Mod – Translates children backward (Y+). <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return a transformation matrix.">[<abbr>Mat</abbr>]</sup>
- [`yrot()`](transforms.scad#functionmodule-yrot) Func/Mod – Rotates children around the Y axis using the right-hand rule. <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return a transformation matrix.">[<abbr>Mat</abbr>]</sup>
- [`yscale()`](transforms.scad#functionmodule-yscale) Func/Mod – Scales children along the Y axis. <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return a transformation matrix.">[<abbr>Mat</abbr>]</sup>
- [`zflip()`](transforms.scad#functionmodule-zflip) Func/Mod – Reflects children across the XY plane. <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return a transformation matrix.">[<abbr>Mat</abbr>]</sup>
- [`up()`](transforms.scad#functionmodule-up) Func/Mod – Translates children upward (Z+). <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return a transformation matrix.">[<abbr>Mat</abbr>]</sup>
- [`zrot()`](transforms.scad#functionmodule-zrot) Func/Mod – Rotates children around the Z axis using the right-hand rule. <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return a transformation matrix.">[<abbr>Mat</abbr>]</sup>
- [`zscale()`](transforms.scad#functionmodule-zscale) Func/Mod – Scales children along the Z axis. <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return a transformation matrix.">[<abbr>Mat</abbr>]</sup>

### Metaballs

- [`metaballs()`](isosurface.scad#functionmodule-metaballs) Func/Mod – Creates a group of 3D metaballs (smoothly connected blobs). <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup>
- [`metaballs2d()`](isosurface.scad#functionmodule-metaballs2d) Func/Mod – Creates a group of 2D metaballs (smoothly connected blobs). <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Region.">[<abbr>Region</abbr>]</sup>

### Mini-Language

- [`turtle()`](drawing.scad#function-turtle) Func – Uses [turtle graphics](https://en.wikipedia.org/wiki/Turtle\_graphics) to generate a 2D path. <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`turtle3d()`](turtle3d.scad#function-turtle3d) Func – Extends [turtle graphics](https://en.wikipedia.org/wiki/Turtle\_graphics) to 3d. Generates a 3D path or returns a list of transforms. <sup title="Can return a list of transformation matrices.">[<abbr>MatList</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>

### Mirroring

- [`mirror()`](transforms.scad#functionmodule-mirror) Func/Mod – Reflects children across an arbitrary plane. <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return a transformation matrix.">[<abbr>Mat</abbr>]</sup> <sup title="Extends the OpenScad keyword of the same name.">[<abbr>Ext</abbr>]</sup>
- [`xflip()`](transforms.scad#functionmodule-xflip) Func/Mod – Reflects children across the YZ plane. <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return a transformation matrix.">[<abbr>Mat</abbr>]</sup>
- [`yflip()`](transforms.scad#functionmodule-yflip) Func/Mod – Reflects children across the XZ plane. <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return a transformation matrix.">[<abbr>Mat</abbr>]</sup>
- [`zflip()`](transforms.scad#functionmodule-zflip) Func/Mod – Reflects children across the XY plane. <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return a transformation matrix.">[<abbr>Mat</abbr>]</sup>

### Miscellaneous

- [`bounding_box()`](miscellaneous.scad#module-bounding_box) Mod – Creates the smallest bounding box that contains all the children. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`chain_hull()`](miscellaneous.scad#module-chain_hull) Mod – Performs the union of hull operations between consecutive pairs of children. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`cylindrical_extrude()`](miscellaneous.scad#module-cylindrical_extrude) Mod – Extrudes 2D children outwards around a cylinder. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`extrude_from_to()`](miscellaneous.scad#module-extrude_from_to) Mod – Extrudes 2D children between two points in 3D space. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`minkowski_difference()`](miscellaneous.scad#module-minkowski_difference) Mod – Removes diff shapes from base shape surface. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`offset3d()`](miscellaneous.scad#module-offset3d) Mod – Expands or contracts the surface of a 3D object. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`path_extrude()`](miscellaneous.scad#module-path_extrude) Mod – Extrudes 2D children along a 3D path. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`path_extrude2d()`](miscellaneous.scad#module-path_extrude2d) Mod – Extrudes 2D children along a 2D path. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`round3d()`](miscellaneous.scad#module-round3d) Mod – Rounds arbitrary 3d objects. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>

### Modifiers

- [`ghost()`](color.scad#module-ghost) Mod – Sets % modifier for attachable children and their descendants. <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup>
- [`ghost_this()`](color.scad#module-ghost_this) Mod – Apply % modifier to children at a single level. <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup>
- [`highlight()`](color.scad#module-highlight) Mod – Sets # modifier for attachable children and their descendants. <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup>
- [`highlight_this()`](color.scad#module-highlight_this) Mod – Apply # modifier to children at a single level. <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup>

### Modular Hose

- [`modular_hose()`](modular_hose.scad#module-modular_hose) Mod – Creates modular hose parts.
- [`modular_hose_radius()`](modular_hose.scad#function-modular_hose_radius) Func – Returns the waist radius of the given modular hose size.

### Motors

- [`nema_motor_info()`](nema_steppers.scad#function-nema_motor_info) Func – Returns dimension info for a given NEMA motor size.
- [`nema_mount_mask()`](nema_steppers.scad#module-nema_mount_mask) Mod – Creates a standard NEMA mount holes mask. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`nema_stepper_motor()`](nema_steppers.scad#module-nema_stepper_motor) Mod – Creates a NEMA standard stepper motor model. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>

### NURBS

- [`debug_nurbs()`](nurbs.scad#module-debug_nurbs) Mod – Shows a NURBS curve and its control points, knots and weights <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>

### NURBS Curves

- [`debug_nurbs_interp()`](nurbs.scad#module-debug_nurbs_interp) Mod – Interpolates a NURBS using [`nurbs_interp()`](#function-nurbs\_interp) and displays the curve with informative overlays.
- [`nurbs_curve()`](nurbs.scad#function-nurbs_curve) Func – Computes one or more points (or derivatives) on a NURBS curve. <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`nurbs_curve_breaks()`](nurbs.scad#function-nurbs_curve_breaks) Func – Returns the parameter-space breakpoints of a NURBS curve.
- [`nurbs_cut()`](nurbs.scad#function-nurbs_cut) Func – Finds the parameter value at a given arc length along a NURBS curve.
- [`nurbs_elevate_degree()`](nurbs.scad#function-nurbs_elevate_degree) Func – Raises the degree of a clamped or open NURBS.
- [`nurbs_interp()`](nurbs.scad#function-nurbs_interp) Func – Finds a NURBS curve passing through a point list with optional derivative constraints.
- [`nurbs_length()`](nurbs.scad#function-nurbs_length) Func – Approximates the arc length of a NURBS curve.

### NURBS Patches

- [`is_nurbs_patch()`](nurbs.scad#function-is_nurbs_patch) Func – Returns true if the given item looks like a NURBS patch.
- [`nurbs_normals()`](nurbs.scad#function-nurbs_normals) Func – Computes unit normal(s) of a NURBS surface patch, tracking per-sector normals at creases.
- [`nurbs_patch_points()`](nurbs.scad#function-nurbs_patch_points) Func – Computes specified point(s) on a NURBS surface patch
- [`nurbs_sheet()`](nurbs.scad#function-nurbs_sheet) Func – Creates a thin sheet from a NURBS patch by offsetting along the patch normals. <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup>
- [`nurbs_vnf()`](nurbs.scad#functionmodule-nurbs_vnf) Func/Mod – Generates a (possibly non-manifold) VNF for a single NURBS surface patch. <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup>

### NURBS Surfaces

- [`nurbs_interp_surface()`](nurbs.scad#functionmodule-nurbs_interp_surface) Func/Mod – Returns a NURBS surface that passes through a grid of 3D data points. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>

### Offsets

- [`bent_cutout_mask()`](rounding.scad#module-bent_cutout_mask) Mod – Create a mask for making a round-edged cutout in a cylindrical shell. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`convex_offset_extrude()`](rounding.scad#module-convex_offset_extrude) Mod – Make a solid from geometry where offset changes along the object's length. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`join_prism()`](rounding.scad#functionmodule-join_prism) Func/Mod – Join an arbitrary prism to a plane, sphere, cylinder or another arbitrary prism with a fillet. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup>
- [`offset_sweep()`](rounding.scad#functionmodule-offset_sweep) Func/Mod – Make a solid from a polygon with offset that changes along its length. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup>
- [`rounded_prism()`](rounding.scad#functionmodule-rounded_prism) Func/Mod – Make a rounded 3d object by connecting two polygons with the same vertex count. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup>

### Partitions

- [`back_half()`](partitions.scad#functionmodule-back_half) Func/Mod – Masks the front half of an object along the X-Z plane, leaving the back half. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup> <sup title="Can return a Region.">[<abbr>Region</abbr>]</sup>
- [`bottom_half()`](partitions.scad#functionmodule-bottom_half) Func/Mod – Masks the top half of an object along the X-Y plane, leaving the bottom half. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup> <sup title="Can return a Region.">[<abbr>Region</abbr>]</sup>
- [`front_half()`](partitions.scad#functionmodule-front_half) Func/Mod – Masks the back half of an object along the X-Z plane, leaving the front half. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup> <sup title="Can return a Region.">[<abbr>Region</abbr>]</sup>
- [`half_of()`](partitions.scad#functionmodule-half_of) Func/Mod – Masks half of an object at a cut plane. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup> <sup title="Can return a Region.">[<abbr>Region</abbr>]</sup>
- [`left_half()`](partitions.scad#functionmodule-left_half) Func/Mod – Masks the right half of an object along the Y-Z plane, leaving the left half. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup> <sup title="Can return a Region.">[<abbr>Region</abbr>]</sup>
- [`partition()`](partitions.scad#module-partition) Mod – Cuts an object in two with matched joining edges, then separates the parts. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup> <sup title="Can return a Region.">[<abbr>Region</abbr>]</sup>
- [`partition_cut_mask()`](partitions.scad#module-partition_cut_mask) Mod – Creates a mask to cut an object into two subparts that can be reassembled. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`partition_mask()`](partitions.scad#module-partition_mask) Mod – Creates a mask to remove half an object with the remaining half suitable for reassembly. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`partition_path()`](partitions.scad#module-partition_path) Mod – Creates a partition path from a path description. <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`right_half()`](partitions.scad#functionmodule-right_half) Func/Mod – Masks the left half of an object along the Y-Z plane, leaving the right half. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup> <sup title="Can return a Region.">[<abbr>Region</abbr>]</sup>
- [`top_half()`](partitions.scad#functionmodule-top_half) Func/Mod – Masks the bottom half of an object along the X-Y plane, leaving the top half. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup> <sup title="Can return a Region.">[<abbr>Region</abbr>]</sup>

### Parts

- [`apply_folding_hinges_and_snaps()`](hinges.scad#module-apply_folding_hinges_and_snaps) Mod – Adds snap shapes and removes living hinges from a child shape. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`auto_profile_shift()`](gears.scad#function-auto_profile_shift) Func – Returns the recommended profile shift for a gear.
- [`ball_bearing()`](ball_bearings.scad#module-ball_bearing) Mod – Creates a standardized ball bearing assembly. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`ball_bearing_info()`](ball_bearings.scad#function-ball_bearing_info) Func – Returns dimensional and feature information for a standardized ball bearing assembly.
- [`bevel_gear()`](gears.scad#functionmodule-bevel_gear) Func/Mod – Creates a straight, zerol, or spiral bevel gear. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup>
- [`bevel_pitch_angle()`](gears.scad#function-bevel_pitch_angle) Func – Returns the pitch cone angle for a bevel gear.
- [`circular_pitch()`](gears.scad#function-circular_pitch) Func – Returns tooth density expressed as "circular pitch".
- [`crown_gear()`](gears.scad#functionmodule-crown_gear) Func/Mod – Creates a crown gear that can mesh with a spur gear. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup>
- [`cubetruss()`](cubetruss.scad#module-cubetruss) Mod – Creates a multi-cube straight cubetruss shape. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`cubetruss_clip()`](cubetruss.scad#module-cubetruss_clip) Mod – Creates a clip for the end of a cubetruss to snap-lock it to another cubetruss. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`cubetruss_corner()`](cubetruss.scad#module-cubetruss_corner) Mod – Creates a multi-cube corner cubetruss shape. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`cubetruss_dist()`](cubetruss.scad#function-cubetruss_dist) Func – Returns the length of a cubetruss truss.
- [`cubetruss_foot()`](cubetruss.scad#module-cubetruss_foot) Mod – Creates a foot that can connect two cubetrusses. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`cubetruss_joiner()`](cubetruss.scad#module-cubetruss_joiner) Mod – Creates a joiner that can connect two cubetrusses end-to-end. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`cubetruss_segment()`](cubetruss.scad#module-cubetruss_segment) Mod – Creates a single cubetruss cube. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`cubetruss_support()`](cubetruss.scad#module-cubetruss_support) Mod – Creates a cubetruss support structure shape. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`cubetruss_uclip()`](cubetruss.scad#module-cubetruss_uclip) Mod – Creates a joiner that can connect two cubetrusses end-to-end. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`diametral_pitch()`](gears.scad#function-diametral_pitch) Func – Returns tooth density expressed as "diametral pitch".
- [`dovetail()`](joiners.scad#module-dovetail) Mod – Creates a possibly tapered dovetail shape. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`enveloping_worm()`](gears.scad#functionmodule-enveloping_worm) Func/Mod – Creates a double-enveloping worm that will mate with a worm gear. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup>
- [`gear_dist()`](gears.scad#function-gear_dist) Func – Returns the distance between two gear centers for spur gears or parallel axis helical gears.
- [`gear_dist_skew()`](gears.scad#function-gear_dist_skew) Func – Returns the distance between two helical gear centers with skew axes.
- [`half_joiner()`](joiners.scad#functionmodule-half_joiner) Func/Mod – Creates a half-joiner shape to mate with a [`half_joiner2()`](#functionmodule-half\_joiner2) shape.. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup>
- [`half_joiner2()`](joiners.scad#functionmodule-half_joiner2) Func/Mod – Creates a half\_joiner2 shape to mate with a [`half_joiner()`](#functionmodule-half\_joiner) shape.. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup>
- [`half_joiner_clear()`](joiners.scad#functionmodule-half_joiner_clear) Func/Mod – Creates a mask to clear space for a [`half_joiner()`](#functionmodule-half\_joiner). <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup>
- [`joiner()`](joiners.scad#module-joiner) Mod – Creates a joiner shape that can mate with another rotated joiner shape. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`joiner_clear()`](joiners.scad#module-joiner_clear) Mod – Creates a mask to clear space for a [`joiner()`](#module-joiner) shape. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`knuckle_hinge()`](hinges.scad#module-knuckle_hinge) Mod – Creates a knuckle-hinge shape. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`linear_bearing()`](linear_bearings.scad#module-linear_bearing) Mod – Creates a generic linear bearing cartridge. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`linear_bearing_housing()`](linear_bearings.scad#module-linear_bearing_housing) Mod – Creates a generic linear bearing mount clamp. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`living_hinge_mask()`](hinges.scad#module-living_hinge_mask) Mod – Creates a mask to make a folding "living" hinge. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`lmXuu_bearing()`](linear_bearings.scad#module-lmxuu_bearing) Mod – Creates a standardized LM*UU linear bearing cartridge. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`lmXuu_housing()`](linear_bearings.scad#module-lmxuu_housing) Mod – Creates a standardized LM*UU linear bearing mount clamp. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`lmXuu_info()`](linear_bearings.scad#function-lmxuu_info) Func – Returns the sizes of a standard LM*UU linear bearing cartridge.
- [`manfrotto_rc2_plate()`](tripod_mounts.scad#module-manfrotto_rc2_plate) Mod – Creates a Manfrotto RC2 tripod quick release mount plate. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`modular_hose()`](modular_hose.scad#module-modular_hose) Mod – Creates modular hose parts.
- [`modular_hose_radius()`](modular_hose.scad#function-modular_hose_radius) Func – Returns the waist radius of the given modular hose size.
- [`module_value()`](gears.scad#function-module_value) Func – Returns tooth density expressed as "module"
- [`nema_motor_info()`](nema_steppers.scad#function-nema_motor_info) Func – Returns dimension info for a given NEMA motor size.
- [`nema_mount_mask()`](nema_steppers.scad#module-nema_mount_mask) Mod – Creates a standard NEMA mount holes mask. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`nema_stepper_motor()`](nema_steppers.scad#module-nema_stepper_motor) Mod – Creates a NEMA standard stepper motor model. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`outer_radius()`](gears.scad#function-outer_radius) Func – Returns the outer radius for a gear.
- [`pitch_radius()`](gears.scad#function-pitch_radius) Func – Returns the pitch radius for a gear.
- [`rabbit_clip()`](joiners.scad#module-rabbit_clip) Mod – Creates a rabbit-eared clip that can snap into a slot. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`rack()`](gears.scad#functionmodule-rack) Func/Mod – Creates a straight or helical gear rack. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup>
- [`rack2d()`](gears.scad#functionmodule-rack2d) Func/Mod – Creates a 2D gear rack. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`rail()`](sliders.scad#module-rail) Mod – Creates a V-groove rail. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`regular_polyhedron()`](polyhedra.scad#module-regular_polyhedron) Mod – Creates a regular polyhedron with optional rounding. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`regular_polyhedron_info()`](polyhedra.scad#function-regular_polyhedron_info) Func – Returns info used to create a regular polyhedron.
- [`ring_gear()`](gears.scad#module-ring_gear) Mod – Creates a 3D ring gear. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`ring_gear2d()`](gears.scad#module-ring_gear2d) Mod – Creates a 2D ring gear. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`ring_hook()`](hooks.scad#module-ring_hook) Mod – A hook with a circular hole or attached cylinder <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`root_radius()`](gears.scad#function-root_radius) Func – Returns the radius of the roots of the teeth
- [`slider()`](sliders.scad#module-slider) Mod – Creates a V-groove slider. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`snap_lock()`](hinges.scad#module-snap_lock) Mod – Creates a snap-lock shape. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`snap_pin()`](joiners.scad#module-snap_pin) Mod – Creates a snap-pin that can slot into a [`snap_pin_socket()`](#module-snap\_pin\_socket) to join two parts. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`snap_pin_socket()`](joiners.scad#module-snap_pin_socket) Mod – Creates a snap-pin socket for a [`snap_pin()`](#module-snap\_pin) to slot into. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`snap_socket()`](hinges.scad#module-snap_socket) Mod – Creates a snap-lock socket shape. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`spur_gear()`](gears.scad#functionmodule-spur_gear) Func/Mod – Creates a spur gear, helical gear, or internal ring gear. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup>
- [`spur_gear2d()`](gears.scad#functionmodule-spur_gear2d) Func/Mod – Creates a 2D spur gear or internal ring gear. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Region.">[<abbr>Region</abbr>]</sup>
- [`worm()`](gears.scad#functionmodule-worm) Func/Mod – Creates a worm that will mate with a worm gear. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup>
- [`worm_dist()`](gears.scad#function-worm_dist) Func – Returns the distance between a worm and a worm gear
- [`worm_gear()`](gears.scad#functionmodule-worm_gear) Func/Mod – Creates a worm gear that will mate with a worm. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup>
- [`worm_gear_thickness()`](gears.scad#function-worm_gear_thickness) Func – Returns the thickness for a worm gear.

### Path Generators

- [`arc()`](drawing.scad#functionmodule-arc) Func/Mod – Draws a 2D pie-slice or returns 2D or 3D path forming an arc. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`egg()`](shapes2d.scad#functionmodule-egg) Func/Mod – Creates an egg-shaped 2d object. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`ellipse()`](shapes2d.scad#functionmodule-ellipse) Func/Mod – Creates the approximation of an ellipse or a circle. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`glued_circles()`](shapes2d.scad#functionmodule-glued_circles) Func/Mod – Creates a shape of two circles joined by a curved waist. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`helix()`](drawing.scad#function-helix) Func – Creates a 3D helical path, including flat spirals. <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`hexagon()`](shapes2d.scad#functionmodule-hexagon) Func/Mod – Creates a regular hexagon. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`keyhole()`](shapes2d.scad#functionmodule-keyhole) Func/Mod – Creates a 2D keyhole shape. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`mask2d_chamfer()`](masks.scad#functionmodule-mask2d_chamfer) Func/Mod – Produces a 2D chamfer mask shape. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`mask2d_cove()`](masks.scad#functionmodule-mask2d_cove) Func/Mod – Creates a 2D cove (quarter-round) mask shape. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`mask2d_dovetail()`](masks.scad#functionmodule-mask2d_dovetail) Func/Mod – Creates a 2D dovetail mask shape. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`mask2d_ogee()`](masks.scad#functionmodule-mask2d_ogee) Func/Mod – Creates a 2D ogee mask shape. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`mask2d_rabbet()`](masks.scad#functionmodule-mask2d_rabbet) Func/Mod – Creates a rabbet mask shape. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`mask2d_roundover()`](masks.scad#functionmodule-mask2d_roundover) Func/Mod – Creates a circular mask shape for rounding edges or beading. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`mask2d_smooth()`](masks.scad#functionmodule-mask2d_smooth) Func/Mod – Creates a continuous curvature mask for rounding edges. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`mask2d_teardrop()`](masks.scad#functionmodule-mask2d_teardrop) Func/Mod – Creates a 2D teardrop shape with specified max angle from vertical. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`octagon()`](shapes2d.scad#functionmodule-octagon) Func/Mod – Creates a regular octagon. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`path_text()`](shapes3d.scad#module-path_text) Mod – Creates 2d or 3d text placed along a path. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`pentagon()`](shapes2d.scad#functionmodule-pentagon) Func/Mod – Creates a regular pentagon. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`rect()`](shapes2d.scad#functionmodule-rect) Func/Mod – Creates a 2d rectangle with optional corner rounding. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`regular_ngon()`](shapes2d.scad#functionmodule-regular_ngon) Func/Mod – Creates a regular N-sided polygon. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`reuleaux_polygon()`](shapes2d.scad#functionmodule-reuleaux_polygon) Func/Mod – Creates a constant-width shape that is not circular. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`right_triangle()`](shapes2d.scad#functionmodule-right_triangle) Func/Mod – Creates a right triangle. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`ring()`](shapes2d.scad#functionmodule-ring) Func/Mod – Draws a 2D ring or partial ring or returns a region or path <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Region.">[<abbr>Region</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`semicircle()`](shapes2d.scad#functionmodule-semicircle) Func/Mod – Creates a semicircle with optional roundings or chamfers <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`squircle()`](shapes2d.scad#functionmodule-squircle) Func/Mod – Creates a shape between a circle and a square. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`star()`](shapes2d.scad#functionmodule-star) Func/Mod – Creates a star-shaped polygon or returns a star-shaped region. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`supershape()`](shapes2d.scad#functionmodule-supershape) Func/Mod – Creates a 2D [Superformula](https://en.wikipedia.org/wiki/Superformula) shape. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`teardrop2d()`](shapes2d.scad#functionmodule-teardrop2d) Func/Mod – Creates a 2D teardrop shape. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`trapezoid()`](shapes2d.scad#functionmodule-trapezoid) Func/Mod – Creates a trapezoid with parallel top and bottom sides. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>

### Path Generators (2D)

- [`circle()`](shapes2d.scad#functionmodule-circle) Func/Mod – Creates the approximation of a circle. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup> <sup title="Extends the OpenScad keyword of the same name.">[<abbr>Ext</abbr>]</sup>
- [`contour()`](isosurface.scad#functionmodule-contour) Func/Mod – Creates a 2D contour from a function or array of values. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup> <sup title="Can return a Region.">[<abbr>Region</abbr>]</sup>
- [`metaballs2d()`](isosurface.scad#functionmodule-metaballs2d) Func/Mod – Creates a group of 2D metaballs (smoothly connected blobs). <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Region.">[<abbr>Region</abbr>]</sup>
- [`path_text()`](shapes3d.scad#module-path_text) Mod – Creates 2d or 3d text placed along a path. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`square()`](shapes2d.scad#functionmodule-square) Func/Mod – Creates a 2D square or rectangle. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup> <sup title="Extends the OpenScad keyword of the same name.">[<abbr>Ext</abbr>]</sup>
- [`turtle()`](drawing.scad#function-turtle) Func – Uses [turtle graphics](https://en.wikipedia.org/wiki/Turtle\_graphics) to generate a 2D path. <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>

### Path Generators (3D)

- [`turtle3d()`](turtle3d.scad#function-turtle3d) Func – Extends [turtle graphics](https://en.wikipedia.org/wiki/Turtle\_graphics) to 3d. Generates a 3D path or returns a list of transforms. <sup title="Can return a list of transformation matrices.">[<abbr>MatList</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>

### Path Subdivision

- [`path_cut()`](paths.scad#function-path_cut) Func – Cuts a [path](Glossary#path) into subpaths at various [points](Glossary#point). <sup title="Can return a list of Paths.">[<abbr>PathList</abbr>]</sup>
- [`path_cut_points()`](paths.scad#function-path_cut_points) Func – Returns a list of cut [points](Glossary#point) at a list of distances from the first point in a [path](Glossary#path).
- [`slice_profiles()`](skin.scad#function-slice_profiles) Func – Linearly interpolates between path profiles. <sup title="Can return a list of Paths.">[<abbr>PathList</abbr>]</sup>
- [`split_path_at_self_crossings()`](paths.scad#function-split_path_at_self_crossings) Func – Split a 2D [path](Glossary#path) wherever it crosses itself. <sup title="Can return a list of Paths.">[<abbr>PathList</abbr>]</sup>
- [`subdivide_and_slice()`](skin.scad#function-subdivide_and_slice) Func – Resample list of paths to have the same point count and interpolate additional paths. <sup title="Can return a list of Paths.">[<abbr>PathList</abbr>]</sup>
- [`subdivide_path()`](paths.scad#function-subdivide_path) Func – Subdivides a path to produce a more finely sampled path. <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>

### Paths

- [`altaz_to_xyz()`](coords.scad#function-altaz_to_xyz) Func – Convert altitude/azimuth/range to 3D cartesian coordinates. <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`associate_vertices()`](skin.scad#function-associate_vertices) Func – Create vertex association to control how [`skin()`](#functionmodule-skin) links vertices. <sup title="Can return a list of Paths.">[<abbr>PathList</abbr>]</sup>
- [`bezier_sweep()`](beziers.scad#functionmodule-bezier_sweep) Func/Mod – Sweep a 2d polygon path along a bezier with exact tangents <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`bezpath_sweep()`](beziers.scad#functionmodule-bezpath_sweep) Func/Mod – Sweep a 2d polygon path along a bezier path with exact tangents <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`catenary()`](drawing.scad#functionmodule-catenary) Func/Mod – Returns a 2D Catenary chain or arch path. <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`cylindrical_to_xyz()`](coords.scad#function-cylindrical_to_xyz) Func – Convert cylindrical coordinates to cartesian coordinates. <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`dashed_stroke()`](drawing.scad#functionmodule-dashed_stroke) Func/Mod – Draws a dashed line along a path or region boundary. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a list of Paths.">[<abbr>PathList</abbr>]</sup>
- [`force_path()`](paths.scad#function-force_path) Func – Checks that path is a region with one component. <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`force_region()`](regions.scad#function-force_region) Func – Given a polygon returns a region. <sup title="Can return a Region.">[<abbr>Region</abbr>]</sup>
- [`helix()`](drawing.scad#function-helix) Func – Creates a 3D helical path, including flat spirals. <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`is_1region()`](paths.scad#function-is_1region) Func – Returns true if [path](Glossary#path) is a [region](Glossary#region) with one component.
- [`is_path()`](paths.scad#function-is_path) Func – Returns True if 'list' is a [path](Glossary#path).
- [`is_path_simple()`](paths.scad#function-is_path_simple) Func – Returns true if a [path](Glossary#path) has no self intersections.
- [`is_region()`](regions.scad#function-is_region) Func – Returns true if the input appears to be a [region](Glossary#region).
- [`is_region_simple()`](regions.scad#function-is_region_simple) Func – Returns true if the input is a region with no corner contact.
- [`is_valid_region()`](regions.scad#function-is_valid_region) Func – Returns true if the input is a valid [region](Glossary#region).
- [`lift_plane()`](coords.scad#function-lift_plane) Func – Map a list of 2D points onto a plane in 3D. <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`list_unwrap()`](comparisons.scad#function-list_unwrap) Func – Removes the last item of a list if its first and last values are equal.
- [`list_wrap()`](comparisons.scad#function-list_wrap) Func – Returns a list whose last value is the same as the first.
- [`make_region()`](regions.scad#function-make_region) Func – Converts lists of intersecting [polygons](Glossary#polygon) into valid [regions](Glossary#region). <sup title="Can return a Region.">[<abbr>Region</abbr>]</sup>
- [`offset()`](regions.scad#function-offset) Func – Takes a 2D [path](Glossary#path), [polygon](Glossary#polygon) or [region](Glossary#region) and returns a path offset by an amount. <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup> <sup title="Can return a Region.">[<abbr>Region</abbr>]</sup> <sup title="Extends the OpenScad keyword of the same name.">[<abbr>Ext</abbr>]</sup>
- [`offset_stroke()`](rounding.scad#functionmodule-offset_stroke) Func/Mod – Draws a line along a path with options to specify angles and roundings at the ends. <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup> <sup title="Can return a Region.">[<abbr>Region</abbr>]</sup>
- [`partition()`](partitions.scad#module-partition) Mod – Cuts an object in two with matched joining edges, then separates the parts. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup> <sup title="Can return a Region.">[<abbr>Region</abbr>]</sup>
- [`partition_cut_mask()`](partitions.scad#module-partition_cut_mask) Mod – Creates a mask to cut an object into two subparts that can be reassembled. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`partition_mask()`](partitions.scad#module-partition_mask) Mod – Creates a mask to remove half an object with the remaining half suitable for reassembly. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`partition_path()`](partitions.scad#module-partition_path) Mod – Creates a partition path from a path description. <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`path2d()`](coords.scad#function-path2d) Func – Convert a path to 2D. <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`path3d()`](coords.scad#function-path3d) Func – Convert a path to 3D. <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`path4d()`](coords.scad#function-path4d) Func – Convert a path to 4d. <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`path_closest_point()`](paths.scad#function-path_closest_point) Func – Returns the closest place on a [path](Glossary#path) to a given [point](Glossary#point).
- [`path_curvature()`](paths.scad#function-path_curvature) Func – Returns the estimated numerical curvature of the [path](Glossary#path).
- [`path_cut()`](paths.scad#function-path_cut) Func – Cuts a [path](Glossary#path) into subpaths at various [points](Glossary#point). <sup title="Can return a list of Paths.">[<abbr>PathList</abbr>]</sup>
- [`path_cut_points()`](paths.scad#function-path_cut_points) Func – Returns a list of cut [points](Glossary#point) at a list of distances from the first point in a [path](Glossary#path).
- [`path_extrude()`](miscellaneous.scad#module-path_extrude) Mod – Extrudes 2D children along a 3D path. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`path_join()`](rounding.scad#function-path_join) Func – Join paths end to end with optional rounding. <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`path_length()`](paths.scad#function-path_length) Func – Returns the path length.
- [`path_length_fractions()`](paths.scad#function-path_length_fractions) Func – Returns the fractional distance of each point along the length of a path.
- [`path_merge_collinear()`](paths.scad#function-path_merge_collinear) Func – Removes unnecessary collinear points from a path. <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`path_merge_collinear_indexed()`](paths.scad#function-path_merge_collinear_indexed) Func – Removes unnecessary collinear points from a path specified as an index list into a list <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`path_normals()`](paths.scad#function-path_normals) Func – Returns normal vectors for each point along a path.
- [`path_segment_lengths()`](paths.scad#function-path_segment_lengths) Func – Returns a list of the lengths of segments in a [path](Glossary#path).
- [`path_sweep()`](skin.scad#functionmodule-path_sweep) Func/Mod – Sweep a 2d polygon path along a 2d or 3d path. <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`path_sweep2d()`](skin.scad#functionmodule-path_sweep2d) Func/Mod – Sweep a 2d polygon path along a 2d path allowing self-intersection. <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`path_tangents()`](paths.scad#function-path_tangents) Func – Returns tangent vectors for each point along a path.
- [`path_text()`](shapes3d.scad#module-path_text) Mod – Creates 2d or 3d text placed along a path. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`path_torsion()`](paths.scad#function-path_torsion) Func – Returns the estimated numerical torsion of the [path](Glossary#path).
- [`polar_to_xy()`](coords.scad#function-polar_to_xy) Func – Convert 2D polar coordinates to cartesian coordinates. <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`polygon_parts()`](paths.scad#function-polygon_parts) Func – Parses a self-intersecting polygon into a list of non-intersecting [polygons](Glossary#polygon). <sup title="Can return a list of Paths.">[<abbr>PathList</abbr>]</sup>
- [`project_plane()`](coords.scad#function-project_plane) Func – Project a set of points onto a specified plane, returning 2D points. <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`region()`](regions.scad#module-region) Mod – Creates the 2D [polygons](Glossary#polygon) described by the given [region](Glossary#region) or list of polygons. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`resample_path()`](paths.scad#function-resample_path) Func – Returns an equidistant set of points along a path. <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`round_corners()`](rounding.scad#function-round_corners) Func – Round or chamfer the corners of a path (clipping them off). <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`simplify_path()`](paths.scad#function-simplify_path) Func – Removes points from an irregular path, preserving dominant features. <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`slice_profiles()`](skin.scad#function-slice_profiles) Func – Linearly interpolates between path profiles. <sup title="Can return a list of Paths.">[<abbr>PathList</abbr>]</sup>
- [`smooth_path()`](rounding.scad#function-smooth_path) Func – Create a smoothed path passing through all the points of a given path, or passing through all the segment midpoint tangents. <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`spherical_to_xyz()`](coords.scad#function-spherical_to_xyz) Func – Convert spherical coordinates to 3D cartesian coordinates. <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`split_path_at_self_crossings()`](paths.scad#function-split_path_at_self_crossings) Func – Split a 2D [path](Glossary#path) wherever it crosses itself. <sup title="Can return a list of Paths.">[<abbr>PathList</abbr>]</sup>
- [`subdivide_and_slice()`](skin.scad#function-subdivide_and_slice) Func – Resample list of paths to have the same point count and interpolate additional paths. <sup title="Can return a list of Paths.">[<abbr>PathList</abbr>]</sup>
- [`subdivide_path()`](paths.scad#function-subdivide_path) Func – Subdivides a path to produce a more finely sampled path. <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`sweep()`](skin.scad#functionmodule-sweep) Func/Mod – Construct a 3d object from arbitrary transformations of a 2d polygon path. <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`sweep_attach()`](skin.scad#module-sweep_attach) Mod – Attach children to sides of a path\_sweep parent object <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`xy_to_polar()`](coords.scad#function-xy_to_polar) Func – Convert 2D cartesian coordinates to polar coordinates (radius and angle)
- [`xyz_to_altaz()`](coords.scad#function-xyz_to_altaz) Func – Convert 3D cartesian coordinates to [altitude,azimuth,range].
- [`xyz_to_cylindrical()`](coords.scad#function-xyz_to_cylindrical) Func – Convert 3D cartesian coordinates to cylindrical coordinates.
- [`xyz_to_spherical()`](coords.scad#function-xyz_to_spherical) Func – Convert 3D cartesian coordinates to spherical coordinates.

### Paths (2D)

- [`arc()`](drawing.scad#functionmodule-arc) Func/Mod – Draws a 2D pie-slice or returns 2D or 3D path forming an arc. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`egg()`](shapes2d.scad#functionmodule-egg) Func/Mod – Creates an egg-shaped 2d object. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`ellipse()`](shapes2d.scad#functionmodule-ellipse) Func/Mod – Creates the approximation of an ellipse or a circle. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`glued_circles()`](shapes2d.scad#functionmodule-glued_circles) Func/Mod – Creates a shape of two circles joined by a curved waist. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`hexagon()`](shapes2d.scad#functionmodule-hexagon) Func/Mod – Creates a regular hexagon. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`keyhole()`](shapes2d.scad#functionmodule-keyhole) Func/Mod – Creates a 2D keyhole shape. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`mask2d_chamfer()`](masks.scad#functionmodule-mask2d_chamfer) Func/Mod – Produces a 2D chamfer mask shape. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`mask2d_cove()`](masks.scad#functionmodule-mask2d_cove) Func/Mod – Creates a 2D cove (quarter-round) mask shape. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`mask2d_dovetail()`](masks.scad#functionmodule-mask2d_dovetail) Func/Mod – Creates a 2D dovetail mask shape. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`mask2d_ogee()`](masks.scad#functionmodule-mask2d_ogee) Func/Mod – Creates a 2D ogee mask shape. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`mask2d_rabbet()`](masks.scad#functionmodule-mask2d_rabbet) Func/Mod – Creates a rabbet mask shape. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`mask2d_roundover()`](masks.scad#functionmodule-mask2d_roundover) Func/Mod – Creates a circular mask shape for rounding edges or beading. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`mask2d_smooth()`](masks.scad#functionmodule-mask2d_smooth) Func/Mod – Creates a continuous curvature mask for rounding edges. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`mask2d_teardrop()`](masks.scad#functionmodule-mask2d_teardrop) Func/Mod – Creates a 2D teardrop shape with specified max angle from vertical. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`octagon()`](shapes2d.scad#functionmodule-octagon) Func/Mod – Creates a regular octagon. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`path_text()`](shapes3d.scad#module-path_text) Mod – Creates 2d or 3d text placed along a path. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`pentagon()`](shapes2d.scad#functionmodule-pentagon) Func/Mod – Creates a regular pentagon. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`rect()`](shapes2d.scad#functionmodule-rect) Func/Mod – Creates a 2d rectangle with optional corner rounding. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`regular_ngon()`](shapes2d.scad#functionmodule-regular_ngon) Func/Mod – Creates a regular N-sided polygon. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`reuleaux_polygon()`](shapes2d.scad#functionmodule-reuleaux_polygon) Func/Mod – Creates a constant-width shape that is not circular. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`right_triangle()`](shapes2d.scad#functionmodule-right_triangle) Func/Mod – Creates a right triangle. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`ring()`](shapes2d.scad#functionmodule-ring) Func/Mod – Draws a 2D ring or partial ring or returns a region or path <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Region.">[<abbr>Region</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`semicircle()`](shapes2d.scad#functionmodule-semicircle) Func/Mod – Creates a semicircle with optional roundings or chamfers <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`squircle()`](shapes2d.scad#functionmodule-squircle) Func/Mod – Creates a shape between a circle and a square. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`star()`](shapes2d.scad#functionmodule-star) Func/Mod – Creates a star-shaped polygon or returns a star-shaped region. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`stroke()`](drawing.scad#module-stroke) Mod – Draws a line along a path or region boundary. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`supershape()`](shapes2d.scad#functionmodule-supershape) Func/Mod – Creates a 2D [Superformula](https://en.wikipedia.org/wiki/Superformula) shape. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`teardrop2d()`](shapes2d.scad#functionmodule-teardrop2d) Func/Mod – Creates a 2D teardrop shape. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`trapezoid()`](shapes2d.scad#functionmodule-trapezoid) Func/Mod – Creates a trapezoid with parallel top and bottom sides. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>

### Paths (3D)

- [`arc()`](drawing.scad#functionmodule-arc) Func/Mod – Draws a 2D pie-slice or returns 2D or 3D path forming an arc. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`path_text()`](shapes3d.scad#module-path_text) Mod – Creates 2d or 3d text placed along a path. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`stroke()`](drawing.scad#module-stroke) Mod – Draws a line along a path or region boundary. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>

### Planes

- [`are_points_on_plane()`](geometry.scad#function-are_points_on_plane) Func – Determine if all of the listed points are on a plane.
- [`plane3pt()`](geometry.scad#function-plane3pt) Func – Return a plane from 3 points.
- [`plane3pt_indexed()`](geometry.scad#function-plane3pt_indexed) Func – Given list of 3d points and 3 indices, return the plane they define.
- [`plane_closest_point()`](geometry.scad#function-plane_closest_point) Func – Returns the orthogonal projection of points onto a plane.
- [`plane_from_normal()`](geometry.scad#function-plane_from_normal) Func – Return plane defined by normal vector and a point.
- [`plane_from_points()`](geometry.scad#function-plane_from_points) Func – Return plane defined by a set of 3D points, with arbitrary normal direction.
- [`plane_from_polygon()`](geometry.scad#function-plane_from_polygon) Func – Given a 3d planar polygon, returns directed plane.
- [`plane_intersection()`](geometry.scad#function-plane_intersection) Func – Returns the intersection of two or three planes.
- [`plane_line_angle()`](geometry.scad#function-plane_line_angle) Func – Returns the angle between a plane and a 3d line.
- [`plane_line_intersection()`](geometry.scad#function-plane_line_intersection) Func – Returns the intersection of a plane and 3d line, segment or ray.
- [`plane_normal()`](geometry.scad#function-plane_normal) Func – Returns the normal vector to a plane.
- [`plane_offset()`](geometry.scad#function-plane_offset) Func – Returns the signed offset of the plane from the origin.
- [`point_plane_distance()`](geometry.scad#function-point_plane_distance) Func – Determine distance between a point and plane.
- [`show_plane()`](geometry.scad#module-show_plane) Mod – Display (part of) a plane <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>

### Points

- [`altaz_to_xyz()`](coords.scad#function-altaz_to_xyz) Func – Convert altitude/azimuth/range to 3D cartesian coordinates. <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`are_points_on_plane()`](geometry.scad#function-are_points_on_plane) Func – Determine if all of the listed points are on a plane.
- [`closest_point()`](vectors.scad#function-closest_point) Func – Finds the closest point in a list of points.
- [`cylindrical_to_xyz()`](coords.scad#function-cylindrical_to_xyz) Func – Convert cylindrical coordinates to cartesian coordinates. <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`furthest_point()`](vectors.scad#function-furthest_point) Func – Finds the furthest point in a list of points.
- [`is_collinear()`](geometry.scad#function-is_collinear) Func – Determine if points are collinear.
- [`is_point_on_line()`](geometry.scad#function-is_point_on_line) Func – Determine if a point is on a line, ray or segment.
- [`lift_plane()`](coords.scad#function-lift_plane) Func – Map a list of 2D points onto a plane in 3D. <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`line_from_points()`](geometry.scad#function-line_from_points) Func – Given a list of collinear points, return the line they define.
- [`path2d()`](coords.scad#function-path2d) Func – Convert a path to 2D. <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`path3d()`](coords.scad#function-path3d) Func – Convert a path to 3D. <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`path4d()`](coords.scad#function-path4d) Func – Convert a path to 4d. <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`plane_from_points()`](geometry.scad#function-plane_from_points) Func – Return plane defined by a set of 3D points, with arbitrary normal direction.
- [`point2d()`](coords.scad#function-point2d) Func – Convert a vector to 2D.
- [`point3d()`](coords.scad#function-point3d) Func – Convert a vector to 3D.
- [`point4d()`](coords.scad#function-point4d) Func – Convert a vector to 4d.
- [`point_in_region()`](regions.scad#function-point_in_region) Func – Tests if a point is inside, outside, or on the border of a [region](Glossary#region).
- [`point_line_distance()`](geometry.scad#function-point_line_distance) Func – Find shortest distance from point to a line, segment or ray.
- [`polar_to_xy()`](coords.scad#function-polar_to_xy) Func – Convert 2D polar coordinates to cartesian coordinates. <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`project_plane()`](coords.scad#function-project_plane) Func – Project a set of points onto a specified plane, returning 2D points. <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`random_points()`](math.scad#function-random_points) Func – Returns a list of random points.
- [`spherical_random_points()`](math.scad#function-spherical_random_points) Func – Returns a list of random points on the surface of a sphere.
- [`spherical_to_xyz()`](coords.scad#function-spherical_to_xyz) Func – Convert spherical coordinates to 3D cartesian coordinates. <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`vector_nearest()`](vectors.scad#function-vector_nearest) Func – Finds the `k` nearest points in a list to a given point.
- [`vector_search()`](vectors.scad#function-vector_search) Func – Finds points in a list that are close to a given point.
- [`vector_search_tree()`](vectors.scad#function-vector_search_tree) Func – Makes a distance search tree for a list of points.
- [`xy_to_polar()`](coords.scad#function-xy_to_polar) Func – Convert 2D cartesian coordinates to polar coordinates (radius and angle)
- [`xyz_to_altaz()`](coords.scad#function-xyz_to_altaz) Func – Convert 3D cartesian coordinates to [altitude,azimuth,range].
- [`xyz_to_cylindrical()`](coords.scad#function-xyz_to_cylindrical) Func – Convert 3D cartesian coordinates to cylindrical coordinates.
- [`xyz_to_spherical()`](coords.scad#function-xyz_to_spherical) Func – Convert 3D cartesian coordinates to spherical coordinates.

### Polygon

- [`random_polygon()`](math.scad#function-random_polygon) Func – Returns the clockwise path of a simple random polygon.

### Polygons

- [`align_polygon()`](geometry.scad#function-align_polygon) Func – Find best alignment of a 2d polygon to a reference 2d polygon over a set of transformations.
- [`are_polygons_equal()`](geometry.scad#function-are_polygons_equal) Func – Check if two polygons (not necessarily in the same point order) are equal.
- [`are_regions_equal()`](regions.scad#function-are_regions_equal) Func – Returns true if given regions are the same polygons.
- [`ccw_polygon()`](geometry.scad#function-ccw_polygon) Func – Return counter-clockwise version of a polygon.
- [`centroid()`](geometry.scad#function-centroid) Func – Compute centroid of a 2d or 3d polygon or a VNF.
- [`clockwise_polygon()`](geometry.scad#function-clockwise_polygon) Func – Return clockwise version of a polygon.
- [`difference()`](regions.scad#functionmodule-difference) Func/Mod – Performs a Boolean difference operation. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Region.">[<abbr>Region</abbr>]</sup>
- [`exclusive_or()`](regions.scad#functionmodule-exclusive_or) Func/Mod – Performs a Boolean exclusive-or operation. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Region.">[<abbr>Region</abbr>]</sup>
- [`fill()`](regions.scad#function-fill) Func – Remove holes from a [region](Glossary#region) <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`force_region()`](regions.scad#function-force_region) Func – Given a polygon returns a region. <sup title="Can return a Region.">[<abbr>Region</abbr>]</sup>
- [`hull_region()`](regions.scad#functionmodule-hull_region) Func/Mod – Compute convex hull of [region](Glossary#region) or 2D [path](Glossary#path) <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`intersection()`](regions.scad#functionmodule-intersection) Func/Mod – Performs a Boolean intersection operation. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Region.">[<abbr>Region</abbr>]</sup>
- [`is_polygon_clockwise()`](geometry.scad#function-is_polygon_clockwise) Func – Determine if a 2d polygon winds clockwise.
- [`is_region()`](regions.scad#function-is_region) Func – Returns true if the input appears to be a [region](Glossary#region).
- [`is_region_simple()`](regions.scad#function-is_region_simple) Func – Returns true if the input is a region with no corner contact.
- [`is_valid_region()`](regions.scad#function-is_valid_region) Func – Returns true if the input is a valid [region](Glossary#region).
- [`make_region()`](regions.scad#function-make_region) Func – Converts lists of intersecting [polygons](Glossary#polygon) into valid [regions](Glossary#region). <sup title="Can return a Region.">[<abbr>Region</abbr>]</sup>
- [`offset()`](regions.scad#function-offset) Func – Takes a 2D [path](Glossary#path), [polygon](Glossary#polygon) or [region](Glossary#region) and returns a path offset by an amount. <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup> <sup title="Can return a Region.">[<abbr>Region</abbr>]</sup> <sup title="Extends the OpenScad keyword of the same name.">[<abbr>Ext</abbr>]</sup>
- [`plane_from_polygon()`](geometry.scad#function-plane_from_polygon) Func – Given a 3d planar polygon, returns directed plane.
- [`point_in_polygon()`](geometry.scad#function-point_in_polygon) Func – Checks if a 2d point is inside or on the boundary of a 2d polygon.
- [`polygon_area()`](geometry.scad#function-polygon_area) Func – Calculate area of a 2d or 3d polygon.
- [`polygon_line_intersection()`](geometry.scad#function-polygon_line_intersection) Func – Find intersection between 2d or 3d polygon and a line, segment or ray.
- [`polygon_normal()`](geometry.scad#function-polygon_normal) Func – Return normal to a polygon.
- [`polygon_parts()`](paths.scad#function-polygon_parts) Func – Parses a self-intersecting polygon into a list of non-intersecting [polygons](Glossary#polygon). <sup title="Can return a list of Paths.">[<abbr>PathList</abbr>]</sup>
- [`region()`](regions.scad#module-region) Mod – Creates the 2D [polygons](Glossary#polygon) described by the given [region](Glossary#region) or list of polygons. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`reindex_polygon()`](geometry.scad#function-reindex_polygon) Func – Adjust point indexing of polygon to minimize pointwise distance to a reference polygon.
- [`reverse_polygon()`](geometry.scad#function-reverse_polygon) Func – Reverse winding direction of polygon.
- [`split_region_at_region_crossings()`](regions.scad#function-split_region_at_region_crossings) Func – Splits [regions](Glossary#region) where [polygons](Glossary#polygon) touch and at intersections.
- [`union()`](regions.scad#functionmodule-union) Func/Mod – Performs a Boolean union operation. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Region.">[<abbr>Region</abbr>]</sup>

### Polyhedra

- [`debug_vnf()`](vnf.scad#module-debug_vnf) Mod – A replacement for `vnf_polyhedron()` to help with debugging. <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup>
- [`regular_polyhedron()`](polyhedra.scad#module-regular_polyhedron) Mod – Creates a regular polyhedron with optional rounding. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`regular_polyhedron_info()`](polyhedra.scad#function-regular_polyhedron_info) Func – Returns info used to create a regular polyhedron.

### Projection

- [`plane_closest_point()`](geometry.scad#function-plane_closest_point) Func – Returns the orthogonal projection of points onto a plane.

### Quantization

- [`quant()`](math.scad#function-quant) Func – Returns `x` quantized to the nearest integer multiple of `y`.
- [`quantdn()`](math.scad#function-quantdn) Func – Returns `x` quantized down to an integer multiple of `y`.
- [`quantup()`](math.scad#function-quantup) Func – Returns `x` quantized uo to an integer multiple of `y`.

### Random

- [`exponential_rands()`](math.scad#function-exponential_rands) Func – Returns a list of random numbers with an exponential distribution.
- [`gaussian_rands()`](math.scad#function-gaussian_rands) Func – Returns a list of random numbers with a gaussian distribution.
- [`rand_int()`](math.scad#function-rand_int) Func – Returns a random integer.
- [`random_points()`](math.scad#function-random_points) Func – Returns a list of random points.
- [`random_polygon()`](math.scad#function-random_polygon) Func – Returns the clockwise path of a simple random polygon.
- [`spherical_random_points()`](math.scad#function-spherical_random_points) Func – Returns a list of random points on the surface of a sphere.

### Reflection

- [`mirror()`](transforms.scad#functionmodule-mirror) Func/Mod – Reflects children across an arbitrary plane. <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return a transformation matrix.">[<abbr>Mat</abbr>]</sup> <sup title="Extends the OpenScad keyword of the same name.">[<abbr>Ext</abbr>]</sup>
- [`xflip()`](transforms.scad#functionmodule-xflip) Func/Mod – Reflects children across the YZ plane. <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return a transformation matrix.">[<abbr>Mat</abbr>]</sup>
- [`yflip()`](transforms.scad#functionmodule-yflip) Func/Mod – Reflects children across the XZ plane. <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return a transformation matrix.">[<abbr>Mat</abbr>]</sup>
- [`zflip()`](transforms.scad#functionmodule-zflip) Func/Mod – Reflects children across the XY plane. <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return a transformation matrix.">[<abbr>Mat</abbr>]</sup>

### Regions

- [`are_regions_equal()`](regions.scad#function-are_regions_equal) Func – Returns true if given regions are the same polygons.
- [`contour()`](isosurface.scad#functionmodule-contour) Func/Mod – Creates a 2D contour from a function or array of values. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup> <sup title="Can return a Region.">[<abbr>Region</abbr>]</sup>
- [`difference()`](regions.scad#functionmodule-difference) Func/Mod – Performs a Boolean difference operation. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Region.">[<abbr>Region</abbr>]</sup>
- [`exclusive_or()`](regions.scad#functionmodule-exclusive_or) Func/Mod – Performs a Boolean exclusive-or operation. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Region.">[<abbr>Region</abbr>]</sup>
- [`fill()`](regions.scad#function-fill) Func – Remove holes from a [region](Glossary#region) <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`force_path()`](paths.scad#function-force_path) Func – Checks that path is a region with one component. <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`force_region()`](regions.scad#function-force_region) Func – Given a polygon returns a region. <sup title="Can return a Region.">[<abbr>Region</abbr>]</sup>
- [`hull_region()`](regions.scad#functionmodule-hull_region) Func/Mod – Compute convex hull of [region](Glossary#region) or 2D [path](Glossary#path) <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`intersection()`](regions.scad#functionmodule-intersection) Func/Mod – Performs a Boolean intersection operation. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Region.">[<abbr>Region</abbr>]</sup>
- [`is_1region()`](paths.scad#function-is_1region) Func – Returns true if [path](Glossary#path) is a [region](Glossary#region) with one component.
- [`is_region()`](regions.scad#function-is_region) Func – Returns true if the input appears to be a [region](Glossary#region).
- [`is_region_simple()`](regions.scad#function-is_region_simple) Func – Returns true if the input is a region with no corner contact.
- [`is_valid_region()`](regions.scad#function-is_valid_region) Func – Returns true if the input is a valid [region](Glossary#region).
- [`make_region()`](regions.scad#function-make_region) Func – Converts lists of intersecting [polygons](Glossary#polygon) into valid [regions](Glossary#region). <sup title="Can return a Region.">[<abbr>Region</abbr>]</sup>
- [`metaballs2d()`](isosurface.scad#functionmodule-metaballs2d) Func/Mod – Creates a group of 2D metaballs (smoothly connected blobs). <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Region.">[<abbr>Region</abbr>]</sup>
- [`offset()`](regions.scad#function-offset) Func – Takes a 2D [path](Glossary#path), [polygon](Glossary#polygon) or [region](Glossary#region) and returns a path offset by an amount. <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup> <sup title="Can return a Region.">[<abbr>Region</abbr>]</sup> <sup title="Extends the OpenScad keyword of the same name.">[<abbr>Ext</abbr>]</sup>
- [`path_merge_collinear()`](paths.scad#function-path_merge_collinear) Func – Removes unnecessary collinear points from a path. <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`path_merge_collinear_indexed()`](paths.scad#function-path_merge_collinear_indexed) Func – Removes unnecessary collinear points from a path specified as an index list into a list <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`point_in_region()`](regions.scad#function-point_in_region) Func – Tests if a point is inside, outside, or on the border of a [region](Glossary#region).
- [`region()`](regions.scad#module-region) Mod – Creates the 2D [polygons](Glossary#polygon) described by the given [region](Glossary#region) or list of polygons. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`region_area()`](regions.scad#function-region_area) Func – Computes the area of the specified valid [region](Glossary#region).
- [`region_parts()`](regions.scad#function-region_parts) Func – Splits a [region](Glossary#region) into a list of connected regions. <sup title="Can return a list of Regions.">[<abbr>RegList</abbr>]</sup>
- [`ring()`](shapes2d.scad#functionmodule-ring) Func/Mod – Draws a 2D ring or partial ring or returns a region or path <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Region.">[<abbr>Region</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`split_region_at_region_crossings()`](regions.scad#function-split_region_at_region_crossings) Func – Splits [regions](Glossary#region) where [polygons](Glossary#polygon) touch and at intersections.
- [`union()`](regions.scad#functionmodule-union) Func/Mod – Performs a Boolean union operation. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Region.">[<abbr>Region</abbr>]</sup>

### Revolution

- [`rotate_sweep()`](skin.scad#functionmodule-rotate_sweep) Func/Mod – Create a surface of revolution from a path with optional texturing. <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>

### Rotation

- [`arc_copies()`](distributors.scad#functionmodule-arc_copies) Func/Mod – Distributes duplicates of children along an arc. <sup title="Can return a list of transformation matrices.">[<abbr>MatList</abbr>]</sup> <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup>
- [`cylindrical_extrude()`](miscellaneous.scad#module-cylindrical_extrude) Mod – Extrudes 2D children outwards around a cylinder. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`frame_map()`](transforms.scad#functionmodule-frame_map) Func/Mod – Rotates and possibly skews children from one frame of reference to another. <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return a transformation matrix.">[<abbr>Mat</abbr>]</sup>
- [`rot()`](transforms.scad#functionmodule-rot) Func/Mod – Rotates children in various ways. <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return a transformation matrix.">[<abbr>Mat</abbr>]</sup>
- [`rot_copies()`](distributors.scad#functionmodule-rot_copies) Func/Mod – Rotates copies of children. <sup title="Can return a list of transformation matrices.">[<abbr>MatList</abbr>]</sup> <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup>
- [`rot_resample()`](skin.scad#function-rot_resample) Func – Resample a list of rotation operators. <sup title="Can return a list of transformation matrices.">[<abbr>MatList</abbr>]</sup>
- [`sphere_copies()`](distributors.scad#functionmodule-sphere_copies) Func/Mod – Distributes copies of children over the surface of a sphere. <sup title="Can return a list of transformation matrices.">[<abbr>MatList</abbr>]</sup> <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup>
- [`tilt()`](transforms.scad#functionmodule-tilt) Func/Mod – Tilts children toward a direction <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return a transformation matrix.">[<abbr>Mat</abbr>]</sup>
- [`xrot()`](transforms.scad#functionmodule-xrot) Func/Mod – Rotates children around the X axis using the right-hand rule. <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return a transformation matrix.">[<abbr>Mat</abbr>]</sup>
- [`xrot_copies()`](distributors.scad#functionmodule-xrot_copies) Func/Mod – Rotates copies of children around the X axis. <sup title="Can return a list of transformation matrices.">[<abbr>MatList</abbr>]</sup> <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup>
- [`yrot()`](transforms.scad#functionmodule-yrot) Func/Mod – Rotates children around the Y axis using the right-hand rule. <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return a transformation matrix.">[<abbr>Mat</abbr>]</sup>
- [`yrot_copies()`](distributors.scad#functionmodule-yrot_copies) Func/Mod – Rotates copies of children around the Y axis. <sup title="Can return a list of transformation matrices.">[<abbr>MatList</abbr>]</sup> <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup>
- [`zrot()`](transforms.scad#functionmodule-zrot) Func/Mod – Rotates children around the Z axis using the right-hand rule. <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return a transformation matrix.">[<abbr>Mat</abbr>]</sup>
- [`zrot_copies()`](distributors.scad#functionmodule-zrot_copies) Func/Mod – Rotates copies of children around the Z axis. <sup title="Can return a list of transformation matrices.">[<abbr>MatList</abbr>]</sup> <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup>

### Rounding

- [`arc()`](drawing.scad#functionmodule-arc) Func/Mod – Draws a 2D pie-slice or returns 2D or 3D path forming an arc. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`attach_prism()`](rounding.scad#module-attach_prism) Mod – Attach a filleted prism with optional rounded end <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`bent_cutout_mask()`](rounding.scad#module-bent_cutout_mask) Mod – Create a mask for making a round-edged cutout in a cylindrical shell. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`convex_offset_extrude()`](rounding.scad#module-convex_offset_extrude) Mod – Make a solid from geometry where offset changes along the object's length. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`cyl()`](shapes3d.scad#functionmodule-cyl) Func/Mod – Creates an attachable cylinder with roundovers, chamfering or texturing. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup>
- [`hemicyl()`](shapes3d.scad#module-hemicyl) Mod – Creates a half cylinder, with optional rounding or chamfers on the flat face.
- [`join_prism()`](rounding.scad#functionmodule-join_prism) Func/Mod – Join an arbitrary prism to a plane, sphere, cylinder or another arbitrary prism with a fillet. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup>
- [`offset_stroke()`](rounding.scad#functionmodule-offset_stroke) Func/Mod – Draws a line along a path with options to specify angles and roundings at the ends. <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup> <sup title="Can return a Region.">[<abbr>Region</abbr>]</sup>
- [`offset_sweep()`](rounding.scad#functionmodule-offset_sweep) Func/Mod – Make a solid from a polygon with offset that changes along its length. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup>
- [`path_join()`](rounding.scad#function-path_join) Func – Join paths end to end with optional rounding. <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`path_to_bezpath()`](beziers.scad#function-path_to_bezpath) Func – Generates a bezier path that passes through all points in a given linear path. <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`prism_connector()`](rounding.scad#module-prism_connector) Mod – Construct a filleted prism that connects objects <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`regular_prism()`](shapes3d.scad#functionmodule-regular_prism) Func/Mod – Creates a regular prism with roundovers and chamfering <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup>
- [`round2d()`](shapes2d.scad#module-round2d) Mod – Rounds the corners of 2d objects. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`round3d()`](miscellaneous.scad#module-round3d) Mod – Rounds arbitrary 3d objects. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`round_corners()`](rounding.scad#function-round_corners) Func – Round or chamfer the corners of a path (clipping them off). <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`rounded_prism()`](rounding.scad#functionmodule-rounded_prism) Func/Mod – Make a rounded 3d object by connecting two polygons with the same vertex count. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup>
- [`rounding_corner_mask()`](masks.scad#module-rounding_corner_mask) Mod – Creates a shape to round 90° corners. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`rounding_cylinder_mask()`](masks.scad#module-rounding_cylinder_mask) Mod – Creates a shape to round the end of a cylinder. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`rounding_edge_mask()`](masks.scad#module-rounding_edge_mask) Mod – Creates a shape to round an arbitrary 3d edge. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`rounding_hole_mask()`](masks.scad#module-rounding_hole_mask) Mod – Creates a shape to round the edge of a round hole. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`semicircle()`](shapes2d.scad#functionmodule-semicircle) Func/Mod – Creates a semicircle with optional roundings or chamfers <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`smooth_path()`](rounding.scad#function-smooth_path) Func – Create a smoothed path passing through all the points of a given path, or passing through all the segment midpoint tangents. <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`teardrop_corner_mask()`](masks.scad#module-teardrop_corner_mask) Mod – Creates a shape to round a 90° corner but limit the angle of overhang. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`teardrop_edge_mask()`](masks.scad#module-teardrop_edge_mask) Mod – Creates a shape to round an edge while limiting the angle of overhang. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`xcyl()`](shapes3d.scad#functionmodule-xcyl) Func/Mod – Creates a cylinder oriented along the X axis. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup>
- [`ycyl()`](shapes3d.scad#functionmodule-ycyl) Func/Mod – Creates a cylinder oriented along the y axis. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup>
- [`zcyl()`](shapes3d.scad#module-zcyl) Mod – Creates a cylinder oriented along the y axis. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup>

### Scaling

- [`fit_to_range()`](math.scad#function-fit_to_range) Func – Scale the values in an array to span a range.
- [`pointlist_bounds()`](vectors.scad#function-pointlist_bounds) Func – Returns the min and max bounding coordinates for the given list of points.
- [`scale()`](transforms.scad#functionmodule-scale) Func/Mod – Scales children arbitrarily. <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return a transformation matrix.">[<abbr>Mat</abbr>]</sup> <sup title="Extends the OpenScad keyword of the same name.">[<abbr>Ext</abbr>]</sup>
- [`xscale()`](transforms.scad#functionmodule-xscale) Func/Mod – Scales children along the X axis. <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return a transformation matrix.">[<abbr>Mat</abbr>]</sup>
- [`yscale()`](transforms.scad#functionmodule-yscale) Func/Mod – Scales children along the Y axis. <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return a transformation matrix.">[<abbr>Mat</abbr>]</sup>
- [`zscale()`](transforms.scad#functionmodule-zscale) Func/Mod – Scales children along the Z axis. <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return a transformation matrix.">[<abbr>Mat</abbr>]</sup>

### Screws

- [`acme_threaded_nut()`](threading.scad#module-acme_threaded_nut) Mod – Creates an ACME threaded nut. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`acme_threaded_rod()`](threading.scad#module-acme_threaded_rod) Mod – Creates an ACME threaded rod. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`ball_screw_rod()`](threading.scad#module-ball_screw_rod) Mod – Creates a ball screw rod. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`bspp_threaded_rod()`](threading.scad#module-bspp_threaded_rod) Mod – Creates British Standard Parallel Pipe (BSPP) threading. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`buttress_threaded_nut()`](threading.scad#module-buttress_threaded_nut) Mod – Creates a buttress-threaded nut. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`buttress_threaded_rod()`](threading.scad#module-buttress_threaded_rod) Mod – Creates a buttress-threaded rod. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`garden_hose_threaded_rod()`](threading.scad#module-garden_hose_threaded_rod) Mod – Creates a threaded rod compatible with the North American garden hose thread. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`generic_threaded_nut()`](threading.scad#module-generic_threaded_nut) Mod – Creates a generic threaded nut. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`generic_threaded_rod()`](threading.scad#module-generic_threaded_rod) Mod – Creates a generic threaded rod. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`hex_drive_mask()`](screw_drive.scad#module-hex_drive_mask) Mod – Creates a mask for a hex drive recess. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`npt_threaded_rod()`](threading.scad#module-npt_threaded_rod) Mod – Creates NPT pipe threading. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`nut()`](screws.scad#module-nut) Mod – Creates a standard nut. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`nut_info()`](screws.scad#function-nut_info) Func – Returns the dimensions and other info for the given nut.
- [`nut_trap_inline()`](screws.scad#module-nut_trap_inline) Mod – Creates an inline nut trap mask. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`nut_trap_side()`](screws.scad#module-nut_trap_side) Mod – Creates a side nut trap mask. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`phillips_depth()`](screw_drive.scad#function-phillips_depth) Func – Returns the depth a phillips recess needs to be for a given diameter.
- [`phillips_diam()`](screw_drive.scad#function-phillips_diam) Func – Returns the diameter of a phillips recess of a given depth.
- [`phillips_mask()`](screw_drive.scad#module-phillips_mask) Mod – Creates a mask for a Philips screw drive. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`robertson_mask()`](screw_drive.scad#module-robertson_mask) Mod – Creates a mask for a Robertson/Square drive recess. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`screw()`](screws.scad#module-screw) Mod – Creates a standard screw with optional tolerances. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`screw_head()`](screws.scad#module-screw_head) Mod – Creates a screw head. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`screw_hole()`](screws.scad#module-screw_hole) Mod – Creates a screw hole. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`screw_info()`](screws.scad#function-screw_info) Func – Returns the dimensions and other info for the given screw.
- [`shoulder_screw()`](screws.scad#module-shoulder_screw) Mod – Creates a shoulder screw. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`square_threaded_nut()`](threading.scad#module-square_threaded_nut) Mod – Creates a square-threaded nut. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`square_threaded_rod()`](threading.scad#module-square_threaded_rod) Mod – Creates a square-threaded rod. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`thread_helix()`](threading.scad#module-thread_helix) Mod – Creates a thread helix to add to a cylinder. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`thread_specification()`](screws.scad#function-thread_specification) Func – Returns the thread geometry for a given screw.
- [`threaded_nut()`](threading.scad#module-threaded_nut) Mod – Creates an UTS/ISO triangular threaded nut. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`threaded_rod()`](threading.scad#module-threaded_rod) Mod – Creates an UTS/ISO triangular threaded rod. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`torx_depth()`](screw_drive.scad#function-torx_depth) Func – Returns the typical depth of a torx drive recess.
- [`torx_diam()`](screw_drive.scad#function-torx_diam) Func – Returns the diameter of a torx drive.
- [`torx_info()`](screw_drive.scad#function-torx_info) Func – Returns the dimensions of a torx drive.
- [`torx_mask()`](screw_drive.scad#module-torx_mask) Mod – Creates a mask for a torx drive recess. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`torx_mask2d()`](screw_drive.scad#module-torx_mask2d) Mod – Creates the 2D cross section for a torx drive recess. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`trapezoidal_threaded_nut()`](threading.scad#module-trapezoidal_threaded_nut) Mod – Creates a trapezoidal threaded nut. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`trapezoidal_threaded_rod()`](threading.scad#module-trapezoidal_threaded_rod) Mod – Creates a trapezoidal threaded rod. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>

### Search

- [`vector_nearest()`](vectors.scad#function-vector_nearest) Func – Finds the `k` nearest points in a list to a given point.
- [`vector_search()`](vectors.scad#function-vector_search) Func – Finds points in a list that are close to a given point.
- [`vector_search_tree()`](vectors.scad#function-vector_search_tree) Func – Makes a distance search tree for a list of points.

### Searching

- [`binsearch()`](fnliterals.scad#function-binsearch) Func – Does a binary search of a sorted list to find the index of a given value.
- [`find_first()`](fnliterals.scad#function-find_first) Func – Returns the index of the first item in a list, after `start`, that a given function returns true for.

### Segments

- [`is_point_on_line()`](geometry.scad#function-is_point_on_line) Func – Determine if a point is on a line, ray or segment.
- [`segment_distance()`](geometry.scad#function-segment_distance) Func – Find smallest distance between two line semgnets.

### Set Handling

- [`set_difference()`](lists.scad#function-set_difference) Func – Returns a list of unique items that are in list A, but not in list B.
- [`set_intersection()`](lists.scad#function-set_intersection) Func – Returns a list of unique items that are in both given lists.
- [`set_union()`](lists.scad#function-set_union) Func – Merges two lists, returning a list of unique items.

### Shapes

- [`regular_polyhedron()`](polyhedra.scad#module-regular_polyhedron) Mod – Creates a regular polyhedron with optional rounding. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`regular_polyhedron_info()`](polyhedra.scad#function-regular_polyhedron_info) Func – Returns info used to create a regular polyhedron.

### Shapes (2D)

- [`arc()`](drawing.scad#functionmodule-arc) Func/Mod – Draws a 2D pie-slice or returns 2D or 3D path forming an arc. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`circle()`](shapes2d.scad#functionmodule-circle) Func/Mod – Creates the approximation of a circle. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup> <sup title="Extends the OpenScad keyword of the same name.">[<abbr>Ext</abbr>]</sup>
- [`debug_polygon()`](drawing.scad#module-debug_polygon) Mod – Draws an annotated polygon. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`debug_region()`](regions.scad#module-debug_region) Mod – Draws an annotated [region](Glossary#region). <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`egg()`](shapes2d.scad#functionmodule-egg) Func/Mod – Creates an egg-shaped 2d object. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`ellipse()`](shapes2d.scad#functionmodule-ellipse) Func/Mod – Creates the approximation of an ellipse or a circle. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`glued_circles()`](shapes2d.scad#functionmodule-glued_circles) Func/Mod – Creates a shape of two circles joined by a curved waist. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`hexagon()`](shapes2d.scad#functionmodule-hexagon) Func/Mod – Creates a regular hexagon. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`keyhole()`](shapes2d.scad#functionmodule-keyhole) Func/Mod – Creates a 2D keyhole shape. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`mask2d_chamfer()`](masks.scad#functionmodule-mask2d_chamfer) Func/Mod – Produces a 2D chamfer mask shape. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`mask2d_cove()`](masks.scad#functionmodule-mask2d_cove) Func/Mod – Creates a 2D cove (quarter-round) mask shape. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`mask2d_dovetail()`](masks.scad#functionmodule-mask2d_dovetail) Func/Mod – Creates a 2D dovetail mask shape. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`mask2d_ogee()`](masks.scad#functionmodule-mask2d_ogee) Func/Mod – Creates a 2D ogee mask shape. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`mask2d_rabbet()`](masks.scad#functionmodule-mask2d_rabbet) Func/Mod – Creates a rabbet mask shape. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`mask2d_roundover()`](masks.scad#functionmodule-mask2d_roundover) Func/Mod – Creates a circular mask shape for rounding edges or beading. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`mask2d_smooth()`](masks.scad#functionmodule-mask2d_smooth) Func/Mod – Creates a continuous curvature mask for rounding edges. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`mask2d_teardrop()`](masks.scad#functionmodule-mask2d_teardrop) Func/Mod – Creates a 2D teardrop shape with specified max angle from vertical. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`octagon()`](shapes2d.scad#functionmodule-octagon) Func/Mod – Creates a regular octagon. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`pentagon()`](shapes2d.scad#functionmodule-pentagon) Func/Mod – Creates a regular pentagon. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`rect()`](shapes2d.scad#functionmodule-rect) Func/Mod – Creates a 2d rectangle with optional corner rounding. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`regular_ngon()`](shapes2d.scad#functionmodule-regular_ngon) Func/Mod – Creates a regular N-sided polygon. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`reuleaux_polygon()`](shapes2d.scad#functionmodule-reuleaux_polygon) Func/Mod – Creates a constant-width shape that is not circular. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`right_triangle()`](shapes2d.scad#functionmodule-right_triangle) Func/Mod – Creates a right triangle. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`ring()`](shapes2d.scad#functionmodule-ring) Func/Mod – Draws a 2D ring or partial ring or returns a region or path <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Region.">[<abbr>Region</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`semicircle()`](shapes2d.scad#functionmodule-semicircle) Func/Mod – Creates a semicircle with optional roundings or chamfers <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`square()`](shapes2d.scad#functionmodule-square) Func/Mod – Creates a 2D square or rectangle. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup> <sup title="Extends the OpenScad keyword of the same name.">[<abbr>Ext</abbr>]</sup>
- [`squircle()`](shapes2d.scad#functionmodule-squircle) Func/Mod – Creates a shape between a circle and a square. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`star()`](shapes2d.scad#functionmodule-star) Func/Mod – Creates a star-shaped polygon or returns a star-shaped region. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`supershape()`](shapes2d.scad#functionmodule-supershape) Func/Mod – Creates a 2D [Superformula](https://en.wikipedia.org/wiki/Superformula) shape. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`teardrop2d()`](shapes2d.scad#functionmodule-teardrop2d) Func/Mod – Creates a 2D teardrop shape. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`trapezoid()`](shapes2d.scad#functionmodule-trapezoid) Func/Mod – Creates a trapezoid with parallel top and bottom sides. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`turtle()`](drawing.scad#function-turtle) Func – Uses [turtle graphics](https://en.wikipedia.org/wiki/Turtle\_graphics) to generate a 2D path. <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>

### Shapes (3D)

- [`chamfer_corner_mask()`](masks.scad#module-chamfer_corner_mask) Mod – Creates a shape to chamfer a 90° corner. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`chamfer_edge_mask()`](masks.scad#module-chamfer_edge_mask) Mod – Creates a shape to chamfer a 90° edge. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`cube()`](shapes3d.scad#functionmodule-cube) Func/Mod – Creates a cube with anchors for attaching children. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Extends the OpenScad keyword of the same name.">[<abbr>Ext</abbr>]</sup>
- [`cuboid()`](shapes3d.scad#module-cuboid) Mod – Creates a cube with chamfering and roundovers. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`cylinder()`](shapes3d.scad#functionmodule-cylinder) Func/Mod – Creates an attachable cylinder. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Extends the OpenScad keyword of the same name.">[<abbr>Ext</abbr>]</sup>
- [`fillet()`](shapes3d.scad#module-fillet) Mod – Creates a smooth fillet between two faces. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup>
- [`hemicyl()`](shapes3d.scad#module-hemicyl) Mod – Creates a half cylinder, with optional rounding or chamfers on the flat face.
- [`octahedron()`](shapes3d.scad#functionmodule-octahedron) Func/Mod – Creates an octahedron with axis-aligned points. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup>
- [`onion()`](shapes3d.scad#functionmodule-onion) Func/Mod – Creates an attachable onion-like shape. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup>
- [`pie_slice()`](shapes3d.scad#functionmodule-pie_slice) Func/Mod – Creates a pie slice shape. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup>
- [`polygon_edge_mask()`](masks.scad#module-polygon_edge_mask) Mod – Extrudes a 2d mask polygon to an edge mask with a correct corner anchor <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`prismoid()`](shapes3d.scad#functionmodule-prismoid) Func/Mod – Creates a rectangular prismoid shape with optional roundovers and chamfering. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup>
- [`rect_tube()`](shapes3d.scad#module-rect_tube) Mod – Creates a rectangular tube. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`regular_prism()`](shapes3d.scad#functionmodule-regular_prism) Func/Mod – Creates a regular prism with roundovers and chamfering <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup>
- [`rounding_corner_mask()`](masks.scad#module-rounding_corner_mask) Mod – Creates a shape to round 90° corners. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`rounding_edge_mask()`](masks.scad#module-rounding_edge_mask) Mod – Creates a shape to round an arbitrary 3d edge. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`sphere()`](shapes3d.scad#functionmodule-sphere) Func/Mod – Creates an attachable spherical object. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Extends the OpenScad keyword of the same name.">[<abbr>Ext</abbr>]</sup>
- [`spheroid()`](shapes3d.scad#functionmodule-spheroid) Func/Mod – Creates an attachable spherical object with controllable triangulation. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup>
- [`teardrop()`](shapes3d.scad#functionmodule-teardrop) Func/Mod – Creates a teardrop shape. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup>
- [`teardrop_corner_mask()`](masks.scad#module-teardrop_corner_mask) Mod – Creates a shape to round a 90° corner but limit the angle of overhang. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`teardrop_edge_mask()`](masks.scad#module-teardrop_edge_mask) Mod – Creates a shape to round an edge while limiting the angle of overhang. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`textured_tile()`](shapes3d.scad#functionmodule-textured_tile) Func/Mod – Creates a cube or trapezoidal prism with a textured top face for attaching to objects. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup>
- [`torus()`](shapes3d.scad#functionmodule-torus) Func/Mod – Creates an attachable torus. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup>
- [`tube()`](shapes3d.scad#module-tube) Mod – Creates a cylindrical or conical tube. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`turtle3d()`](turtle3d.scad#function-turtle3d) Func – Extends [turtle graphics](https://en.wikipedia.org/wiki/Turtle\_graphics) to 3d. Generates a 3D path or returns a list of transforms. <sup title="Can return a list of transformation matrices.">[<abbr>MatList</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`wedge()`](shapes3d.scad#functionmodule-wedge) Func/Mod – Creates a 3d triangular wedge. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup>

### Shapes2D

- [`difference()`](regions.scad#functionmodule-difference) Func/Mod – Performs a Boolean difference operation. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Region.">[<abbr>Region</abbr>]</sup>
- [`exclusive_or()`](regions.scad#functionmodule-exclusive_or) Func/Mod – Performs a Boolean exclusive-or operation. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Region.">[<abbr>Region</abbr>]</sup>
- [`fill()`](regions.scad#function-fill) Func – Remove holes from a [region](Glossary#region) <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`hull_region()`](regions.scad#functionmodule-hull_region) Func/Mod – Compute convex hull of [region](Glossary#region) or 2D [path](Glossary#path) <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup>
- [`intersection()`](regions.scad#functionmodule-intersection) Func/Mod – Performs a Boolean intersection operation. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Region.">[<abbr>Region</abbr>]</sup>
- [`union()`](regions.scad#functionmodule-union) Func/Mod – Performs a Boolean union operation. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Region.">[<abbr>Region</abbr>]</sup>

### Shapes3D

- [`difference()`](regions.scad#functionmodule-difference) Func/Mod – Performs a Boolean difference operation. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Region.">[<abbr>Region</abbr>]</sup>
- [`exclusive_or()`](regions.scad#functionmodule-exclusive_or) Func/Mod – Performs a Boolean exclusive-or operation. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Region.">[<abbr>Region</abbr>]</sup>
- [`intersection()`](regions.scad#functionmodule-intersection) Func/Mod – Performs a Boolean intersection operation. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Region.">[<abbr>Region</abbr>]</sup>
- [`union()`](regions.scad#functionmodule-union) Func/Mod – Performs a Boolean union operation. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a Region.">[<abbr>Region</abbr>]</sup>

### Shearing

- [`skew()`](transforms.scad#functionmodule-skew) Func/Mod – Skews (or shears) children along various axes. <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return a transformation matrix.">[<abbr>Mat</abbr>]</sup>

### Shell

- [`shell2d()`](shapes2d.scad#module-shell2d) Mod – Creates a shell from 2D children. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>

### Skewing

- [`skew()`](transforms.scad#functionmodule-skew) Func/Mod – Skews (or shears) children along various axes. <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return a transformation matrix.">[<abbr>Mat</abbr>]</sup>

### Skin

- [`skin()`](skin.scad#functionmodule-skin) Func/Mod – Connect a sequence of arbitrary polygons into a 3D object. <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>

### Skinning

- [`associate_vertices()`](skin.scad#function-associate_vertices) Func – Create vertex association to control how [`skin()`](#functionmodule-skin) links vertices. <sup title="Can return a list of Paths.">[<abbr>PathList</abbr>]</sup>

### Sliders

- [`rail()`](sliders.scad#module-rail) Mod – Creates a V-groove rail. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`slider()`](sliders.scad#module-slider) Mod – Creates a V-groove slider. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>

### Slop

- [`get_slop()`](constants.scad#function-get_slop) Func – Returns the $slop value.

### Spheres

- [`sphere_line_intersection()`](geometry.scad#function-sphere_line_intersection) Func – Find intersection between a sphere and line, ray or segment.

### Spiral

- [`spiral_sweep()`](skin.scad#functionmodule-spiral_sweep) Func/Mod – Sweep a path along a helix. <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>

### Statistics

- [`convolve()`](math.scad#function-convolve) Func – Returns the convolution of `p` and `q`.
- [`cumprod()`](math.scad#function-cumprod) Func – Returns the running cumulative product of a list of values.
- [`cumsum()`](math.scad#function-cumsum) Func – Returns the running cumulative sum of a list of values.
- [`deltas()`](math.scad#function-deltas) Func – Returns the deltas between a list of values.
- [`exponential_rands()`](math.scad#function-exponential_rands) Func – Returns a list of random numbers with an exponential distribution.
- [`gaussian_rands()`](math.scad#function-gaussian_rands) Func – Returns a list of random numbers with a gaussian distribution.
- [`mean()`](math.scad#function-mean) Func – Returns the mean value of a list of values.
- [`median()`](math.scad#function-median) Func – Returns the median value of a list of values.
- [`product()`](math.scad#function-product) Func – Returns the multiplicative product of a list of values.
- [`sum_of_sines()`](math.scad#function-sum_of_sines) Func – Returns the sum of one or more sine waves at a given angle.

### String Operators

- [`f_chr()`](fnliterals.scad#function-f_chr) Func – Returns a function to get a string character from its ordinal number.
- [`f_len()`](fnliterals.scad#function-f_len) Func – Returns a function to calculate the length of a string or list.
- [`f_ord()`](fnliterals.scad#function-f_ord) Func – Returns a function to get the ordinal number of a string character.
- [`f_str()`](fnliterals.scad#function-f_str) Func – Returns a function to get the string representation of an arbitrary value.
- [`f_str2()`](fnliterals.scad#function-f_str2) Func – Returns a function to concatenate the string representations of two arbitrary values.

### Strings

- [`downcase()`](strings.scad#function-downcase) Func – Lowercases all characters in a string.
- [`ends_with()`](strings.scad#function-ends_with) Func – Returns true if the string ends with a given substring.
- [`format()`](strings.scad#function-format) Func – Formats multiple values into a string with a given format.
- [`format_fixed()`](strings.scad#function-format_fixed) Func – Formats a float into a string with a fixed number of decimal places.
- [`format_float()`](strings.scad#function-format_float) Func – Formats a float into a string with a given number of significant digits.
- [`format_int()`](strings.scad#function-format_int) Func – Formats an integer into a string, with possible leading zeros.
- [`is_digit()`](strings.scad#function-is_digit) Func – Returns true if all characters in the string are decimal digits.
- [`is_hexdigit()`](strings.scad#function-is_hexdigit) Func – Returns true if all characters in the string are hexidecimal digits.
- [`is_letter()`](strings.scad#function-is_letter) Func – Returns true if all characters in the string are letters.
- [`is_lower()`](strings.scad#function-is_lower) Func – Returns true if all characters in the string are lowercase.
- [`is_upper()`](strings.scad#function-is_upper) Func – Returns true if all characters in the string are uppercase.
- [`parse_float()`](strings.scad#function-parse_float) Func – Parse a float from a string.
- [`parse_frac()`](strings.scad#function-parse_frac) Func – Parse a float from a fraction string.
- [`parse_int()`](strings.scad#function-parse_int) Func – Parse an integer from a string.
- [`parse_num()`](strings.scad#function-parse_num) Func – Parse a float from a decimal or fraction string.
- [`rand_str()`](strings.scad#function-rand_str) Func – Create a randomized string.
- [`starts_with()`](strings.scad#function-starts_with) Func – Returns true if the string starts with a given substring.
- [`str_collapse_char()`](strings.scad#function-str_collapse_char) Func – Collapse a specific repeating character in a string.
- [`str_find()`](strings.scad#function-str_find) Func – Finds a substring in a string.
- [`str_join()`](strings.scad#function-str_join) Func – Joints a list of strings into a single string.
- [`str_pad()`](strings.scad#function-str_pad) Func – Pads a string to a given length.
- [`str_replace()`](strings.scad#function-str_replace) Func – Replace all occurrences of the specified substring in a string with another string.
- [`str_replace_char()`](strings.scad#function-str_replace_char) Func – Replace specified character in a string with a string.
- [`str_split()`](strings.scad#function-str_split) Func – Splits a longer string wherever a given substring occurs.
- [`str_strip()`](strings.scad#function-str_strip) Func – Strips given leading and trailing characters from a string.
- [`substr()`](strings.scad#function-substr) Func – Returns a substring from a string.
- [`substr_match()`](strings.scad#function-substr_match) Func – Returns true if the string `pattern` matches the string `str`.
- [`suffix()`](strings.scad#function-suffix) Func – Returns the last few characters of a string.
- [`upcase()`](strings.scad#function-upcase) Func – Uppercases all characters in a string.

### Sweep

- [`attach_prism()`](rounding.scad#module-attach_prism) Mod – Attach a filleted prism with optional rounded end <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`bezier_sweep()`](beziers.scad#functionmodule-bezier_sweep) Func/Mod – Sweep a 2d polygon path along a bezier with exact tangents <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`bezpath_sweep()`](beziers.scad#functionmodule-bezpath_sweep) Func/Mod – Sweep a 2d polygon path along a bezier path with exact tangents <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`linear_sweep()`](skin.scad#functionmodule-linear_sweep) Func/Mod – Create a linear extrusion from a path, with optional texturing. <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`path_sweep()`](skin.scad#functionmodule-path_sweep) Func/Mod – Sweep a 2d polygon path along a 2d or 3d path. <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`path_sweep2d()`](skin.scad#functionmodule-path_sweep2d) Func/Mod – Sweep a 2d polygon path along a 2d path allowing self-intersection. <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`prism_connector()`](rounding.scad#module-prism_connector) Mod – Construct a filleted prism that connects objects <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`rotate_sweep()`](skin.scad#functionmodule-rotate_sweep) Func/Mod – Create a surface of revolution from a path with optional texturing. <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`spiral_sweep()`](skin.scad#functionmodule-spiral_sweep) Func/Mod – Sweep a path along a helix. <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`sweep()`](skin.scad#functionmodule-sweep) Func/Mod – Construct a 3d object from arbitrary transformations of a 2d polygon path. <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`sweep_attach()`](skin.scad#module-sweep_attach) Mod – Attach children to sides of a path\_sweep parent object <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>

### Tangents

- [`circle_2tangents()`](geometry.scad#function-circle_2tangents) Func – Given two 2d or 3d rays, find a circle tangent to both.
- [`circle_circle_tangents()`](geometry.scad#function-circle_circle_tangents) Func – Find tangents to a pair of circles in 2d.
- [`circle_point_tangents()`](geometry.scad#function-circle_point_tangents) Func – Given a circle and point, find tangents to circle passing through the point.

### Test

- [`is_polygon_convex()`](geometry.scad#function-is_polygon_convex) Func – Check if a polygon is convex.

### Testing

- [`is_consistent()`](utility.scad#function-is_consistent) Func – Returns true if the argument is a list with consistent structure and finite numerical data.
- [`same_shape()`](utility.scad#function-same_shape) Func – Returns true if the argument lists are numeric and of the same shape.
- [`shape_compare()`](utility.scad#module-shape_compare) Mod – Compares two child shapes. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>

### Text

- [`path_text()`](shapes3d.scad#module-path_text) Mod – Creates 2d or 3d text placed along a path. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`text()`](shapes2d.scad#module-text) Mod – Creates an attachable block of text. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`text3d()`](shapes3d.scad#module-text3d) Mod – Creates an attachable 3d text block. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>

### Textures

- [`bezier_sweep()`](beziers.scad#functionmodule-bezier_sweep) Func/Mod – Sweep a 2d polygon path along a bezier with exact tangents <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`bezpath_sweep()`](beziers.scad#functionmodule-bezpath_sweep) Func/Mod – Sweep a 2d polygon path along a bezier path with exact tangents <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`cube()`](shapes3d.scad#functionmodule-cube) Func/Mod – Creates a cube with anchors for attaching children. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Extends the OpenScad keyword of the same name.">[<abbr>Ext</abbr>]</sup>
- [`cyl()`](shapes3d.scad#functionmodule-cyl) Func/Mod – Creates an attachable cylinder with roundovers, chamfering or texturing. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup>
- [`linear_sweep()`](skin.scad#functionmodule-linear_sweep) Func/Mod – Create a linear extrusion from a path, with optional texturing. <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`path_sweep()`](skin.scad#functionmodule-path_sweep) Func/Mod – Sweep a 2d polygon path along a 2d or 3d path. <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`regular_prism()`](shapes3d.scad#functionmodule-regular_prism) Func/Mod – Creates a regular prism with roundovers and chamfering <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup>
- [`rotate_sweep()`](skin.scad#functionmodule-rotate_sweep) Func/Mod – Create a surface of revolution from a path with optional texturing. <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`sweep()`](skin.scad#functionmodule-sweep) Func/Mod – Construct a 3d object from arbitrary transformations of a 2d polygon path. <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`texture()`](skin.scad#function-texture) Func – Produce a standard texture.
- [`textured_tile()`](shapes3d.scad#functionmodule-textured_tile) Func/Mod – Creates a cube or trapezoidal prism with a textured top face for attaching to objects. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup>
- [`vnf_vertex_array()`](vnf.scad#functionmodule-vnf_vertex_array) Func/Mod – Returns a VNF structure from a rectangular vertex list. <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`xcyl()`](shapes3d.scad#functionmodule-xcyl) Func/Mod – Creates a cylinder oriented along the X axis. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup>
- [`ycyl()`](shapes3d.scad#functionmodule-ycyl) Func/Mod – Creates a cylinder oriented along the y axis. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup>
- [`zcyl()`](shapes3d.scad#module-zcyl) Mod – Creates a cylinder oriented along the y axis. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup>

### Threading

- [`acme_threaded_nut()`](threading.scad#module-acme_threaded_nut) Mod – Creates an ACME threaded nut. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`acme_threaded_rod()`](threading.scad#module-acme_threaded_rod) Mod – Creates an ACME threaded rod. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`ball_screw_rod()`](threading.scad#module-ball_screw_rod) Mod – Creates a ball screw rod. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`bottle_adapter_cap_to_cap()`](bottlecaps.scad#module-bottle_adapter_cap_to_cap) Mod – Creates a generic adaptor between a cap and a cap. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`bottle_adapter_neck_to_cap()`](bottlecaps.scad#module-bottle_adapter_neck_to_cap) Mod – Creates a generic adapter between a neck and a cap. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`bottle_adapter_neck_to_neck()`](bottlecaps.scad#module-bottle_adapter_neck_to_neck) Mod – Creates a generic adaptor between a neck and a neck. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`bspp_threaded_rod()`](threading.scad#module-bspp_threaded_rod) Mod – Creates British Standard Parallel Pipe (BSPP) threading. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`buttress_threaded_nut()`](threading.scad#module-buttress_threaded_nut) Mod – Creates a buttress-threaded nut. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`buttress_threaded_rod()`](threading.scad#module-buttress_threaded_rod) Mod – Creates a buttress-threaded rod. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`garden_hose_female()`](threading.scad#module-garden_hose_female) Mod – Creates a female garden hose coupler with textured surface <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`garden_hose_gasket()`](threading.scad#module-garden_hose_gasket) Mod – Creates a North American garden hose washer or gasket <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`garden_hose_male()`](threading.scad#module-garden_hose_male) Mod – Creates a male garden hose coupler <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`garden_hose_threaded_rod()`](threading.scad#module-garden_hose_threaded_rod) Mod – Creates a threaded rod compatible with the North American garden hose thread. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`generic_bottle_cap()`](bottlecaps.scad#module-generic_bottle_cap) Mod – Creates a generic cap for a bottle. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`generic_bottle_neck()`](bottlecaps.scad#module-generic_bottle_neck) Mod – Creates a generic neck for a bottle. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`generic_threaded_nut()`](threading.scad#module-generic_threaded_nut) Mod – Creates a generic threaded nut. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`generic_threaded_rod()`](threading.scad#module-generic_threaded_rod) Mod – Creates a generic threaded rod. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`mason_cap()`](bottlecaps.scad#module-mason_cap) Mod – Creates a threaded mason jar cap. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`mason_neck()`](bottlecaps.scad#module-mason_neck) Mod – Creates a threaded glass mason jar neck. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`npt_threaded_rod()`](threading.scad#module-npt_threaded_rod) Mod – Creates NPT pipe threading. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`nut()`](screws.scad#module-nut) Mod – Creates a standard nut. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`nut_info()`](screws.scad#function-nut_info) Func – Returns the dimensions and other info for the given nut.
- [`nut_trap_inline()`](screws.scad#module-nut_trap_inline) Mod – Creates an inline nut trap mask. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`nut_trap_side()`](screws.scad#module-nut_trap_side) Mod – Creates a side nut trap mask. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`pco1810_cap()`](bottlecaps.scad#module-pco1810_cap) Mod – Creates a cap for a PCO1810 standard bottle. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`pco1810_neck()`](bottlecaps.scad#module-pco1810_neck) Mod – Creates a neck for a PCO1810 standard bottle. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`pco1881_cap()`](bottlecaps.scad#module-pco1881_cap) Mod – Creates a cap for a PCO1881 standard bottle. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`pco1881_neck()`](bottlecaps.scad#module-pco1881_neck) Mod – Creates a neck for a PCO1881 standard bottle. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`screw()`](screws.scad#module-screw) Mod – Creates a standard screw with optional tolerances. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`screw_head()`](screws.scad#module-screw_head) Mod – Creates a screw head. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`screw_hole()`](screws.scad#module-screw_hole) Mod – Creates a screw hole. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`screw_info()`](screws.scad#function-screw_info) Func – Returns the dimensions and other info for the given screw.
- [`shoulder_screw()`](screws.scad#module-shoulder_screw) Mod – Creates a shoulder screw. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`sp_cap()`](bottlecaps.scad#module-sp_cap) Mod – Creates an SPI threaded bottle cap. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`sp_diameter()`](bottlecaps.scad#function-sp_diameter) Func – Returns the base diameter of an SPI bottle neck from the nominal diameter and type number.
- [`sp_neck()`](bottlecaps.scad#module-sp_neck) Mod – Creates an SPI threaded bottle neck. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`square_threaded_nut()`](threading.scad#module-square_threaded_nut) Mod – Creates a square-threaded nut. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`square_threaded_rod()`](threading.scad#module-square_threaded_rod) Mod – Creates a square-threaded rod. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`thread_helix()`](threading.scad#module-thread_helix) Mod – Creates a thread helix to add to a cylinder. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`thread_specification()`](screws.scad#function-thread_specification) Func – Returns the thread geometry for a given screw.
- [`threaded_nut()`](threading.scad#module-threaded_nut) Mod – Creates an UTS/ISO triangular threaded nut. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`threaded_rod()`](threading.scad#module-threaded_rod) Mod – Creates an UTS/ISO triangular threaded rod. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`trapezoidal_threaded_nut()`](threading.scad#module-trapezoidal_threaded_nut) Mod – Creates a trapezoidal threaded nut. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`trapezoidal_threaded_rod()`](threading.scad#module-trapezoidal_threaded_rod) Mod – Creates a trapezoidal threaded rod. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>

### Transformations

- [`arc_copies()`](distributors.scad#functionmodule-arc_copies) Func/Mod – Distributes duplicates of children along an arc. <sup title="Can return a list of transformation matrices.">[<abbr>MatList</abbr>]</sup> <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup>
- [`desc_copies()`](attachments.scad#module-desc_copies) Mod – Places copies according to a list of transformation matrices and supplies descriptions for the copies. <sup title="Can return a list of transformation matrices.">[<abbr>MatList</abbr>]</sup> <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup>
- [`grid_copies()`](distributors.scad#functionmodule-grid_copies) Func/Mod – Places copies of children in an [X,Y] grid. <sup title="Can return a list of transformation matrices.">[<abbr>MatList</abbr>]</sup> <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup>
- [`line_copies()`](distributors.scad#functionmodule-line_copies) Func/Mod – Places copies of children along an arbitrary line. <sup title="Can return a list of transformation matrices.">[<abbr>MatList</abbr>]</sup> <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup>
- [`mirror_copy()`](distributors.scad#functionmodule-mirror_copy) Func/Mod – Makes a copy of children mirrored across a given plane. <sup title="Can return a list of transformation matrices.">[<abbr>MatList</abbr>]</sup> <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup>
- [`move_copies()`](distributors.scad#functionmodule-move_copies) Func/Mod – Translates copies of all children. <sup title="Can return a list of transformation matrices.">[<abbr>MatList</abbr>]</sup> <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup>
- [`path_copies()`](distributors.scad#functionmodule-path_copies) Func/Mod – Uniformly distributes copies of children along a path. <sup title="Can return a list of transformation matrices.">[<abbr>MatList</abbr>]</sup> <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup>
- [`rot_copies()`](distributors.scad#functionmodule-rot_copies) Func/Mod – Rotates copies of children. <sup title="Can return a list of transformation matrices.">[<abbr>MatList</abbr>]</sup> <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup>
- [`sphere_copies()`](distributors.scad#functionmodule-sphere_copies) Func/Mod – Distributes copies of children over the surface of a sphere. <sup title="Can return a list of transformation matrices.">[<abbr>MatList</abbr>]</sup> <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup>
- [`xcopies()`](distributors.scad#functionmodule-xcopies) Func/Mod – Places copies of children along the X axis. <sup title="Can return a list of transformation matrices.">[<abbr>MatList</abbr>]</sup> <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup>
- [`xflip_copy()`](distributors.scad#functionmodule-xflip_copy) Func/Mod – Makes a copy of children mirrored across the X axis. <sup title="Can return a list of transformation matrices.">[<abbr>MatList</abbr>]</sup> <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup>
- [`xrot_copies()`](distributors.scad#functionmodule-xrot_copies) Func/Mod – Rotates copies of children around the X axis. <sup title="Can return a list of transformation matrices.">[<abbr>MatList</abbr>]</sup> <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup>
- [`ycopies()`](distributors.scad#functionmodule-ycopies) Func/Mod – Places copies of children along the Y axis. <sup title="Can return a list of transformation matrices.">[<abbr>MatList</abbr>]</sup> <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup>
- [`yflip_copy()`](distributors.scad#functionmodule-yflip_copy) Func/Mod – Makes a copy of children mirrored across the Y axis. <sup title="Can return a list of transformation matrices.">[<abbr>MatList</abbr>]</sup> <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup>
- [`yrot_copies()`](distributors.scad#functionmodule-yrot_copies) Func/Mod – Rotates copies of children around the Y axis. <sup title="Can return a list of transformation matrices.">[<abbr>MatList</abbr>]</sup> <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup>
- [`zcopies()`](distributors.scad#functionmodule-zcopies) Func/Mod – Places copies of children along the Z axis. <sup title="Can return a list of transformation matrices.">[<abbr>MatList</abbr>]</sup> <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup>
- [`zflip_copy()`](distributors.scad#functionmodule-zflip_copy) Func/Mod – Makes a copy of children mirrored across the Z axis. <sup title="Can return a list of transformation matrices.">[<abbr>MatList</abbr>]</sup> <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup>
- [`zrot_copies()`](distributors.scad#functionmodule-zrot_copies) Func/Mod – Rotates copies of children around the Z axis. <sup title="Can return a list of transformation matrices.">[<abbr>MatList</abbr>]</sup> <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup>

### Transforms

- [`apply()`](transforms.scad#function-apply) Func – Applies a transformation matrix to a point, list of points, array of points, or a VNF. <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return a transformation matrix.">[<abbr>Mat</abbr>]</sup>
- [`back()`](transforms.scad#functionmodule-back) Func/Mod – Translates children backward (Y+). <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return a transformation matrix.">[<abbr>Mat</abbr>]</sup>
- [`down()`](transforms.scad#functionmodule-down) Func/Mod – Translates children downward (Z-). <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return a transformation matrix.">[<abbr>Mat</abbr>]</sup>
- [`frame_map()`](transforms.scad#functionmodule-frame_map) Func/Mod – Rotates and possibly skews children from one frame of reference to another. <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return a transformation matrix.">[<abbr>Mat</abbr>]</sup>
- [`fwd()`](transforms.scad#functionmodule-fwd) Func/Mod – Translates children forward (Y-). <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return a transformation matrix.">[<abbr>Mat</abbr>]</sup>
- [`IDENT`](constants.scad#constant-ident) Const – A constant, the 3D identity transformation matrix. <sup title="Can return a transformation matrix.">[<abbr>Mat</abbr>]</sup>
- [`ident()`](linalg.scad#function-ident) Func – Return identity matrix.
- [`is_rotation()`](linalg.scad#function-is_rotation) Func – Check if a transformation matrix represents a rotation.
- [`left()`](transforms.scad#functionmodule-left) Func/Mod – Translates children leftward (X-). <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return a transformation matrix.">[<abbr>Mat</abbr>]</sup>
- [`mirror()`](transforms.scad#functionmodule-mirror) Func/Mod – Reflects children across an arbitrary plane. <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return a transformation matrix.">[<abbr>Mat</abbr>]</sup> <sup title="Extends the OpenScad keyword of the same name.">[<abbr>Ext</abbr>]</sup>
- [`move()`](transforms.scad#functionmodule-move) Func/Mod – Translates children in an arbitrary direction. <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return a transformation matrix.">[<abbr>Mat</abbr>]</sup>
- [`parent()`](attachments.scad#function-parent) Func – Returns a description (transformation state and attachment geometry) of the parent
- [`parent_part()`](attachments.scad#function-parent_part) Func – Returns a description (transformation state and attachment geometry) of a part defined by the parent
- [`restore()`](attachments.scad#module-restore) Mod – Restores transformation state and attachment geometry from a description
- [`right()`](transforms.scad#functionmodule-right) Func/Mod – Translates children rightward (X+). <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return a transformation matrix.">[<abbr>Mat</abbr>]</sup>
- [`rot()`](transforms.scad#functionmodule-rot) Func/Mod – Rotates children in various ways. <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return a transformation matrix.">[<abbr>Mat</abbr>]</sup>
- [`rot_decode()`](geometry.scad#function-rot_decode) Func – Extract axis and rotation angle from a rotation matrix.
- [`scale()`](transforms.scad#functionmodule-scale) Func/Mod – Scales children arbitrarily. <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return a transformation matrix.">[<abbr>Mat</abbr>]</sup> <sup title="Extends the OpenScad keyword of the same name.">[<abbr>Ext</abbr>]</sup>
- [`skew()`](transforms.scad#functionmodule-skew) Func/Mod – Skews (or shears) children along various axes. <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return a transformation matrix.">[<abbr>Mat</abbr>]</sup>
- [`tilt()`](transforms.scad#functionmodule-tilt) Func/Mod – Tilts children toward a direction <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return a transformation matrix.">[<abbr>Mat</abbr>]</sup>
- [`move()`](transforms.scad#functionmodule-move) Func/Mod – Translates children in an arbitrary direction. <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return a transformation matrix.">[<abbr>Mat</abbr>]</sup>
- [`up()`](transforms.scad#functionmodule-up) Func/Mod – Translates children upward (Z+). <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return a transformation matrix.">[<abbr>Mat</abbr>]</sup>
- [`xflip()`](transforms.scad#functionmodule-xflip) Func/Mod – Reflects children across the YZ plane. <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return a transformation matrix.">[<abbr>Mat</abbr>]</sup>
- [`right()`](transforms.scad#functionmodule-right) Func/Mod – Translates children rightward (X+). <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return a transformation matrix.">[<abbr>Mat</abbr>]</sup>
- [`xrot()`](transforms.scad#functionmodule-xrot) Func/Mod – Rotates children around the X axis using the right-hand rule. <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return a transformation matrix.">[<abbr>Mat</abbr>]</sup>
- [`xscale()`](transforms.scad#functionmodule-xscale) Func/Mod – Scales children along the X axis. <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return a transformation matrix.">[<abbr>Mat</abbr>]</sup>
- [`yflip()`](transforms.scad#functionmodule-yflip) Func/Mod – Reflects children across the XZ plane. <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return a transformation matrix.">[<abbr>Mat</abbr>]</sup>
- [`back()`](transforms.scad#functionmodule-back) Func/Mod – Translates children backward (Y+). <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return a transformation matrix.">[<abbr>Mat</abbr>]</sup>
- [`yrot()`](transforms.scad#functionmodule-yrot) Func/Mod – Rotates children around the Y axis using the right-hand rule. <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return a transformation matrix.">[<abbr>Mat</abbr>]</sup>
- [`yscale()`](transforms.scad#functionmodule-yscale) Func/Mod – Scales children along the Y axis. <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return a transformation matrix.">[<abbr>Mat</abbr>]</sup>
- [`zflip()`](transforms.scad#functionmodule-zflip) Func/Mod – Reflects children across the XY plane. <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return a transformation matrix.">[<abbr>Mat</abbr>]</sup>
- [`up()`](transforms.scad#functionmodule-up) Func/Mod – Translates children upward (Z+). <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return a transformation matrix.">[<abbr>Mat</abbr>]</sup>
- [`zrot()`](transforms.scad#functionmodule-zrot) Func/Mod – Rotates children around the Z axis using the right-hand rule. <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return a transformation matrix.">[<abbr>Mat</abbr>]</sup>
- [`zscale()`](transforms.scad#functionmodule-zscale) Func/Mod – Scales children along the Z axis. <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return a transformation matrix.">[<abbr>Mat</abbr>]</sup>

### Translation

- [`back()`](transforms.scad#functionmodule-back) Func/Mod – Translates children backward (Y+). <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return a transformation matrix.">[<abbr>Mat</abbr>]</sup>
- [`down()`](transforms.scad#functionmodule-down) Func/Mod – Translates children downward (Z-). <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return a transformation matrix.">[<abbr>Mat</abbr>]</sup>
- [`fwd()`](transforms.scad#functionmodule-fwd) Func/Mod – Translates children forward (Y-). <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return a transformation matrix.">[<abbr>Mat</abbr>]</sup>
- [`grid_copies()`](distributors.scad#functionmodule-grid_copies) Func/Mod – Places copies of children in an [X,Y] grid. <sup title="Can return a list of transformation matrices.">[<abbr>MatList</abbr>]</sup> <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup>
- [`left()`](transforms.scad#functionmodule-left) Func/Mod – Translates children leftward (X-). <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return a transformation matrix.">[<abbr>Mat</abbr>]</sup>
- [`line_copies()`](distributors.scad#functionmodule-line_copies) Func/Mod – Places copies of children along an arbitrary line. <sup title="Can return a list of transformation matrices.">[<abbr>MatList</abbr>]</sup> <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup>
- [`mirror_copy()`](distributors.scad#functionmodule-mirror_copy) Func/Mod – Makes a copy of children mirrored across a given plane. <sup title="Can return a list of transformation matrices.">[<abbr>MatList</abbr>]</sup> <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup>
- [`move()`](transforms.scad#functionmodule-move) Func/Mod – Translates children in an arbitrary direction. <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return a transformation matrix.">[<abbr>Mat</abbr>]</sup>
- [`move_copies()`](distributors.scad#functionmodule-move_copies) Func/Mod – Translates copies of all children. <sup title="Can return a list of transformation matrices.">[<abbr>MatList</abbr>]</sup> <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup>
- [`right()`](transforms.scad#functionmodule-right) Func/Mod – Translates children rightward (X+). <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return a transformation matrix.">[<abbr>Mat</abbr>]</sup>
- [`move()`](transforms.scad#functionmodule-move) Func/Mod – Translates children in an arbitrary direction. <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return a transformation matrix.">[<abbr>Mat</abbr>]</sup>
- [`up()`](transforms.scad#functionmodule-up) Func/Mod – Translates children upward (Z+). <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return a transformation matrix.">[<abbr>Mat</abbr>]</sup>
- [`xcopies()`](distributors.scad#functionmodule-xcopies) Func/Mod – Places copies of children along the X axis. <sup title="Can return a list of transformation matrices.">[<abbr>MatList</abbr>]</sup> <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup>
- [`xflip_copy()`](distributors.scad#functionmodule-xflip_copy) Func/Mod – Makes a copy of children mirrored across the X axis. <sup title="Can return a list of transformation matrices.">[<abbr>MatList</abbr>]</sup> <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup>
- [`right()`](transforms.scad#functionmodule-right) Func/Mod – Translates children rightward (X+). <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return a transformation matrix.">[<abbr>Mat</abbr>]</sup>
- [`ycopies()`](distributors.scad#functionmodule-ycopies) Func/Mod – Places copies of children along the Y axis. <sup title="Can return a list of transformation matrices.">[<abbr>MatList</abbr>]</sup> <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup>
- [`yflip_copy()`](distributors.scad#functionmodule-yflip_copy) Func/Mod – Makes a copy of children mirrored across the Y axis. <sup title="Can return a list of transformation matrices.">[<abbr>MatList</abbr>]</sup> <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup>
- [`back()`](transforms.scad#functionmodule-back) Func/Mod – Translates children backward (Y+). <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return a transformation matrix.">[<abbr>Mat</abbr>]</sup>
- [`zcopies()`](distributors.scad#functionmodule-zcopies) Func/Mod – Places copies of children along the Z axis. <sup title="Can return a list of transformation matrices.">[<abbr>MatList</abbr>]</sup> <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup>
- [`zflip_copy()`](distributors.scad#functionmodule-zflip_copy) Func/Mod – Makes a copy of children mirrored across the Z axis. <sup title="Can return a list of transformation matrices.">[<abbr>MatList</abbr>]</sup> <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup>
- [`up()`](transforms.scad#functionmodule-up) Func/Mod – Translates children upward (Z+). <sup title="Can transform children.">[<abbr>Trans</abbr>]</sup> <sup title="Can return a Path.">[<abbr>Path</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return a transformation matrix.">[<abbr>Mat</abbr>]</sup>

### Triangles

- [`adj_ang_to_hyp()`](trigonometry.scad#function-adj_ang_to_hyp) Func – Returns the hypotenuse length from the length of the adjacent side and the reference reference angle.
- [`adj_ang_to_opp()`](trigonometry.scad#function-adj_ang_to_opp) Func – Returns the opposite side length from the length of the adjacent side and the reference reference angle.
- [`adj_hyp_to_ang()`](trigonometry.scad#function-adj_hyp_to_ang) Func – Returns the reference angle from the lengths of the adjacent side and the hypotenuse.
- [`adj_hyp_to_opp()`](trigonometry.scad#function-adj_hyp_to_opp) Func – Returns the opposite side length from the lengths of the adjacent side and the hypotenuse.
- [`adj_opp_to_ang()`](trigonometry.scad#function-adj_opp_to_ang) Func – Returns the reference angle from the lengths of the adjacent and opposite sides.
- [`adj_opp_to_hyp()`](trigonometry.scad#function-adj_opp_to_hyp) Func – Returns the hypotenuse length from the lengths of the adjacent and opposite sides.
- [`ang_adj_to_hyp()`](trigonometry.scad#function-ang_adj_to_hyp) Func – Returns the hypotenuse length from the reference reference angle and length of the adjacent side.
- [`ang_adj_to_opp()`](trigonometry.scad#function-ang_adj_to_opp) Func – Returns the opposite side length from the reference reference angle and the length of the adjacent side.
- [`ang_hyp_to_adj()`](trigonometry.scad#function-ang_hyp_to_adj) Func – Returns the adjacent side length from the reference reference angle and the length of the hypotenuse.
- [`ang_hyp_to_opp()`](trigonometry.scad#function-ang_hyp_to_opp) Func – Returns the opposite side length from the reference reference angle and the length of the hypotenuse.
- [`ang_opp_to_adj()`](trigonometry.scad#function-ang_opp_to_adj) Func – Returns the adjacent side length from the reference reference angle and the length of the opposite side.
- [`ang_opp_to_hyp()`](trigonometry.scad#function-ang_opp_to_hyp) Func – Returns the hypotenuse length from the reference reference angle and the length of the opposite side.
- [`hyp_adj_to_ang()`](trigonometry.scad#function-hyp_adj_to_ang) Func – Returns the reference reference angle from the lengths of the hypotenuse and the adjacent side.
- [`hyp_adj_to_opp()`](trigonometry.scad#function-hyp_adj_to_opp) Func – Returns the opposite side length from the lengths of the hypotenuse and the adjacent side.
- [`hyp_ang_to_adj()`](trigonometry.scad#function-hyp_ang_to_adj) Func – Returns the adjacent side length from the length of the hypotenuse and the reference reference angle.
- [`hyp_ang_to_opp()`](trigonometry.scad#function-hyp_ang_to_opp) Func – Returns the opposite side length from the length of the hypotenuse and the reference reference angle.
- [`hyp_opp_to_adj()`](trigonometry.scad#function-hyp_opp_to_adj) Func – Returns the adjacent side length from the lengths of the hypotenuse and the opposite side.
- [`hyp_opp_to_ang()`](trigonometry.scad#function-hyp_opp_to_ang) Func – Returns the reference reference angle from the lengths of the hypotenuse and the opposite side.
- [`law_of_cosines()`](trigonometry.scad#function-law_of_cosines) Func – Applies the Law of Cosines for an arbitrary triangle.
- [`law_of_sines()`](trigonometry.scad#function-law_of_sines) Func – Applies the Law of Sines for an arbitrary triangle.
- [`opp_adj_to_ang()`](trigonometry.scad#function-opp_adj_to_ang) Func – Returns the reference reference angle from the lengths of the opposite and adjacent sides.
- [`opp_adj_to_hyp()`](trigonometry.scad#function-opp_adj_to_hyp) Func – Returns the hypotenuse length from the lengths of the opposite and adjacent sides.
- [`opp_ang_to_adj()`](trigonometry.scad#function-opp_ang_to_adj) Func – Returns the adjacent side length from the length of the opposite side and the reference reference angle.
- [`opp_ang_to_hyp()`](trigonometry.scad#function-opp_ang_to_hyp) Func – Returns the hypotenuse length from the length of the opposite side and the reference reference angle.
- [`opp_hyp_to_adj()`](trigonometry.scad#function-opp_hyp_to_adj) Func – Returns the adjacent side length from the lengths of the opposite side and the hypotenuse.
- [`opp_hyp_to_ang()`](trigonometry.scad#function-opp_hyp_to_ang) Func – Returns the reference reference angle from the lengths of the opposite side and the hypotenuse.

### Triangulation

- [`polygon_triangulate()`](geometry.scad#function-polygon_triangulate) Func – Divide a polygon into triangles.

### Trigonometry

- [`acosh()`](math.scad#function-acosh) Func – Returns the hyperbolic arc-cosine of the given value.
- [`adj_ang_to_hyp()`](trigonometry.scad#function-adj_ang_to_hyp) Func – Returns the hypotenuse length from the length of the adjacent side and the reference reference angle.
- [`adj_ang_to_opp()`](trigonometry.scad#function-adj_ang_to_opp) Func – Returns the opposite side length from the length of the adjacent side and the reference reference angle.
- [`adj_hyp_to_ang()`](trigonometry.scad#function-adj_hyp_to_ang) Func – Returns the reference angle from the lengths of the adjacent side and the hypotenuse.
- [`adj_hyp_to_opp()`](trigonometry.scad#function-adj_hyp_to_opp) Func – Returns the opposite side length from the lengths of the adjacent side and the hypotenuse.
- [`adj_opp_to_ang()`](trigonometry.scad#function-adj_opp_to_ang) Func – Returns the reference angle from the lengths of the adjacent and opposite sides.
- [`adj_opp_to_hyp()`](trigonometry.scad#function-adj_opp_to_hyp) Func – Returns the hypotenuse length from the lengths of the adjacent and opposite sides.
- [`ang_adj_to_hyp()`](trigonometry.scad#function-ang_adj_to_hyp) Func – Returns the hypotenuse length from the reference reference angle and length of the adjacent side.
- [`ang_adj_to_opp()`](trigonometry.scad#function-ang_adj_to_opp) Func – Returns the opposite side length from the reference reference angle and the length of the adjacent side.
- [`ang_hyp_to_adj()`](trigonometry.scad#function-ang_hyp_to_adj) Func – Returns the adjacent side length from the reference reference angle and the length of the hypotenuse.
- [`ang_hyp_to_opp()`](trigonometry.scad#function-ang_hyp_to_opp) Func – Returns the opposite side length from the reference reference angle and the length of the hypotenuse.
- [`ang_opp_to_adj()`](trigonometry.scad#function-ang_opp_to_adj) Func – Returns the adjacent side length from the reference reference angle and the length of the opposite side.
- [`ang_opp_to_hyp()`](trigonometry.scad#function-ang_opp_to_hyp) Func – Returns the hypotenuse length from the reference reference angle and the length of the opposite side.
- [`asinh()`](math.scad#function-asinh) Func – Returns the hyperbolic arc-sine of the given value.
- [`atanh()`](math.scad#function-atanh) Func – Returns the hyperbolic arc-tangent of the given value.
- [`cosh()`](math.scad#function-cosh) Func – Returns the hyperbolic cosine of the given value.
- [`hyp_adj_to_ang()`](trigonometry.scad#function-hyp_adj_to_ang) Func – Returns the reference reference angle from the lengths of the hypotenuse and the adjacent side.
- [`hyp_adj_to_opp()`](trigonometry.scad#function-hyp_adj_to_opp) Func – Returns the opposite side length from the lengths of the hypotenuse and the adjacent side.
- [`hyp_ang_to_adj()`](trigonometry.scad#function-hyp_ang_to_adj) Func – Returns the adjacent side length from the length of the hypotenuse and the reference reference angle.
- [`hyp_ang_to_opp()`](trigonometry.scad#function-hyp_ang_to_opp) Func – Returns the opposite side length from the length of the hypotenuse and the reference reference angle.
- [`hyp_opp_to_adj()`](trigonometry.scad#function-hyp_opp_to_adj) Func – Returns the adjacent side length from the lengths of the hypotenuse and the opposite side.
- [`hyp_opp_to_ang()`](trigonometry.scad#function-hyp_opp_to_ang) Func – Returns the reference reference angle from the lengths of the hypotenuse and the opposite side.
- [`law_of_cosines()`](trigonometry.scad#function-law_of_cosines) Func – Applies the Law of Cosines for an arbitrary triangle.
- [`law_of_sines()`](trigonometry.scad#function-law_of_sines) Func – Applies the Law of Sines for an arbitrary triangle.
- [`opp_adj_to_ang()`](trigonometry.scad#function-opp_adj_to_ang) Func – Returns the reference reference angle from the lengths of the opposite and adjacent sides.
- [`opp_adj_to_hyp()`](trigonometry.scad#function-opp_adj_to_hyp) Func – Returns the hypotenuse length from the lengths of the opposite and adjacent sides.
- [`opp_ang_to_adj()`](trigonometry.scad#function-opp_ang_to_adj) Func – Returns the adjacent side length from the length of the opposite side and the reference reference angle.
- [`opp_ang_to_hyp()`](trigonometry.scad#function-opp_ang_to_hyp) Func – Returns the hypotenuse length from the length of the opposite side and the reference reference angle.
- [`opp_hyp_to_adj()`](trigonometry.scad#function-opp_hyp_to_adj) Func – Returns the adjacent side length from the lengths of the opposite side and the hypotenuse.
- [`opp_hyp_to_ang()`](trigonometry.scad#function-opp_hyp_to_ang) Func – Returns the reference reference angle from the lengths of the opposite side and the hypotenuse.
- [`sinh()`](math.scad#function-sinh) Func – Returns the hyperbolic sine of the given value.
- [`tanh()`](math.scad#function-tanh) Func – Returns the hyperbolic tangent of the given value.

### Trusses

- [`cubetruss()`](cubetruss.scad#module-cubetruss) Mod – Creates a multi-cube straight cubetruss shape. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`cubetruss_clip()`](cubetruss.scad#module-cubetruss_clip) Mod – Creates a clip for the end of a cubetruss to snap-lock it to another cubetruss. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`cubetruss_corner()`](cubetruss.scad#module-cubetruss_corner) Mod – Creates a multi-cube corner cubetruss shape. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`cubetruss_dist()`](cubetruss.scad#function-cubetruss_dist) Func – Returns the length of a cubetruss truss.
- [`cubetruss_foot()`](cubetruss.scad#module-cubetruss_foot) Mod – Creates a foot that can connect two cubetrusses. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`cubetruss_joiner()`](cubetruss.scad#module-cubetruss_joiner) Mod – Creates a joiner that can connect two cubetrusses end-to-end. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`cubetruss_segment()`](cubetruss.scad#module-cubetruss_segment) Mod – Creates a single cubetruss cube. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`cubetruss_support()`](cubetruss.scad#module-cubetruss_support) Mod – Creates a cubetruss support structure shape. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`cubetruss_uclip()`](cubetruss.scad#module-cubetruss_uclip) Mod – Creates a joiner that can connect two cubetrusses end-to-end. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>

### Type Checking

- [`all()`](utility.scad#function-all) Func – Returns true if all items in the argument list are true.
- [`all_integer()`](utility.scad#function-all_integer) Func – Returns true if all of the numbers in the argument are integers.
- [`any()`](utility.scad#function-any) Func – Returns true if any item in the argument list is true.
- [`is_bezier_patch()`](beziers.scad#function-is_bezier_patch) Func – Returns true if the given item is a bezier patch.
- [`is_consistent()`](utility.scad#function-is_consistent) Func – Returns true if the argument is a list with consistent structure and finite numerical data.
- [`is_def()`](utility.scad#function-is_def) Func – Returns true if `x` is not `undef`.
- [`is_finite()`](utility.scad#function-is_finite) Func – Returns true if the argument is a finite number.
- [`is_func()`](utility.scad#function-is_func) Func – Returns true if the argument is a function literal.
- [`is_homogeneous()`](lists.scad#function-is_homogeneous) Func – Returns true if all members of a list are of the same type.
- [`is_homogeneous()`](lists.scad#function-is_homogeneous) Func – Returns true if all members of a list are of the same type.
- [`is_int()`](utility.scad#function-is_int) Func – Returns true if the argument is an integer.
- [`is_int()`](utility.scad#function-is_int) Func – Returns true if the argument is an integer.
- [`is_nan()`](utility.scad#function-is_nan) Func – Return true if the argument is "not a number".
- [`is_nurbs_patch()`](nurbs.scad#function-is_nurbs_patch) Func – Returns true if the given item looks like a NURBS patch.
- [`is_range()`](utility.scad#function-is_range) Func – Returns true if the argument is a range.
- [`is_str()`](utility.scad#function-is_str) Func – Returns true if the argument is a string.
- [`is_type()`](utility.scad#function-is_type) Func – Returns true if the type of 'x' is one of those in the list `types`.
- [`same_shape()`](utility.scad#function-same_shape) Func – Returns true if the argument lists are numeric and of the same shape.
- [`typeof()`](utility.scad#function-typeof) Func – Returns a string representing the type of the value.
- [`valid_range()`](utility.scad#function-valid_range) Func – Returns true if the argument is a valid range.

### Type Conversion

- [`list()`](lists.scad#function-list) Func – Expands a range into a full list.

### Type Queries

- [`f_is_bezier_patch()`](fnliterals.scad#function-f_is_bezier_patch) Func – Returns a function to determine if a value is a Bezier Patch structure.
- [`f_is_bool()`](fnliterals.scad#function-f_is_bool) Func – Returns a function to determine if a value is a boolean.
- [`f_is_def()`](fnliterals.scad#function-f_is_def) Func – Returns a function to determine if a value is not `undef`.
- [`f_is_finite()`](fnliterals.scad#function-f_is_finite) Func – Returns a function to determine if a value is a number type that is finite.
- [`f_is_function()`](fnliterals.scad#function-f_is_function) Func – Returns a function to determine if a value is a function literal.
- [`f_is_int()`](fnliterals.scad#function-f_is_int) Func – Returns a function to determine if a value is an integer number.
- [`f_is_list()`](fnliterals.scad#function-f_is_list) Func – Returns a function to determine if a value is a list.
- [`f_is_nan()`](fnliterals.scad#function-f_is_nan) Func – Returns a function to determine if a value is a number type that is Not a Number (NaN).
- [`f_is_num()`](fnliterals.scad#function-f_is_num) Func – Returns a function to determine if a value is a number.
- [`f_is_path()`](fnliterals.scad#function-f_is_path) Func – Returns a function to determine if a value is a Path (a list of points).
- [`f_is_range()`](fnliterals.scad#function-f_is_range) Func – Returns a function to determine if a value is a range.
- [`f_is_region()`](fnliterals.scad#function-f_is_region) Func – Returns a function to determine if a value is a Region (a list of Paths).
- [`f_is_string()`](fnliterals.scad#function-f_is_string) Func – Returns a function to determine if a value is a string.
- [`f_is_undef()`](fnliterals.scad#function-f_is_undef) Func – Returns a function to determine if a value is `undef`.
- [`f_is_vector()`](fnliterals.scad#function-f_is_vector) Func – Returns a function to determine if a value is a list of numbers.
- [`f_is_vnf()`](fnliterals.scad#function-f_is_vnf) Func – Returns a function to determine if a value is a VNF structure.

### Undef Handling

- [`all_defined()`](utility.scad#function-all_defined) Func – Returns true if all items in the given array are defined.
- [`any_defined()`](utility.scad#function-any_defined) Func – Returns true if any item in the argument list is not `undef`.
- [`default()`](utility.scad#function-default) Func – Returns a default value if the argument is 'undef', else returns the argument.
- [`first_defined()`](utility.scad#function-first_defined) Func – Returns the first value in the argument list that is not 'undef'.
- [`num_defined()`](utility.scad#function-num_defined) Func – Returns the number of defined values in the the argument list.
- [`one_defined()`](utility.scad#function-one_defined) Func – Returns the defined value in the argument list if only a single value is defined.
- [`u_add()`](utility.scad#function-u_add) Func – Returns the sum of 2 numbers if both are defined, otherwise returns undef.
- [`u_div()`](utility.scad#function-u_div) Func – Returns the quotient of 2 numbers if both are defined, otherwise returns undef.
- [`u_mul()`](utility.scad#function-u_mul) Func – Returns the product of 2 numbers if both are defined, otherwise returns undef.
- [`u_sub()`](utility.scad#function-u_sub) Func – Returns the difference of 2 numbers if both are defined, otherwise returns undef.

### VNF Generators

- [`cube()`](shapes3d.scad#functionmodule-cube) Func/Mod – Creates a cube with anchors for attaching children. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Extends the OpenScad keyword of the same name.">[<abbr>Ext</abbr>]</sup>
- [`cylinder()`](shapes3d.scad#functionmodule-cylinder) Func/Mod – Creates an attachable cylinder. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Extends the OpenScad keyword of the same name.">[<abbr>Ext</abbr>]</sup>
- [`isosurface()`](isosurface.scad#functionmodule-isosurface) Func/Mod – Creates a 3D isosurface (a 3D contour) from a function or array of values. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup>
- [`metaballs()`](isosurface.scad#functionmodule-metaballs) Func/Mod – Creates a group of 3D metaballs (smoothly connected blobs). <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup>
- [`octahedron()`](shapes3d.scad#functionmodule-octahedron) Func/Mod – Creates an octahedron with axis-aligned points. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup>
- [`onion()`](shapes3d.scad#functionmodule-onion) Func/Mod – Creates an attachable onion-like shape. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup>
- [`pie_slice()`](shapes3d.scad#functionmodule-pie_slice) Func/Mod – Creates a pie slice shape. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup>
- [`prismoid()`](shapes3d.scad#functionmodule-prismoid) Func/Mod – Creates a rectangular prismoid shape with optional roundovers and chamfering. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup>
- [`rect_tube()`](shapes3d.scad#module-rect_tube) Mod – Creates a rectangular tube. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`sphere()`](shapes3d.scad#functionmodule-sphere) Func/Mod – Creates an attachable spherical object. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Extends the OpenScad keyword of the same name.">[<abbr>Ext</abbr>]</sup>
- [`spheroid()`](shapes3d.scad#functionmodule-spheroid) Func/Mod – Creates an attachable spherical object with controllable triangulation. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup>
- [`teardrop()`](shapes3d.scad#functionmodule-teardrop) Func/Mod – Creates a teardrop shape. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup>
- [`textured_tile()`](shapes3d.scad#functionmodule-textured_tile) Func/Mod – Creates a cube or trapezoidal prism with a textured top face for attaching to objects. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup>
- [`torus()`](shapes3d.scad#functionmodule-torus) Func/Mod – Creates an attachable torus. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup>
- [`tube()`](shapes3d.scad#module-tube) Mod – Creates a cylindrical or conical tube. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`vnf_from_polygons()`](vnf.scad#function-vnf_from_polygons) Func – Returns a VNF from a list of 3D polygons. <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup>
- [`vnf_from_region()`](vnf.scad#function-vnf_from_region) Func – Returns a 3D VNF given a 2D region. <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup>
- [`vnf_join()`](vnf.scad#function-vnf_join) Func – Returns a single VNF structure from a list of VNF structures. <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup>
- [`vnf_tri_array()`](vnf.scad#functionmodule-vnf_tri_array) Func/Mod – Returns a VNF from an array of points. The array need not be rectangular. <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup>
- [`vnf_vertex_array()`](vnf.scad#functionmodule-vnf_vertex_array) Func/Mod – Returns a VNF structure from a rectangular vertex list. <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup> <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`wedge()`](shapes3d.scad#functionmodule-wedge) Func/Mod – Creates a 3d triangular wedge. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup> <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup>

### VNF Manipulation

- [`fit_to_box()`](vectors.scad#function-fit_to_box) Func – Scale the x, y, and/or z coordinates of a list of points to span a range.
- [`is_vnf()`](vnf.scad#function-is_vnf) Func – Returns true given a VNF-like structure.
- [`is_vnf_list()`](vnf.scad#function-is_vnf_list) Func – Returns true given a list of VNF-like structures.
- [`projection()`](vnf.scad#function-projection) Func – Returns projection or intersection of vnf with XY plane <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup>
- [`vnf_area()`](vnf.scad#function-vnf_area) Func – Returns the surface area of a VNF.
- [`vnf_bend()`](vnf.scad#function-vnf_bend) Func – Bends a VNF around an axis. <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup>
- [`vnf_boundary()`](vnf.scad#function-vnf_boundary) Func – Returns the boundary of a VNF as a list of paths <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup>
- [`vnf_bounds()`](vnf.scad#function-vnf_bounds) Func – Returns the min and max bounding coordinates for the VNF.
- [`vnf_drop_unused_points()`](vnf.scad#function-vnf_drop_unused_points) Func – Removes unreferenced vertices from a VNF. <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup>
- [`vnf_faces()`](vnf.scad#function-vnf_faces) Func – Returns the list of faces from a VNF.
- [`vnf_halfspace()`](vnf.scad#function-vnf_halfspace) Func – Returns the intersection of the vnf with a half space. <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup>
- [`vnf_merge_points()`](vnf.scad#function-vnf_merge_points) Func – Consolidates duplicate vertices of a VNF. <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup>
- [`vnf_polyhedron()`](vnf.scad#module-vnf_polyhedron) Mod – Returns a polyhedron from a VNF or list of VNFs. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`vnf_quantize()`](vnf.scad#function-vnf_quantize) Func – Quantizes the vertex coordinates of a VNF. <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup>
- [`vnf_reverse_faces()`](vnf.scad#function-vnf_reverse_faces) Func – Reverses the faces of a VNF. <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup>
- [`vnf_sheet()`](vnf.scad#function-vnf_sheet) Func – Extends a VNF into a thin sheet by extruding normal to the VNF <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup>
- [`vnf_slice()`](vnf.scad#function-vnf_slice) Func – Slice the faces of a VNF along an axis. <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup>
- [`vnf_small_offset()`](vnf.scad#function-vnf_small_offset) Func – Computes an offset surface to a VNF for small offset distances <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup>
- [`vnf_triangulate()`](vnf.scad#function-vnf_triangulate) Func – Triangulates the faces of a VNF. <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup>
- [`vnf_unify_faces()`](vnf.scad#function-vnf_unify_faces) Func – Remove triangulation from VNF, returning a copy with full faces <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup>
- [`vnf_validate()`](vnf.scad#module-vnf_validate) Mod – Echos non-manifold VNF errors to the console. <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup>
- [`vnf_vertices()`](vnf.scad#function-vnf_vertices) Func – Returns the list of vertex points from a VNF.
- [`vnf_volume()`](vnf.scad#function-vnf_volume) Func – Returns the volume of a VNF.
- [`vnf_wireframe()`](vnf.scad#module-vnf_wireframe) Mod – Creates a wireframe model from a VNF. <sup title="Can return a VNF.">[<abbr>VNF</abbr>]</sup>

### Vectors

- [`add_scalar()`](vectors.scad#function-add_scalar) Func – Adds a scalar value to every item in a vector.
- [`BACK`](constants.scad#constant-back) Const – The backwards (Y+) direction vector constant `[0,1,0]`.
- [`BOTTOM`](constants.scad#constant-bottom) Const – The down-wards (Z-) direction vector constant `[0,0,-1]`.
- [`BOTTOM`](constants.scad#constant-bottom) Const – The down-wards (Z-) direction vector constant `[0,0,-1]`.
- [`CENTER`](constants.scad#constant-center) Const – The center vector constant `[0,0,0]`.
- [`CENTER`](constants.scad#constant-center) Const – The center vector constant `[0,0,0]`.
- [`CENTER`](constants.scad#constant-center) Const – The center vector constant `[0,0,0]`.
- [`BOTTOM`](constants.scad#constant-bottom) Const – The down-wards (Z-) direction vector constant `[0,0,-1]`.
- [`f_cross()`](fnliterals.scad#function-f_cross) Func – Returns a function to calculate the norm of a given vector.
- [`f_norm()`](fnliterals.scad#function-f_norm) Func – Returns a function to calculate the norm of a given vector.
- [`FRONT`](constants.scad#constant-front) Const – The front-wards (Y-) direction vector constant `[0,-1,0]`.
- [`FRONT`](constants.scad#constant-front) Const – The front-wards (Y-) direction vector constant `[0,-1,0]`.
- [`FRONT`](constants.scad#constant-front) Const – The front-wards (Y-) direction vector constant `[0,-1,0]`.
- [`is_vector()`](vectors.scad#function-is_vector) Func – Returns true if the given value is a vector.
- [`LEFT`](constants.scad#constant-left) Const – The left-wards (X-) direction vector constant `[-1,0,0]`.
- [`RIGHT`](constants.scad#constant-right) Const – The right-wards (X+) direction vector constant `[1,0,0]`.
- [`TOP`](constants.scad#constant-top) Const – The top-wards (Z+) direction vector constant `[0,0,1]`.
- [`unit()`](vectors.scad#function-unit) Func – Returns the unit length of a given vector.
- [`TOP`](constants.scad#constant-top) Const – The top-wards (Z+) direction vector constant `[0,0,1]`.
- [`v_abs()`](vectors.scad#function-v_abs) Func – Returns the absolute values of the given vector.
- [`v_ceil()`](vectors.scad#function-v_ceil) Func – Returns the values of the given vector, rounded up.
- [`v_div()`](vectors.scad#function-v_div) Func – Returns the element-wise division of two equal-length vectors.
- [`v_floor()`](vectors.scad#function-v_floor) Func – Returns the values of the given vector, rounded down.
- [`v_lookup()`](vectors.scad#function-v_lookup) Func – Like `lookup()`, but it can interpolate between vector results.
- [`v_mul()`](vectors.scad#function-v_mul) Func – Returns the element-wise multiplication of two equal-length vectors.
- [`v_round()`](vectors.scad#function-v_round) Func – Returns the values of the given vector, rounded to the nearest whole number.
- [`v_theta()`](vectors.scad#function-v_theta) Func – Returns the angle counter-clockwise from X+ on the XY plane.
- [`vector_angle()`](vectors.scad#function-vector_angle) Func – Returns the minor angle between two vectors.
- [`vector_axis()`](vectors.scad#function-vector_axis) Func – Returns the perpendicular axis between two vectors.
- [`vector_bisect()`](vectors.scad#function-vector_bisect) Func – Returns the vector that bisects two vectors.
- [`vector_perp()`](vectors.scad#function-vector_perp) Func – Returns component of a vector perpendicular to a second vector

### Versioning

- [`assert_supported()`](version.scad#function-assert_supported) Func – Asserts that a language extension feature is supported.
- [`bosl_required()`](version.scad#module-bosl_required) Mod – Asserts that the current version of the library is at least the given version.
- [`bosl_version()`](version.scad#function-bosl_version) Func – Returns the BOSL2 version as a list.
- [`bosl_version_num()`](version.scad#function-bosl_version_num) Func – Returns the BOSL2 version as a float.
- [`bosl_version_str()`](version.scad#function-bosl_version_str) Func – Returns the BOSL2 version as a string.
- [`version_cmp()`](version.scad#function-version_cmp) Func – Compares two versions.
- [`version_to_list()`](version.scad#function-version_to_list) Func – Splits a version into a list of integer version parts.
- [`version_to_num()`](version.scad#function-version_to_num) Func – Coerces a version into a standard version float.
- [`version_to_str()`](version.scad#function-version_to_str) Func – Coerces a version into a standard version string.

### versioning

- [`supports()`](version.scad#function-supports) Func – Checks if a language extension feature is supported.

### Walls

- [`corrugated_wall()`](walls.scad#module-corrugated_wall) Mod – Makes a corrugated rectangular wall. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`hex_panel()`](walls.scad#module-hex_panel) Mod – Create a hexagon braced panel of any shape <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`sparse_cuboid()`](walls.scad#module-sparse_cuboid) Mod – Makes an open cross-braced cuboid <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`sparse_wall()`](walls.scad#module-sparse_wall) Mod – Makes an open cross-braced rectangular wall. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`sparse_wall2d()`](walls.scad#module-sparse_wall2d) Mod – Makes an open cross-braced rectangular wall. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`thinning_triangle()`](walls.scad#module-thinning_triangle) Mod – Makes a triangular wall with a thin middle. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>
- [`thinning_wall()`](walls.scad#module-thinning_wall) Mod – Makes a rectangular wall with a thin middle. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>

### Wiring

- [`wire_bundle()`](wiring.scad#module-wire_bundle) Mod – Creates a wire bundle for a given number of wires. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>


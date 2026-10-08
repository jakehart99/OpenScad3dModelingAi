# LibFile: geometry.scad

Perform calculations on lines, polygons, planes and circles, including
normals, intersections of objects, distance between objects, and tangent lines.
Throughout this library, lines can be treated as either unbounded lines, as rays with
a single endpoint or as segments, bounded by endpoints at both ends.

To use, add the following lines to the beginning of your file:

    include <BOSL2/std.scad>

## File Contents

1. [Section: Lines, Rays, and Segments](#section-lines-rays-and-segments)
    - [`is_point_on_line()`](#function-is_point_on_line) – Determine if a point is on a line, ray or segment.
    - [`is_collinear()`](#function-is_collinear) – Determine if points are collinear.
    - [`point_line_distance()`](#function-point_line_distance) – Find shortest distance from point to a line, segment or ray.
    - [`segment_distance()`](#function-segment_distance) – Find smallest distance between two line semgnets.
    - [`line_normal()`](#function-line_normal) – Return normal vector to given line.
    - [`line_intersection()`](#function-line_intersection) – Compute intersection of two lines, segments or rays.
    - [`line_closest_point()`](#function-line_closest_point) – Find point on given line, segment or ray that is closest to a given point.
    - [`line_from_points()`](#function-line_from_points) – Given a list of collinear points, return the line they define.

2. [Section: Planes](#section-planes)
    - [`is_coplanar()`](#function-is_coplanar) – Check if 3d points are coplanar and not collinear.
    - [`plane3pt()`](#function-plane3pt) – Return a plane from 3 points.
    - [`plane3pt_indexed()`](#function-plane3pt_indexed) – Given list of 3d points and 3 indices, return the plane they define.
    - [`plane_from_normal()`](#function-plane_from_normal) – Return plane defined by normal vector and a point.
    - [`plane_from_points()`](#function-plane_from_points) – Return plane defined by a set of 3D points, with arbitrary normal direction.
    - [`plane_from_polygon()`](#function-plane_from_polygon) – Given a 3d planar polygon, returns directed plane.
    - [`plane_normal()`](#function-plane_normal) – Returns the normal vector to a plane.
    - [`plane_offset()`](#function-plane_offset) – Returns the signed offset of the plane from the origin.
    - [`plane_line_intersection()`](#function-plane_line_intersection) – Returns the intersection of a plane and 3d line, segment or ray.
    - [`plane_intersection()`](#function-plane_intersection) – Returns the intersection of two or three planes.
    - [`plane_line_angle()`](#function-plane_line_angle) – Returns the angle between a plane and a 3d line.
    - [`plane_closest_point()`](#function-plane_closest_point) – Returns the orthogonal projection of points onto a plane.
    - [`point_plane_distance()`](#function-point_plane_distance) – Determine distance between a point and plane.
    - [`are_points_on_plane()`](#function-are_points_on_plane) – Determine if all of the listed points are on a plane.
    - [`show_plane()`](#module-show_plane) – Display (part of) a plane <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>

3. [Section: Circle Calculations](#section-circle-calculations)
    - [`circle_line_intersection()`](#function-circle_line_intersection) – Find the intersection points between a 2d circle and a line, ray or segment.
    - [`circle_circle_intersection()`](#function-circle_circle_intersection) – Find the intersection points of two 2d circles.
    - [`circle_2tangents()`](#function-circle_2tangents) – Given two 2d or 3d rays, find a circle tangent to both.
    - [`circle_3points()`](#function-circle_3points) – Find a circle passing through three 2d or 3d points.
    - [`circle_point_tangents()`](#function-circle_point_tangents) – Given a circle and point, find tangents to circle passing through the point.
    - [`circle_circle_tangents()`](#function-circle_circle_tangents) – Find tangents to a pair of circles in 2d.

4. [Section: Sphere Calculations](#section-sphere-calculations)
    - [`sphere_line_intersection()`](#function-sphere_line_intersection) – Find intersection between a sphere and line, ray or segment.

5. [Section: Polygons](#section-polygons)
    - [`polygon_area()`](#function-polygon_area) – Calculate area of a 2d or 3d polygon.
    - [`centroid()`](#function-centroid) – Compute centroid of a 2d or 3d polygon or a VNF.
    - [`polygon_normal()`](#function-polygon_normal) – Return normal to a polygon.
    - [`point_in_polygon()`](#function-point_in_polygon) – Checks if a 2d point is inside or on the boundary of a 2d polygon.
    - [`polygon_line_intersection()`](#function-polygon_line_intersection) – Find intersection between 2d or 3d polygon and a line, segment or ray.
    - [`polygon_triangulate()`](#function-polygon_triangulate) – Divide a polygon into triangles.
    - [`is_polygon_clockwise()`](#function-is_polygon_clockwise) – Determine if a 2d polygon winds clockwise.
    - [`clockwise_polygon()`](#function-clockwise_polygon) – Return clockwise version of a polygon.
    - [`ccw_polygon()`](#function-ccw_polygon) – Return counter-clockwise version of a polygon.
    - [`reverse_polygon()`](#function-reverse_polygon) – Reverse winding direction of polygon.
    - [`reindex_polygon()`](#function-reindex_polygon) – Adjust point indexing of polygon to minimize pointwise distance to a reference polygon.
    - [`align_polygon()`](#function-align_polygon) – Find best alignment of a 2d polygon to a reference 2d polygon over a set of transformations.
    - [`are_polygons_equal()`](#function-are_polygons_equal) – Check if two polygons (not necessarily in the same point order) are equal.

6. [Section: Convex Hull](#section-convex-hull)
    - [`hull()`](#function-hull) – Convex hull of a list of 2d or 3d points. <sup title="Extends the OpenScad keyword of the same name.">[<abbr>Ext</abbr>]</sup>
    - [`hull_points()`](#module-hull_points) – Convex hull of a list of 2d or 3d points.
    - [`hull2d_path()`](#function-hull2d_path) – Convex hull of a list of 2d points.
    - [`hull3d_faces()`](#function-hull3d_faces) – Convex hull of a list of 3d points.

7. [Section: Convex Sets](#section-convex-sets)
    - [`is_polygon_convex()`](#function-is_polygon_convex) – Check if a polygon is convex.
    - [`convex_distance()`](#function-convex_distance) – Compute distance between convex hull of two point lists.
    - [`convex_collision()`](#function-convex_collision) – Check whether the convex hulls of two point lists intersect.

8. [Section: Rotation Decoding](#section-rotation-decoding)
    - [`rot_decode()`](#function-rot_decode) – Extract axis and rotation angle from a rotation matrix.


## Section: Lines, Rays, and Segments


### Function: is\_point\_on\_line()

**Synopsis:** Determine if a point is on a line, ray or segment.

**Topics:** [Geometry](Topics#geometry), [Points](Topics#points), [Segments](Topics#segments)

**See Also:** [is\_collinear()](#function-is_collinear), [point\_line\_distance()](#function-point_line_distance), [line\_from\_points()](#function-line_from_points)

**Usage:** 

- pt = is_point_on_line(point, line, [bounded], [eps]);

**Description:** 

Determine if the point is on the line segment, ray or segment defined by the two between two points.
Returns true if yes, and false if not.  If bounded is set to true it specifies a segment, with
both lines bounded at the ends.  Set bounded to `[true,false]` to get a ray.  You can use
the shorthands RAY and SEGMENT to set bounded.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`point`              | The point to test.
`line`               | Array of two points defining the line, ray, or segment to test against.
`bounded`            | boolean or list of two booleans defining endpoint conditions for the line. If false treat the line as an unbounded line.  If true treat it as a segment.  If [true,false] treat as a ray, based at the first endpoint.  Default: false
`eps`                | Tolerance in geometric comparisons.  Default: 1e-9

---

### Function: is\_collinear()

**Synopsis:** Determine if points are collinear.

**Topics:** [Geometry](Topics#geometry), [Points](Topics#points), [Collinearity](Topics#collinearity)

**See Also:** [is\_point\_on\_line()](#function-is_point_on_line), [point\_line\_distance()](#function-point_line_distance), [line\_from\_points()](#function-line_from_points)

**Usage:** 

- bool = is_collinear(a, [b, c], [eps]);

**Description:** 

Returns true if the points `a`, `b` and `c` are co-linear or if the list of points `a` is collinear.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`a`                  | First point or list of points.
`b`                  | Second point or undef; it should be undef if `c` is undef
`c`                  | Third point or undef.
`eps`                | Tolerance in geometric comparisons.  Default: 1e-9

---

### Function: point\_line\_distance()

**Synopsis:** Find shortest distance from point to a line, segment or ray.

**Topics:** [Geometry](Topics#geometry), [Points](Topics#points), [Lines](Topics#lines), [Distance](Topics#distance)

**See Also:** [is\_collinear()](#function-is_collinear), [is\_point\_on\_line()](#function-is_point_on_line), [line\_from\_points()](#function-line_from_points)

**Usage:** 

- dist = point_line_distance(pt, line, [bounded]);

**Description:** 

Finds the shortest distance from the point `pt` to the specified line, segment or ray.
The bounded parameter specifies the whether the endpoints give a ray or segment.
By default assumes an unbounded line.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`pt`                 | A point to find the distance of from the line.
`line`               | A list of two points defining a line.
`bounded`            | a boolean or list of two booleans specifiying whether each end is bounded.  Default: false

**Example 1:** 

    include <BOSL2/std.scad>
    dist1 = point_line_distance([3,8], [[-10,0], [10,0]]);  // Returns: 8
    dist2 = point_line_distance([3,8], [[-10,0], [10,0]],SEGMENT);  // Returns: 8
    dist3 = point_line_distance([14,3], [[-10,0], [10,0]],SEGMENT);  // Returns: 5

<br clear="all" /><br/>

---

### Function: segment\_distance()

**Synopsis:** Find smallest distance between two line semgnets.

**Topics:** [Geometry](Topics#geometry), [Segments](Topics#segments), [Distance](Topics#distance)

**See Also:** [convex\_collision()](#function-convex_collision), [convex\_distance()](#function-convex_distance)

**Usage:** 

- dist = segment_distance(seg1, seg2, [eps]);

**Description:** 

Returns the smallest distance of the points on two given line segments.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`seg1`               | The list of two points representing the first line segment to check the distance of.
`seg2`               | The list of two points representing the second line segment to check the distance of.
`eps`                | tolerance for point comparisons

**Example 1:** 

    include <BOSL2/std.scad>
    dist = segment_distance([[-14,3], [-15,9]], [[-10,0], [10,0]]);  // Returns: 5
    dist2 = segment_distance([[-5,5], [5,-5]], [[-10,3], [10,-3]]);  // Returns: 0

<br clear="all" /><br/>

---

### Function: line\_normal()

**Synopsis:** Return normal vector to given line.

**Topics:** [Geometry](Topics#geometry), [Lines](Topics#lines)

**See Also:** [line\_intersection()](#function-line_intersection), [line\_from\_points()](#function-line_from_points)

**Usage:** 

- vec = line_normal([P1,P2])
- vec = line_normal(p1,p2)

**Description:** 

Returns the 2D normal vector to the given 2D line. This is otherwise known as the perpendicular vector counter-clockwise to the given ray.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`p1`                 | First point on 2D line.
`p2`                 | Second point on 2D line.

**Example 1:** 

<img align="left" alt="line\_normal() Example 1" src="images/geometry/line_normal.png" width="320" height="240">

    include <BOSL2/std.scad>
    p1 = [10,10];
    p2 = [50,30];
    n = line_normal(p1,p2);
    stroke([p1,p2], endcap2="arrow2");
    color("green") stroke([p1,p1+10*n], endcap2="arrow2");
    color("blue") move_copies([p1,p2]) circle(d=2, $fn=12);

<br clear="all" /><br/>

---

### Function: line\_intersection()

**Synopsis:** Compute intersection of two lines, segments or rays.

**Topics:** [Geometry](Topics#geometry), [Lines](Topics#lines)

**See Also:** [line\_normal()](#function-line_normal), [line\_from\_points()](#function-line_from_points)

**Usage:** 

- pt = line_intersection(line1, line2, [bounded1], [bounded2], [bounded=], [eps=]);

**Description:** 

Returns the intersection point of any two 2D lines, segments or rays.  Returns undef
if they do not intersect.  You specify a line by giving two distinct points on the
line.  You specify rays or segments by giving a pair of points and indicating
bounded[0]=true to bound the line at the first point, creating rays based at l1[0] and l2[0],
or bounded[1]=true to bound the line at the second point, creating the reverse rays bounded
at l1[1] and l2[1].  If bounded=[true, true] then you have segments defined by their two
endpoints.  By using bounded1 and bounded2 you can mix segments, rays, and lines as needed.
You can set the bounds parameters to true as a shorthand for [true,true] to sepcify segments.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`line1`              | List of two points in 2D defining the first line, segment or ray
`line2`              | List of two points in 2D defining the second line, segment or ray
`bounded1`           | boolean or list of two booleans defining which ends are bounded for line1.  Default: [false,false]
`bounded2`           | boolean or list of two booleans defining which ends are bounded for line2.  Default: [false,false]

<abbr title="These args must be used by name, ie: name=value">By&nbsp;Name</abbr> | What it does
-------------------- | ------------
`bounded`            | boolean or list of two booleans defining which ends are bounded for both lines.  The bounded1 and bounded2 parameters override this if both are given.
`eps`                | tolerance for geometric comparisons.  Default: 1e-9

**Example 1:** The segments do not intersect but the lines do in this example.

<img align="left" alt="line\_intersection() Example 1" src="images/geometry/line_intersection.png" width="320" height="240">

    include <BOSL2/std.scad>
    line1 = 10*[[9, 4], [5, 7]];
    line2 = 10*[[2, 3], [6, 5]];
    stroke(line1, endcaps="arrow2");
    stroke(line2, endcaps="arrow2");
    isect = line_intersection(line1, line2);
    color("red") translate(isect) circle(r=1,$fn=12);

<br clear="all" /><br/>

**Example 2:** Specifying a ray and segment using the shorthand variables.

<img align="left" alt="line\_intersection() Example 2" src="images/geometry/line_intersection_2.png" width="320" height="240">

    include <BOSL2/std.scad>
    line1 = 10*[[0, 2], [4, 7]];
    line2 = 10*[[10, 4], [3, 4]];
    stroke(line1);
    stroke(line2, endcap2="arrow2");
    isect = line_intersection(line1, line2, SEGMENT, RAY);
    color("red") translate(isect) circle(r=1,$fn=12);

<br clear="all" /><br/>

**Example 3:** Here we use the same example as above, but specify two segments using the bounded argument.

<img align="left" alt="line\_intersection() Example 3" src="images/geometry/line_intersection_3.png" width="320" height="240">

<br clear="all" />

    include <BOSL2/std.scad>
    line1 = 10*[[0, 2], [4, 7]];
    line2 = 10*[[10, 4], [3, 4]];
    stroke(line1);
    stroke(line2);
    isect = line_intersection(line1, line2, bounded=true);  // Returns undef

---

### Function: line\_closest\_point()

**Synopsis:** Find point on given line, segment or ray that is closest to a given point.

**Topics:** [Geometry](Topics#geometry), [Lines](Topics#lines), [Distance](Topics#distance)

**See Also:** [line\_normal()](#function-line_normal), [point\_line\_distance()](#function-point_line_distance)

**Usage:** 

- pt = line_closest_point(line, pt, [bounded]);

**Description:** 

Returns the point on the given line, segment or ray that is closest to the given point `pt`.
The inputs `line` and `pt` args should be of the same dimension.  The parameter bounded indicates
whether the points of `line` should be treated as endpoints.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`line`               | A list of two points that are on the unbounded line.
`pt`                 | The point to find the closest point on the line to.
`bounded`            | boolean or list of two booleans indicating that the line is bounded at that end.  Default: [false,false]

**Example 1:** 

<img align="left" alt="line\_closest\_point() Example 1" src="images/geometry/line_closest_point.png" width="320" height="240">

    include <BOSL2/std.scad>
    line = [[-30,0],[30,30]];
    pt = [-32,-10];
    p2 = line_closest_point(line,pt);
    stroke(line, endcaps="arrow2");
    color("blue") translate(pt) circle(r=1,$fn=12);
    color("red") translate(p2) circle(r=1,$fn=12);

<br clear="all" /><br/>

**Example 2:** If the line is bounded on the left you get the endpoint instead

<img align="left" alt="line\_closest\_point() Example 2" src="images/geometry/line_closest_point_2.png" width="320" height="240">

    include <BOSL2/std.scad>
    line = [[-30,0],[30,30]];
    pt = [-32,-10];
    p2 = line_closest_point(line,pt,bounded=[true,false]);
    stroke(line, endcap2="arrow2");
    color("blue") translate(pt) circle(r=1,$fn=12);
    color("red") translate(p2) circle(r=1,$fn=12);

<br clear="all" /><br/>

**Example 3:** In this case it doesn't matter how bounded is set.  Using SEGMENT is the most restrictive option.

<img align="left" alt="line\_closest\_point() Example 3" src="images/geometry/line_closest_point_3.png" width="320" height="240">

    include <BOSL2/std.scad>
    line = [[-30,0],[30,30]];
    pt = [-5,0];
    p2 = line_closest_point(line,pt,SEGMENT);
    stroke(line);
    color("blue") translate(pt) circle(r=1,$fn=12);
    color("red") translate(p2) circle(r=1,$fn=12);

<br clear="all" /><br/>

**Example 4:** The result here is the same for a line or a ray.

<img align="left" alt="line\_closest\_point() Example 4" src="images/geometry/line_closest_point_4.png" width="320" height="240">

    include <BOSL2/std.scad>
    line = [[-30,0],[30,30]];
    pt = [40,25];
    p2 = line_closest_point(line,pt,RAY);
    stroke(line, endcap2="arrow2");
    color("blue") translate(pt) circle(r=1,$fn=12);
    color("red") translate(p2) circle(r=1,$fn=12);

<br clear="all" /><br/>

**Example 5:** But with a segment we get a different result

<img align="left" alt="line\_closest\_point() Example 5" src="images/geometry/line_closest_point_5.png" width="320" height="240">

    include <BOSL2/std.scad>
    line = [[-30,0],[30,30]];
    pt = [40,25];
    p2 = line_closest_point(line,pt,SEGMENT);
    stroke(line);
    color("blue") translate(pt) circle(r=1,$fn=12);
    color("red") translate(p2) circle(r=1,$fn=12);

<br clear="all" /><br/>

**Example 6:** The shorthand RAY uses the first point as the base of the ray.  But you can specify a reversed ray directly, and in this case the result is the same as the result above for the segment.

<img align="left" alt="line\_closest\_point() Example 6" src="images/geometry/line_closest_point_6.png" width="320" height="240">

    include <BOSL2/std.scad>
    line = [[-30,0],[30,30]];
    pt = [40,25];
    p2 = line_closest_point(line,pt,[false,true]);
    stroke(line,endcap1="arrow2");
    color("blue") translate(pt) circle(r=1,$fn=12);
    color("red") translate(p2) circle(r=1,$fn=12);

<br clear="all" /><br/>

**Example 7:** A 3D example

<img align="left" alt="line\_closest\_point() Example 7" src="images/geometry/line_closest_point_7.png" width="320" height="240">

    include <BOSL2/std.scad>
    line = [[-30,-15,0],[30,15,30]];
    pt = [5,5,5];
    p2 = line_closest_point(line,pt);
    stroke(line, endcaps="arrow2");
    color("blue") translate(pt) sphere(r=1,$fn=12);
    color("red") translate(p2) sphere(r=1,$fn=12);

<br clear="all" /><br/>

---

### Function: line\_from\_points()

**Synopsis:** Given a list of collinear points, return the line they define.

**Topics:** [Geometry](Topics#geometry), [Lines](Topics#lines), [Points](Topics#points)

**Usage:** 

- line = line_from_points(points, [check_collinear], [eps]);

**Description:** 

Given a list of 2 or more collinear points, returns two points defining a line containing them.
If `check_collinear=true` a line is returned if the points are collinear; otherwise `undef` is returned.
if `check_collinear=false`, then the collinearity test is skipped and a best-fit line is returned (where "best fit"
means minimal perpendiclular point-line distances, not minimal vertical distances as one would get with least-squares fitting).

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`points`             | The list of points to find the line through.
`check_collinear`    | If true, don't verify that all points are collinear.  Default: false
`eps`                | How much variance is allowed in testing each point against the line.  Default: 1e-9

**Example 1:** A line fitted to a cloud of points.

<img align="left" alt="line\_from\_points() Example 1" src="images/geometry/line_from_points.png" width="320" height="240">

    include <BOSL2/std.scad>
    points = rot(45, v=[-0.5,1,0],
        p=random_points(100,3,scale=[5,5,50],seed=47));
    line = line_from_points(points);
    stroke(line, color="#06f");
    %move_copies(points) sphere(d=2, $fn=12);

<br clear="all" /><br/>

---

## Section: Planes


### Function: is\_coplanar()

**Synopsis:** Check if 3d points are coplanar and not collinear.

**Topics:** [Geometry](Topics#geometry), [Coplanarity](Topics#coplanarity)

**See Also:** [plane3pt()](#function-plane3pt), [plane3pt\_indexed()](#function-plane3pt_indexed), [plane\_from\_normal()](#function-plane_from_normal), [plane\_from\_points()](#function-plane_from_points), [plane\_from\_polygon()](#function-plane_from_polygon)

**Usage:** 

- bool = is_coplanar(points,[eps]);

**Description:** 

Returns true if the given 3D points are non-collinear and are on a plane.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`points`             | The points to test.
`eps`                | Tolerance in geometric comparisons.  Default: 1e-9

---

### Function: plane3pt()

**Synopsis:** Return a plane from 3 points.

**Topics:** [Geometry](Topics#geometry), [Planes](Topics#planes)

**See Also:** [plane3pt\_indexed()](#function-plane3pt_indexed), [plane\_from\_normal()](#function-plane_from_normal), [plane\_from\_points()](#function-plane_from_points), [plane\_from\_polygon()](#function-plane_from_polygon)

**Usage:** 

- plane = plane3pt(p1, p2, p3);
- plane = plane3pt([p1, p2, p3]);

**Description:** 

Generates the normalized cartesian equation of a plane from three 3d points.
Returns [A,B,C,D] where Ax + By + Cz = D is the equation of a plane.
Returns undef, if the points are collinear.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`p1`                 | The first point on the plane.
`p2`                 | The second point on the plane.
`p3`                 | The third point on the plane.

---

### Function: plane3pt\_indexed()

**Synopsis:** Given list of 3d points and 3 indices, return the plane they define.

**Topics:** [Geometry](Topics#geometry), [Planes](Topics#planes)

**See Also:** [plane3pt()](#function-plane3pt), [plane\_from\_normal()](#function-plane_from_normal), [plane\_from\_points()](#function-plane_from_points), [plane\_from\_polygon()](#function-plane_from_polygon)

**Usage:** 

- plane = plane3pt_indexed(points, i1, i2, i3);

**Description:** 

Given a list of 3d points, and the indices of three of those points,
generates the normalized cartesian equation of a plane that those points all
lie on. If the points are not collinear, returns [A,B,C,D] where Ax+By+Cz=D is the equation of a plane.
If they are collinear, returns [].

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`points`             | A list of points.
`i1`                 | The index into `points` of the first point on the plane.
`i2`                 | The index into `points` of the second point on the plane.
`i3`                 | The index into `points` of the third point on the plane.

---

### Function: plane\_from\_normal()

**Synopsis:** Return plane defined by normal vector and a point.

**Topics:** [Geometry](Topics#geometry), [Planes](Topics#planes)

**See Also:** [plane3pt()](#function-plane3pt), [plane3pt\_indexed()](#function-plane3pt_indexed), [plane\_from\_points()](#function-plane_from_points), [plane\_from\_polygon()](#function-plane_from_polygon)

**Usage:** 

- plane = plane_from_normal(normal, [pt])

**Description:** 

Returns a plane defined by a normal vector and a point.  If you omit `pt`, you get a plane
passing through the origin.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`normal`             | Normal vector to the plane to find.
`pt`                 | Point 3D on the plane to find.

**Example 1:** 

    include <BOSL2/std.scad>
    plane_from_normal([0,0,1], [2,2,2]);  // Returns the xy plane passing through the point (2,2,2)

<br clear="all" /><br/>

---

### Function: plane\_from\_points()

**Synopsis:** Return plane defined by a set of 3D points, with arbitrary normal direction.

**Topics:** [Geometry](Topics#geometry), [Planes](Topics#planes), [Points](Topics#points)

**See Also:** [plane3pt()](#function-plane3pt), [plane3pt\_indexed()](#function-plane3pt_indexed), [plane\_from\_normal()](#function-plane_from_normal), [plane\_from\_polygon()](#function-plane_from_polygon)

**Usage:** 

- plane = plane_from_points(points, [check_coplanar], [eps]);

**Description:** 

Given a list of 3 or more 3D points, returns the coefficients of the normalized cartesian equation of a plane,
that is [A,B,C,D] where Ax+By+Cz=D is the equation of the plane and norm([A,B,C])=1.

If `check_coplanar=true`, the plane is returned if the points are all coplanar; otherwise `undef` is returned if the points are collinear or not coplanar.
If `check_coplanar=false`, then the coplanarity check is skipped and a best-fit plane is returned (where "best fit"
means minimal perpendiclular point-plane distances, not minimal vertical distances as one would get with least-squares fitting).
The direction of the plane's normal is arbitrary and is not determined by the point order, unlike [`plane_from_polygon()`](#function-plane_from_polygon).

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`points`             | The list of points to find the best-fit plane.
`check_coplanar`     | If true, verify the point coplanarity within `eps` tolerance.  Default: false
`eps`                | Tolerance in geometric comparisons.  Default: 1e-9

**Example 1:** 100 non-coplanar random points (yellow spheres) distributed in a volume, showing the best-fit plane (transparent square) with its normal vector.

<img align="left" alt="plane\_from\_points() Example 1" src="images/geometry/plane_from_points.png" width="320" height="240">

    include <BOSL2/std.scad>
    points = rot(45, v=[-0.3,1,0],
        p=random_points(100,3,scale=[50,50,15],seed=47));
    plane = plane_from_points(points);
    move_copies(points) sphere(d=3, $fn=12);
    cp = mean(points);
    move(cp) rot(from=UP,to=plane_normal(plane)) {
        color("#06f") anchor_arrow(50, flag=false);
        %linear_extrude(0.1) square(100, center=true);
    }

<br clear="all" /><br/>

---

### Function: plane\_from\_polygon()

**Synopsis:** Given a 3d planar polygon, returns directed plane.

**Topics:** [Geometry](Topics#geometry), [Planes](Topics#planes), [Polygons](Topics#polygons)

**See Also:** [plane3pt()](#function-plane3pt), [plane3pt\_indexed()](#function-plane3pt_indexed), [plane\_from\_normal()](#function-plane_from_normal), [plane\_from\_points()](#function-plane_from_points)

**Usage:** 

- plane = plane_from_polygon(points, [check_coplanar], [eps]);

**Description:** 

Given a 3D planar polygon, returns the normalized cartesian equation of its plane.
Returns [A,B,C,D] where Ax+By+Cz=D is the equation of the plane where norm([A,B,C])=1.
If not all the points in the polygon are coplanar, then [] is returned.
If `check_coplanar=true` and the points in the list are collinear or not coplanar, then `undef` is returned.
if `check_coplanar=false`, then the coplanarity test is skipped and a plane passing through 3 non-collinear arbitrary points is returned.
The normal direction is determined by the order of the points and the right hand rule.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`poly`               | The planar 3D polygon to find the plane of.
`check_coplanar`     | If false, doesn't verify that all points in the polygon are coplanar.  Default: true
`eps`                | Tolerance in geometric comparisons.  Default: 1e-9

**Example 1:** 

<img align="left" alt="plane\_from\_polygon() Example 1" src="images/geometry/plane_from_polygon.png" width="320" height="240">

<br clear="all" />

    include <BOSL2/std.scad>
    xyzpath = rot(45, v=[0,1,0], p=path3d(star(n=5,step=2,d=100), 70));
    plane = plane_from_polygon(xyzpath);
    #stroke(xyzpath,closed=true,width=3);
    cp = centroid(xyzpath);
    move(cp) rot(from=UP,to=plane_normal(plane)) anchor_arrow(45);

---

### Function: plane\_normal()

**Synopsis:** Returns the normal vector to a plane.

**Topics:** [Geometry](Topics#geometry), [Planes](Topics#planes)

**See Also:** [plane3pt()](#function-plane3pt), [plane3pt\_indexed()](#function-plane3pt_indexed), [plane\_from\_normal()](#function-plane_from_normal), [plane\_from\_points()](#function-plane_from_points), [plane\_from\_polygon()](#function-plane_from_polygon), [plane\_offset()](#function-plane_offset)

**Usage:** 

- vec = plane_normal(plane);

**Description:** 

Returns the unit length normal vector for the given plane.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`plane`              | The `[A,B,C,D]` plane definition where `Ax+By+Cz=D` is the formula of the plane.

---

### Function: plane\_offset()

**Synopsis:** Returns the signed offset of the plane from the origin.

**Topics:** [Geometry](Topics#geometry), [Planes](Topics#planes)

**See Also:** [plane3pt()](#function-plane3pt), [plane3pt\_indexed()](#function-plane3pt_indexed), [plane\_from\_normal()](#function-plane_from_normal), [plane\_from\_points()](#function-plane_from_points), [plane\_from\_polygon()](#function-plane_from_polygon), [plane\_normal()](#function-plane_normal)

**Usage:** 

- d = plane_offset(plane);

**Description:** 

Returns coeficient D of the normalized plane equation `Ax+By+Cz=D`, or the scalar offset of the plane from the origin.
This value may be negative.
The absolute value of this coefficient is the distance of the plane from the origin.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`plane`              | The `[A,B,C,D]` plane definition where `Ax+By+Cz=D` is the formula of the plane.

---

### Function: plane\_line\_intersection()

**Synopsis:** Returns the intersection of a plane and 3d line, segment or ray.

**Topics:** [Geometry](Topics#geometry), [Planes](Topics#planes), [Lines](Topics#lines), [Intersection](Topics#intersection)

**See Also:** [plane3pt()](#function-plane3pt), [plane\_from\_normal()](#function-plane_from_normal), [plane\_from\_points()](#function-plane_from_points), [plane\_from\_polygon()](#function-plane_from_polygon), [line\_intersection()](#function-line_intersection)

**Usage:** 

- pt = plane_line_intersection(plane, line, [bounded], [eps]);

**Description:** 

Takes a line, and a plane [A,B,C,D] where the equation of that plane is `Ax+By+Cz=D`.
If `line` intersects `plane` at one point, then that intersection point is returned.
If `line` lies on `plane`, then the original given `line` is returned.
If `line` is parallel to, but not on `plane`, then undef is returned.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`plane`              | The [A,B,C,D] values for the equation of the plane.
`line`               | A list of two distinct 3D points that are on the line.
`bounded`            | If false, the line is considered unbounded.  If true, it is treated as a bounded line segment.  If given as `[true, false]` or `[false, true]`, the boundedness of the points are specified individually, allowing the line to be treated as a half-bounded ray.  Default: false (unbounded)
`eps`                | Tolerance in geometric comparisons.  Default: 1e-9

---

### Function: plane\_intersection()

**Synopsis:** Returns the intersection of two or three planes.

**Topics:** [Geometry](Topics#geometry), [Planes](Topics#planes), [Intersection](Topics#intersection)

**See Also:** [plane3pt()](#function-plane3pt), [plane\_from\_normal()](#function-plane_from_normal), [plane\_from\_points()](#function-plane_from_points), [plane\_from\_polygon()](#function-plane_from_polygon), [line\_intersection()](#function-line_intersection)

**Usage:** 

- line = plane_intersection(plane1, plane2)
- pt = plane_intersection(plane1, plane2, plane3)

**Description:** 

Compute the point that is the intersection of the three planes, or the line intersection of two planes.
If you give three planes the intersection is returned as a point.  If you give two planes the intersection
is returned as a list of two points on the line of intersection.  If any two input planes are parallel
or coincident then returns undef.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`plane1`             | The [A,B,C,D] coefficients for the first plane equation `Ax+By+Cz=D`.
`plane2`             | The [A,B,C,D] coefficients for the second plane equation `Ax+By+Cz=D`.
`plane3`             | The [A,B,C,D] coefficients for the third plane equation `Ax+By+Cz=D`.

---

### Function: plane\_line\_angle()

**Synopsis:** Returns the angle between a plane and a 3d line.

**Topics:** [Geometry](Topics#geometry), [Planes](Topics#planes), [Lines](Topics#lines), [Angle](Topics#angle)

**See Also:** [plane3pt()](#function-plane3pt), [plane\_from\_normal()](#function-plane_from_normal), [plane\_from\_points()](#function-plane_from_points), [plane\_from\_polygon()](#function-plane_from_polygon), [plane\_intersection()](#function-plane_intersection), [line\_intersection()](#function-line_intersection), [vector\_angle()](vectors.scad#function-vector_angle)

**Usage:** 

- angle = plane_line_angle(plane,line);

**Description:** 

Compute the angle between a plane [A, B, C, D] and a 3d line, specified as a pair of 3d points [p1,p2].
The resulting angle is signed, with the sign positive if the vector p2-p1 lies above the plane, on
the same side of the plane as the plane's normal vector.

---

### Function: plane\_closest\_point()

**Synopsis:** Returns the orthogonal projection of points onto a plane.

**Topics:** [Geometry](Topics#geometry), [Planes](Topics#planes), [Projection](Topics#projection)

**See Also:** [plane3pt()](#function-plane3pt), [line\_closest\_point()](#function-line_closest_point), [point\_plane\_distance()](#function-point_plane_distance)

**Usage:** 

- pts = plane_closest_point(plane, points);

**Description:** 

Given a plane definition `[A,B,C,D]`, where `Ax+By+Cz=D`, and a list of 2d or
3d points, return the closest 3D orthogonal projection of the points on the plane.
In other words, for every point given, returns the closest point to it on the plane.
If points is a single point then returns a single point result.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`plane`              | The `[A,B,C,D]` plane definition where `Ax+By+Cz=D` is the formula of the plane.
`points`             | List of points to project

**Example 1:** 

<img align="left" alt="plane\_closest\_point() Example 1" src="images/geometry/plane_closest_point.png" width="320" height="240">

<br clear="all" />

    include <BOSL2/std.scad>
    points = move([10,20,30], p=yrot(25, p=path3d(circle(d=100, $fn=36))));
    plane = plane_from_normal([1,0,1]);
    proj = plane_closest_point(plane,points);
    color("red") move_copies(points) sphere(d=4,$fn=12);
    color("blue") move_copies(proj) sphere(d=4,$fn=12);
    move(centroid(proj)) {
        rot(from=UP,to=plane_normal(plane)) {
            anchor_arrow(50);
            %cube([120,150,0.1],center=true);
        }
    }

---

### Function: point\_plane\_distance()

**Synopsis:** Determine distance between a point and plane.

**Topics:** [Geometry](Topics#geometry), [Planes](Topics#planes), [Distance](Topics#distance)

**See Also:** [plane3pt()](#function-plane3pt), [line\_closest\_point()](#function-line_closest_point), [plane\_closest\_point()](#function-plane_closest_point)

**Usage:** 

- dist = point_plane_distance(plane, point)

**Description:** 

Given a plane as [A,B,C,D] where the cartesian equation for that plane
is Ax+By+Cz=D, determines how far from that plane the given point is.
The returned distance is positive if the point is above the
plane, meaning on the side where the plane normal points.
If the point is below the plane, then the distance returned
is negative.  The normal of the plane is [A,B,C].

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`plane`              | The `[A,B,C,D]` plane definition where `Ax+By+Cz=D` is the formula of the plane.
`point`              | The distance evaluation point.

---

### Function: are\_points\_on\_plane()

**Synopsis:** Determine if all of the listed points are on a plane.

**Topics:** [Geometry](Topics#geometry), [Planes](Topics#planes), [Points](Topics#points)

**See Also:** [plane3pt()](#function-plane3pt), [line\_closest\_point()](#function-line_closest_point), [plane\_closest\_point()](#function-plane_closest_point), [is\_coplanar()](#function-is_coplanar)

**Usage:** 

- bool = are_points_on_plane(points, plane, [eps]);

**Description:** 

Returns true if the given 3D points are on the given plane.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`plane`              | The plane to test the points on.
`points`             | The list of 3D points to test.
`eps`                | Tolerance in geometric comparisons.  Default: 1e-9

---

### Module: show\_plane()

**Synopsis:** Display (part of) a plane <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>

**Topics:** [Planes](Topics#planes), [Debugging](Topics#debugging)

**Usage:** 

- show_plane(plane, size, [offset]) [ATTACHMENTS];

**Description:** 

Display a rectangular portion of the specified plane for debugging or visualization purposes.
The size parameter specifies the size of the plane when projected along the coordinate axis that is closest to
the plane's normal vector.  The offset parameter shifts the plane location perpendicular to the normal vector.
This object is a non-manifold VNF (it has edges) so it will not render.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`plane`              | Plane to display
`size`               | scalar or 2-vector size parameter
`offset`             | scalar of 2-vector offset

**Example 1:** 

<img align="left" alt="show\_plane() Example 1" src="images/geometry/show_plane.png" width="320" height="240">

    include <BOSL2/std.scad>
    sphere(r=15,$fn=48);
    plane = plane_from_normal([2,-3,9],[4,-5,12]);
    %show_plane(plane, [35,25], [4,-7]);

<br clear="all" /><br/>

---

## Section: Circle Calculations


### Function: circle\_line\_intersection()

**Synopsis:** Find the intersection points between a 2d circle and a line, ray or segment.

**Topics:** [Geometry](Topics#geometry), [Circles](Topics#circles), [Lines](Topics#lines), [Intersection](Topics#intersection)

**See Also:** [circle\_circle\_intersection()](#function-circle_circle_intersection), [circle\_2tangents()](#function-circle_2tangents), [circle\_3points()](#function-circle_3points), [circle\_point\_tangents()](#function-circle_point_tangents), [circle\_circle\_tangents()](#function-circle_circle_tangents)

**Usage:** 

- pts = circle_line_intersection(r|d=, cp, line, [bounded], [eps=]);

**Description:** 

Find intersection points between a 2D circle and a line, ray or segment specified by two points.
By default the line is unbounded.  Returns the list of zero or more intersection points.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`r`                  | Radius of circle
`cp`                 | Center of circle
`line`               | Two points defining the line
`bounded`            | False for unbounded line, true for a segment, or a vector [false,true] or [true,false] to specify a ray with the first or second end unbounded.  Default: false

<abbr title="These args must be used by name, ie: name=value">By&nbsp;Name</abbr> | What it does
-------------------- | ------------
`d`                  | Diameter of circle
`eps`                | Epsilon used for identifying the case with one solution.  Default: `1e-9`

**Example 1:** Standard intersection returns two points.

<img align="left" alt="circle\_line\_intersection() Example 1" src="images/geometry/circle_line_intersection.png" width="320" height="240">

    include <BOSL2/std.scad>
    line = [[-15,2], [15,7]];
    cp = [1,2]; r = 10;
    translate(cp) circle(r=r);
    color("black") stroke(line, endcaps="arrow2", width=0.5);
    isects = circle_line_intersection(r=r, cp=cp, line=line);
    color("red") move_copies(isects) circle(d=1);

<br clear="all" /><br/>

**Example 2:** Tangent intersection returns one point.

<img align="left" alt="circle\_line\_intersection() Example 2" src="images/geometry/circle_line_intersection_2.png" width="320" height="240">

    include <BOSL2/std.scad>
    line = [[-10,12], [10,12]];
    cp = [1,2]; r = 10;
    translate(cp) circle(r=r);
    color("black") stroke(line, endcaps="arrow2", width=0.5);
    isects = circle_line_intersection(r=r, cp=cp, line=line);
    color("#f44") move_copies(isects) circle(d=1);

<br clear="all" /><br/>

**Example 3:** A bounded ray might intersect only in one direction.

<img align="left" alt="circle\_line\_intersection() Example 3" src="images/geometry/circle_line_intersection_3.png" width="320" height="240">

<br clear="all" />

    include <BOSL2/std.scad>
    line = [[-5,2], [5,7]];
    extended = [line[0], line[0]+22*unit(line[1]-line[0])];
    cp = [1,2]; r = 10;
    translate(cp) circle(r=r);
    color("gray") dashed_stroke(extended, width=0.2);
    color("black") stroke(line, endcap2="arrow2", width=0.5);
    isects = circle_line_intersection(r=r, cp=cp, line=line, bounded=[true,false]);
    color("#f44") move_copies(isects) circle(d=1);

**Example 4:** If they don't intersect at all, then an empty list is returned.

<img align="left" alt="circle\_line\_intersection() Example 4" src="images/geometry/circle_line_intersection_4.png" width="320" height="240">

    include <BOSL2/std.scad>
    line = [[-12,12], [12,8]];
    cp = [-5,-2]; r = 10;
    translate(cp) circle(r=r);
    color("black") stroke(line, endcaps="arrow2", width=0.5);
    isects = circle_line_intersection(r=r, cp=cp, line=line);
    color("#f44") move_copies(isects) circle(d=1);

<br clear="all" /><br/>

---

### Function: circle\_circle\_intersection()

**Synopsis:** Find the intersection points of two 2d circles.

**Topics:** [Geometry](Topics#geometry), [Circles](Topics#circles)

**See Also:** [circle\_line\_intersection()](#function-circle_line_intersection), [circle\_2tangents()](#function-circle_2tangents), [circle\_3points()](#function-circle_3points), [circle\_point\_tangents()](#function-circle_point_tangents), [circle\_circle\_tangents()](#function-circle_circle_tangents)

**Usage:** 

- pts = circle_circle_intersection(r1|d1=, cp1, r2|d2=, cp2, [eps]);

**Description:** 

Compute the intersection points of two circles.  Returns a list of the intersection points, which
contains two points in the general case, one point for tangent circles, or returns an empty list
if the circles do not intersect.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`r1`                 | Radius of the first circle.
`cp1`                | Centerpoint of the first circle.
`r2`                 | Radius of the second circle.
`cp2`                | Centerpoint of the second circle.
`eps`                | Tolerance for detecting tangent circles.  Default: 1e-9

<abbr title="These args must be used by name, ie: name=value">By&nbsp;Name</abbr> | What it does
-------------------- | ------------
`d1`                 | Diameter of the first circle.
`d2`                 | Diameter of the second circle.

**Example 1:** Circles intersect in two points.

<img align="left" alt="circle\_circle\_intersection() Example 1" src="images/geometry/circle_circle_intersection.png" width="320" height="240">

    include <BOSL2/std.scad>
    $fn=32;
    cp1 = [4,4];  r1 = 3;
    cp2 = [7,7];  r2 = 2;
    pts = circle_circle_intersection(r1, cp1, r2, cp2);
    move(cp1) stroke(circle(r=r1), width=0.2, closed=true);
    move(cp2) stroke(circle(r=r2), width=0.2, closed=true);
    color("red") move_copies(pts) circle(r=.3);

<br clear="all" /><br/>

**Example 2:** Circles are tangent, so one intersection point:

<img align="left" alt="circle\_circle\_intersection() Example 2" src="images/geometry/circle_circle_intersection_2.png" width="320" height="240">

    include <BOSL2/std.scad>
    $fn=32;
    cp1 = [4,4];  r1 = 4;
    cp2 = [4,10]; r2 = 2;
    pts = circle_circle_intersection(r1, cp1, r2, cp2);
    move(cp1) stroke(circle(r=r1), width=0.2, closed=true);
    move(cp2) stroke(circle(r=r2), width=0.2, closed=true);
    color("red") move_copies(pts) circle(r=.3);

<br clear="all" /><br/>

**Example 3:** Another tangent example:

<img align="left" alt="circle\_circle\_intersection() Example 3" src="images/geometry/circle_circle_intersection_3.png" width="320" height="240">

    include <BOSL2/std.scad>
    $fn=32;
    cp1 = [4,4];  r1 = 4;
    cp2 = [5,5];  r2 = 4-sqrt(2);
    pts = circle_circle_intersection(r1, cp1, r2, cp2);
    move(cp1) stroke(circle(r=r1), width=0.2, closed=true);
    move(cp2) stroke(circle(r=r2), width=0.2, closed=true);
    color("red") move_copies(pts) circle(r=.3);

<br clear="all" /><br/>

**Example 4:** Circles do not intersect.  Returns empty list.

<img align="left" alt="circle\_circle\_intersection() Example 4" src="images/geometry/circle_circle_intersection_4.png" width="320" height="240">

    include <BOSL2/std.scad>
    $fn=32;
    cp1 = [3,4];  r1 = 2;
    cp2 = [7,10]; r2 = 3;
    pts = circle_circle_intersection(r1, cp1, r2, cp2);
    move(cp1) stroke(circle(r=r1), width=0.2, closed=true);
    move(cp2) stroke(circle(r=r2), width=0.2, closed=true);
    color("red") move_copies(pts) circle(r=.3);

<br clear="all" /><br/>

---

### Function: circle\_2tangents()

**Synopsis:** Given two 2d or 3d rays, find a circle tangent to both.

**Topics:** [Geometry](Topics#geometry), [Circles](Topics#circles), [Tangents](Topics#tangents)

**See Also:** [circle\_line\_intersection()](#function-circle_line_intersection), [circle\_circle\_intersection()](#function-circle_circle_intersection), [circle\_3points()](#function-circle_3points), [circle\_point\_tangents()](#function-circle_point_tangents), [circle\_circle\_tangents()](#function-circle_circle_tangents)

**Usage:** 

- circ = circle_2tangents(r|d=, pt1, pt2, pt3, [tangents=]);
- circ = circle_2tangents(r|d=, [PT1, PT2, PT3], [tangents=]);

**Description:** 

Given a pair of 2d or 3d rays with a common origin, and a known circle radius/diameter, finds
the centerpoint for the circle of that size that touches both rays tangentally.
Both rays start at `pt2`, one passing through `pt1`, and the other through `pt3`.

When called with collinear rays, returns `undef`.
Otherwise, when called with `tangents=false`, returns `[CP,NORMAL]`.
Otherwise, when called with `tangents=true`, returns `[CP,NORMAL,TANPT1,TANPT2]`.
- CP is the centerpoint of the circle.
- NORMAL is the normal vector of the plane that the circle is on (UP or DOWN if the points are 2D).
- TANPT1 is the point where the circle is tangent to the ray `[pt2,pt1]`.
- TANPT2 is the point where the circle is tangent to the ray `[pt2,pt3]`.

**Figure 3.3.1:** 

<img align="left" alt="circle\_2tangents() Figure 3.3.1" src="images/geometry/figure_3_3_1.png" width="480" height="360">

<br clear="all" />

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`r`                  | The radius of the circle to find.
`pt1`                | A point that the first ray passes though.
`pt2`                | The starting point of both rays.
`pt3`                | A point that the second ray passes though.

<abbr title="These args must be used by name, ie: name=value">By&nbsp;Name</abbr> | What it does
-------------------- | ------------
`d`                  | The diameter of the circle to find.
`tangents`           | If true, extended information about the tangent points is calculated and returned.  Default: false

**Example 1:** 

<img align="left" alt="circle\_2tangents() Example 1" src="images/geometry/circle_2tangents.png" width="320" height="240">

<br clear="all" />

    include <BOSL2/std.scad>
    pts = [[40,40], [10,10], [55,5]];  rad = 10;
    circ = circle_2tangents(r=rad, pt1=pts[0], pt2=pts[1], pt3=pts[2]);
    stroke(pts, endcaps="arrow2");
    color("red") move(circ[0]) circle(r=rad);

**Example 2:** 

<img align="left" alt="circle\_2tangents() Example 2" src="images/geometry/circle_2tangents_2.png" width="320" height="240">

<br clear="all" />

    include <BOSL2/std.scad>
    pts = [[20,40], [10,10], [55,20]];  rad = 10;
    circ = circle_2tangents(r=rad, pt1=pts[0], pt2=pts[1], pt3=pts[2], tangents=true);
    stroke(pts, endcaps="arrow2");
    color("red") move(circ[0]) circle(r=rad);
    color("blue") move_copies(select(circ,2,3)) circle(d=2);

**Example 3:** Fit into 3D path corner.

<img align="left" alt="circle\_2tangents() Example 3" src="images/geometry/circle_2tangents_3.png" width="320" height="240">

    include <BOSL2/std.scad>
    pts = [[45,5,10], [10,10,15], [30,40,30]];  rad = 10;
    circ = circle_2tangents(rad, [pts[0], pts[1], pts[2]]);
    stroke(pts, endcaps="arrow2");
    color("red") move(circ[0]) cyl(h=10, r=rad, orient=circ[1]);

<br clear="all" /><br/>

**Example 4:** 

<img align="left" alt="circle\_2tangents() Example 4" src="images/geometry/circle_2tangents_4.png" width="320" height="240">

    include <BOSL2/std.scad>
    path = yrot(20, p=path3d(star(d=100, n=5, step=2)));
    stroke(path, closed=true);
    for (i = [0:1:5]) {
        crn = select(path, i*2-1, i*2+1);
        ci = circle_2tangents(5, crn[0], crn[1], crn[2]);
        move(ci[0]) cyl(h=10,r=5,orient=ci[1]);
    }

<br clear="all" /><br/>

---

### Function: circle\_3points()

**Synopsis:** Find a circle passing through three 2d or 3d points.

**Topics:** [Geometry](Topics#geometry), [Circles](Topics#circles)

**See Also:** [circle\_line\_intersection()](#function-circle_line_intersection), [circle\_circle\_intersection()](#function-circle_circle_intersection), [circle\_2tangents()](#function-circle_2tangents), [circle\_point\_tangents()](#function-circle_point_tangents), [circle\_circle\_tangents()](#function-circle_circle_tangents)

**Usage:** 

- circ = circle_3points(pt1, pt2, pt3);
- circ = circle_3points([PT1, PT2, PT3]);

**Description:** 

Returns the [CENTERPOINT, RADIUS, NORMAL] of the circle that passes through three non-collinear
points where NORMAL is the normal vector of the plane that the circle is on (UP or DOWN if the points are 2D).
The centerpoint is a 2D or 3D vector, depending on the points input.  If all three
points are 2D, then the resulting centerpoint will be 2D, and the normal is UP ([0,0,1]).
If any of the points are 3D, then the resulting centerpoint will be 3D.  If the three points are
collinear, then `[undef,undef,undef]` is returned.  The normal is a normalized 3D
vector with a non-negative Z axis.  Instead of 3 arguments, it is acceptable to input the 3 points
as a list given in `pt1`, leaving `pt2`and `pt3` as undef.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`pt1`                | The first point.
`pt2`                | The second point.
`pt3`                | The third point.

**Example 1:** 

<img align="left" alt="circle\_3points() Example 1" src="images/geometry/circle_3points.png" width="320" height="240">

<br clear="all" />

    include <BOSL2/std.scad>
    pts = [[60,40], [10,10], [65,5]];
    circ = circle_3points(pts[0], pts[1], pts[2]);
    translate(circ[0]) color("green") stroke(circle(r=circ[1]),closed=true,$fn=72);
    translate(circ[0]) color("red") circle(d=3, $fn=12);
    move_copies(pts) color("blue") circle(d=3, $fn=12);

---

### Function: circle\_point\_tangents()

**Synopsis:** Given a circle and point, find tangents to circle passing through the point.

**Topics:** [Geometry](Topics#geometry), [Circles](Topics#circles), [Tangents](Topics#tangents)

**See Also:** [circle\_line\_intersection()](#function-circle_line_intersection), [circle\_circle\_intersection()](#function-circle_circle_intersection), [circle\_2tangents()](#function-circle_2tangents), [circle\_3points()](#function-circle_3points), [circle\_circle\_tangents()](#function-circle_circle_tangents)

**Usage:** 

- tangents = circle_point_tangents(r|d=, cp, pt);

**Description:** 

Given a 2d circle and a 2d point outside that circle, finds the 2d tangent point(s) on the circle for a
line passing through the point.  Returns a list of zero or more 2D tangent points.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`r`                  | Radius of the circle.
`cp`                 | The coordinates of the 2d circle centerpoint.
`pt`                 | The coordinates of the 2d external point.

<abbr title="These args must be used by name, ie: name=value">By&nbsp;Name</abbr> | What it does
-------------------- | ------------
`d`                  | Diameter of the circle.

**Example 1:** 

<img align="left" alt="circle\_point\_tangents() Example 1" src="images/geometry/circle_point_tangents.png" width="320" height="240">

<br clear="all" />

    include <BOSL2/std.scad>
    cp = [-10,-10];  r = 30;  pt = [30,10];
    tanpts = circle_point_tangents(r=r, cp=cp, pt=pt);
    color("yellow") translate(cp) circle(r=r);
    color("cyan") for(tp=tanpts) {stroke([tp,pt]); stroke([tp,cp]);}
    color("red") move_copies(tanpts) circle(d=3,$fn=12);
    color("blue") move_copies([cp,pt]) circle(d=3,$fn=12);

---

### Function: circle\_circle\_tangents()

**Synopsis:** Find tangents to a pair of circles in 2d.

**Topics:** [Geometry](Topics#geometry), [Circles](Topics#circles), [Tangents](Topics#tangents)

**See Also:** [circle\_line\_intersection()](#function-circle_line_intersection), [circle\_circle\_intersection()](#function-circle_circle_intersection), [circle\_2tangents()](#function-circle_2tangents), [circle\_3points()](#function-circle_3points), [circle\_point\_tangents()](#function-circle_point_tangents)

**Usage:** 

- segs = circle_circle_tangents(r1|d1=, cp1, r2|d2=, cp2);

**Description:** 

Computes 2d lines tangents to a pair of circles in 2d.  Returns a list of line endpoints [p1,p2] where
p1 is the tangent point on circle 1 and p2 is the tangent point on circle 2.
If four tangents exist then the first one is the left hand exterior tangent as regarded looking from
circle 1 toward circle 2.  The second value is the right hand exterior tangent.  The third entry
gives the interior tangent that starts on the left of circle 1 and crosses to the right side of
circle 2.  And the fourth entry is the last interior tangent that starts on the right side of
circle 1.  If the circles intersect then the interior tangents don't exist and the function
returns only two entries.  If one circle is inside the other one then no tangents exist
so the function returns the empty set.  When the circles are tangent a degenerate tangent line
passes through the point of tangency of the two circles:  this degenerate line is NOT returned.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`r1`                 | Radius of the first circle.
`cp1`                | Centerpoint of the first circle.
`r2`                 | Radius of the second circle.
`cp2`                | Centerpoint of the second circle.

<abbr title="These args must be used by name, ie: name=value">By&nbsp;Name</abbr> | What it does
-------------------- | ------------
`d1`                 | Diameter of the first circle.
`d2`                 | Diameter of the second circle.

**Example 1:** Four tangents, first in green, second in black, third in blue, last in red.

<img align="left" alt="circle\_circle\_tangents() Example 1" src="images/geometry/circle_circle_tangents.png" width="320" height="240">

<br clear="all" />

    include <BOSL2/std.scad>
    $fn=32;
    cp1 = [3,4];  r1 = 2;
    cp2 = [7,10]; r2 = 3;
    pts = circle_circle_tangents(r1, cp1, r2, cp2);
    move(cp1) stroke(circle(r=r1), width=0.2, closed=true);
    move(cp2) stroke(circle(r=r2), width=0.2, closed=true);
    colors = ["green","black","blue","red"];
    for(i=[0:len(pts)-1]) color(colors[i]) stroke(pts[i],width=0.2);

**Example 2:** Circles overlap so only exterior tangents exist.

<img align="left" alt="circle\_circle\_tangents() Example 2" src="images/geometry/circle_circle_tangents_2.png" width="320" height="240">

<br clear="all" />

    include <BOSL2/std.scad>
    $fn=32;
    cp1 = [4,4];  r1 = 3;
    cp2 = [7,7];  r2 = 2;
    pts = circle_circle_tangents(r1, cp1, r2, cp2);
    move(cp1) stroke(circle(r=r1), width=0.2, closed=true);
    move(cp2) stroke(circle(r=r2), width=0.2, closed=true);
    colors = ["green","black","blue","red"];
    for(i=[0:len(pts)-1]) color(colors[i]) stroke(pts[i],width=0.2);

**Example 3:** Circles are tangent.  Only exterior tangents are returned.  The degenerate internal tangent is not returned.

<img align="left" alt="circle\_circle\_tangents() Example 3" src="images/geometry/circle_circle_tangents_3.png" width="320" height="240">

<br clear="all" />

    include <BOSL2/std.scad>
    $fn=32;
    cp1 = [4,4];  r1 = 4;
    cp2 = [4,10]; r2 = 2;
    pts = circle_circle_tangents(r1, cp1, r2, cp2);
    move(cp1) stroke(circle(r=r1), width=0.2, closed=true);
    move(cp2) stroke(circle(r=r2), width=0.2, closed=true);
    colors = ["green","black","blue","red"];
    for(i=[0:1:len(pts)-1]) color(colors[i]) stroke(pts[i],width=0.2);

**Example 4:** One circle is inside the other: no tangents exist.  If the interior circle is tangent the single degenerate tangent is not returned.

<img align="left" alt="circle\_circle\_tangents() Example 4" src="images/geometry/circle_circle_tangents_4.png" width="320" height="240">

    include <BOSL2/std.scad>
    $fn=32;
    cp1 = [4,4];  r1 = 4;
    cp2 = [5,5];  r2 = 2;
    pts = circle_circle_tangents(r1, cp1, r2, cp2);
    move(cp1) stroke(circle(r=r1), width=0.2, closed=true);
    move(cp2) stroke(circle(r=r2), width=0.2, closed=true);
    echo(pts);   // Returns []

<br clear="all" /><br/>

---

## Section: Sphere Calculations


### Function: sphere\_line\_intersection()

**Synopsis:** Find intersection between a sphere and line, ray or segment.

**Topics:** [Geometry](Topics#geometry), [Spheres](Topics#spheres), [Lines](Topics#lines), [Intersection](Topics#intersection)

**See Also:** [circle\_line\_intersection()](#function-circle_line_intersection), [circle\_circle\_intersection()](#function-circle_circle_intersection), [circle\_2tangents()](#function-circle_2tangents), [circle\_3points()](#function-circle_3points), [circle\_point\_tangents()](#function-circle_point_tangents), [circle\_circle\_tangents()](#function-circle_circle_tangents)

**Usage:** 

- isect = sphere_line_intersection(r|d=, cp, line, [bounded], [eps=]);

**Description:** 

Find intersection points between a sphere and a line, ray or segment specified by two points.
By default the line is unbounded.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`r`                  | Radius of sphere
`cp`                 | Centerpoint of sphere
`line`               | Two points defining the line
`bounded`            | false for unbounded line, true for a segment, or a vector [false,true] or [true,false] to specify a ray with the first or second end unbounded.  Default: false

<abbr title="These args must be used by name, ie: name=value">By&nbsp;Name</abbr> | What it does
-------------------- | ------------
`d`                  | diameter of sphere
`eps`                | epsilon used for identifying the case with one solution.  Default: 1e-9

**Example 1:** 

<img align="left" alt="sphere\_line\_intersection() Example 1" src="images/geometry/sphere_line_intersection.png" width="320" height="240">

    include <BOSL2/std.scad>
    cp = [10,20,5];  r = 40;
    line = [[-50,-10,25], [70,0,40]];
    isects = sphere_line_intersection(r=r, cp=cp, line=line);
    color("cyan") stroke(line);
    move(cp) sphere(r=r, $fn=72);
    color("red") move_copies(isects) sphere(d=3, $fn=12);

<br clear="all" /><br/>

---

## Section: Polygons


### Function: polygon\_area()

**Synopsis:** Calculate area of a 2d or 3d polygon.

**Topics:** [Geometry](Topics#geometry), [Polygons](Topics#polygons), [Area](Topics#area)

**See Also:** [centroid()](#function-centroid), [polygon\_normal()](#function-polygon_normal), [point\_in\_polygon()](#function-point_in_polygon), [polygon\_line\_intersection()](#function-polygon_line_intersection)

**Usage:** 

- area = polygon_area(poly, [signed]);

**Description:** 

Given a 2D or 3D simple planar polygon, returns the area of that polygon.
If the polygon is non-planar the result is `undef.`  If the polygon is self-intersecting
then the returned area is a meaningless number.
When `signed` is true and the polygon is 2d, a signed area is returned: a positive area indicates a counter-clockwise polygon.
The area of 3d polygons is always nonnegative.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`poly`               | Polygon to compute the area of.
`signed`             | If true, a signed area is returned. Default: false.

---

### Function: centroid()

**Synopsis:** Compute centroid of a 2d or 3d polygon or a VNF.

**Topics:** [Geometry](Topics#geometry), [Polygons](Topics#polygons), [Centroid](Topics#centroid)

**See Also:** [polygon\_area()](#function-polygon_area), [polygon\_normal()](#function-polygon_normal), [point\_in\_polygon()](#function-point_in_polygon), [polygon\_line\_intersection()](#function-polygon_line_intersection)

**Usage:** 

- c = centroid(object, [eps]);

**Description:** 

Given a simple 2D polygon, returns the 2D coordinates of the polygon's centroid.
Given a simple 3D planar polygon, returns the 3D coordinates of the polygon's centroid.
Providing a non-planar or collinear polygon results in an error.  For self-intersecting
polygons you may get an error or you may get meaningless results.

Given a [region](regions.scad), returns the 2D coordinates of the region's centroid.

Given a manifold [VNF](vnf.scad) then returns the 3D centroid of the polyhedron.  The VNF must
describe a valid polyhedron with consistent face direction and no holes in the mesh; otherwise
the results are undefined.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`object`             | object to compute the centroid of
`eps`                | epsilon value for identifying degenerate cases

**Example 1:** 

<img align="left" alt="centroid() Example 1" src="images/geometry/centroid.png" width="320" height="240">

    include <BOSL2/std.scad>
    path = [
        [-10,10], [-5,15], [15,15], [20,0],
        [15,-5], [25,-20], [25,-27], [15,-20],
        [0,-30], [-15,-25], [-5,-5]
    ];
    linear_extrude(height=0.01) polygon(path);
    cp = centroid(path);
    color("red") move(cp) sphere(d=2);

<br clear="all" /><br/>

---

### Function: polygon\_normal()

**Synopsis:** Return normal to a polygon.

**Topics:** [Geometry](Topics#geometry), [Polygons](Topics#polygons)

**See Also:** [polygon\_area()](#function-polygon_area), [centroid()](#function-centroid), [point\_in\_polygon()](#function-point_in_polygon), [polygon\_line\_intersection()](#function-polygon_line_intersection)

**Usage:** 

- vec = polygon_normal(poly);

**Description:** 

Given a 3D simple planar polygon, returns a unit normal vector for the polygon.  The vector
is oriented so that if the normal points toward the viewer, the polygon winds in the clockwise
direction.  If the polygon has zero area, returns `undef`.  If the polygon is self-intersecting
the the result is undefined.  It doesn't check for coplanarity.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`poly`               | The list of 3D path points for the perimeter of the polygon.

**Example 1:** 

<img align="left" alt="polygon\_normal() Example 1" src="images/geometry/polygon_normal.png" width="320" height="240">

    include <BOSL2/std.scad>
    path = rot([0,30,15], p=path3d(star(n=5, d=100, step=2)));
    stroke(path, closed=true);
    n = polygon_normal(path);
    rot(from=UP, to=n)
        color("red")
            stroke([[0,0,0], [0,0,20]], endcap2="arrow2");

<br clear="all" /><br/>

---

### Function: point\_in\_polygon()

**Synopsis:** Checks if a 2d point is inside or on the boundary of a 2d polygon.

**Topics:** [Geometry](Topics#geometry), [Polygons](Topics#polygons)

**See Also:** [polygon\_area()](#function-polygon_area), [centroid()](#function-centroid), [polygon\_normal()](#function-polygon_normal), [polygon\_line\_intersection()](#function-polygon_line_intersection)

**Usage:** 

- bool = point_in_polygon(point, poly, [nonzero], [eps])

**Description:** 

This function tests whether the given 2D point is inside, outside or on the boundary of
the specified 2D polygon.
The polygon is given as a list of 2D points, not including the repeated end point.
Returns -1 if the point is outside the polygon.
Returns 0 if the point is on the boundary.
Returns 1 if the point lies in the interior.
The polygon does not need to be simple: it may have self-intersections.
But the polygon cannot have holes (it must be simply connected).
Rounding errors may give mixed results for points on or near the boundary.

When polygons intersect themselves different definitions exist for determining which points
are inside the polygon.  The figure below shows the difference.
OpenSCAD uses the Even-Odd rule when creating polygons, where membership in overlapping regions
depends on how many times they overlap.  The Nonzero rule considers point inside the polygon if
the polygon overlaps them any number of times.  For more information see
https://en.wikipedia.org/wiki/Nonzero-rule and https://en.wikipedia.org/wiki/Even–odd_rule.

**Figure 5.4.1:** 

<img align="left" alt="point\_in\_polygon() Figure 5.4.1" src="images/geometry/figure_5_4_1.png" width="480" height="360">

<br clear="all" />

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`point`              | The 2D point to check
`poly`               | The list of 2D points forming the perimeter of the polygon.
`nonzero`            | The rule to use: true for "Nonzero" rule and false for "Even-Odd". Default: false (Even-Odd)
`eps`                | Tolerance in geometric comparisons.  Default: 1e-9

**Example 1:** With nonzero set to false (the default), we get this result. Green dots are inside the polygon and red are outside:

<img align="left" alt="point\_in\_polygon() Example 1" src="images/geometry/point_in_polygon.png" width="320" height="240">

<br clear="all" />

    include <BOSL2/std.scad>
    a=20*2/3;
    b=30*2/3;
    ofs = 17*2/3;
    curve = [for(theta=[0:10:140])  [a * theta/360*2*PI - b*sin(theta), a-b*cos(theta)]];
    path = deduplicate(concat( reverse(offset(curve,r=ofs,closed=false)),
                   xflip(offset(curve,r=ofs,closed=false)),
                   xflip(reverse(curve)),
                   curve
                 ));
    stroke(path,closed=true);
    pts = [[0,0],[10,0],[0,20]];
    for(p=pts){
      color(point_in_polygon(p,path)==1 ? "green" : "red")
      move(p)circle(r=1.5, $fn=12);
    }

**Example 2:** With nonzero set to true, one dot changes color:

<img align="left" alt="point\_in\_polygon() Example 2" src="images/geometry/point_in_polygon_2.png" width="320" height="240">

<br clear="all" />

    include <BOSL2/std.scad>
    a=20*2/3;
    b=30*2/3;
    ofs = 17*2/3;
    curve = [for(theta=[0:10:140])  [a * theta/360*2*PI - b*sin(theta), a-b*cos(theta)]];
    path = deduplicate(concat( reverse(offset(curve,r=ofs,closed=false)),
                   xflip(offset(curve,r=ofs,closed=false)),
                   xflip(reverse(curve)),
                   curve
                 ));
    stroke(path,closed=true);
    pts = [[0,0],[10,0],[0,20]];
    for(p=pts){
      color(point_in_polygon(p,path,nonzero=true)==1 ? "green" : "red")
      move(p)circle(r=1.5, $fn=12);
    }

---

### Function: polygon\_line\_intersection()

**Synopsis:** Find intersection between 2d or 3d polygon and a line, segment or ray.

**Topics:** [Geometry](Topics#geometry), [Polygons](Topics#polygons), [Lines](Topics#lines), [Intersection](Topics#intersection)

**See Also:** [polygon\_area()](#function-polygon_area), [centroid()](#function-centroid), [polygon\_normal()](#function-polygon_normal), [point\_in\_polygon()](#function-point_in_polygon)

**Usage:** 

- pt_or_segments = polygon_line_intersection(poly, line, [bounded], [nonzero], [eps]);

**Description:** 

Takes a possibly bounded line, and a 2D or 3D planar polygon, and finds their intersection.  The polygon is
treated as its boundary and interior, so the intersection may include both points and line segments.
Returns:
  * If the line does not intersect the polygon: `undef`.
  * In 3D if the line is not coplanar with the polygon but intersects it: the intersection point as a 3-vector, `[x,y,z]`.
  * In the 2D case or the 3D case when the line is coplanar with the polygon: list of segments or degenerate single point "segments".

In 3D, you can distinguish output cases using [`is_vector()`](vectors.scad#function-is_vector).  When run on the output it returns `true` when the output is a single
intersection point from a non-coplanar line.

In the 2D or coplanar case, the result is a **list** of segments, so the common case of a single segment will be a
singleton list of the form `[[p1,p2]]`.  A single point appears on the segment list as a degenerate segment or the form `[p]`,
so this means in 3D a single point will appears as `[[[x,y,z]]]` in the coplanar case.  This makes it possible to distinguish
the coplanar and non-coplanar cases.  An intersection featuring two segments and a point could look like `[[p1,p2], [q], [r1,r2]]`.
To determine if an entry in the segment list is a true segment, check its length, which is 2 for a segment and 1 for a point.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`poly`               | The 3D planar polygon to find the intersection with.
`line`               | A list of two distinct 3D points on the line.
`bounded`            | If false, the line is considered unbounded.  If true, it is treated as a bounded line segment.  If given as `[true, false]` or `[false, true]`, the boundedness of the points are specified individually, allowing the line to be treated as a half-bounded ray.  Default: false (unbounded)
`nonzero`            | set to true to use the nonzero rule for determining it points are in a polygon.  See [`point_in_polygon()`](#function-point_in_polygon).  Default: false.
`eps`                | Tolerance in geometric comparisons.  Default: 1e-9

**Example 1:** The line intersects the 3d hexagon in a single point.

<img align="left" alt="polygon\_line\_intersection() Example 1" src="images/geometry/polygon_line_intersection.png" width="320" height="240">

    include <BOSL2/std.scad>
    hex = zrot(140,p=rot([-45,40,20],p=path3d(hexagon(r=15))));
    line = [[5,0,-13],[-3,-5,13]];
    isect = polygon_line_intersection(hex,line);
    stroke(hex,closed=true);
    stroke(line);
    color("red")move(isect)sphere(r=1,$fn=12);

<br clear="all" /><br/>

**Example 2:** In 2D things are more complicated.  The output is a list of intersection parts, in the simplest case a single segment.

<img align="left" alt="polygon\_line\_intersection() Example 2" src="images/geometry/polygon_line_intersection_2.png" width="320" height="240">

    include <BOSL2/std.scad>
    hex = hexagon(r=15);
    line = [[-20,10],[25,-7]];
    isect = polygon_line_intersection(hex,line);
    stroke(hex,closed=true);
    stroke(line,endcaps="arrow2");
    color("red")
      for(part=isect)
         if(len(part)==1)
           move(part[0]) sphere(r=1);
         else
           stroke(part);

<br clear="all" /><br/>

**Example 3:** Here the line is treated as a ray.

<img align="left" alt="polygon\_line\_intersection() Example 3" src="images/geometry/polygon_line_intersection_3.png" width="320" height="240">

    include <BOSL2/std.scad>
    hex = hexagon(r=15);
    line = [[0,0],[25,-7]];
    isect = polygon_line_intersection(hex,line,RAY);
    stroke(hex,closed=true);
    stroke(line,endcap2="arrow2");
    color("red")
      for(part=isect)
         if(len(part)==1)
           move(part[0]) circle(r=1,$fn=12);
         else
           stroke(part);

<br clear="all" /><br/>

**Example 4:** Here the intersection is a single point, which is returned as a single point "path" on the path list.

<img align="left" alt="polygon\_line\_intersection() Example 4" src="images/geometry/polygon_line_intersection_4.png" width="320" height="240">

    include <BOSL2/std.scad>
    hex = hexagon(r=15);
    line = [[15,-10],[15,13]];
    isect = polygon_line_intersection(hex,line,RAY);
    stroke(hex,closed=true);
    stroke(line,endcap2="arrow2");
    color("red")
      for(part=isect)
         if(len(part)==1)
           move(part[0]) circle(r=1,$fn=12);
         else
           stroke(part);

<br clear="all" /><br/>

**Example 5:** Another way to get a single segment

<img align="left" alt="polygon\_line\_intersection() Example 5" src="images/geometry/polygon_line_intersection_5.png" width="320" height="240">

    include <BOSL2/std.scad>
    hex = hexagon(r=15);
    line = rot(30,p=[[15,-10],[15,25]],cp=[15,0]);
    isect = polygon_line_intersection(hex,line,RAY);
    stroke(hex,closed=true);
    stroke(line,endcap2="arrow2");
    color("red")
      for(part=isect)
         if(len(part)==1)
           move(part[0]) circle(r=1,$fn=12);
         else
           stroke(part);

<br clear="all" /><br/>

**Example 6:** Single segment again

<img align="left" alt="polygon\_line\_intersection() Example 6" src="images/geometry/polygon_line_intersection_6.png" width="320" height="240">

    include <BOSL2/std.scad>
    star = star(r=15,n=8,step=2);
    line = [[20,-5],[-5,20]];
    isect = polygon_line_intersection(star,line,RAY);
    stroke(star,closed=true);
    stroke(line,endcap2="arrow2");
    color("red")
      for(part=isect)
         if(len(part)==1)
           move(part[0]) circle(r=1,$fn=12);
         else
           stroke(part);

<br clear="all" /><br/>

**Example 7:** Solution is two points

<img align="left" alt="polygon\_line\_intersection() Example 7" src="images/geometry/polygon_line_intersection_7.png" width="320" height="240">

    include <BOSL2/std.scad>
    star = star(r=15,n=8,step=3);
    line = rot(22.5,p=[[15,-10],[15,20]],cp=[15,0]);
    isect = polygon_line_intersection(star,line,SEGMENT);
    stroke(star,closed=true);
    stroke(line);
    color("red")
      for(part=isect)
         if(len(part)==1)
           move(part[0]) circle(r=1,$fn=12);
         else
           stroke(part);

<br clear="all" /><br/>

**Example 8:** Solution is list of three segments

<img align="left" alt="polygon\_line\_intersection() Example 8" src="images/geometry/polygon_line_intersection_8.png" width="320" height="240">

    include <BOSL2/std.scad>
    star = star(r=25,ir=9,n=8);
    line = [[-25,12],[25,12]];
    isect = polygon_line_intersection(star,line);
    stroke(star,closed=true);
    stroke(line,endcaps="arrow2");
    color("red")
      for(part=isect)
         if(len(part)==1)
           move(part[0]) circle(r=1,$fn=12);
         else
           stroke(part);

<br clear="all" /><br/>

**Example 9:** Solution is a mixture of segments and points

<img align="left" alt="polygon\_line\_intersection() Example 9" src="images/geometry/polygon_line_intersection_9.png" width="320" height="240">

    include <BOSL2/std.scad>
    star = star(r=25,ir=9,n=7);
    line = [left(10,p=star[8]), right(50,p=star[8])];
    isect = polygon_line_intersection(star,line);
    stroke(star,closed=true);
    stroke(line,endcaps="arrow2");
    color("red")
      for(part=isect)
         if(len(part)==1)
           move(part[0]) circle(r=1,$fn=12);
         else
           stroke(part);

<br clear="all" /><br/>

---

### Function: polygon\_triangulate()

**Synopsis:** Divide a polygon into triangles.

**Topics:** [Geometry](Topics#geometry), [Triangulation](Topics#triangulation)

**See Also:** [vnf\_triangulate()](vnf.scad#function-vnf_triangulate)

**Usage:** 

- triangles = polygon_triangulate(poly, [ind], [error], [eps])

**Description:** 

Given a simple polygon in 2D or 3D, triangulates it and returns a list
of triples indexing into the polygon vertices. When the optional argument `ind` is
given, it is used as an index list into `poly` to define the polygon vertices. In that case,
`poly` may have a length greater than `ind`. When `ind` is undefined, all points in `poly`
are considered as vertices of the polygon.

For 2d polygons, the output triangleshave the same winding (CW or CCW) of
the input polygon. For 3d polygons, the triangle windings induce a normal
vector with the same direction of the polygon normal.

The function produces correct triangulations for some non-twisted non-simple polygons.
A polygon is non-twisted if it is simple or it has a partition in
simple polygons with the same winding such that the intersection of any two partitions is
made of full edges and/or vertices of both partitions. These polygons may have "touching" vertices
(two vertices having the same coordinates, but distinct adjacencies) and "contact" edges
(edges whose vertex pairs have the same pairwise coordinates but are in reversed order) but has
no self-crossing. See examples bellow. If all polygon edges are contact edges (polygons with
zero area), it returns an empty list for 2d polygons and reports an error for 3d polygons.
Triangulation errors are reported either by an assert error (when `error=true`) or by returning
`undef` (when `error=false`). Invalid arguments always produce an assert error.

Twisted polygons have no consistent winding and when input to this function usually reports
an error but when an error is not reported the outputs are not correct triangulations. The function
can work for 3d non-planar polygons if they are close enough to planar but may otherwise
report an error for this case.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`poly`               | Array of the polygon vertices.
`ind`                | If given, a list of indices indexing the vertices of the polygon in `poly`.  Default: use all the points of poly
`error`              | If false, returns `undef` when the polygon cannot be triangulated; otherwise, issues an assert error. Default: true.
`eps`                | A maximum tolerance in geometrical tests. Default: 1e-9

**Example 1:** a simple polygon; see from above

<img align="left" alt="polygon\_triangulate() Example 1" src="images/geometry/polygon_triangulate.png" width="320" height="240">

<br clear="all" />

    include <BOSL2/std.scad>
    poly = star(id=10, od=15,n=11);
    tris =  polygon_triangulate(poly);
    color("lightblue") for(tri=tris) polygon(select(poly,tri));
    color("blue")    up(1) for(tri=tris) { stroke(select(poly,tri),.15,closed=true); }
    color("magenta") up(2) stroke(poly,.25,closed=true);
    color("black")   up(3) debug_vnf([path3d(poly),[]],faces=false,size=1);

**Example 2:** a polygon with a hole and one "contact" edge; see from above

<img align="left" alt="polygon\_triangulate() Example 2" src="images/geometry/polygon_triangulate_2.png" width="320" height="240">

<br clear="all" />

    include <BOSL2/std.scad>
    poly = [ [-10,0], [10,0], [0,10], [-10,0], [-4,4], [4,4], [0,2], [-4,4] ];
    tris =  polygon_triangulate(poly);
    color("lightblue") for(tri=tris) polygon(select(poly,tri));
    color("blue")    up(1) for(tri=tris) { stroke(select(poly,tri),.15,closed=true); }
    color("magenta") up(2) stroke(poly,.25,closed=true);
    color("black")   up(3) debug_vnf([path3d(poly),[]],faces=false,size=1);

**Example 3:** a polygon with "touching" vertices and no holes; see from above

<img align="left" alt="polygon\_triangulate() Example 3" src="images/geometry/polygon_triangulate_3.png" width="320" height="240">

<br clear="all" />

    include <BOSL2/std.scad>
    poly = [ [0,0], [5,5], [-5,5], [0,0], [-5,-5], [5,-5] ];
    tris =  polygon_triangulate(poly);
    color("lightblue") for(tri=tris) polygon(select(poly,tri));
    color("blue")    up(1) for(tri=tris) { stroke(select(poly,tri),.15,closed=true); }
    color("magenta") up(2) stroke(poly,.25,closed=true);
    color("black")   up(3) debug_vnf([path3d(poly),[]],faces=false,size=1);

**Example 4:** a polygon with "contact" edges and no holes; see from above

<img align="left" alt="polygon\_triangulate() Example 4" src="images/geometry/polygon_triangulate_4.png" width="320" height="240">

<br clear="all" />

    include <BOSL2/std.scad>
    poly = [ [0,0], [10,0], [10,10], [0,10], [0,0], [3,3], [7,3],
             [7,7], [7,3], [3,3] ];
    tris =  polygon_triangulate(poly);
    color("lightblue") for(tri=tris) polygon(select(poly,tri));
    color("blue")    up(1) for(tri=tris) { stroke(select(poly,tri),.15,closed=true); }
    color("magenta") up(2) stroke(poly,.25,closed=true);
    color("black")   up(3) debug_vnf([path3d(poly),[]],faces=false,size=1);

**Example 5:** 

<img align="left" alt="polygon\_triangulate() Example 5" src="images/geometry/polygon_triangulate_5.png" width="320" height="240">

<br clear="all" />

    include <BOSL2/std.scad>
    include <BOSL2/polyhedra.scad>
    vnf = regular_polyhedron_info(name="dodecahedron",side=5,info="vnf");
    vnf_polyhedron(vnf);
    vnf_tri = [vnf[0], [for(face=vnf[1]) each polygon_triangulate(vnf[0], face) ] ];
    color("blue")
    vnf_wireframe(vnf_tri, width=.15);

---

### Function: is\_polygon\_clockwise()

**Synopsis:** Determine if a 2d polygon winds clockwise.

**Topics:** [Geometry](Topics#geometry), [Polygons](Topics#polygons), [Clockwise](Topics#clockwise)

**See Also:** [clockwise\_polygon()](#function-clockwise_polygon), [ccw\_polygon()](#function-ccw_polygon), [reverse\_polygon()](#function-reverse_polygon)

**Usage:** 

- bool = is_polygon_clockwise(poly);

**Description:** 

Return true if the given 2D simple polygon is in clockwise order, false otherwise.
Results for complex (self-intersecting) polygon are indeterminate.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`poly`               | The list of 2D path points for the perimeter of the polygon.

---

### Function: clockwise\_polygon()

**Synopsis:** Return clockwise version of a polygon.

**Topics:** [Geometry](Topics#geometry), [Polygons](Topics#polygons), [Clockwise](Topics#clockwise)

**See Also:** [is\_polygon\_clockwise()](#function-is_polygon_clockwise), [ccw\_polygon()](#function-ccw_polygon), [reverse\_polygon()](#function-reverse_polygon)

**Usage:** 

- newpoly = clockwise_polygon(poly);

**Description:** 

Given a 2D polygon path, returns the clockwise winding version of that path.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`poly`               | The list of 2D path points for the perimeter of the polygon.

---

### Function: ccw\_polygon()

**Synopsis:** Return counter-clockwise version of a polygon.

**Topics:** [Geometry](Topics#geometry), [Polygons](Topics#polygons), [Clockwise](Topics#clockwise)

**See Also:** [is\_polygon\_clockwise()](#function-is_polygon_clockwise), [clockwise\_polygon()](#function-clockwise_polygon), [reverse\_polygon()](#function-reverse_polygon)

**Usage:** 

- newpoly = ccw_polygon(poly);

**Description:** 

Given a 2D polygon poly, returns the counter-clockwise winding version of that poly.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`poly`               | The list of 2D path points for the perimeter of the polygon.

---

### Function: reverse\_polygon()

**Synopsis:** Reverse winding direction of polygon.

**Topics:** [Geometry](Topics#geometry), [Polygons](Topics#polygons), [Clockwise](Topics#clockwise)

**See Also:** [is\_polygon\_clockwise()](#function-is_polygon_clockwise), [ccw\_polygon()](#function-ccw_polygon), [clockwise\_polygon()](#function-clockwise_polygon)

**Usage:** 

- newpoly = reverse_polygon(poly)

**Description:** 

Reverses a polygon's winding direction, while still using the same start point.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`poly`               | The list of the path points for the perimeter of the polygon.

---

### Function: reindex\_polygon()

**Synopsis:** Adjust point indexing of polygon to minimize pointwise distance to a reference polygon.

**Topics:** [Geometry](Topics#geometry), [Polygons](Topics#polygons)

**See Also:** [align\_polygon()](#function-align_polygon), [are\_polygons\_equal()](#function-are_polygons_equal)

**Usage:** 

- newpoly = reindex_polygon(reference, poly);

**Description:** 

Rotates and possibly reverses the point order of a 2d or 3d polygon path to optimize its pairwise point
association with a reference polygon.  The two polygons must have the same number of vertices and be the same dimension.
The optimization is done by computing the distance, norm(reference[i]-poly[i]), between
corresponding pairs of vertices of the two polygons and choosing the polygon point index rotation that
makes the total sum over all pairs as small as possible.  Returns the reindexed polygon.  Note
that the geometry of the polygon is not changed by this operation, just the labeling of its
vertices.  If the input polygon is 2d and is oriented opposite the reference then its point order is
reversed.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`reference`          | reference polygon path
`poly`               | input polygon to reindex

**Example 1:** The red dots show the 0th entry in the two input path lists.  Note that the red dots are not near each other.  The blue dot shows the 0th entry in the output polygon

<img align="left" alt="reindex\_polygon() Example 1" src="images/geometry/reindex_polygon.png" width="320" height="240">

<br clear="all" />

    include <BOSL2/std.scad>
    pent = subdivide_path([for(i=[0:4])[sin(72*i),cos(72*i)]],30);
    circ = circle($fn=30,r=2.2);
    reindexed = reindex_polygon(circ,pent);
    move_copies(concat(circ,pent)) circle(r=.1,$fn=32);
    color("red") move_copies([pent[0],circ[0]]) circle(r=.1,$fn=32);
    color("blue") translate(reindexed[0])circle(r=.1,$fn=32);

**Example 2:** The indexing that minimizes the total distance does not necessarily associate the nearest point of `poly` with the reference, as in this example where again the blue dot indicates the 0th entry in the reindexed result.

<img align="left" alt="reindex\_polygon() Example 2" src="images/geometry/reindex_polygon_2.png" width="320" height="240">

<br clear="all" />

    include <BOSL2/std.scad>
    pent = move([3.5,-1],p=subdivide_path([for(i=[0:4])[sin(72*i),cos(72*i)]],30));
    circ = circle($fn=30,r=2.2);
    reindexed = reindex_polygon(circ,pent);
    move_copies(concat(circ,pent)) circle(r=.1,$fn=32);
    color("red") move_copies([pent[0],circ[0]]) circle(r=.1,$fn=32);
    color("blue") translate(reindexed[0])circle(r=.1,$fn=32);

---

### Function: align\_polygon()

**Synopsis:** Find best alignment of a 2d polygon to a reference 2d polygon over a set of transformations.

**Topics:** [Geometry](Topics#geometry), [Polygons](Topics#polygons)

**See Also:** [reindex\_polygon()](#function-reindex_polygon), [are\_polygons\_equal()](#function-are_polygons_equal)

**Usage:** 

- newpoly = align_polygon(reference, poly, [angles], [cp], [tran], [return_ind]);

**Description:** 

Find the best alignment of a specified 2D polygon with a reference 2D polygon over a set of
transformations.  You can specify a list or range of angles and a centerpoint or you can
give a list of arbitrary 2d transformation matrices.  For each transformation or angle, the polygon is
reindexed, which is a costly operation so if run time is a problem, use a smaller sampling of angles or
transformations.  By default returns the rotated and reindexed polygon.  You can also request that
the best angle or the index into the transformation list be returned.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`reference`          | reference polygon
`poly`               | polygon to rotate into alignment with the reference
`angles`             | list or range of angles to test
`cp`                 | centerpoint for rotations

<abbr title="These args must be used by name, ie: name=value">By&nbsp;Name</abbr> | What it does
-------------------- | ------------
`tran`               | list of 2D transformation matrices to optimize over
`return_ind`         | if true, return the best angle (if you specified angles) or the index into tran otherwise of best alignment

**Example 1:** Rotating the poorly aligned light gray triangle by 105 degrees produces the best alignment, shown in blue:

<img align="left" alt="align\_polygon() Example 1" src="images/geometry/align_polygon.png" width="320" height="240">

    include <BOSL2/std.scad>
    ellipse = yscale(3,circle(r=10, $fn=32));
    tri = move([-50/3,-9],
               subdivide_path([[0,0], [50,0], [0,27]], 32));
    aligned = align_polygon(ellipse,tri, [0:5:180]);
    color("white")stroke(tri,width=.5,closed=true);
    stroke(ellipse, width=.5, closed=true);
    color("blue")stroke(aligned,width=.5,closed=true);

<br clear="all" /><br/>

**Example 2:** Translating a triangle (light gray) to the best alignment (blue)

<img align="left" alt="align\_polygon() Example 2" src="images/geometry/align_polygon_2.png" width="320" height="240">

    include <BOSL2/std.scad>
    ellipse = yscale(2,circle(r=10, $fn=32));
    tri = subdivide_path([[0,0], [27,0], [-7,50]], 32);
    T = [for(x=[-10:0], y=[-30:-15]) move([x,y])];
    aligned = align_polygon(ellipse,tri, trans=T);
    color("white")stroke(tri,width=.5,closed=true);
    stroke(ellipse, width=.5, closed=true);
    color("blue")stroke(aligned,width=.5,closed=true);

<br clear="all" /><br/>

---

### Function: are\_polygons\_equal()

**Synopsis:** Check if two polygons (not necessarily in the same point order) are equal.

**Topics:** [Geometry](Topics#geometry), [Polygons](Topics#polygons), [Comparators](Topics#comparators)

**See Also:** [reindex\_polygon()](#function-reindex_polygon), [align\_polygon()](#function-align_polygon)

**Usage:** 

- bool = are_polygons_equal(poly1, poly2, [eps])

**Description:** 

Returns true if poly1 and poly2 are the same polongs
within given epsilon tolerance.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`poly1`              | first polygon
`poly2`              | second polygon
`eps`                | tolerance for comparison

**Example 1:** 

    include <BOSL2/std.scad>
    are_polygons_equal(pentagon(r=4),
                   rot(360/5, p=pentagon(r=4))); // returns true
    are_polygons_equal(pentagon(r=4),
                   rot(90, p=pentagon(r=4)));    // returns false

<br clear="all" /><br/>

---

## Section: Convex Hull


### Function: hull()

**Synopsis:** Convex hull of a list of 2d or 3d points. <sup title="Extends the OpenScad keyword of the same name.">[<abbr>Ext</abbr>]</sup>

**Topics:** [Geometry](Topics#geometry), [Hulling](Topics#hulling)

**See Also:** [hull\_points()](#module-hull_points), [hull2d\_path()](#function-hull2d_path), [hull3d\_faces()](#function-hull3d_faces)

**Usage:** 

- face_list_or_index_list = hull(points);

**Description:** 

This is documentation for the BOSL2 function form of `hull()`.  [Click Here for documentation for the builtin module.](https://github.com/BelfrySCAD/BelfrySCAD/wiki/Language-Other-Modules#hull)

Takes a list of 2D or 3D points (but not both in the same list) and returns either the list of
indexes into `points` that forms the 2D convex hull perimeter path, or the list of faces that
form the 3d convex hull surface.  Each face is a list of indexes into `points`.  If the input
points are collinear, the indexes of the two extrema points are returned.  If the input
points are coplanar, then a simple list of vertex indices forming a planar perimeter is
returned. Otherwise a list of faces is returned, where each face is a simple list of
vertex indices for the perimeter of the face.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`points`             | The set of 2D or 3D points to find the hull of.

---

### Module: hull\_points()

**Synopsis:** Convex hull of a list of 2d or 3d points.

**Topics:** [Geometry](Topics#geometry), [Hulling](Topics#hulling)

**See Also:** [hull()](#function-hull), [hull2d\_path()](#function-hull2d_path), [hull3d\_faces()](#function-hull3d_faces)

**Usage:** 

- hull_points(points, [fast]);

**Description:** 

If given a list of 2D points, creates a 2D convex hull polygon that encloses all those points.
If given a list of 3D points, creates a 3D polyhedron that encloses all the points.  This should
handle about 4000 points in slow mode.  If `fast` is set to true, this should be able to handle
far more.  When fast mode is off, 3d hulls that lie in a plane produce a single face of a polyhedron, which can be viewed in preview but will not render.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`points`             | The list of points to form a hull around.
`fast`               | If true for 3d case, uses a faster cheat that may handle more points, but also may emit warnings that can stop your script if you have "Halt on first warning" enabled.  Ignored for the 2d case.  Default: false

**Example 1:** 

<img align="left" alt="hull\_points() Example 1" src="images/geometry/hull_points.png" width="320" height="240">

    include <BOSL2/std.scad>
    pts = [[-10,-10], [0,10], [10,10], [12,-10]];
    hull_points(pts);

<br clear="all" /><br/>

**Example 2:** 

<img align="left" alt="hull\_points() Example 2" src="images/geometry/hull_points_2.png" width="320" height="240">

<br clear="all" />

    include <BOSL2/std.scad>
    pts = [for (phi = [30:60:150], theta = [0:60:359]) spherical_to_xyz(10, theta, phi)];
    hull_points(pts);

---

### Function: hull2d\_path()

**Synopsis:** Convex hull of a list of 2d points.

**Topics:** [Geometry](Topics#geometry), [Hulling](Topics#hulling)

**See Also:** [hull()](#function-hull), [hull\_points()](#module-hull_points), [hull3d\_faces()](#function-hull3d_faces)

**Usage:** 

- index_list = hull2d_path(points,all)

**Description:** 

Takes a list of arbitrary 2D points, and finds the convex hull polygon to enclose them.
Returns a path as a list of indices into `points`.
When all==true, returns extra points that are on edges of the hull.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`points`             | list of 2d points to get the hull of.
`all`                | when true, includes all points on the edges of the convex hull. Default: false.

**Example 1:** 

<img align="left" alt="hull2d\_path() Example 1" src="images/geometry/hull2d_path.png" width="320" height="240">

    include <BOSL2/std.scad>
    pts = [[-10,-10], [0,10], [10,10], [12,-10]];
    path = hull2d_path(pts);
    move_copies(pts) color("red") circle(1,$fn=12);
    polygon(points=pts, paths=[path]);

<br clear="all" /><br/>

---

### Function: hull3d\_faces()

**Synopsis:** Convex hull of a list of 3d points.

**Topics:** [Geometry](Topics#geometry), [Hulling](Topics#hulling)

**See Also:** [hull()](#function-hull), [hull\_points()](#module-hull_points), [hull2d\_path()](#function-hull2d_path)

**Usage:** 

- faces = hull3d_faces(points)

**Description:** 

Takes a list of arbitrary 3D points, and finds the convex hull polyhedron to enclose
them.  Returns a list of triangular faces, where each face is a list of indexes into the given `points`
list.  The output is valid for use with the `polyhedron()` command, but may include vertices that are in the interior of a face of the hull, so it is not
necessarily the minimal representation of the hull.
If all points passed to it are coplanar, then the return is the list of indices of points
forming the convex hull polygon.

**Example 1:** 

<img align="left" alt="hull3d\_faces() Example 1" src="images/geometry/hull3d_faces.png" width="320" height="240">

    include <BOSL2/std.scad>
    pts = [[-20,-20,0], [20,-20,0], [0,20,5], [0,0,20]];
    faces = hull3d_faces(pts);
    move_copies(pts) color("red") sphere(1);
    %polyhedron(points=pts, faces=faces);

<br clear="all" /><br/>

---

## Section: Convex Sets


### Function: is\_polygon\_convex()

**Synopsis:** Check if a polygon is convex.

**Topics:** [Geometry](Topics#geometry), [Convexity](Topics#convexity), [Test](Topics#test)

**See Also:** [clockwise\_polygon()](#function-clockwise_polygon), [ccw\_polygon()](#function-ccw_polygon)

**Usage:** 

- bool = is_polygon_convex(poly, [eps]);

**Description:** 

Returns true if the given 2D or 3D polygon is convex.
The result is meaningless if the polygon is not simple (self-crossing) or non coplanar.
If the points are collinear or not coplanar an error may be generated.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`poly`               | Polygon to check.
`eps`                | Tolerance for the collinearity and coplanarity tests. Default: 1e-9.

**Example 1:** 

    include <BOSL2/std.scad>
    test1 = is_polygon_convex(circle(d=50));                                 // Returns: true
    test2 = is_polygon_convex(rot([50,120,30], p=path3d(circle(1,$fn=50)))); // Returns: true
    spiral = [for (i=[0:36]) let(a=-i*10) (10+i)*[cos(a),sin(a)]];
    test = is_polygon_convex(spiral);                                        // Returns: false

<br clear="all" /><br/>

---

### Function: convex\_distance()

**Synopsis:** Compute distance between convex hull of two point lists.

**Topics:** [Geometry](Topics#geometry), [Convexity](Topics#convexity), [Distance](Topics#distance)

**Usage:** 

- dist = convex_distance(points1, points2,eps);

**Description:** 

Returns the smallest distance between a point in convex hull of `points1`
and a point in the convex hull of `points2`. All the points in the lists
should have the same dimension, either 2D or 3D.
A zero result means the hulls intercept whithin a tolerance `eps`.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`points1`            | first list of 2d or 3d points.
`points2`            | second list of 2d or 3d points.
`eps`                | tolerance in distance evaluations. Default: 1e-9.

**Example 1:** 

<img align="left" alt="convex\_distance() Example 1" src="images/geometry/convex_distance.png" width="320" height="240">

    include <BOSL2/std.scad>
    pts1 = move([-3,0], p=square(3,center=true));
    pts2 = rot(a=45, p=square(2,center=true));
    pts3 = [ [2,0], [1,2],[3,2], [3,-2], [1,-2] ];
    polygon(pts1);
    polygon(pts2);
    polygon(pts3);
    echo(convex_distance(pts1,pts2)); // Returns: 0.0857864
    echo(convex_distance(pts2,pts3)); // Returns: 0

<br clear="all" /><br/>

**Example 2:** 

<img align="left" alt="convex\_distance() Example 2" src="images/geometry/convex_distance_2.png" width="320" height="240">

    include <BOSL2/std.scad>
    sphr1 = sphere(2,$fn=10);
    sphr2 = move([4,0,0], p=sphr1);
    sphr3 = move([4.5,0,0], p=sphr1);
    vnf_polyhedron(sphr1);
    vnf_polyhedron(sphr2);
    echo(convex_distance(sphr1[0], sphr2[0])); // Returns: 0
    echo(convex_distance(sphr1[0], sphr3[0])); // Returns: 0.5

<br clear="all" /><br/>

---

### Function: convex\_collision()

**Synopsis:** Check whether the convex hulls of two point lists intersect.

**Topics:** [Geometry](Topics#geometry), [Convexity](Topics#convexity), [Collision](Topics#collision), [Intersection](Topics#intersection)

**Usage:** 

- bool = convex_collision(points1, points2, [eps]);

**Description:** 

Returns `true` if the convex hull of `points1` intersects the convex hull of `points2`
otherwise, `false`.
All the points in the lists should have the same dimension, either 2D or 3D.
This function is tipically faster than `convex_distance` to find a non-collision.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`points1`            | first list of 2d or 3d points.
`points2`            | second list of 2d or 3d points.
`eps - tolerance for the intersection tests. Default: 1e-9.`

**Example 1:** 

<img align="left" alt="convex\_collision() Example 1" src="images/geometry/convex_collision.png" width="320" height="240">

    include <BOSL2/std.scad>
    pts1 = move([-3,0], p=square(3,center=true));
    pts2 = rot(a=45, p=square(2,center=true));
    pts3 = [ [2,0], [1,2],[3,2], [3,-2], [1,-2] ];
    polygon(pts1);
    polygon(pts2);
    polygon(pts3);
    echo(convex_collision(pts1,pts2)); // Returns: false
    echo(convex_collision(pts2,pts3)); // Returns: true

<br clear="all" /><br/>

**Example 2:** 

<img align="left" alt="convex\_collision() Example 2" src="images/geometry/convex_collision_2.png" width="320" height="240">

    include <BOSL2/std.scad>
    sphr1 = sphere(2,$fn=10);
    sphr2 = move([4,0,0], p=sphr1);
    sphr3 = move([4.5,0,0], p=sphr1);
    vnf_polyhedron(sphr1);
    vnf_polyhedron(sphr2);
    echo(convex_collision(sphr1[0], sphr2[0])); // Returns: true
    echo(convex_collision(sphr1[0], sphr3[0])); // Returns: false

<br clear="all" /><br/>

---

## Section: Rotation Decoding


### Function: rot\_decode()

**Synopsis:** Extract axis and rotation angle from a rotation matrix.

**Topics:** [Affine](Topics#affine), [Matrices](Topics#matrices), [Transforms](Topics#transforms)

**Usage:** 

- info = rot_decode(rotation,[long]); // Returns: [angle,axis,cp,translation]

**Description:** 

Given an input 3D rigid transformation operator (one composed of just rotations and translations) represented
as a 4x4 matrix, compute the rotation and translation parameters of the operator.  Returns a list of the
four parameters, the angle, in the interval [0,180], the rotation axis as a unit vector, a centerpoint for
the rotation, and a translation.  If you set `parms = rot_decode(rotation)` then the transformation can be
reconstructed from parms as `move(parms[3]) * rot(a=parms[0],v=parms[1],cp=parms[2])`.  This decomposition
makes it possible to perform interpolation.  If you construct a transformation using `rot` the decoding
may flip the axis (if you gave an angle outside of [0,180]).  The returned axis is a unit vector, and
the centerpoint lies on the plane through the origin that is perpendicular to the axis.  It may be different
than the centerpoint you used to construct the transformation.

If you set `long` to true then return the reversed rotation, with the angle in [180,360].

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`rotation`           | rigid transformation to decode
`long`               | if true return the "long way" around, with the angle in [180,360].  Default: false

**Example 1:** 

    include <BOSL2/std.scad>
    info = rot_decode(rot(45));
           // Returns: [45, [0,0,1], [0,0,0], [0,0,0]]
    info = rot_decode(rot(a=37, v=[1,2,3], cp=[4,3,-7])));
           // Returns: [37, [0.26, 0.53, 0.80], [4.8, 4.6, -4.6], [0,0,0]]
    info = rot_decode(left(12)*xrot(-33));
           // Returns: [33, [-1,0,0], [0,0,0], [-12,0,0]]
    info = rot_decode(translate([3,4,5]));
           // Returns: [0, [0,0,1], [0,0,0], [3,4,5]]

<br clear="all" /><br/>

---


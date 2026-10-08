# LibFile: utility.scad

Functions for type checking, handling undefs, processing function arguments,
and testing.

To use, add the following lines to the beginning of your file:

    include <BOSL2/std.scad>

## File Contents

1. [Section: Type Checking](#section-type-checking)
    - [`typeof()`](#function-typeof) – Returns a string representing the type of the value.
    - [`is_type()`](#function-is_type) – Returns true if the type of 'x' is one of those in the list `types`.
    - [`is_def()`](#function-is_def) – Returns true if `x` is not `undef`.
    - [`is_str()`](#function-is_str) – Returns true if the argument is a string.
    - [`is_int()`](#function-is_int) – Returns true if the argument is an integer.
    - [`all_integer()`](#function-all_integer) – Returns true if all of the numbers in the argument are integers.
    - [`is_nan()`](#function-is_nan) – Return true if the argument is "not a number".
    - [`is_finite()`](#function-is_finite) – Returns true if the argument is a finite number.
    - [`is_range()`](#function-is_range) – Returns true if the argument is a range.
    - [`valid_range()`](#function-valid_range) – Returns true if the argument is a valid range.
    - [`is_func()`](#function-is_func) – Returns true if the argument is a function literal.
    - [`is_consistent()`](#function-is_consistent) – Returns true if the argument is a list with consistent structure and finite numerical data.
    - [`same_shape()`](#function-same_shape) – Returns true if the argument lists are numeric and of the same shape.
    - [`is_bool_list()`](#function-is_bool_list) – Returns true if the argument list contains only booleans.

2. [Section: Boolean list testing](#section-boolean-list-testing)
    - [`any()`](#function-any) – Returns true if any item in the argument list is true.
    - [`all()`](#function-all) – Returns true if all items in the argument list are true.
    - [`num_true()`](#function-num_true) – Returns the number of true entries in the arguemnt list.

3. [Section: Handling `undef`s.](#section-handling-undefs)
    - [`default()`](#function-default) – Returns a default value if the argument is 'undef', else returns the argument.
    - [`first_defined()`](#function-first_defined) – Returns the first value in the argument list that is not 'undef'.
    - [`one_defined()`](#function-one_defined) – Returns the defined value in the argument list if only a single value is defined.
    - [`num_defined()`](#function-num_defined) – Returns the number of defined values in the the argument list.
    - [`any_defined()`](#function-any_defined) – Returns true if any item in the argument list is not `undef`.
    - [`all_defined()`](#function-all_defined) – Returns true if all items in the given array are defined.

4. [Section: Undef Safe Arithmetic](#section-undef-safe-arithmetic)
    - [`u_add()`](#function-u_add) – Returns the sum of 2 numbers if both are defined, otherwise returns undef.
    - [`u_sub()`](#function-u_sub) – Returns the difference of 2 numbers if both are defined, otherwise returns undef.
    - [`u_mul()`](#function-u_mul) – Returns the product of 2 numbers if both are defined, otherwise returns undef.
    - [`u_div()`](#function-u_div) – Returns the quotient of 2 numbers if both are defined, otherwise returns undef.

5. [Section: Processing Arguments to Functions and Modules](#section-processing-arguments-to-functions-and-modules)
    - [`get_anchor()`](#function-get_anchor) – Returns the correct anchor from `anchor` and `center`.
    - [`get_radius()`](#function-get_radius) – Given various radii and diameters, returns the most specific radius.
    - [`scalar_vec3()`](#function-scalar_vec3) – Expands a scalar or a list with length less than 3 to a length 3 vector.
    - [`segs()`](#function-segs) – Returns the number of sides for a circle given `$fn`, `$fa`, and `$fs`.
    - [`no_children()`](#module-no_children) – Assert that the calling module does not support children.
    - [`req_children()`](#module-req_children) – Assert that the calling module requires children.
    - [`no_function()`](#function-no_function) – Assert that the argument exists only as a module and not as a function.
    - [`no_module()`](#module-no_module) – Assert that the argument exists only as a function and not as a module.
    - [`deprecate()`](#module-deprecate) – Display a console note that a module is deprecated and suggest a replacement.
    - [`echo_viewport()`](#module-echo_viewport) – Display the current viewport parameters.

6. [Section: Testing Helpers](#section-testing-helpers)
    - [`assert_approx()`](#module-assert_approx) – Assert that a value is approximately what was expected.
    - [`assert_equal()`](#module-assert_equal) – Assert that a value is expected.
    - [`shape_compare()`](#module-shape_compare) – Compares two child shapes. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>

7. [Section: C-Style For Loop Helpers](#section-c-style-for-loop-helpers)
    - [`looping()`](#function-looping) – Returns true if the argument indicates the current C-style loop should continue.
    - [`loop_while()`](#function-loop_while) – Returns true if both arguments indicate the current C-style loop should continue.
    - [`loop_done()`](#function-loop_done) – Returns true if the argument indicates the current C-style loop is finishing.


## Section: Type Checking


### Function: typeof()

**Synopsis:** Returns a string representing the type of the value.

**Topics:** [Type Checking](Topics#type-checking)

**See Also:** [is\_type()](#function-is_type)

**Usage:** 

- typ = typeof(x);

**Description:** 

Returns a string representing the type of the value.  One of "undef", "boolean", "number", "nan", "string", "list", "range", "function" or "invalid".
Some malformed "ranges", like '[0:NAN:INF]' and '[0:"a":INF]', may be classified as "undef" or "invalid".

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`x`                  | value whose type to check

**Example 1:** 

    include <BOSL2/std.scad>
    typ = typeof(undef);  // Returns: "undef"
    typ = typeof(true);  // Returns: "boolean"
    typ = typeof(42);  // Returns: "number"
    typ = typeof(NAN);  // Returns: "nan"
    typ = typeof("foo");  // Returns: "string"
    typ = typeof([3,4,5]);  // Returns: "list"
    typ = typeof([3:1:8]);  // Returns: "range"
    typ = typeof(function (x,y) x+y);  // Returns: "function"

<br clear="all" /><br/>

---

### Function: is\_type()

**Synopsis:** Returns true if the type of 'x' is one of those in the list `types`.

**Topics:** [Type Checking](Topics#type-checking)

**See Also:** [typeof()](#function-typeof)

**Usage:** 

- bool = is_type(x, types);

**Description:** 

Returns true if the type of the value `x` is one of those given as strings in the list `types`.
Valid types are "undef", "boolean", "number", "nan", "string", "list", "range", or "function".

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`x`                  | The value to check the type of.
`types`              | A list of types to check

**Example 1:** 

    include <BOSL2/std.scad>
    is_str_or_list = is_type("foo", ["string","list"]);   // Returns: true
    is_str_or_list2 = is_type([1,2,3], ["string","list"]);  // Returns: true
    is_str_or_list3 = is_type(2, ["string","list"]);  // Returns: false
    is_str = is_type("foo", "string");  // Returns: true
    is_str2 = is_type([3,4], "string");  // Returns: false
    is_str3 = is_type(["foo"], "string");  // Returns: false
    is_str4 = is_type(3, "string");  // Returns: false

<br clear="all" /><br/>

---

### Function: is\_def()

**Synopsis:** Returns true if `x` is not `undef`.

**Topics:** [Type Checking](Topics#type-checking)

**See Also:** [typeof()](#function-typeof), [is\_type()](#function-is_type), [is\_str()](#function-is_str)

**Usage:** 

- bool = is_def(x);

**Description:** 

Returns true if `x` is not `undef`.  False if `x==undef`.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`x`                  | value to check

**Example 1:** 

    include <BOSL2/std.scad>
    bool = is_def(undef);  // Returns: false
    bool = is_def(false);  // Returns: true
    bool = is_def(42);     // Returns: true
    bool = is_def("foo");  // Returns: true

<br clear="all" /><br/>

---

### Function: is\_str()

**Synopsis:** Returns true if the argument is a string.

**Topics:** [Type Checking](Topics#type-checking)

**See Also:** [typeof()](#function-typeof), [is\_type()](#function-is_type), [is\_int()](#function-is_int), [is\_def()](#function-is_def), [is\_int()](#function-is_int)

**Usage:** 

- bool = is_str(x);

**Description:** 

Returns true if `x` is a string.  A shortcut for `is_string()`.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`x`                  | value to check

**Example 1:** 

    include <BOSL2/std.scad>
    bool = is_str(undef);  // Returns: false
    bool = is_str(false);  // Returns: false
    bool = is_str(42);     // Returns: false
    bool = is_str("foo");  // Returns: true

<br clear="all" /><br/>

---

### Function: is\_int()

**Alias:** is\_integer()


**Synopsis:** Returns true if the argument is an integer.

**Topics:** [Type Checking](Topics#type-checking)

**See Also:** [typeof()](#function-typeof), [is\_type()](#function-is_type), [is\_str()](#function-is_str), [is\_def()](#function-is_def)

**Usage:** 

- bool = is_int(n);
- bool = is_integer(n);

**Description:** 

Returns true if the given value is an integer (it is a number and it rounds to itself).

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`n`                  | value to check

**Example 1:** 

    include <BOSL2/std.scad>
    bool = is_int(undef);  // Returns: false
    bool = is_int(false);  // Returns: false
    bool = is_int(42);     // Returns: true
    bool = is_int("foo");  // Returns: false

<br clear="all" /><br/>

---

### Function: all\_integer()

**Synopsis:** Returns true if all of the numbers in the argument are integers.

**Topics:** [Type Checking](Topics#type-checking)

**Usage:** 

- bool = all_integer(x);

**Description:** 

If given a number, returns true if the number is a finite integer.
If given an empty list, returns false.  If given a non-empty list, returns
true if every item of the list is an integer.  Otherwise, returns false.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`x`                  | The value to check.

**Example 1:** 

    include <BOSL2/std.scad>
    b = all_integer(true);  // Returns: false
    b = all_integer("foo"); // Returns: false
    b = all_integer(4);     // Returns: true
    b = all_integer(4.5);   // Returns: false
    b = all_integer([]);    // Returns: false
    b = all_integer([3,4,5]);   // Returns: true
    b = all_integer([3,4.2,5]); // Returns: false
    b = all_integer([3,[4,7],5]); // Returns: false

<br clear="all" /><br/>

---

### Function: is\_nan()

**Synopsis:** Return true if the argument is "not a number".

**Topics:** [Type Checking](Topics#type-checking)

**See Also:** [typeof()](#function-typeof), [is\_type()](#function-is_type), [is\_str()](#function-is_str), [is\_def()](#function-is_def), [is\_int()](#function-is_int), [is\_finite()](#function-is_finite)

**Usage:** 

- bool = is_nan(x);

**Description:** 

Returns true if a given value `x` is nan, a floating point value representing "not a number".

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`x`                  | value to check

**Example 1:** 

    include <BOSL2/std.scad>
    bool = is_nan(undef);  // Returns: false
    bool = is_nan(false);  // Returns: false
    bool = is_nan(42);     // Returns: false
    bool = is_nan("foo");  // Returns: false
    bool = is_nan(NAN);    // Returns: true

<br clear="all" /><br/>

---

### Function: is\_finite()

**Synopsis:** Returns true if the argument is a finite number.

**Topics:** [Type Checking](Topics#type-checking)

**See Also:** [typeof()](#function-typeof), [is\_type()](#function-is_type), [is\_str()](#function-is_str), [is\_def()](#function-is_def), [is\_int()](#function-is_int), [is\_nan()](#function-is_nan)

**Usage:** 

- bool = is_finite(x);

**Description:** 

Returns true if a given value `x` is a finite number.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`x`                  | value to check

**Example 1:** 

    include <BOSL2/std.scad>
    bool = is_finite(undef);  // Returns: false
    bool = is_finite(false);  // Returns: false
    bool = is_finite(42);     // Returns: true
    bool = is_finite("foo");  // Returns: false
    bool = is_finite(NAN);    // Returns: false
    bool = is_finite(INF);    // Returns: false
    bool = is_finite(-INF);   // Returns: false

<br clear="all" /><br/>

---

### Function: is\_range()

**Synopsis:** Returns true if the argument is a range.

**Topics:** [Type Checking](Topics#type-checking)

**See Also:** [typeof()](#function-typeof), [is\_type()](#function-is_type), [is\_str()](#function-is_str), [is\_def()](#function-is_def), [is\_int()](#function-is_int)

**Usage:** 

- bool = is_range(x);

**Description:** 

Returns true if its argument is a range

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`x`                  | value to check

**Example 1:** 

    include <BOSL2/std.scad>
    bool = is_range(undef);   // Returns: false
    bool = is_range(false);   // Returns: false
    bool = is_range(42);      // Returns: false
    bool = is_range([3,4,5]); // Returns: false
    bool = is_range("foo");   // Returns: false
    bool = is_range([3:5]);   // Returns: true

<br clear="all" /><br/>

---

### Function: valid\_range()

**Synopsis:** Returns true if the argument is a valid range.

**Topics:** [Type Checking](Topics#type-checking)

**See Also:** [typeof()](#function-typeof), [is\_type()](#function-is_type), [is\_str()](#function-is_str), [is\_def()](#function-is_def), [is\_int()](#function-is_int), [is\_range()](#function-is_range)

**Usage:** 

- bool = valid_range(x);

**Description:** 

Returns true if its argument is a valid range (deprecated ranges excluded).

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`x`                  | value to check

**Example 1:** 

    include <BOSL2/std.scad>
    bool = is_range(undef);   // Returns: false
    bool = is_range(false);   // Returns: false
    bool = is_range(42);      // Returns: false
    bool = is_range([3,4,5]); // Returns: false
    bool = is_range("foo");   // Returns: false
    bool = is_range([3:5]);   // Returns: true
    bool = is_range([3:1]);   // Returns: false

<br clear="all" /><br/>

---

### Function: is\_func()

**Synopsis:** Returns true if the argument is a function literal.

**Topics:** [Type Checking](Topics#type-checking), [Function Literals](Topics#function-literals)

**Usage:** 

- bool = is_func(x);

**Description:** 

Returns true if OpenSCAD supports function literals, and the given item is one.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`x`                  | The value to check

**Example 1:** 

    include <BOSL2/std.scad>
    f = function (a) a==2;
    bool = is_func(f);  // Returns: true

<br clear="all" /><br/>

---

### Function: is\_consistent()

**Synopsis:** Returns true if the argument is a list with consistent structure and finite numerical data.

**Topics:** [Type Checking](Topics#type-checking), [Testing](Topics#testing)

**See Also:** [typeof()](#function-typeof), [is\_type()](#function-is_type), [is\_str()](#function-is_str), [is\_def()](#function-is_def), [is\_int()](#function-is_int), [is\_range()](#function-is_range), [is\_homogeneous()](lists.scad#function-is_homogeneous)

**Usage:** 

- bool = is_consistent(list, [pattern]);

**Description:** 

Tests whether input is a list of entries which all have the same list structure
and are filled with finite numerical data.  You can optionally specify a required
list structure with the pattern argument.
It returns `true` for the empty list regardless the value of the `pattern`.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`list`               | list to check
`pattern`            | optional pattern required to match

**Example 1:** 

    include <BOSL2/std.scad>
    is_consistent([3,4,5]);              // Returns true
    is_consistent([[3,4],[4,5],[6,7]]);  // Returns true
    is_consistent([[3,4,5],[3,4]]);      // Returns false
    is_consistent([[3,[3,4,[5]]], [5,[2,9,[9]]]]); // Returns true
    is_consistent([[3,[3,4,[5]]], [5,[2,9,9]]]);   // Returns false
    is_consistent([3,4,5], 0);            // Returns true
    is_consistent([3,4,undef], 0);        // Returns false
    is_consistent([[3,4],[4,5]], [1,1]);  // Returns true
    is_consistent([[3,"a"],[4,true]], [1,undef]);  // Returns true
    is_consistent([[3,4], 6, [4,5]], [1,1]);  // Returns false
    is_consistent([[1,[3,4]], [4,[5,6]]], [1,[2,3]]);    // Returns true
    is_consistent([[1,[3,INF]], [4,[5,6]]], [1,[2,3]]);  // Returns false
    is_consistent([], [1,[2,3]]);                        // Returns true

<br clear="all" /><br/>

---

### Function: same\_shape()

**Synopsis:** Returns true if the argument lists are numeric and of the same shape.

**Topics:** [Type Checking](Topics#type-checking), [Testing](Topics#testing)

**See Also:** [is\_homogeneous()](lists.scad#function-is_homogeneous), [is\_consistent()](#function-is_consistent)

**Usage:** 

- bool = same_shape(a,b);

**Description:** 

Tests whether the inputs `a` and `b` are both numeric and are the same shaped list.

**Example 1:** 

    include <BOSL2/std.scad>
    same_shape([3,[4,5]],[7,[3,4]]);   // Returns true
    same_shape([3,4,5], [7,[3,4]]);    // Returns false

<br clear="all" /><br/>

---

### Function: is\_bool\_list()

**Synopsis:** Returns true if the argument list contains only booleans.

**Topics:** [Boolean Testing](Topics#boolean-testing)

**See Also:** [is\_homogeneous()](lists.scad#function-is_homogeneous), [is\_consistent()](#function-is_consistent)

**Usage:** 

- check = is_bool_list(list,[length])

**Description:** 

Tests whether input is a list containing only booleans, and optionally checks its length.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`list`               | list to test
`length`             | if given, list must be this length

---

## Section: Boolean list testing


### Function: any()

**Synopsis:** Returns true if any item in the argument list is true.

**Topics:** [Type Checking](Topics#type-checking)

**See Also:** [all()](#function-all), [num\_true()](#function-num_true)

**Usage:** 

- bool = any(l);
- bool = any(l, func);   // Requires OpenSCAD 2021.01 or later.

**Requirements:** 

- Requires OpenSCAD 2021.01 or later to use the `func` argument.

**Description:** 

Returns true if any item in list `l` evaluates as true.
If `func` is given then returns true if the function evaluates as true on any list entry.
Items that evaluate as true include nonempty lists, nonempty strings, and nonzero numbers.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`l`                  | The list to test for true items.
`func`               | An optional function literal of signature (x), returning bool, to test each list item with.

**Example 1:** 

    include <BOSL2/std.scad>
    any([0,false,undef]);  // Returns false.
    any([1,false,undef]);  // Returns true.
    any([1,5,true]);       // Returns true.
    any([[0,0], [0,0]]);   // Returns true.
    any([[0,0], [1,0]]);   // Returns true.

<br clear="all" /><br/>

---

### Function: all()

**Synopsis:** Returns true if all items in the argument list are true.

**Topics:** [Type Checking](Topics#type-checking)

**See Also:** [any()](#function-any), [num\_true()](#function-num_true)

**Usage:** 

- bool = all(l);
- bool = all(l, func);   // Requires OpenSCAD 2021.01 or later.

**Requirements:** 

- Requires OpenSCAD 2021.01 or later to use the `func` argument.

**Description:** 

Returns true if all items in list `l` evaluate as true.
If `func` is given then returns true if the function evaluates as true on all list etnries.
Items that evaluate as true include nonempty lists, nonempty strings, and nonzero numbers.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`l`                  | The list to test for true items.
`func`               | An optional function literal of signature (x), returning bool, to test each list item with.

**Example 1:** 

    include <BOSL2/std.scad>
    test1 = all([0,false,undef]);  // Returns false.
    test2 = all([1,false,undef]);  // Returns false.
    test3 = all([1,5,true]);       // Returns true.
    test4 = all([[0,0], [0,0]]);   // Returns true.
    test5 = all([[0,0], [1,0]]);   // Returns true.
    test6 = all([[1,1], [1,1]]);   // Returns true.

<br clear="all" /><br/>

---

### Function: num\_true()

**Synopsis:** Returns the number of true entries in the arguemnt list.

**Topics:** [Boolean Testing](Topics#boolean-testing)

**See Also:** [any()](#function-any), [all()](#function-all)

**Usage:** 

- seq = num_true(l);
- seq = num_true(l, func);  // Requires OpenSCAD 2021.01 or later.

**Requirements:** 

- Requires OpenSCAD 2021.01 or later to use the `func=` argument.

**Description:** 

Returns the number of items in `l` that evaluate as true.  If `func` is given then counts
list entries where the function evaluates as true.
Items that evaluate as true include nonempty lists, nonempty strings, and nonzero numbers.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`l`                  | The list to test for true items.
`func`               | An optional function literal of signature (x), returning bool, to test each list item with.

**Example 1:** 

    include <BOSL2/std.scad>
    num1 = num_true([0,false,undef]);  // Returns 0.
    num2 = num_true([1,false,undef]);  // Returns 1.
    num3 = num_true([1,5,false]);      // Returns 2.
    num4 = num_true([1,5,true]);       // Returns 3.
    num5 = num_true([[0,0], [0,0]]);   // Returns 2.
    num6 = num_true([[], [1,0]]);      // Returns 1.

<br clear="all" /><br/>

---

## Section: Handling `undef`s.


### Function: default()

**Synopsis:** Returns a default value if the argument is 'undef', else returns the argument.

**Topics:** [Undef Handling](Topics#undef-handling)

**See Also:** [first\_defined()](#function-first_defined), [one\_defined()](#function-one_defined), [num\_defined()](#function-num_defined)

**Usage:** 

- val = default(val, dflt);

**Description:** 

Returns the value given as `v` if it is not `undef`.
Otherwise, returns the value of `dflt`.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`v`                  | Value to pass through if not `undef`.
`dflt`               | Value to return if `v` *is* `undef`.  Default: undef

---

### Function: first\_defined()

**Synopsis:** Returns the first value in the argument list that is not 'undef'.

**Topics:** [Undef Handling](Topics#undef-handling)

**See Also:** [default()](#function-default), [one\_defined()](#function-one_defined), [num\_defined()](#function-num_defined), [any\_defined()](#function-any_defined), [all\_defined()](#function-all_defined)

**Usage:** 

- val = first_defined(v, [recursive]);

**Description:** 

Returns the first item in the list that is not `undef`.
If all items are `undef`, or list is empty, returns `undef`.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`v`                  | The list whose items are being checked.
`recursive`          | If true, sublists are checked recursively for defined values.  The first sublist that has a defined item is returned.  Default: false

**Example 1:** 

    include <BOSL2/std.scad>
    val = first_defined([undef,7,undef,true]);  // Returns: 7

<br clear="all" /><br/>

---

### Function: one\_defined()

**Synopsis:** Returns the defined value in the argument list if only a single value is defined.

**Topics:** [Undef Handling](Topics#undef-handling)

**See Also:** [default()](#function-default), [first\_defined()](#function-first_defined), [num\_defined()](#function-num_defined), [any\_defined()](#function-any_defined), [all\_defined()](#function-all_defined)

**Usage:** 

- val = one_defined(vals, names, [dflt])

**Description:** 

Examines the input list `vals` and returns the entry which is not `undef`.
If more than one entry is not `undef` then an error is asserted, specifying
"Must define exactly one of" followed by the names in the `names` parameter.
If `dflt` is given, and all `vals` are `undef`, then the value in `dflt` is returned.
If `dflt` is *not* given, and all `vals` are `undef`, then an error is asserted.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`vals`               | The values to return the first one which is not `undef`.
`names`              | A string with comma-separated names for the arguments whose values are passed in `vals`.
`dflt`               | If given, the value returned if all `vals` are `undef`.

**Example 1:** 

    include <BOSL2/std.scad>
    length1 = one_defined([length,L,l], ["length","L","l"]);
    length2 = one_defined([length,L,l], "length,L,l", dflt=1);

<br clear="all" /><br/>

---

### Function: num\_defined()

**Synopsis:** Returns the number of defined values in the the argument list.

**Topics:** [Undef Handling](Topics#undef-handling)

**See Also:** [default()](#function-default), [first\_defined()](#function-first_defined), [one\_defined()](#function-one_defined), [any\_defined()](#function-any_defined), [all\_defined()](#function-all_defined)

**Usage:** 

- cnt = num_defined(v);

**Description:** 

Counts how many items in list `v` are not `undef`.

**Example 1:** 

    include <BOSL2/std.scad>
    cnt = num_defined([3,7,undef,2,undef,undef,1]);  // Returns: 4

<br clear="all" /><br/>

---

### Function: any\_defined()

**Synopsis:** Returns true if any item in the argument list is not `undef`.

**Topics:** [Undef Handling](Topics#undef-handling)

**See Also:** [default()](#function-default), [first\_defined()](#function-first_defined), [one\_defined()](#function-one_defined), [num\_defined()](#function-num_defined), [all\_defined()](#function-all_defined)

**Usage:** 

- bool = any_defined(v, [recursive]);

**Description:** 

Returns true if any item in the given array is not `undef`.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`v`                  | The list whose items are being checked.
`recursive`          | If true, any sublists are evaluated recursively.  Default: false

**Example 1:** 

    include <BOSL2/std.scad>
    bool = any_defined([undef,undef,undef]);    // Returns: false
    bool = any_defined([undef,42,undef]);       // Returns: true
    bool = any_defined([34,42,87]);             // Returns: true
    bool = any_defined([undef,undef,[undef]]);  // Returns: true
    bool = any_defined([undef,undef,[undef]],recursive=true);  // Returns: false
    bool = any_defined([undef,undef,[42]],recursive=true);     // Returns: true

<br clear="all" /><br/>

---

### Function: all\_defined()

**Synopsis:** Returns true if all items in the given array are defined.

**Topics:** [Undef Handling](Topics#undef-handling)

**See Also:** [default()](#function-default), [first\_defined()](#function-first_defined), [one\_defined()](#function-one_defined), [num\_defined()](#function-num_defined)

**Usage:** 

- bool = all_defined(v, [recursive]);

**Description:** 

Returns true if all items in the given array are not `undef`.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`v`                  | The list whose items are being checked.
`recursive`          | If true, any sublists are evaluated recursively.  Default: false

**Example 1:** 

    include <BOSL2/std.scad>
    bool = all_defined([undef,undef,undef]);    // Returns: false
    bool = all_defined([undef,42,undef]);       // Returns: false
    bool = all_defined([34,42,87]);             // Returns: true
    bool = all_defined([23,34,[undef]]);        // Returns: true
    bool = all_defined([23,34,[undef]],recursive=true);  // Returns: false
    bool = all_defined([23,34,[42]],recursive=true);     // Returns: true

<br clear="all" /><br/>

---

## Section: Undef Safe Arithmetic


### Function: u\_add()

**Synopsis:** Returns the sum of 2 numbers if both are defined, otherwise returns undef.

**Topics:** [Undef Handling](Topics#undef-handling)

**See Also:** [u\_sub()](#function-u_sub), [u\_mul()](#function-u_mul), [u\_div()](#function-u_div)

**Usage:** 

- x = u_add(a, b);

**Description:** 

Adds `a` to `b`, returning the result, or undef if either value is `undef`.
This emulates the way undefs used to be handled in versions of OpenSCAD before 2020.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`a`                  | First value.
`b`                  | Second value.

---

### Function: u\_sub()

**Synopsis:** Returns the difference of 2 numbers if both are defined, otherwise returns undef.

**Topics:** [Undef Handling](Topics#undef-handling)

**See Also:** [u\_add()](#function-u_add), [u\_mul()](#function-u_mul), [u\_div()](#function-u_div)

**Usage:** 

- x = u_sub(a, b);

**Description:** 

Subtracts `b` from `a`, returning the result, or undef if either value is `undef`.
This emulates the way undefs used to be handled in versions of OpenSCAD before 2020.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`a`                  | First value.
`b`                  | Second value.

---

### Function: u\_mul()

**Synopsis:** Returns the product of 2 numbers if both are defined, otherwise returns undef.

**Topics:** [Undef Handling](Topics#undef-handling)

**See Also:** [u\_add()](#function-u_add), [u\_sub()](#function-u_sub), [u\_div()](#function-u_div)

**Usage:** 

- x = u_mul(a, b);

**Description:** 

Multiplies `a` by `b`, returning the result, or undef if either value is `undef`.
This emulates the way undefs used to be handled in versions of OpenSCAD before 2020.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`a`                  | First value.
`b`                  | Second value.

---

### Function: u\_div()

**Synopsis:** Returns the quotient of 2 numbers if both are defined, otherwise returns undef.

**Topics:** [Undef Handling](Topics#undef-handling)

**See Also:** [u\_add()](#function-u_add), [u\_sub()](#function-u_sub), [u\_mul()](#function-u_mul)

**Usage:** 

- x = u_div(a, b);

**Description:** 

Divides `a` by `b`, returning the result, or undef if either value is `undef`.
This emulates the way undefs used to be handled in versions of OpenSCAD before 2020.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`a`                  | First value.
`b`                  | Second value.

---

## Section: Processing Arguments to Functions and Modules


### Function: get\_anchor()

**Synopsis:** Returns the correct anchor from `anchor` and `center`.

**Topics:** [Argument Handling](Topics#argument-handling)

**See Also:** [get\_radius()](#function-get_radius)

**Usage:** 

- anchr = get_anchor(anchor,center,[uncentered],[dflt]);

**Description:** 

Calculated the correct anchor from `anchor` and `center`.  In order:
- If `center` is not `undef` and `center` evaluates as true, then `CENTER` (`[0,0,0]`) is returned.
- Otherwise, if `center` is not `undef` and `center` evaluates as false, then the value of `uncentered` is returned.
- Otherwise, if `anchor` is not `undef`, then the value of `anchor` is returned.
- Otherwise, the value of `dflt` is returned.

This ordering ensures that `center` will override `anchor`.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`anchor`             | The anchor name or vector.
`center`             | If not `undef`, this overrides the value of `anchor`.
`uncentered`         | The value to return if `center` is not `undef` and evaluates as false.  Default: BOTTOM
`dflt`               | The default value to return if both `anchor` and `center` are `undef`.  Default: `CENTER`

**Example 1:** 

    include <BOSL2/std.scad>
    anchr1 = get_anchor(undef, undef, BOTTOM, TOP);  // Returns: [0, 0, 1] (TOP)
    anchr2 = get_anchor(RIGHT, undef, BOTTOM, TOP);  // Returns: [1, 0, 0] (RIGHT)
    anchr3 = get_anchor(undef, false, BOTTOM, TOP);  // Returns: [0, 0,-1] (BOTTOM)
    anchr4 = get_anchor(RIGHT, false, BOTTOM, TOP);  // Returns: [0, 0,-1] (BOTTOM)
    anchr5 = get_anchor(undef, true,  BOTTOM, TOP);  // Returns: [0, 0, 0] (CENTER)
    anchr6 = get_anchor(RIGHT, true,  BOTTOM, TOP);  // Returns: [0, 0, 0] (CENTER)

<br clear="all" /><br/>

---

### Function: get\_radius()

**Synopsis:** Given various radii and diameters, returns the most specific radius.

**Topics:** [Argument Handling](Topics#argument-handling)

**See Also:** [get\_anchor()](#function-get_anchor)

**Usage:** 

- r = get_radius([r1=], [r2=], [r=], [d1=], [d2=], [d=], [dflt=]);

**Description:** 

Given various radii and diameters, returns the most specific radius.  If a diameter is most
specific, returns half its value, giving the radius.  If no radii or diameters are defined,
returns the value of `dflt`.  Value specificity order is `r1`, `r2`, `d1`, `d2`, `r`, `d`,
then `dflt`.  Only one of `r1`, `r2`, `d1`, or `d2` can be defined at once, or else it errors
out, complaining about conflicting radius/diameter values.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`r1`                 | Most specific radius.
`r2`                 | Second most specific radius.
`r`                  | Most general radius.
`d1`                 | Most specific diameter.
`d2`                 | Second most specific diameter.
`d`                  | Most general diameter.
`dflt`               | Value to return if all other values given are `undef`.

**Example 1:** 

    include <BOSL2/std.scad>
    r = get_radius(r1=undef, r=undef, dflt=undef);  // Returns: undef
    r = get_radius(r1=undef, r=undef, dflt=1);      // Returns: 1
    r = get_radius(r1=undef, r=6, dflt=1);          // Returns: 6
    r = get_radius(r1=7, r=6, dflt=1);              // Returns: 7
    r = get_radius(r1=undef, r2=8, r=6, dflt=1);    // Returns: 8
    r = get_radius(r1=undef, r2=8, d=6, dflt=1);    // Returns: 8
    r = get_radius(r1=undef, d=6, dflt=1);          // Returns: 3
    r = get_radius(d1=7, d=6, dflt=1);              // Returns: 3.5
    r = get_radius(d1=7, d2=8, d=6, dflt=1);        // Returns: 3.5
    r = get_radius(d1=undef, d2=8, d=6, dflt=1);    // Returns: 4
    r = get_radius(r1=8, d=6, dflt=1);              // Returns: 8

<br clear="all" /><br/>

---

### Function: scalar\_vec3()

**Synopsis:** Expands a scalar or a list with length less than 3 to a length 3 vector.

**Topics:** [Argument Handling](Topics#argument-handling)

**See Also:** [get\_anchor()](#function-get_anchor), [get\_radius()](#function-get_radius), [force\_list()](lists.scad#function-force_list)

**Usage:** 

- vec = scalar_vec3(v, [dflt]);

**Description:** 

This is expands a scalar or a list with length less than 3 to a length 3 vector in the
same way that OpenSCAD expands short vectors in some contexts, e.g. cube(10) or rotate([45,90]).
If `v` is a scalar, and `dflt==undef`, returns `[v, v, v]`.
If `v` is a scalar, and `dflt!=undef`, returns `[v, dflt, dflt]`.
if `v` is a list of length 3 or more then returns `v`
If `v` is a list and dflt is defined, returns a length 3 list by padding with `dflt`
If `v` is a list and dflt is undef, returns a length 3 list by padding with 0
If `v` is `undef`, returns `undef`.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`v`                  | Value to return vector from.
`dflt`               | Default value to set empty vector parts from.

**Example 1:** 

    include <BOSL2/std.scad>
    vec = scalar_vec3(undef);      // Returns: undef
    vec = scalar_vec3(10);         // Returns: [10,10,10]
    vec = scalar_vec3(10,1);       // Returns: [10,1,1]
    vec = scalar_vec3([10,10],1);  // Returns: [10,10,1]
    vec = scalar_vec3([10,10]);    // Returns: [10,10,0]
    vec = scalar_vec3([10]);       // Returns: [10,0,0]

<br clear="all" /><br/>

---

### Function: segs()

**Synopsis:** Returns the number of sides for a circle given `$fn`, `$fa`, and `$fs`.

**Topics:** [Geometry](Topics#geometry)

**See Also:** [circle()](shapes2d.scad#functionmodule-circle), [cyl()](shapes3d.scad#functionmodule-cyl)

**Usage:** 

- sides = segs(r, [angle]);

**Description:** 

Calculate the standard number of sides OpenSCAD would give a circle based on `$fn`, `$fa`, and `$fs`.
If angle is given, calculate for an arc of the given angle.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`r`                  | Radius of circle/arc to get the number of segments for.
`angle`              | Angle of arc to get the get the number of segments for.

**Example 1:** 

    include <BOSL2/std.scad>
    $fn=12; sides=segs(10);           // Returns: 12
    $fa=2; $fs=3; sides=segs(10);     // Returns: 21
    $fa=2; $fs=3; sides=segs(10,180); // Returns: 11

<br clear="all" /><br/>

---

### Module: no\_children()

**Synopsis:** Assert that the calling module does not support children.

**Topics:** [Error Checking](Topics#error-checking)

**See Also:** [no\_function()](#function-no_function), [no\_module()](#module-no_module), [req\_children()](#module-req_children)

**Usage:** 

- no_children($children);

**Description:** 

Assert that the calling module does not support children.  Prints an error message to this effect and fails if children are present,
as indicated by its argument.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`$children`          | number of children the module has.

**Example 1:** 

    include <BOSL2/std.scad>
    module foo() {
        no_children($children);
    }

<br clear="all" /><br/>

---

### Module: req\_children()

**Synopsis:** Assert that the calling module requires children.

**Topics:** [Error Checking](Topics#error-checking)

**See Also:** [no\_function()](#function-no_function), [no\_module()](#module-no_module)

**Usage:** 

- req_children($children);

**Description:** 

Assert that the calling module requires children.  Prints an error message and fails if no
children are present as indicated by its argument.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`$children`          | number of children the module has.

**Example 1:** 

    include <BOSL2/std.scad>
    module foo() {
        req_children($children);
    }

<br clear="all" /><br/>

---

### Function: no\_function()

**Synopsis:** Assert that the argument exists only as a module and not as a function.

**Topics:** [Error Checking](Topics#error-checking)

**See Also:** [no\_children()](#module-no_children), [no\_module()](#module-no_module)

**Usage:** 

- dummy = no_function(name)

**Description:** 

Asserts that the function, "name", only exists as a module.

**Example 1:** 

    include <BOSL2/std.scad>
    x = no_function("foo");

<br clear="all" /><br/>

---

### Module: no\_module()

**Synopsis:** Assert that the argument exists only as a function and not as a module.

**Topics:** [Error Checking](Topics#error-checking)

**See Also:** [no\_children()](#module-no_children), [no\_function()](#function-no_function)

**Usage:** 

- no_module();

**Description:** 

Asserts that the called module exists only as a function.

**Example 1:** 

    include <BOSL2/std.scad>
    module foo() { no_module(); }

<br clear="all" /><br/>

---

### Module: deprecate()

**Synopsis:** Display a console note that a module is deprecated and suggest a replacement.

**Topics:** [Error Checking](Topics#error-checking)

**See Also:** [no\_function()](#function-no_function), [no\_module()](#module-no_module)

**Usage:** 

- deprecate(new_name);

**Description:** 

Display info that the current module is deprecated and you should switch to a new name

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`new_name`           | name of the new module that replaces the old one

---

### Module: echo\_viewport()

**Synopsis:** Display the current viewport parameters.

**Usage:** 

- echo_viewport();

**Description:** 

Display the current viewport parameters so that they can be pasted into examples for the wiki.
The viewport should have a 4:3 aspect ratio to ensure proper framing of the object.

---

## Section: Testing Helpers


### Module: assert\_approx()

**Synopsis:** Assert that a value is approximately what was expected.

**Topics:** [Error Checking](Topics#error-checking), [Debugging](Topics#debugging)

**See Also:** [no\_children()](#module-no_children), [no\_function()](#function-no_function), [no\_module()](#module-no_module), [assert\_equal()](#module-assert_equal)

**Usage:** 

- assert_approx(got, expected, [info]);

**Description:** 

Tests if the value gotten is what was expected, plus or minus 1e-9.  If not, then
the expected and received values are printed to the console and
an assertion is thrown to stop execution.
Returns false if both 'got' and 'expected' are 'nan'.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`got`                | The value actually received.
`expected`           | The value that was expected.
`info`               | Extra info to print out to make the error clearer.

**Example 1:** 

    include <BOSL2/std.scad>
    assert_approx(1/3, 0.333333333333333, str("number=",1,", denom=",3));

<br clear="all" /><br/>

---

### Module: assert\_equal()

**Synopsis:** Assert that a value is expected.

**Topics:** [Error Checking](Topics#error-checking), [Debugging](Topics#debugging)

**See Also:** [no\_children()](#module-no_children), [no\_function()](#function-no_function), [no\_module()](#module-no_module), [assert\_approx()](#module-assert_approx)

**Usage:** 

- assert_equal(got, expected, [info]);

**Description:** 

Tests if the value gotten is what was expected.  If not, then the expected and received values
are printed to the console and an assertion is thrown to stop execution.
Returns true if both 'got' and 'expected' are 'nan'.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`got`                | The value actually received.
`expected`           | The value that was expected.
`info`               | Extra info to print out to make the error clearer.

**Example 1:** 

    include <BOSL2/std.scad>
    assert_equal(3*9, 27, str("a=",3,", b=",9));

<br clear="all" /><br/>

---

### Module: shape\_compare()

**Synopsis:** Compares two child shapes. <sup title="Can return geometry.">[<abbr>Geom</abbr>]</sup>

**Topics:** [Error Checking](Topics#error-checking), [Debugging](Topics#debugging), [Testing](Topics#testing)

**See Also:** [assert\_approx()](#module-assert_approx), [assert\_equal()](#module-assert_equal)

**Usage:** 

- shape_compare([eps]) {TEST_SHAPE; EXPECTED_SHAPE;}

**Description:** 

Compares two child shapes, returning empty geometry if they are very nearly the same shape and size.
Returns the differential geometry if they are not quite the same shape and size.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`eps`                | The surface of the two shapes must be within this size of each other.  Default: 1/1024

**Example 1:** (Example disabled because OpenSCAD bug prevents it from displaying)

    include <BOSL2/std.scad>
    $fn=36;
    shape_compare() {
        sphere(d=100);
        rotate_extrude() right_half(planar=true) circle(d=100);
    }

<br clear="all" /><br/>

---

## Section: C-Style For Loop Helpers

You can use a list comprehension with a C-style for loop to iteratively make a calculation.

The syntax is: `[for (INIT; CONDITION; NEXT) RETVAL]` where:
- INIT is zero or more `let()` style assignments that are evaluated exactly one time, before the first loop.
- CONDITION is an expression evaluated at the start of each loop.  If true, continues with the loop.
- RETVAL is an expression that returns a list item for each loop.
- NEXT is one or more `let()` style assignments that is evaluated at the end of each loop.

Since the INIT phase is only run once, and the CONDITION and RETVAL expressions cannot update
variables, that means that only the NEXT phase can be used for iterative calculations.
Unfortunately, the NEXT phase runs *after* the RETVAL expression, which means that you need
to run the loop one extra time to return the final value.  This tends to make the loop code
look rather ugly.  The `looping()`, `loop_while()` and `loop_done()` functions
can make this somewhat more legible.

```openscad
function flat_sum(l) = [
    for (
        i = 0,
        total = 0,
        state = 0;

        looping(state);

        state = loop_while(state, i < len(l)),
        total = total +
            loop_done(state) ? 0 :
            let( x = l[i] )
            is_list(x) ? flat_sum(x) : x,
        i = i + 1
    ) if (loop_done(state)) total;
].x;
```

### Function: looping()

**Synopsis:** Returns true if the argument indicates the current C-style loop should continue.

**Topics:** [Iteration](Topics#iteration)

**See Also:** [loop\_while()](#function-loop_while), [loop\_done()](#function-loop_done)

**Usage:** 

- bool = looping(state);

**Description:** 

Returns true if the `state` value indicates the current loop should continue.  This is useful
when using C-style for loops to iteratively calculate a value.  Used with `loop_while()` and
`loop_done()`.  See [Looping Helpers](utility.scad#section-c-style-for-loop-helpers) for an example.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`state`              | The loop state value.

---

### Function: loop\_while()

**Synopsis:** Returns true if both arguments indicate the current C-style loop should continue.

**Topics:** [Iteration](Topics#iteration)

**See Also:** [looping()](#function-looping), [loop\_done()](#function-loop_done)

**Usage:** 

- state = loop_while(state, continue);

**Description:** 

Given the current `state`, and a boolean `continue` that indicates if the loop should still be
continuing, returns the updated state value for the the next loop.  This is useful when using
C-style for loops to iteratively calculate a value.  Used with `looping()` and `loop_done()`.
See [Looping Helpers](utility.scad#section-c-style-for-loop-helpers) for an example.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`state`              | The loop state value.
`continue`           | A boolean value indicating whether the current loop should progress.

---

### Function: loop\_done()

**Synopsis:** Returns true if the argument indicates the current C-style loop is finishing.

**Topics:** [Iteration](Topics#iteration)

**See Also:** [looping()](#function-looping), [loop\_while()](#function-loop_while)

**Usage:** 

- bool = loop_done(state);

**Description:** 

Returns true if the `state` value indicates the loop is finishing.  This is useful when using
C-style for loops to iteratively calculate a value.  Used with `looping()` and `loop_while()`.
See [Looping Helpers](utility.scad#section-c-style-for-loop-helpers) for an example.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`state`              | The loop state value.

---


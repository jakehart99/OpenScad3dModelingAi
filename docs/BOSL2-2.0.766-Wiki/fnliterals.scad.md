# LibFile: fnliterals.scad

Handlers for function literals, and Function literal generators.

To use, add the following lines to the beginning of your file:

    include <BOSL2/std.scad>
    include <BOSL2/fnliterals.scad>

## File Contents

1. [Section: Function Literal Algorithms](#section-function-literal-algorithms)
    - [`map()`](#function-map) – Applies a function to each item in a list.
    - [`filter()`](#function-filter) – Returns just the list items which the given function returns true for.
    - [`reduce()`](#function-reduce) – Applies a 2-arg function cumulatively to the items of a list, returning the final result.
    - [`accumulate()`](#function-accumulate) – Applies a 2-arg function cumulatively to the items of a list, returning a list of every result.
    - [`while()`](#function-while) – While a `cond` function returns true, iteratively calls a work function, returning the final result.
    - [`for_n()`](#function-for_n) – Iteratively calls a work function `n` times, returning the final result.
    - [`find_all()`](#function-find_all) – Returns the indices of all items in a list that a given function returns true for.
    - [`find_first()`](#function-find_first) – Returns the index of the first item in a list, after `start`, that a given function returns true for.
    - [`binsearch()`](#function-binsearch) – Does a binary search of a sorted list to find the index of a given value.
    - [`simple_hash()`](#function-simple_hash) – Returns an integer hash of a given value.
    - [`hashmap()`](#function-hashmap) – Creates a hashmap manipulation function.

2. [Section: Function Meta-Generators](#section-function-meta-generators)
    - [`f_1arg()`](#function-f_1arg) – Creates a factory for a 2-arg function literal, where you can optionally pre-fill the arg.
    - [`f_2arg()`](#function-f_2arg) – Creates a factory for a 2-arg function literal, where you can optionally pre-fill the args.
    - [`f_2arg_simple()`](#function-f_2arg_simple) – Creates a factory for a 2-arg function literal, where you can optionally pre-fill the args.
    - [`f_3arg()`](#function-f_3arg) – Creates a factory for a 3-arg function literal, where you can optionally pre-fill the args.
    - [`ival()`](#function-ival) – Generates a function with signature `(i,x)` that calls `func(i)`
    - [`xval()`](#function-xval) – Generates a function with signature `(i,x)` that calls `func(x)`

3. [Section: Comparator Generators](#section-comparator-generators)
    - [`f_cmp()`](#function-f_cmp) – Returns a function to compare values.
    - [`f_gt()`](#function-f_gt) – Returns a function to compare if `a` is greater than `b`.
    - [`f_lt()`](#function-f_lt) – Returns a function to compare if `a` is less than `b`.
    - [`f_gte()`](#function-f_gte) – Returns a function to compare if `a` is greater than or equal to `b`.
    - [`f_lte()`](#function-f_lte) – Returns a function to compare if `a` is less than or equal to `b`.
    - [`f_eq()`](#function-f_eq) – Returns a function to compare if `a` is exactly equal to `b`.
    - [`f_neq()`](#function-f_neq) – Returns a function to compare if `a` is not exactly equal to `b`.
    - [`f_approx()`](#function-f_approx) – Returns a function to compare if `a` is approximately equal to `b`.
    - [`f_napprox()`](#function-f_napprox) – Returns a function to compare if `a` is not approximately equal to `b`.

4. [Section: Logic Operators](#section-logic-operators)
    - [`f_or()`](#function-f_or) – Returns a function to check if either `a` or `b` is true.
    - [`f_and()`](#function-f_and) – Returns a function to check if both `a` and `b` are true.
    - [`f_nor()`](#function-f_nor) – Returns a function to check if neither `a` nor `b` are true.
    - [`f_nand()`](#function-f_nand) – Returns a function to check if `a` and `b` are not both true.
    - [`f_xor()`](#function-f_xor) – Returns a function to check if either `a` or `b`, but not both, are true.
    - [`f_not()`](#function-f_not) – Returns a function to check if `a` is not true.
    - [`f_even()`](#function-f_even) – Returns a function to check if `a` is an even number.
    - [`f_odd()`](#function-f_odd) – Returns a function to check if `a` is an odd number.

5. [Section: Math Operators](#section-math-operators)
    - [`f_add()`](#function-f_add) – Returns a function to add `a` and `b`.
    - [`f_sub()`](#function-f_sub) – Returns a function to subtract `a` from `b`.
    - [`f_mul()`](#function-f_mul) – Returns a function to multiply `a` by `b`.
    - [`f_div()`](#function-f_div) – Returns a function to divide `a` by `b`.
    - [`f_mod()`](#function-f_mod) – Returns a function to calculate the modulo of `a` divided by `b`.
    - [`f_pow()`](#function-f_pow) – Returns a function to calculate `a` to the power of `b`.
    - [`f_neg()`](#function-f_neg) – Returns a function to calculate `-a`

6. [Section: Min/Max Operators](#section-minmax-operators)
    - [`f_min()`](#function-f_min) – Returns a function to calculate the minimum value of a list.
    - [`f_max()`](#function-f_max) – Returns a function to calculate the maximum value of a list.
    - [`f_min2()`](#function-f_min2) – Returns a function to calculate the minimum of two values.
    - [`f_max2()`](#function-f_max2) – Returns a function to calculate the maximum of two values.
    - [`f_min3()`](#function-f_min3) – Returns a function to calculate the minimum of three values.
    - [`f_max3()`](#function-f_max3) – Returns a function to calculate the maximum of three values.

7. [Section: Trigonometry Operators](#section-trigonometry-operators)
    - [`f_sin()`](#function-f_sin) – Returns a function to calculate the sine of a value.
    - [`f_cos()`](#function-f_cos) – Returns a function to calculate the cosine of a value.
    - [`f_tan()`](#function-f_tan) – Returns a function to calculate the tangent of a value.
    - [`f_asin()`](#function-f_asin) – Returns a function to calculate the arcsine of a value.
    - [`f_acos()`](#function-f_acos) – Returns a function to calculate the arccosine of a value.
    - [`f_atan()`](#function-f_atan) – Returns a function to calculate the arctangent of a value.
    - [`f_atan2()`](#function-f_atan2) – Returns a function to calculate the arctangent of `y` and `x`

8. [Section: String Operators](#section-string-operators)
    - [`f_len()`](#function-f_len) – Returns a function to calculate the length of a string or list.
    - [`f_chr()`](#function-f_chr) – Returns a function to get a string character from its ordinal number.
    - [`f_ord()`](#function-f_ord) – Returns a function to get the ordinal number of a string character.
    - [`f_str()`](#function-f_str) – Returns a function to get the string representation of an arbitrary value.
    - [`f_str2()`](#function-f_str2) – Returns a function to concatenate the string representations of two arbitrary values.
    - [`f_str3()`](#function-f_str3) – Returns a function to concatenate the string representations of three arbitrary values.

9. [Section: Miscellaneous Operators](#section-miscellaneous-operators)
    - [`f_floor()`](#function-f_floor) – Returns a function to calculate the integer floor of a given number.
    - [`f_round()`](#function-f_round) – Returns a function to calculate the integer rounding of a given number.
    - [`f_ceil()`](#function-f_ceil) – Returns a function to calculate the integer ceiling of a given number.
    - [`f_abs()`](#function-f_abs) – Returns a function to calculate the absolute value of a given number.
    - [`f_sign()`](#function-f_sign) – Returns a function to calculate the sign of a given number.
    - [`f_ln()`](#function-f_ln) – Returns a function to calculate the natural logarithm of a given number.
    - [`f_log()`](#function-f_log) – Returns a function to calculate the base 10 logarithm of a given number.
    - [`f_exp()`](#function-f_exp) – Returns a function to calculate the natural exponent of a given number.
    - [`f_sqr()`](#function-f_sqr) – Returns a function to calculate the square of a given number.
    - [`f_sqrt()`](#function-f_sqrt) – Returns a function to calculate the square root of a given number.
    - [`f_norm()`](#function-f_norm) – Returns a function to calculate the norm of a given vector.
    - [`f_cross()`](#function-f_cross) – Returns a function to calculate the norm of a given vector.

10. [Section: Type Queries](#section-type-queries)
    - [`f_is_def()`](#function-f_is_def) – Returns a function to determine if a value is not `undef`.
    - [`f_is_undef()`](#function-f_is_undef) – Returns a function to determine if a value is `undef`.
    - [`f_is_bool()`](#function-f_is_bool) – Returns a function to determine if a value is a boolean.
    - [`f_is_num()`](#function-f_is_num) – Returns a function to determine if a value is a number.
    - [`f_is_int()`](#function-f_is_int) – Returns a function to determine if a value is an integer number.
    - [`f_is_nan()`](#function-f_is_nan) – Returns a function to determine if a value is a number type that is Not a Number (NaN).
    - [`f_is_finite()`](#function-f_is_finite) – Returns a function to determine if a value is a number type that is finite.
    - [`f_is_string()`](#function-f_is_string) – Returns a function to determine if a value is a string.
    - [`f_is_list()`](#function-f_is_list) – Returns a function to determine if a value is a list.
    - [`f_is_range()`](#function-f_is_range) – Returns a function to determine if a value is a range.
    - [`f_is_function()`](#function-f_is_function) – Returns a function to determine if a value is a function literal.
    - [`f_is_vector()`](#function-f_is_vector) – Returns a function to determine if a value is a list of numbers.
    - [`f_is_path()`](#function-f_is_path) – Returns a function to determine if a value is a Path (a list of points).
    - [`f_is_region()`](#function-f_is_region) – Returns a function to determine if a value is a Region (a list of Paths).
    - [`f_is_vnf()`](#function-f_is_vnf) – Returns a function to determine if a value is a VNF structure.
    - [`f_is_bezier_patch()`](#function-f_is_bezier_patch) – Returns a function to determine if a value is a Bezier Patch structure.


## Section: Function Literal Algorithms


### Function: map()

**Synopsis:** Applies a function to each item in a list.

**Topics:** [Function Literals](Topics#function-literals), [Looping](Topics#looping)

**See Also:** [filter()](#function-filter), [reduce()](#function-reduce), [accumulate()](#function-accumulate), [while()](#function-while), [for\_n()](#function-for_n)

**Usage:** 

- lst = map(func, list);
- lst = map(function (x) x+1, list);

**Description:** 

Applies the function `func` to all items in `list`, returning the list of results.
In pseudo-code, this is effectively:
```
function map(func,list):
    out = [];
    foreach item in list:
        append func(item) to out;
    return out;
```

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`func`               | The function of signature (x) to evaluate for each item in `list`.
`list`               | The input list.

**Example 1:** 

    include <BOSL2/std.scad>
    include <BOSL2/fnliterals.scad>
    func = function(x) x*x;
    echo(map(func, [1,2,3,4]));
    // ECHO: [1,4,9,16]

<br clear="all" /><br/>

**Example 2:** 

    include <BOSL2/std.scad>
    include <BOSL2/fnliterals.scad>
    path = star(n=5,step=2,d=100);
    seglens = map(function (p) norm(p[1]-p[0]), pair(path,wrap=true));

<br clear="all" /><br/>

---

### Function: filter()

**Synopsis:** Returns just the list items which the given function returns true for.

**Topics:** [Function Literals](Topics#function-literals), [Looping](Topics#looping), [Filters](Topics#filters)

**See Also:** [map()](#function-map), [reduce()](#function-reduce), [accumulate()](#function-accumulate), [while()](#function-while), [for\_n()](#function-for_n), [find\_all()](#function-find_all)

**Usage:** 

- lst = filter(func, list);
- lst = filter(function (x) x>1, list);

**Description:** 

Returns all items in `list` that the function `func` returns true for.
In pseudo-code, this is effectively:
```
function filter(func,list):
    out = [];
    foreach item in list:
        if func(item) is true:
            append item to out;
    return out;
```

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`func`               | The function of signature `function (x)` to evaluate for each item in `list`.
`list`               | The input list.

**Example 1:** 

    include <BOSL2/std.scad>
    include <BOSL2/fnliterals.scad>
    func = function(x) x>5;
    echo(filter(func, [3,4,5,6,7]));
    // ECHO: [6,7]

<br clear="all" /><br/>

---

### Function: reduce()

**Synopsis:** Applies a 2-arg function cumulatively to the items of a list, returning the final result.

**Topics:** [Function Literals](Topics#function-literals), [Looping](Topics#looping)

**See Also:** [map()](#function-map), [filter()](#function-filter), [accumulate()](#function-accumulate), [while()](#function-while), [for\_n()](#function-for_n)

**Usage:** 

- res = reduce(func, list, [init]);
- res = reduce(function (a,b) a+b, list, <init=);

**Description:** 

First the accumulator is set to the value in `init`.  Then, for each item in `list`, the function
in `func` is called with the accumulator and that list item, and the result is stored in the
acumulator for the next iteration.  Once all list items have been processed, the value in the
accumulator is returned.  Ie: `reduce(function (a,b) a+b, list)` is the equivalent of `sum(list)`.
In pseduo-code, this is effectively:
```
function reduce(func, list, init=0):
    x = init;
    foreach item in list:
        x = func(x, item);
    return x;
```

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`func`               | The function of signature `function (x)` to evaluate for each item in `list`.
`list`               | The input list.
`init`               | The starting value for the accumulator.  Default: 0

**Example 1:** Re-Implement sum()

    include <BOSL2/std.scad>
    include <BOSL2/fnliterals.scad>
    x = reduce(f_add(),[3,4,5]);  // Returns: 12

<br clear="all" /><br/>

**Example 2:** Re-Implement product()

    include <BOSL2/std.scad>
    include <BOSL2/fnliterals.scad>
    x = reduce(f_mul(),[3,4,5]);  // Returns: 60

<br clear="all" /><br/>

**Example 3:** Re-Implement all()

    include <BOSL2/std.scad>
    include <BOSL2/fnliterals.scad>
    x = reduce(f_and(),[true,true,true]);   // Returns: true
    y = reduce(f_and(),[true,false,true]);  // Returns: false

<br clear="all" /><br/>

**Example 4:** Re-Implement any()

    include <BOSL2/std.scad>
    include <BOSL2/fnliterals.scad>
    x = reduce(f_or(),[false,false,false]); // Returns: false
    y = reduce(f_or(),[true,false,true]);   // Returns: true

<br clear="all" /><br/>

---

### Function: accumulate()

**Synopsis:** Applies a 2-arg function cumulatively to the items of a list, returning a list of every result.

**Topics:** [Function Literals](Topics#function-literals), [Looping](Topics#looping)

**See Also:** [map()](#function-map), [filter()](#function-filter), [reduce()](#function-reduce), [while()](#function-while), [for\_n()](#function-for_n)

**Usage:** 

- res = accumulate(func, list, [init]);
- res = accumulate(function (a,b) a+b, list, [init=]);

**Description:** 

First the accumulator is set to the value in `init`.  Then, for each item in `list`, the function
in `func` is called with the accumulator and that list item, and the result is stored in the
acumulator for the next iteration.  That value is also appended to the output list.  Once all
list items have been processed, the list of accumulator values is returned.
In pseduo-code, this is effectively:
```
function accumulate(func, list, init=0):
    out = []
    x = init;
    foreach item in list:
        x = func(x, item);
        append x to out;
    return out;
```

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`func`               | The function of signature `function (a,b)` to evaluate for each item in `list`.  Default: `f_add()`
`list`               | The input list.
`init`               | The starting value for the accumulator.  Default: 0

**Example 1:** Reimplement cumsum()

    include <BOSL2/std.scad>
    include <BOSL2/fnliterals.scad>
    echo(accumulate(function (a,b) a+b, [3,4,5],0));  // ECHO: [3,7,12]

<br clear="all" /><br/>

**Example 2:** Reimplement cumprod()

    include <BOSL2/std.scad>
    include <BOSL2/fnliterals.scad>
    echo(accumulate(f_mul(),[3,4,5],1)); // ECHO: [3,12,60,360]

<br clear="all" /><br/>

---

### Function: while()

**Synopsis:** While a `cond` function returns true, iteratively calls a work function, returning the final result.

**Topics:** [Function Literals](Topics#function-literals), [Looping](Topics#looping), [Iteration](Topics#iteration)

**See Also:** [map()](#function-map), [filter()](#function-filter), [reduce()](#function-reduce), [accumulate()](#function-accumulate), [for\_n()](#function-for_n)

**Usage:** 

- x = while(init, cond, func);

**Description:** 

Repeatedly calls the function literals in `cond` and `func` until the `cond` call returns false.
Both `cond` and `func` have the signature `function (i,x)`. The variable `i` is passed the iteration
number, starting with 0.  On the first iteration, the variable `x` is given by `init`.  On subsequent
iterations, `x` is given by the results of the previous call to `func`.  Returns the resulting `x` of
the final iteration.  In pseudo-code, this is effectively:
```
function while(init, cond, func):
    x = init;
    i = 0;
    while cond(i, x):
        x = func(i, x);
        i = i + 1;
    return x;
```

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`init`               | The initial value for `x`.
`cond`               | A function literal with signature `function (i,x)`, called to determine if the loop should continue.  Returns true if the loop should continue.
`func`               | A function literal with signature `function (i,x)`, called on each iteration.  The returned value is passed as `x` on the next iteration.

**Example 1:** 

    include <BOSL2/std.scad>
    include <BOSL2/fnliterals.scad>
    fibs = while(
        init = [1,1],
        cond = function (i,x) select(x,-1)<25,
        func = function (i,x) concat(x, [sum(select(x,-2,-1))])
    );  // Returns: [1,1,2,3,5,8,13,21]

<br clear="all" /><br/>

---

### Function: for\_n()

**Synopsis:** Iteratively calls a work function `n` times, returning the final result.

**Topics:** [Function Literals](Topics#function-literals), [Looping](Topics#looping), [Iteration](Topics#iteration)

**See Also:** [map()](#function-map), [filter()](#function-filter), [reduce()](#function-reduce), [accumulate()](#function-accumulate), [while()](#function-while)

**Usage:** 

- x = for_n(n, init, func);

**Description:** 

Given the function literal `func`, with the signature `function (i,x)`, repeatedly calls it `n` times.
If `n` is given as a scalar, the `i` value will traverse the range `[0:1:n-1]`, one value per call.
If `n` is given as a range, the `i` value will traverse the given range, one value per call.
The `x` value for the first  iteration is given in `init`, and in all subsequent iterations `x` will be the result of the previous call.
In pseudo-code, this is effectively:
```
function for_n(n, init, func):
    x = init;
    if is_range(n):
        iterate i over range n:
            x = func(i,x);
    else:
        iterate i from 0 to n-1 by 1:
            x = func(i,x);
    return x;
```

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`n`                  | The number of iterations to perform, or, if given as a range, the range to traverse.
`init`               | The initial value to pass as `x` to the function in `func`.
`func`               | The function literal to call, with signature `function (i,x)`.

**Example 1:** 

    include <BOSL2/std.scad>
    include <BOSL2/fnliterals.scad>
    fib = function(n) for_n(
        n, [],
        function(i,x) x? [x[1], x[0]+x[1]] : [0,1]
    )[1];

<br clear="all" /><br/>

---

### Function: find\_all()

**Synopsis:** Returns the indices of all items in a list that a given function returns true for.

**Topics:** [Function Literals](Topics#function-literals), [Looping](Topics#looping), [Filters](Topics#filters)

**See Also:** [reduce()](#function-reduce), [find\_first()](#function-find_first), [binsearch()](#function-binsearch)

**Usage:** 

- indices = find_all(func, list);
- indices = find_all(function (x) x>1, list);

**Description:** 

Returns the indices of all items in `list` that the function `func` returns true for.
In pseudo-code, this is effectively:
```
function find_all(func,list):
    out = [];
    foreach item in list:
        if func(item) is true:
            append item index to out;
    return out;
```

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`func`               | The function of signature `function (x)` to evaluate for each item in `list`.
`list`               | The input list.

**Example 1:** 

    include <BOSL2/std.scad>
    include <BOSL2/fnliterals.scad>
    func = function(x) x>5;
    echo(find_all(func, [3,4,5,6,7]));
    // ECHO: [3,4]

<br clear="all" /><br/>

---

### Function: find\_first()

**Synopsis:** Returns the index of the first item in a list, after `start`, that a given function returns true for.

**Topics:** [Function Literals](Topics#function-literals), [Searching](Topics#searching)

**See Also:** [find\_all()](#function-find_all), [filter()](#function-filter), [binsearch()](#function-binsearch), [find\_all()](#function-find_all)

**Usage:** 

- idx = find_first(func, list, [start=]);

**Description:** 

Finds the index of the first item in `list`, after index `start`,  which the function literal in `func` will return true for.
The signature of the function literal in `func` is `function (x)`, and it is expected to return true when the
value compares as matching.  It should return false otherwise.  If you need to find *all* matching items in the
list, you should use [`find_all()`](#function-find_all) instead.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`func`               | The function literal to use to check each item in `list`.  Expects the signature `function (x)`, and a boolean return value.
`list`               | The list to search.

<abbr title="These args must be used by name, ie: name=value">By&nbsp;Name</abbr> | What it does
-------------------- | ------------
`start`              | The first item to check.

**Example 1:** 

    include <BOSL2/std.scad>
    include <BOSL2/fnliterals.scad>
    data = [8,5,3,7,4,2,9];
    echo(find_first(f_lte(4), data));
    // ECHO: 2

<br clear="all" /><br/>

**Example 2:** 

    include <BOSL2/std.scad>
    include <BOSL2/fnliterals.scad>
    data = [8,5,3,7,4,2,9];
    echo(find_first(f_lte(4), data, start=3));
    // ECHO: 4

<br clear="all" /><br/>

---

### Function: binsearch()

**Synopsis:** Does a binary search of a sorted list to find the index of a given value.

**Topics:** [Function Literals](Topics#function-literals), [Data Structures](Topics#data-structures), [Searching](Topics#searching)

**See Also:** [map()](#function-map), [filter()](#function-filter), [reduce()](#function-reduce), [accumulate()](#function-accumulate), [hashmap()](#function-hashmap), [find\_all()](#function-find_all), [find\_first()](#function-find_first)

**Usage:** 

- idx = binsearch(key,list, [cmp]);

**Description:** 

Searches a sorted list for an entry with the given key, using a binary search strategy.
Returns the index of the matching item found.  If none found, returns undef.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`key`                | The key to look for.
`list`               | The list of items to search through.
`idx`                | If given, the index of the item sublists to use as the item key.
`cmp`                | The comparator function literal to use.  Default: `f_cmp()`

**Example 1:** 

    include <BOSL2/std.scad>
    include <BOSL2/fnliterals.scad>
    items = unique(rands(0,100,10000));
    idx = binsearch(44, items);

<br clear="all" /><br/>

**Example 2:** 

    include <BOSL2/std.scad>
    include <BOSL2/fnliterals.scad>
    items = unique(rands(0,100,10000));
    idx = binsearch(44, items, cmp=function(a,b) a-b);

<br clear="all" /><br/>

**Example 3:** 

    include <BOSL2/std.scad>
    include <BOSL2/fnliterals.scad>
    items = [for (i=[32:126]) [chr(i), i]];
    idx = binsearch("G", items, idx=0);

<br clear="all" /><br/>

---

### Function: simple\_hash()

**Synopsis:** Returns an integer hash of a given value.

**Topics:** [Function Literals](Topics#function-literals), [Hashing](Topics#hashing), [Data Structures](Topics#data-structures)

**See Also:** [hashmap()](#function-hashmap)

**Usage:** 

- hx = simple_hash(x);

**Description:** 

Given an arbitrary value, returns the integer hash value for it.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`x`                  | The value to get the simple hash value  of.

**Example 1:** 

    include <BOSL2/std.scad>
    include <BOSL2/fnliterals.scad>
    x = simple_hash("Foobar");
    x = simple_hash([[10,20],[-5,3]]);

<br clear="all" /><br/>

---

### Function: hashmap()

**Synopsis:** Creates a hashmap manipulation function.

**Topics:** [Function Literals](Topics#function-literals), [Data Structures](Topics#data-structures), [Hashing](Topics#hashing)

**See Also:** [simple\_hash()](#function-simple_hash)

**Usage:** Creating an Empty HashMap.

- hm = hashmap([hashsize=]);

**Usage:** Creating a Populated HashMap.

- hm = hashmap(items=KEYVAL_LIST, [hashsize=]);

**Usage:** Adding an Entry

- hm2 = hm(key, val);

**Usage:** Adding Multiple Entries

- hm2 = hm(additems=KEYVAL_LIST);

**Usage:** Removing an Entry

- hm2 = hm(del=KEY);

**Usage:** Fetching a Value

- x = hm(key);

**Usage:** Iterating a HashMap

- for (kv=hm()) let(k=kv[0], v=kv[1]) ...

**Description:** 

This is a factory function for creating hashmap data structure functions.  You can use a hashmap
to store large amounts of [key,value] data.  At around 4000 items, this becomes faster than using
`search()` through the list.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`hashsize`           | The number of hashtable buckets to form.
`items`              | A list of [key,value] pairs to initialize the hashmap with.

**FunctionLiteral Args:** 

Positional | Definition
---------- | ----------
k | The key name.
v | The value to store with the key.

Named | Definition
----- | ----------
del | If given the key of an item to delete, makes a new hashmap with that item removed.
additems | If given a list of [key,val] pairs, makes a new hashmap with the items added.

**Example 1:** 

    include <BOSL2/std.scad>
    include <BOSL2/fnliterals.scad>
    hm = hashmap(items=[for (i=[0:9999]) [str("foo",i),i]]);
    a = hm("foo37");  // Returns: 37
    hm2 = hm("Blah", 39);  // Adds entry "Blah" with val 39.
    b = hm2("Blah");  // Returns: 39
    hm3 = hm2(additems=[["bar",39],["qux",21]]);  // Adds "bar" and "qux"
    hm4 = hm3(del="Blah");  // Deletes entry "Blah".
    for (kv = hm4()) {  // Iterates over all key/value pairs.
       echo(key=kv[0], val=kv[1]);
    }

<br clear="all" /><br/>

---

## Section: Function Meta-Generators


### Function: f\_1arg()

**Synopsis:** Creates a factory for a 2-arg function literal, where you can optionally pre-fill the arg.

**Topics:** [Function Literals](Topics#function-literals)

**See Also:** [f\_2arg()](#function-f_2arg), [f\_3arg()](#function-f_3arg)

**Usage:** 

- fn = f_1arg(func);

**Description:** 

Takes a function literal that accepts one argument, and returns a function
literal factory that can be used to pre-fill out that argument with a constant.

**Example 1:** 

    include <BOSL2/std.scad>
    include <BOSL2/fnliterals.scad>
    f_str = f_1arg(function(a) str(a));
    fn_str = f_str();   // = function(a) str(a);
    fn_str3 = f_str(3); // = function() str(3);

<br clear="all" /><br/>

---

### Function: f\_2arg()

**Synopsis:** Creates a factory for a 2-arg function literal, where you can optionally pre-fill the args.

**Topics:** [Function Literals](Topics#function-literals)

**See Also:** [f\_1arg()](#function-f_1arg), [f\_3arg()](#function-f_3arg)

**Usage:** 

- fn = f_2arg(target_func);

**Description:** 

Takes a function literal that accepts two arguments, and returns a function
literal factory that can be used to pre-fill out one or both of those arguments
with a constant.

**Example 1:** 

    include <BOSL2/std.scad>
    include <BOSL2/fnliterals.scad>
    f_lt = f_2arg(function(a,b) a<b);
    fn_lt = f_lt();      // = function(a,b) a<b;
    fn_3lt = f_lt(3);    // = function(b) 3<b;
    fn_3lt = f_lt(a=3);  // = function(b) 3<b;
    fn_lt3 = f_lt(b=3);  // = function(a) a<3;
    fn_3lt4 = f_lt(3,4); // = function() 3<4;

<br clear="all" /><br/>

---

### Function: f\_2arg\_simple()

**Synopsis:** Creates a factory for a 2-arg function literal, where you can optionally pre-fill the args.

**Topics:** [Function Literals](Topics#function-literals)

**See Also:** [f\_1arg()](#function-f_1arg), [f\_3arg()](#function-f_3arg)

**Usage:** 

- fn = f_2arg_simple(target_func);

**Description:** 

Takes a function literal that accepts two arguments, and returns a function
literal factory that can be used to pre-fill out one or both of those arguments
with a constant.  When given a single argument, fills out the segond function
argument with a constant.

**Example 1:** 

    include <BOSL2/std.scad>
    include <BOSL2/fnliterals.scad>
    f_lt = f_2arg_simple(function(a,b) a<b);
    fn_lt = f_lt();       // = function(a,b) a<b;
    fn_lt3 = f_lt(3);     // = function(a) a<3;
    fn_3lt4 = f_lt(3,4);  // = function() 3<4;

<br clear="all" /><br/>

---

### Function: f\_3arg()

**Synopsis:** Creates a factory for a 3-arg function literal, where you can optionally pre-fill the args.

**Topics:** [Function Literals](Topics#function-literals)

**See Also:** [f\_1arg()](#function-f_1arg), [f\_2arg()](#function-f_2arg)

**Usage:** 

- fn = f_3arg(target_func);

**Description:** 

Takes a function literal that accepts three arguments, and returns a function
literal factory that can be used to pre-fill out some or all of those arguments
with a constant.

**Example 1:** 

    include <BOSL2/std.scad>
    include <BOSL2/fnliterals.scad>
    p1 = [10,4]; p2 = [3,7];
    f_va = f_3arg(function(a,b,c) vector_angle(a,b,c));
    fn_va = f_va();       // = function(a,b,c) vector_angle(a,b,c);
    fn_va2 = f_lt(c=p1);  // = function(a,b) vector_angle(a,b,p1);
    fn_va3 = f_lt(a=p2);  // = function(a,c) vector_angle(a,p2,c);
    fn_va4 = f_lt(a=p1,c=p2); // = function() vector_angle(p1,b,p2);

<br clear="all" /><br/>

---

### Function: ival()

**Synopsis:** Generates a function with signature `(i,x)` that calls `func(i)`

**Topics:** [Function Literals](Topics#function-literals)

**See Also:** [f\_1arg()](#function-f_1arg), [f\_2arg()](#function-f_2arg), [f\_3arg()](#function-f_3arg), [xval()](#function-xval)

**Usage:** 

- newfunc = ival(func);

**Description:** 

Wraps a single-argument function literal so that it can take two arguments,
passing the first argument along to the wrapped function.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`target_func`        | The function of signature (x) to wrap.

**FunctionLiteral Args:** 

Positional | Definition
---------- | ----------
a | The argument that will be passed through.
b | The argumen that will be discarded.

**Example 1:** 

    include <BOSL2/std.scad>
    include <BOSL2/fnliterals.scad>
    x = while(0, ival(f_lt(5)), xval(f_add(1)));

<br clear="all" /><br/>

---

### Function: xval()

**Synopsis:** Generates a function with signature `(i,x)` that calls `func(x)`

**Topics:** [Function Literals](Topics#function-literals)

**See Also:** [f\_1arg()](#function-f_1arg), [f\_2arg()](#function-f_2arg), [f\_3arg()](#function-f_3arg), [ival()](#function-ival)

**Usage:** 

- newfunc = xval(func);

**Description:** 

Wraps a single-argument function literal so that it can take two arguments,
passing the first argument along to the wrapped function.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`target_func`        | The function of signature (x) to wrap.

**FunctionLiteral Args:** 

Positional | Definition
---------- | ----------
a | The argument that will be passed through.
b | The argumen that will be discarded.

**Example 1:** 

    include <BOSL2/std.scad>
    include <BOSL2/fnliterals.scad>
    x = while(0, ival(f_lt(5)), xval(f_add(1)));

<br clear="all" /><br/>

---

## Section: Comparator Generators


### Function: f\_cmp()

**Synopsis:** Returns a function to compare values.

**Topics:** [Function Literals](Topics#function-literals), [Comparators](Topics#comparators)

**See Also:** [f\_gt()](#function-f_gt), [f\_lt()](#function-f_lt), [f\_gte()](#function-f_gte), [f\_lte()](#function-f_lte), [f\_eq()](#function-f_eq), [f\_neq()](#function-f_neq), [f\_approx()](#function-f_approx), [f\_napprox()](#function-f_napprox)

**Usage:** 

- fn = f_cmp();
- fn = f_cmp(b);
- fn = f_cmp(a,b);

**Description:** 

A factory that generates function literals that compare `a` and `b`, where one or
both arguments can be replaced with constants.  If `a` and `b` are equal, the function
literal will return 0.  If a<b then -1 is returned.  If a>b then 1 is returned.

**Example 1:** 

    include <BOSL2/std.scad>
    include <BOSL2/fnliterals.scad>
    fn_cmp = f_cmp();       // = function(a,b) a==b?0: a>b?1: -1;
    fn_cmp3 = f_cmp(3);     // = function(a) a==3?0: a>3?1: -1;
    fn_3cmp4 = f_cmp(3,4);  // = function() 3==4?0: 3>4?1: -1;

<br clear="all" /><br/>

---

### Function: f\_gt()

**Synopsis:** Returns a function to compare if `a` is greater than `b`.

**Topics:** [Function Literals](Topics#function-literals), [Comparators](Topics#comparators)

**See Also:** [f\_cmp()](#function-f_cmp), [f\_lt()](#function-f_lt), [f\_gte()](#function-f_gte), [f\_lte()](#function-f_lte), [f\_eq()](#function-f_eq), [f\_neq()](#function-f_neq), [f\_approx()](#function-f_approx), [f\_napprox()](#function-f_napprox)

**Usage:** 

- fn = f_gt();
- fn = f_gt(b);
- fn = f_gt(a,b);

**Description:** 

A factory that generates function literals based on `a > b`, where one
or both of the arguments can be replaced with constants.

**Example 1:** 

    include <BOSL2/std.scad>
    include <BOSL2/fnliterals.scad>
    fn_gt = f_gt();       // = function(a,b) a>b;
    fn_gt3 = f_gt(3);     // = function(a) a>3;
    fn_3gt4 = f_gt(3,4);  // = function() 3>4;

<br clear="all" /><br/>

---

### Function: f\_lt()

**Synopsis:** Returns a function to compare if `a` is less than `b`.

**Topics:** [Function Literals](Topics#function-literals), [Comparators](Topics#comparators)

**See Also:** [f\_cmp()](#function-f_cmp), [f\_gt()](#function-f_gt), [f\_gte()](#function-f_gte), [f\_lte()](#function-f_lte), [f\_eq()](#function-f_eq), [f\_neq()](#function-f_neq), [f\_approx()](#function-f_approx), [f\_napprox()](#function-f_napprox)

**Usage:** 

- fn = f_lt();
- fn = f_lt(b);
- fn = f_lt(a,b);

**Description:** 

A factory that generates function literals based on `a < b`, where one
or both of the arguments can be replaced with constants.

**Example 1:** 

    include <BOSL2/std.scad>
    include <BOSL2/fnliterals.scad>
    fn_lt = f_lt();       // = function(a,b) a<b;
    fn_lt3 = f_lt(3);     // = function(a) a<3;
    fn_3lt4 = f_lt(3,4);  // = function() 3<4;

<br clear="all" /><br/>

---

### Function: f\_gte()

**Synopsis:** Returns a function to compare if `a` is greater than or equal to `b`.

**Topics:** [Function Literals](Topics#function-literals), [Comparators](Topics#comparators)

**See Also:** [f\_cmp()](#function-f_cmp), [f\_gt()](#function-f_gt), [f\_lt()](#function-f_lt), [f\_lte()](#function-f_lte), [f\_eq()](#function-f_eq), [f\_neq()](#function-f_neq), [f\_approx()](#function-f_approx), [f\_napprox()](#function-f_napprox)

**Usage:** 

- fn = f_gte();
- fn = f_gte(b);
- fn = f_gte(a,b);

**Description:** 

A factory that generates function literals based on `a >= b`, where one
or both of the arguments can be replaced with constants.

**Example 1:** 

    include <BOSL2/std.scad>
    include <BOSL2/fnliterals.scad>
    fn_gte = f_gte();       // = function(a,b) a>=b;
    fn_gte3 = f_gte(3);     // = function(a) a>=3;
    fn_3gte4 = f_gte(3,4);  // = function() 3>=4;

<br clear="all" /><br/>

---

### Function: f\_lte()

**Synopsis:** Returns a function to compare if `a` is less than or equal to `b`.

**Topics:** [Function Literals](Topics#function-literals), [Comparators](Topics#comparators)

**See Also:** [f\_cmp()](#function-f_cmp), [f\_gt()](#function-f_gt), [f\_lt()](#function-f_lt), [f\_gte()](#function-f_gte), [f\_eq()](#function-f_eq), [f\_neq()](#function-f_neq), [f\_approx()](#function-f_approx), [f\_napprox()](#function-f_napprox)

**Usage:** 

- fn = f_lte();
- fn = f_lte(b);
- fn = f_lte(a,b);

**Description:** 

A factory that generates function literals based on `a <= b`, where
one or both arguments can be replaced with constants.

**Example 1:** 

    include <BOSL2/std.scad>
    include <BOSL2/fnliterals.scad>
    fn_lte = f_lte();       // = function(a,b) a<=b;
    fn_lte3 = f_lte(3);     // = function(a) a<=3;
    fn_3lte4 = f_lte(3,4);  // = function() 3<=4;

<br clear="all" /><br/>

---

### Function: f\_eq()

**Synopsis:** Returns a function to compare if `a` is exactly equal to `b`.

**Topics:** [Function Literals](Topics#function-literals), [Comparators](Topics#comparators)

**See Also:** [f\_cmp()](#function-f_cmp), [f\_gt()](#function-f_gt), [f\_lt()](#function-f_lt), [f\_gte()](#function-f_gte), [f\_lte()](#function-f_lte), [f\_neq()](#function-f_neq), [f\_approx()](#function-f_approx), [f\_napprox()](#function-f_napprox)

**Usage:** 

- fn = f_eq();
- fn = f_eq(b);
- fn = f_eq(a,b);

**Description:** 

A factory that generates function literals based on `a == b`, where
one or both arguments can be replaced with constants.

**Example 1:** 

    include <BOSL2/std.scad>
    include <BOSL2/fnliterals.scad>
    fn_eq = f_eq();       // = function(a,b) a==b;
    fn_eq3 = f_eq(3);     // = function(a) a==3;
    fn_3eq4 = f_eq(3,4);  // = function() 3==4;

<br clear="all" /><br/>

---

### Function: f\_neq()

**Synopsis:** Returns a function to compare if `a` is not exactly equal to `b`.

**Topics:** [Function Literals](Topics#function-literals), [Comparators](Topics#comparators)

**See Also:** [f\_cmp()](#function-f_cmp), [f\_gt()](#function-f_gt), [f\_lt()](#function-f_lt), [f\_gte()](#function-f_gte), [f\_lte()](#function-f_lte), [f\_eq()](#function-f_eq), [f\_approx()](#function-f_approx), [f\_napprox()](#function-f_napprox)

**Usage:** 

- fn = f_neq();
- fn = f_neq(b);
- fn = f_neq(a,b);

**Description:** 

A factory that generates function literals based on `a != b`, where
one or both arguments can be replaced with constants.

**Example 1:** 

    include <BOSL2/std.scad>
    include <BOSL2/fnliterals.scad>
    fn_neq = f_neq();       // = function(a,b) a!=b;
    fn_neq3 = f_neq(3);     // = function(a) a!=3;
    fn_3neq4 = f_neq(3,4);  // = function() 3!=4;

<br clear="all" /><br/>

---

### Function: f\_approx()

**Synopsis:** Returns a function to compare if `a` is approximately equal to `b`.

**Topics:** [Function Literals](Topics#function-literals), [Comparators](Topics#comparators)

**See Also:** [f\_cmp()](#function-f_cmp), [f\_gt()](#function-f_gt), [f\_lt()](#function-f_lt), [f\_gte()](#function-f_gte), [f\_lte()](#function-f_lte), [f\_eq()](#function-f_eq), [f\_neq()](#function-f_neq), [f\_napprox()](#function-f_napprox)

**Usage:** 

- fn = f_approx();
- fn = f_approx(b);
- fn = f_approx(a,b);

**Description:** 

A factory that generates function literals based on `approx(a,b)`, where
one or both arguments can be replaced with constants.

**Example 1:** 

    include <BOSL2/std.scad>
    include <BOSL2/fnliterals.scad>
    fn_approx = f_approx();       // = function(a,b) approx(a,b);
    fn_approx3 = f_approx(3);     // = function(a) approx(a,3);
    fn_3approx4 = f_approx(3,4);  // = function() approx(3,4);

<br clear="all" /><br/>

---

### Function: f\_napprox()

**Synopsis:** Returns a function to compare if `a` is not approximately equal to `b`.

**Topics:** [Function Literals](Topics#function-literals), [Comparators](Topics#comparators)

**See Also:** [f\_cmp()](#function-f_cmp), [f\_gt()](#function-f_gt), [f\_lt()](#function-f_lt), [f\_gte()](#function-f_gte), [f\_lte()](#function-f_lte), [f\_eq()](#function-f_eq), [f\_neq()](#function-f_neq), [f\_approx()](#function-f_approx)

**Usage:** 

- fn = f_napprox();
- fn = f_napprox(b);
- fn = f_napprox(a,b);

**Description:** 

A factory that generates function literals based on `!approx(a,b)`, where
one or both arguments can be replaced with constants.

**Example 1:** 

    include <BOSL2/std.scad>
    include <BOSL2/fnliterals.scad>
    fn_napprox = f_napprox();       // = function(a,b) napprox(a,b);
    fn_napprox3 = f_napprox(3);     // = function(a) napprox(a,3);
    fn_3napprox4 = f_napprox(3,4);  // = function() napprox(3,4);

<br clear="all" /><br/>

---

## Section: Logic Operators


### Function: f\_or()

**Synopsis:** Returns a function to check if either `a` or `b` is true.

**Topics:** [Function Literals](Topics#function-literals), [Logic](Topics#logic), [Boolean Operations](Topics#boolean-operations)

**See Also:** [f\_and()](#function-f_and), [f\_nor()](#function-f_nor), [f\_nand()](#function-f_nand), [f\_xor()](#function-f_xor), [f\_not()](#function-f_not)

**Usage:** 

- fn = f_or();
- fn = f_or(a=);
- fn = f_or(b=);
- fn = f_or(a=,b=);

**Description:** 

A factory that generates function literals based on `a || b`, where
either or both of the `a` or `b` arguments can be replaced with constants.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`a`                  | If given, replaces the first argument.
`b`                  | If given, replaces the second argument.

---

### Function: f\_and()

**Synopsis:** Returns a function to check if both `a` and `b` are true.

**Topics:** [Function Literals](Topics#function-literals), [Logic](Topics#logic), [Boolean Operations](Topics#boolean-operations)

**See Also:** [f\_or()](#function-f_or), [f\_nor()](#function-f_nor), [f\_nand()](#function-f_nand), [f\_xor()](#function-f_xor), [f\_not()](#function-f_not)

**Usage:** 

- fn = f_and();
- fn = f_and(a=);
- fn = f_and(b=);
- fn = f_and(a=,b=);

**Description:** 

A factory that generates function literals based on `a && b`, where
either or both of the `a` or `b` arguments can be replaced with constants.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`a`                  | If given, replaces the first argument.
`b`                  | If given, replaces the second argument.

---

### Function: f\_nor()

**Synopsis:** Returns a function to check if neither `a` nor `b` are true.

**Topics:** [Function Literals](Topics#function-literals), [Logic](Topics#logic), [Boolean Operations](Topics#boolean-operations)

**See Also:** [f\_or()](#function-f_or), [f\_and()](#function-f_and), [f\_nand()](#function-f_nand), [f\_xor()](#function-f_xor), [f\_not()](#function-f_not)

**Usage:** 

- fn = f_nor();
- fn = f_nor(a=);
- fn = f_nor(b=);
- fn = f_nor(a=,b=);

**Description:** 

A factory that generates function literals based on `!(a || b)`, where
either or both of the `a` or `b` arguments can be replaced with constants.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`a`                  | If given, replaces the first argument.
`b`                  | If given, replaces the second argument.

---

### Function: f\_nand()

**Synopsis:** Returns a function to check if `a` and `b` are not both true.

**Topics:** [Function Literals](Topics#function-literals), [Logic](Topics#logic), [Boolean Operations](Topics#boolean-operations)

**See Also:** [f\_or()](#function-f_or), [f\_and()](#function-f_and), [f\_nor()](#function-f_nor), [f\_xor()](#function-f_xor), [f\_not()](#function-f_not)

**Usage:** 

- fn = f_nand();
- fn = f_nand(a=);
- fn = f_nand(b=);
- fn = f_nand(a=,b=);

**Description:** 

A factory that generates function literals based on `!(a && b)`, where
either or both of the `a` or `b` arguments can be replaced with constants.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`a`                  | If given, replaces the first argument.
`b`                  | If given, replaces the second argument.

---

### Function: f\_xor()

**Synopsis:** Returns a function to check if either `a` or `b`, but not both, are true.

**Topics:** [Function Literals](Topics#function-literals), [Logic](Topics#logic), [Boolean Operations](Topics#boolean-operations)

**See Also:** [f\_or()](#function-f_or), [f\_and()](#function-f_and), [f\_nor()](#function-f_nor), [f\_nand()](#function-f_nand), [f\_not()](#function-f_not)

**Usage:** 

- fn = f_xor();
- fn = f_xor(a=);
- fn = f_xor(b);
- fn = f_xor(a=,b=);

**Description:** 

A factory that generates function literals based on `(!a && b) || (a && !b)`, where
either or both of the `a` or `b` arguments can be replaced with constants.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`a`                  | If given, replaces the first argument.
`b`                  | If given, replaces the second argument.

---

### Function: f\_not()

**Synopsis:** Returns a function to check if `a` is not true.

**Topics:** [Function Literals](Topics#function-literals), [Logic](Topics#logic), [Boolean Operations](Topics#boolean-operations)

**See Also:** [f\_or()](#function-f_or), [f\_and()](#function-f_and), [f\_nor()](#function-f_nor), [f\_nand()](#function-f_nand), [f\_xor()](#function-f_xor)

**Usage:** 

- fn = f_not();
- fn = f_not(a);

**Description:** 

A factory that generates function literals based on `!a`, where the `a`
argument can be replaced with a constant.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`a`                  | If given, replaces the argument.

---

### Function: f\_even()

**Synopsis:** Returns a function to check if `a` is an even number.

**Topics:** [Function Literals](Topics#function-literals), [Math Operators](Topics#math-operators)

**See Also:** [f\_odd()](#function-f_odd)

**Usage:** 

- fn = f_even();
- fn = f_even(a);

**Description:** 

A factory that generates function literals based on `a % 2 == 0`, where the `a`
argument can optionally be replaced with a constant.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`a`                  | If given, replaces the argument.

**Example 1:** 

    include <BOSL2/std.scad>
    include <BOSL2/fnliterals.scad>
    l2 = filter(f_even(), [3,4,5,6,7,8]);  // Returns: [4,6,8]

<br clear="all" /><br/>

---

### Function: f\_odd()

**Synopsis:** Returns a function to check if `a` is an odd number.

**Topics:** [Function Literals](Topics#function-literals), [Math Operators](Topics#math-operators)

**See Also:** [f\_even()](#function-f_even)

**Usage:** 

- fn = f_odd();
- fn = f_odd(a);

**Description:** 

A factory that generates function literals based on `a % 2 != 0`, where the `a`
argument can optionally be replaced with a constant.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`a`                  | If given, replaces the argument.

**Example 1:** 

    include <BOSL2/std.scad>
    include <BOSL2/fnliterals.scad>
    l2 = filter(f_odd(), [3,4,5,6,7,8]);  // Returns: [3,5,7]

<br clear="all" /><br/>

---

## Section: Math Operators


### Function: f\_add()

**Synopsis:** Returns a function to add `a` and `b`.

**Topics:** [Function Literals](Topics#function-literals), [Math Operators](Topics#math-operators)

**See Also:** [f\_sub()](#function-f_sub), [f\_mul()](#function-f_mul), [f\_div()](#function-f_div), [f\_mod()](#function-f_mod), [f\_pow()](#function-f_pow), [f\_neg()](#function-f_neg)

**Usage:** 

- fn = f_add();
- fn = f_add(a=);
- fn = f_add(b);
- fn = f_add(a=,b=);

**Description:** 

A factory that generates function literals based on `a + b`, where either
or both of the `a` or `b` arguments can be replaced with constants.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`a`                  | If given, replaces the first argument.
`b`                  | If given, replaces the second argument.

---

### Function: f\_sub()

**Synopsis:** Returns a function to subtract `a` from `b`.

**Topics:** [Function Literals](Topics#function-literals), [Math Operators](Topics#math-operators)

**See Also:** [f\_add()](#function-f_add), [f\_mul()](#function-f_mul), [f\_div()](#function-f_div), [f\_mod()](#function-f_mod), [f\_pow()](#function-f_pow), [f\_neg()](#function-f_neg)

**Usage:** 

- fn = f_sub();
- fn = f_sub(a=);
- fn = f_sub(b);
- fn = f_sub(a=,b=);

**Description:** 

A factory that generates function literals based on `a - b`, where either
or both of the `a` or `b` arguments can be replaced with constants.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`a`                  | If given, replaces the first argument.
`b`                  | If given, replaces the second argument.

---

### Function: f\_mul()

**Synopsis:** Returns a function to multiply `a` by `b`.

**Topics:** [Function Literals](Topics#function-literals), [Math Operators](Topics#math-operators)

**See Also:** [f\_add()](#function-f_add), [f\_sub()](#function-f_sub), [f\_div()](#function-f_div), [f\_mod()](#function-f_mod), [f\_pow()](#function-f_pow), [f\_neg()](#function-f_neg)

**Usage:** 

- fn = f_mul();
- fn = f_mul(a=);
- fn = f_mul(b);
- fn = f_mul(a=,b=);

**Description:** 

A factory that generates function literals based on `a * b`, where either
or both of the `a` or `b` arguments can be replaced with constants.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`a`                  | If given, replaces the first argument.
`b`                  | If given, replaces the second argument.

---

### Function: f\_div()

**Synopsis:** Returns a function to divide `a` by `b`.

**Topics:** [Function Literals](Topics#function-literals), [Math Operators](Topics#math-operators)

**See Also:** [f\_add()](#function-f_add), [f\_sub()](#function-f_sub), [f\_mul()](#function-f_mul), [f\_mod()](#function-f_mod), [f\_pow()](#function-f_pow), [f\_neg()](#function-f_neg)

**Usage:** 

- fn = f_div();
- fn = f_div(a=);
- fn = f_div(b);
- fn = f_div(a=,b=);

**Description:** 

A factory that generates function literals based on `a / b`, where either
or both of the `a` or `b` arguments can be replaced with constants.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`a`                  | If given, replaces the first argument.
`b`                  | If given, replaces the second argument.

---

### Function: f\_mod()

**Synopsis:** Returns a function to calculate the modulo of `a` divided by `b`.

**Topics:** [Function Literals](Topics#function-literals), [Math Operators](Topics#math-operators)

**See Also:** [f\_add()](#function-f_add), [f\_sub()](#function-f_sub), [f\_mul()](#function-f_mul), [f\_div()](#function-f_div), [f\_pow()](#function-f_pow), [f\_neg()](#function-f_neg)

**Usage:** 

- fn = f_mod();
- fn = f_mod(a=);
- fn = f_mod(b);
- fn = f_mod(a=,b=);

**Description:** 

A factory that generates function literals based on `a % b`, where either
or both of the `a` or `b` arguments can be replaced with constants.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`a`                  | If given, replaces the first argument.
`b`                  | If given, replaces the second argument.

---

### Function: f\_pow()

**Synopsis:** Returns a function to calculate `a` to the power of `b`.

**Topics:** [Function Literals](Topics#function-literals), [Math Operators](Topics#math-operators)

**See Also:** [f\_add()](#function-f_add), [f\_sub()](#function-f_sub), [f\_mul()](#function-f_mul), [f\_div()](#function-f_div), [f\_mod()](#function-f_mod), [f\_neg()](#function-f_neg)

**Usage:** 

- fn = f_pow();
- fn = f_pow(a=);
- fn = f_pow(b);
- fn = f_pow(a=,b=);

**Description:** 

A factory that generates function literals based on `pow(a,b)`, where either
or both of the `a` or `b` arguments can be replaced with constants.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`a`                  | If given, replaces the first argument.
`b`                  | If given, replaces the second argument.

---

### Function: f\_neg()

**Synopsis:** Returns a function to calculate `-a`

**Topics:** [Function Literals](Topics#function-literals), [Math Operators](Topics#math-operators)

**See Also:** [f\_add()](#function-f_add), [f\_sub()](#function-f_sub), [f\_mul()](#function-f_mul), [f\_div()](#function-f_div), [f\_mod()](#function-f_mod), [f\_pow()](#function-f_pow)

**Usage:** 

- fn = f_neg();
- fn = f_neg(a);

**Description:** 

A factory that generates function literals based on `-a`, where the `a`
argument can optionally be replaced with a constant.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`a`                  | If given, replaces the argument.

---

## Section: Min/Max Operators


### Function: f\_min()

**Synopsis:** Returns a function to calculate the minimum value of a list.

**Topics:** [Function Literals](Topics#function-literals), [Math Operators](Topics#math-operators)

**See Also:** [f\_max()](#function-f_max), [f\_min2()](#function-f_min2), [f\_max2()](#function-f_max2), [f\_min3()](#function-f_min3), [f\_max3()](#function-f_max3)

**Usage:** 

- fn = f_min();
- fn = f_min(a);

**Description:** 

A factory that generates function literals based on `min(a)`, where the `a`
argument can optionally be replaced with a constant.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`a`                  | If given, replaces the argument.

---

### Function: f\_max()

**Synopsis:** Returns a function to calculate the maximum value of a list.

**Topics:** [Function Literals](Topics#function-literals), [Math Operators](Topics#math-operators)

**See Also:** [f\_min()](#function-f_min), [f\_min2()](#function-f_min2), [f\_max2()](#function-f_max2), [f\_min3()](#function-f_min3), [f\_max3()](#function-f_max3)

**Usage:** 

- fn = f_max();
- fn = f_max(a);

**Description:** 

A factory that generates function literals based on `max(a)`, where the `a`
argument can optionally be replaced with a constant.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`a`                  | If given, replaces the argument.

---

### Function: f\_min2()

**Synopsis:** Returns a function to calculate the minimum of two values.

**Topics:** [Function Literals](Topics#function-literals), [Math Operators](Topics#math-operators)

**See Also:** [f\_min()](#function-f_min), [f\_max()](#function-f_max), [f\_max2()](#function-f_max2), [f\_min3()](#function-f_min3), [f\_max3()](#function-f_max3)

**Usage:** 

- fn = f_min2();
- fn = f_min2(a=);
- fn = f_min2(b);
- fn = f_min2(a=,b=);

**Description:** 

A factory that generates function literals based on `min(a,b)`, where either
or both of the `a` or `b` arguments can be replaced with constants.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`a`                  | If given, replaces the first argument.
`b`                  | If given, replaces the second argument.

---

### Function: f\_max2()

**Synopsis:** Returns a function to calculate the maximum of two values.

**Topics:** [Function Literals](Topics#function-literals), [Math Operators](Topics#math-operators)

**See Also:** [f\_min()](#function-f_min), [f\_max()](#function-f_max), [f\_min2()](#function-f_min2), [f\_min3()](#function-f_min3), [f\_max3()](#function-f_max3)

**Usage:** 

- fn = f_max2();
- fn = f_max2(a=);
- fn = f_max2(b);
- fn = f_max2(a=,b=);

**Description:** 

A factory that generates function literals based on `max(a,b)`, where either
or both of the `a` or `b` arguments can be replaced with constants.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`a`                  | If given, replaces the first argument.
`b`                  | If given, replaces the second argument.

---

### Function: f\_min3()

**Synopsis:** Returns a function to calculate the minimum of three values.

**Topics:** [Function Literals](Topics#function-literals), [Math Operators](Topics#math-operators)

**See Also:** [f\_min()](#function-f_min), [f\_max()](#function-f_max), [f\_min2()](#function-f_min2), [f\_max2()](#function-f_max2), [f\_max3()](#function-f_max3)

**Usage:** 

- fn = f_min3();
- fn = f_min3(a=);
- fn = f_min3(b=);
- fn = f_min3(c=);
- fn = f_min3(a=,b=);
- fn = f_min3(b=,c=);
- fn = f_min3(a=,c=);
- fn = f_min3(a=,b=,c=);

**Description:** 

A factory that generates function literals based on `min(a,b,c)`, where any
or all of the `a`, `b`, or`c` arguments can be replaced with constants.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`a`                  | If given, replaces the first argument.
`b`                  | If given, replaces the second argument.
`c`                  | If given, replaces the third argument.

---

### Function: f\_max3()

**Synopsis:** Returns a function to calculate the maximum of three values.

**Topics:** [Function Literals](Topics#function-literals), [Math Operators](Topics#math-operators)

**See Also:** [f\_min()](#function-f_min), [f\_max()](#function-f_max), [f\_min2()](#function-f_min2), [f\_max2()](#function-f_max2), [f\_min3()](#function-f_min3)

**Usage:** 

- fn = f_max3();
- fn = f_max3(a=);
- fn = f_max3(b=);
- fn = f_max3(c=);
- fn = f_max3(a=,b=);
- fn = f_max3(b=,c=);
- fn = f_max3(a=,c=);
- fn = f_max3(a=,b=,c=);

**Description:** 

A factory that generates function literals based on `min(a,b,c)`, where any
or all of the `a`, `b`, or`c` arguments can be replaced with constants.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`a`                  | If given, replaces the first argument.
`b`                  | If given, replaces the second argument.
`c`                  | If given, replaces the third argument.

---

## Section: Trigonometry Operators


### Function: f\_sin()

**Synopsis:** Returns a function to calculate the sine of a value.

**Topics:** [Function Literals](Topics#function-literals), [Math Operators](Topics#math-operators)

**See Also:** [f\_cos()](#function-f_cos), [f\_tan()](#function-f_tan), [f\_asin()](#function-f_asin), [f\_acos()](#function-f_acos), [f\_atan()](#function-f_atan), [f\_atan2()](#function-f_atan2)

**Usage:** 

- fn = f_sin();
- fn = f_sin(a);

**Description:** 

A factory that generates function literals based on `sin(a)`, where the `a`
argument can optionally be replaced with a constant.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`a`                  | If given, replaces the argument.

---

### Function: f\_cos()

**Synopsis:** Returns a function to calculate the cosine of a value.

**Topics:** [Function Literals](Topics#function-literals), [Math Operators](Topics#math-operators)

**See Also:** [f\_sin()](#function-f_sin), [f\_tan()](#function-f_tan), [f\_asin()](#function-f_asin), [f\_acos()](#function-f_acos), [f\_atan()](#function-f_atan), [f\_atan2()](#function-f_atan2)

**Usage:** 

- fn = f_cos();
- fn = f_cos(a);

**Description:** 

A factory that generates function literals based on `cos(a)`, where the `a`
argument can optionally be replaced with a constant.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`a`                  | If given, replaces the argument.

---

### Function: f\_tan()

**Synopsis:** Returns a function to calculate the tangent of a value.

**Topics:** [Function Literals](Topics#function-literals), [Math Operators](Topics#math-operators)

**See Also:** [f\_sin()](#function-f_sin), [f\_cos()](#function-f_cos), [f\_asin()](#function-f_asin), [f\_acos()](#function-f_acos), [f\_atan()](#function-f_atan), [f\_atan2()](#function-f_atan2)

**Usage:** 

- fn = f_tan();
- fn = f_tan(a);

**Description:** 

A factory that generates function literals based on `tan(a)`, where the `a`
argument can optionally be replaced with a constant.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`a`                  | If given, replaces the argument.

---

### Function: f\_asin()

**Synopsis:** Returns a function to calculate the arcsine of a value.

**Topics:** [Function Literals](Topics#function-literals), [Math Operators](Topics#math-operators)

**See Also:** [f\_sin()](#function-f_sin), [f\_cos()](#function-f_cos), [f\_tan()](#function-f_tan), [f\_acos()](#function-f_acos), [f\_atan()](#function-f_atan), [f\_atan2()](#function-f_atan2)

**Usage:** 

- fn = f_asin();
- fn = f_asin(a);

**Description:** 

A factory that generates function literals based on `asin(a)`, where the `a`
argument can optionally be replaced with a constant.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`a`                  | If given, replaces the argument.

---

### Function: f\_acos()

**Synopsis:** Returns a function to calculate the arccosine of a value.

**Topics:** [Function Literals](Topics#function-literals), [Math Operators](Topics#math-operators)

**See Also:** [f\_sin()](#function-f_sin), [f\_cos()](#function-f_cos), [f\_tan()](#function-f_tan), [f\_asin()](#function-f_asin), [f\_atan()](#function-f_atan), [f\_atan2()](#function-f_atan2)

**Usage:** 

- fn = f_acos();
- fn = f_acos(a);

**Description:** 

A factory that generates function literals based on `acos(a)`, where the `a`
argument can optionally be replaced with a constant.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`a`                  | If given, replaces the argument.

---

### Function: f\_atan()

**Synopsis:** Returns a function to calculate the arctangent of a value.

**Topics:** [Function Literals](Topics#function-literals), [Math Operators](Topics#math-operators)

**See Also:** [f\_sin()](#function-f_sin), [f\_cos()](#function-f_cos), [f\_tan()](#function-f_tan), [f\_asin()](#function-f_asin), [f\_acos()](#function-f_acos), [f\_atan2()](#function-f_atan2)

**Usage:** 

- fn = f_atan();
- fn = f_atan(a);

**Description:** 

A factory that generates function literals based on `atan(a)`, where the `a`
argument can optionally be replaced with a constant.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`a`                  | If given, replaces the argument.

---

### Function: f\_atan2()

**Synopsis:** Returns a function to calculate the arctangent of `y` and `x`

**Topics:** [Function Literals](Topics#function-literals), [Math Operators](Topics#math-operators)

**See Also:** [f\_sin()](#function-f_sin), [f\_cos()](#function-f_cos), [f\_tan()](#function-f_tan), [f\_asin()](#function-f_asin), [f\_acos()](#function-f_acos), [f\_atan()](#function-f_atan)

**Usage:** 

- fn = f_atan2();
- fn = f_atan2(a=);
- fn = f_atan2(b);
- fn = f_atan2(a=,b=);

**Description:** 

A factory that generates function literals based on `atan2(a,b)`, where either
or both of the `a` or `b` arguments can be replaced with constants.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`a`                  | If given, replaces the first argument.
`b`                  | If given, replaces the second argument.

---

## Section: String Operators


### Function: f\_len()

**Synopsis:** Returns a function to calculate the length of a string or list.

**Topics:** [Function Literals](Topics#function-literals), [String Operators](Topics#string-operators)

**See Also:** [f\_chr()](#function-f_chr), [f\_ord()](#function-f_ord), [f\_str()](#function-f_str), [f\_str2()](#function-f_str2), [f\_str3()](#function-f_str3)

**Usage:** 

- fn = f_len();
- fn = f_len(a);

**Description:** 

A factory that generates function literals based on `len(a)`, where the `a`
argument can optionally be replaced with a constant.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`a`                  | If given, replaces the argument.

---

### Function: f\_chr()

**Synopsis:** Returns a function to get a string character from its ordinal number.

**Topics:** [Function Literals](Topics#function-literals), [String Operators](Topics#string-operators)

**See Also:** [f\_len()](#function-f_len), [f\_ord()](#function-f_ord), [f\_str()](#function-f_str), [f\_str2()](#function-f_str2), [f\_str3()](#function-f_str3)

**Usage:** 

- fn = f_chr();
- fn = f_chr(a);

**Description:** 

A factory that generates function literals based on `chr(a)`, where the `a`
argument can optionally be replaced with a constant.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`a`                  | If given, replaces the argument.

---

### Function: f\_ord()

**Synopsis:** Returns a function to get the ordinal number of a string character.

**Topics:** [Function Literals](Topics#function-literals), [String Operators](Topics#string-operators)

**See Also:** [f\_len()](#function-f_len), [f\_chr()](#function-f_chr), [f\_str()](#function-f_str), [f\_str2()](#function-f_str2), [f\_str3()](#function-f_str3)

**Usage:** 

- fn = f_ord();
- fn = f_ord(a);

**Description:** 

A factory that generates function literals based on `ord(a)`, where the `a`
argument can optionally be replaced with a constant.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`a`                  | If given, replaces the argument.

---

### Function: f\_str()

**Synopsis:** Returns a function to get the string representation of an arbitrary value.

**Topics:** [Function Literals](Topics#function-literals), [String Operators](Topics#string-operators)

**See Also:** [f\_len()](#function-f_len), [f\_chr()](#function-f_chr), [f\_ord()](#function-f_ord), [f\_str2()](#function-f_str2), [f\_str3()](#function-f_str3)

**Usage:** 

- fn = f_str();
- fn = f_str(a);

**Description:** 

A factory that generates function literals based on `str(a)`, where the `a`
argument can optionally be replaced with a constant.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`a`                  | If given, replaces the argument.

---

### Function: f\_str2()

**Synopsis:** Returns a function to concatenate the string representations of two arbitrary values.

**Topics:** [Function Literals](Topics#function-literals), [String Operators](Topics#string-operators)

**See Also:** [f\_len()](#function-f_len), [f\_chr()](#function-f_chr), [f\_ord()](#function-f_ord), [f\_str()](#function-f_str), [f\_str3()](#function-f_str3)

**Usage:** 

- fn = f_str2();
- fn = f_str2(a=);
- fn = f_str2(b);
- fn = f_str2(a=,b=);

**Description:** 

A factory that generates function literals based on `str(a,b)`, where either
or both of the `a` or `b` arguments can be replaced with constants.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`a`                  | If given, replaces the first argument.
`b`                  | If given, replaces the second argument.

---

### Function: f\_str3()

**Synopsis:** Returns a function to concatenate the string representations of three arbitrary values.

**Topics:** [Function Literals](Topics#function-literals), [Math Operators](Topics#math-operators)

**See Also:** [f\_len()](#function-f_len), [f\_chr()](#function-f_chr), [f\_ord()](#function-f_ord), [f\_str()](#function-f_str), [f\_str2()](#function-f_str2)

**Usage:** 

- fn = f_str3();
- fn = f_str3(a=);
- fn = f_str3(b=);
- fn = f_str3(c=);
- fn = f_str3(a=,b=);
- fn = f_str3(b=,c=);
- fn = f_str3(a=,c=);
- fn = f_str3(a=,b=,c=);

**Description:** 

A factory that generates function literals based on `str(a,b,c)`, where any
or all of the `a`, `b`, or`c` arguments can be replaced with constants.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`a`                  | If given, replaces the first argument.
`b`                  | If given, replaces the second argument.
`c`                  | If given, replaces the third argument.

---

## Section: Miscellaneous Operators


### Function: f\_floor()

**Synopsis:** Returns a function to calculate the integer floor of a given number.

**Topics:** [Function Literals](Topics#function-literals), [Math Operators](Topics#math-operators)

**See Also:** [f\_ceil()](#function-f_ceil), [f\_round()](#function-f_round)

**Usage:** 

- fn = f_floor();
- fn = f_floor(a);

**Description:** 

A factory that generates function literals based on `floor(a)`, where the `a`
argument can optionally be replaced with a constant.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`a`                  | If given, replaces the argument.

---

### Function: f\_round()

**Synopsis:** Returns a function to calculate the integer rounding of a given number.

**Topics:** [Function Literals](Topics#function-literals), [Math Operators](Topics#math-operators)

**See Also:** [f\_floor()](#function-f_floor), [f\_ceil()](#function-f_ceil)

**Usage:** 

- fn = f_round();
- fn = f_round(a);

**Description:** 

A factory that generates function literals based on `round(a)`, where the `a`
argument can optionally be replaced with a constant.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`a`                  | If given, replaces the argument.

---

### Function: f\_ceil()

**Synopsis:** Returns a function to calculate the integer ceiling of a given number.

**Topics:** [Function Literals](Topics#function-literals), [Math Operators](Topics#math-operators)

**See Also:** [f\_floor()](#function-f_floor), [f\_round()](#function-f_round)

**Usage:** 

- fn = f_ceil();
- fn = f_ceil(a);

**Description:** 

A factory that generates function literals based on `ceil(a)`, where the `a`
argument can optionally be replaced with a constant.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`a`                  | If given, replaces the argument.

---

### Function: f\_abs()

**Synopsis:** Returns a function to calculate the absolute value of a given number.

**Topics:** [Function Literals](Topics#function-literals), [Math Operators](Topics#math-operators)

**See Also:** [f\_sign()](#function-f_sign), [f\_ln()](#function-f_ln), [f\_log()](#function-f_log), [f\_exp()](#function-f_exp), [f\_sqr()](#function-f_sqr), [f\_sqrt()](#function-f_sqrt)

**Usage:** 

- fn = f_abs();
- fn = f_abs(a);

**Description:** 

A factory that generates function literals based on `abs(a)`, where the `a`
argument can optionally be replaced with a constant.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`a`                  | If given, replaces the argument.

---

### Function: f\_sign()

**Synopsis:** Returns a function to calculate the sign of a given number.

**Topics:** [Function Literals](Topics#function-literals), [Math Operators](Topics#math-operators)

**See Also:** [f\_abs()](#function-f_abs), [f\_ln()](#function-f_ln), [f\_log()](#function-f_log), [f\_exp()](#function-f_exp), [f\_sqr()](#function-f_sqr), [f\_sqrt()](#function-f_sqrt)

**Usage:** 

- fn = f_sign();
- fn = f_sign(a);

**Description:** 

A factory that generates function literals based on `sign(a)`, where the `a`
argument can optionally be replaced with a constant.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`a`                  | If given, replaces the argument.

---

### Function: f\_ln()

**Synopsis:** Returns a function to calculate the natural logarithm of a given number.

**Topics:** [Function Literals](Topics#function-literals), [Math Operators](Topics#math-operators)

**See Also:** [f\_abs()](#function-f_abs), [f\_sign()](#function-f_sign), [f\_log()](#function-f_log), [f\_exp()](#function-f_exp), [f\_sqr()](#function-f_sqr), [f\_sqrt()](#function-f_sqrt)

**Usage:** 

- fn = f_ln();
- fn = f_ln(a);

**Description:** 

A factory that generates function literals based on `ln(a)`, where the `a`
argument can optionally be replaced with a constant.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`a`                  | If given, replaces the argument.

---

### Function: f\_log()

**Synopsis:** Returns a function to calculate the base 10 logarithm of a given number.

**Topics:** [Function Literals](Topics#function-literals), [Math Operators](Topics#math-operators)

**See Also:** [f\_abs()](#function-f_abs), [f\_sign()](#function-f_sign), [f\_ln()](#function-f_ln), [f\_exp()](#function-f_exp), [f\_sqr()](#function-f_sqr), [f\_sqrt()](#function-f_sqrt)

**Usage:** 

- fn = f_log();
- fn = f_log(a);

**Description:** 

A factory that generates function literals based on `log(a)`, where the `a`
argument can optionally be replaced with a constant.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`a`                  | If given, replaces the argument.

---

### Function: f\_exp()

**Synopsis:** Returns a function to calculate the natural exponent of a given number.

**Topics:** [Function Literals](Topics#function-literals), [Math Operators](Topics#math-operators)

**See Also:** [f\_abs()](#function-f_abs), [f\_sign()](#function-f_sign), [f\_ln()](#function-f_ln), [f\_log()](#function-f_log), [f\_sqr()](#function-f_sqr), [f\_sqrt()](#function-f_sqrt)

**Usage:** 

- fn = f_exp();
- fn = f_exp(a);

**Description:** 

A factory that generates function literals based on `exp(a)`, where the `a`
argument can optionally be replaced with a constant.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`a`                  | If given, replaces the argument.

---

### Function: f\_sqr()

**Synopsis:** Returns a function to calculate the square of a given number.

**Topics:** [Function Literals](Topics#function-literals), [Math Operators](Topics#math-operators)

**See Also:** [f\_abs()](#function-f_abs), [f\_sign()](#function-f_sign), [f\_ln()](#function-f_ln), [f\_log()](#function-f_log), [f\_exp()](#function-f_exp), [f\_sqrt()](#function-f_sqrt)

**Usage:** 

- fn = f_sqr();
- fn = f_sqr(a);

**Description:** 

A factory that generates function literals based on `a*a`, where the `a`
argument can optionally be replaced with a constant.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`a`                  | If given, replaces the argument.

---

### Function: f\_sqrt()

**Synopsis:** Returns a function to calculate the square root of a given number.

**Topics:** [Function Literals](Topics#function-literals), [Math Operators](Topics#math-operators)

**See Also:** [f\_abs()](#function-f_abs), [f\_sign()](#function-f_sign), [f\_ln()](#function-f_ln), [f\_log()](#function-f_log), [f\_exp()](#function-f_exp), [f\_sqr()](#function-f_sqr)

**Usage:** 

- fn = f_sqrt();
- fn = f_sqrt(a);

**Description:** 

A factory that generates function literals based on `sqrt(a)`, where the `a`
argument can optionally be replaced with a constant.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`a`                  | If given, replaces the argument.

---

### Function: f\_norm()

**Synopsis:** Returns a function to calculate the norm of a given vector.

**Topics:** [Function Literals](Topics#function-literals), [Vectors](Topics#vectors)

**See Also:** [f\_abs()](#function-f_abs), [f\_sign()](#function-f_sign), [f\_cross()](#function-f_cross)

**Usage:** 

- fn = f_norm();
- fn = f_norm(a);

**Description:** 

A factory that generates function literals based on `norm(a)`, where the `a`
argument can optionally be replaced with a constant.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`a`                  | If given, replaces the argument.

---

### Function: f\_cross()

**Synopsis:** Returns a function to calculate the norm of a given vector.

**Topics:** [Function Literals](Topics#function-literals), [Vectors](Topics#vectors)

**See Also:** [f\_norm()](#function-f_norm), [f\_abs()](#function-f_abs), [f\_sign()](#function-f_sign)

**Usage:** 

- fn = f_cross();
- fn = f_cross(a=);
- fn = f_cross(b);
- fn = f_cross(a=,b=);

**Description:** 

A factory that generates function literals based on `str(a,b)`, where either
or both of the `a` or `b` arguments can be replaced with constants.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`a`                  | If given, replaces the first argument.
`b`                  | If given, replaces the second argument.

---

## Section: Type Queries


### Function: f\_is\_def()

**Synopsis:** Returns a function to determine if a value is not `undef`.

**Topics:** [Function Literals](Topics#function-literals), [Type Queries](Topics#type-queries)

**See Also:** [f\_is\_undef()](#function-f_is_undef), [f\_is\_bool()](#function-f_is_bool), [f\_is\_num()](#function-f_is_num), [f\_is\_string()](#function-f_is_string), [f\_is\_list()](#function-f_is_list)

**Usage:** 

- fn = f_is_def();

**Description:** 

A factory that returns function literals equivalent to `is_def(a)`.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`a`                  | If given, replaces the argument.

---

### Function: f\_is\_undef()

**Synopsis:** Returns a function to determine if a value is `undef`.

**Topics:** [Function Literals](Topics#function-literals), [Type Queries](Topics#type-queries)

**See Also:** [f\_is\_bool()](#function-f_is_bool), [f\_is\_num()](#function-f_is_num), [f\_is\_string()](#function-f_is_string), [f\_is\_list()](#function-f_is_list)

**Usage:** 

- fn = f_is_undef();

**Description:** 

A factory that returns function literals equivalent to `is_undef(a)`.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`a`                  | If given, replaces the argument.

---

### Function: f\_is\_bool()

**Synopsis:** Returns a function to determine if a value is a boolean.

**Topics:** [Function Literals](Topics#function-literals), [Type Queries](Topics#type-queries)

**See Also:** [f\_is\_undef()](#function-f_is_undef), [f\_is\_num()](#function-f_is_num), [f\_is\_string()](#function-f_is_string), [f\_is\_list()](#function-f_is_list)

**Usage:** 

- fn = f_is_bool();

**Description:** 

A factory that returns function literals equivalent to `is_bool(a)`.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`a`                  | If given, replaces the argument.

---

### Function: f\_is\_num()

**Synopsis:** Returns a function to determine if a value is a number.

**Topics:** [Function Literals](Topics#function-literals), [Type Queries](Topics#type-queries)

**See Also:** [f\_is\_undef()](#function-f_is_undef), [f\_is\_bool()](#function-f_is_bool), [f\_is\_string()](#function-f_is_string), [f\_is\_list()](#function-f_is_list)

**Usage:** 

- fn = f_is_num();

**Description:** 

A factory that returns function literals equivalent to `is_num(a)`.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`a`                  | If given, replaces the argument.

---

### Function: f\_is\_int()

**Synopsis:** Returns a function to determine if a value is an integer number.

**Topics:** [Function Literals](Topics#function-literals), [Type Queries](Topics#type-queries)

**See Also:** [f\_is\_undef()](#function-f_is_undef), [f\_is\_bool()](#function-f_is_bool), [f\_is\_num()](#function-f_is_num), [f\_is\_string()](#function-f_is_string), [f\_is\_list()](#function-f_is_list)

**Usage:** 

- fn = f_is_int();

**Description:** 

A factory that returns function literals equivalent to `is_int(a)`.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`a`                  | If given, replaces the argument.

---

### Function: f\_is\_nan()

**Synopsis:** Returns a function to determine if a value is a number type that is Not a Number (NaN).

**Topics:** [Function Literals](Topics#function-literals), [Type Queries](Topics#type-queries)

**See Also:** [f\_is\_undef()](#function-f_is_undef), [f\_is\_bool()](#function-f_is_bool), [f\_is\_num()](#function-f_is_num), [f\_is\_int()](#function-f_is_int), [f\_is\_string()](#function-f_is_string), [f\_is\_list()](#function-f_is_list)

**Usage:** 

- fn = f_is_nan();

**Description:** 

A factory that returns function literals equivalent to `is_nan(a)`.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`a`                  | If given, replaces the argument.

---

### Function: f\_is\_finite()

**Synopsis:** Returns a function to determine if a value is a number type that is finite.

**Topics:** [Function Literals](Topics#function-literals), [Type Queries](Topics#type-queries)

**See Also:** [f\_is\_undef()](#function-f_is_undef), [f\_is\_bool()](#function-f_is_bool), [f\_is\_num()](#function-f_is_num), [f\_is\_int()](#function-f_is_int), [f\_is\_string()](#function-f_is_string), [f\_is\_list()](#function-f_is_list)

**Usage:** 

- fn = f_is_finite();

**Description:** 

A factory that returns function literals equivalent to `is_finite(a)`.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`a`                  | If given, replaces the argument.

---

### Function: f\_is\_string()

**Synopsis:** Returns a function to determine if a value is a string.

**Topics:** [Function Literals](Topics#function-literals), [Type Queries](Topics#type-queries)

**See Also:** [f\_is\_undef()](#function-f_is_undef), [f\_is\_bool()](#function-f_is_bool), [f\_is\_num()](#function-f_is_num), [f\_is\_int()](#function-f_is_int), [f\_is\_list()](#function-f_is_list)

**Usage:** 

- fn = f_is_string();

**Description:** 

A factory that returns function literals equivalent to `is_string(a)`.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`a`                  | If given, replaces the argument.

---

### Function: f\_is\_list()

**Synopsis:** Returns a function to determine if a value is a list.

**Topics:** [Function Literals](Topics#function-literals), [Type Queries](Topics#type-queries)

**See Also:** [f\_is\_undef()](#function-f_is_undef), [f\_is\_bool()](#function-f_is_bool), [f\_is\_num()](#function-f_is_num), [f\_is\_int()](#function-f_is_int), [f\_is\_string()](#function-f_is_string)

**Usage:** 

- fn = f_is_list();

**Description:** 

A factory that returns function literals equivalent to `is_list(a)`.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`a`                  | If given, replaces the argument.

---

### Function: f\_is\_range()

**Synopsis:** Returns a function to determine if a value is a range.

**Topics:** [Function Literals](Topics#function-literals), [Type Queries](Topics#type-queries)

**See Also:** [f\_is\_undef()](#function-f_is_undef), [f\_is\_bool()](#function-f_is_bool), [f\_is\_num()](#function-f_is_num), [f\_is\_int()](#function-f_is_int), [f\_is\_string()](#function-f_is_string), [f\_is\_list()](#function-f_is_list)

**Usage:** 

- fn = f_is_range();

**Description:** 

A factory that returns function literals equivalent to `is_range(a)`.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`a`                  | If given, replaces the argument.

---

### Function: f\_is\_function()

**Synopsis:** Returns a function to determine if a value is a function literal.

**Topics:** [Function Literals](Topics#function-literals), [Type Queries](Topics#type-queries)

**See Also:** [f\_is\_undef()](#function-f_is_undef), [f\_is\_bool()](#function-f_is_bool), [f\_is\_num()](#function-f_is_num), [f\_is\_int()](#function-f_is_int), [f\_is\_string()](#function-f_is_string), [f\_is\_list()](#function-f_is_list)

**Usage:** 

- fn = f_is_function();

**Description:** 

A factory that returns function literals equivalent to `is_function(a)`.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`a`                  | If given, replaces the argument.

---

### Function: f\_is\_vector()

**Synopsis:** Returns a function to determine if a value is a list of numbers.

**Topics:** [Function Literals](Topics#function-literals), [Type Queries](Topics#type-queries)

**See Also:** [f\_is\_undef()](#function-f_is_undef), [f\_is\_bool()](#function-f_is_bool), [f\_is\_num()](#function-f_is_num), [f\_is\_int()](#function-f_is_int), [f\_is\_string()](#function-f_is_string), [f\_is\_list()](#function-f_is_list)

**Usage:** 

- fn = f_is_vector();

**Description:** 

A factory that returns function literals equivalent to `is_vector(a)`.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`a`                  | If given, replaces the argument.

---

### Function: f\_is\_path()

**Synopsis:** Returns a function to determine if a value is a Path (a list of points).

**Topics:** [Function Literals](Topics#function-literals), [Type Queries](Topics#type-queries)

**See Also:** [f\_is\_undef()](#function-f_is_undef), [f\_is\_bool()](#function-f_is_bool), [f\_is\_num()](#function-f_is_num), [f\_is\_int()](#function-f_is_int), [f\_is\_string()](#function-f_is_string), [f\_is\_list()](#function-f_is_list)

**Usage:** 

- fn = f_is_path();

**Description:** 

A factory that returns function literals equivalent to `is_path(a)`.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`a`                  | If given, replaces the argument.

---

### Function: f\_is\_region()

**Synopsis:** Returns a function to determine if a value is a Region (a list of Paths).

**Topics:** [Function Literals](Topics#function-literals), [Type Queries](Topics#type-queries)

**See Also:** [f\_is\_undef()](#function-f_is_undef), [f\_is\_bool()](#function-f_is_bool), [f\_is\_num()](#function-f_is_num), [f\_is\_int()](#function-f_is_int), [f\_is\_string()](#function-f_is_string), [f\_is\_list()](#function-f_is_list)

**Usage:** 

- fn = f_is_region();

**Description:** 

A factory that returns function literals equivalent to `is_region(a)`.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`a`                  | If given, replaces the argument.

---

### Function: f\_is\_vnf()

**Synopsis:** Returns a function to determine if a value is a VNF structure.

**Topics:** [Function Literals](Topics#function-literals), [Type Queries](Topics#type-queries)

**See Also:** [f\_is\_undef()](#function-f_is_undef), [f\_is\_bool()](#function-f_is_bool), [f\_is\_num()](#function-f_is_num), [f\_is\_int()](#function-f_is_int), [f\_is\_string()](#function-f_is_string), [f\_is\_list()](#function-f_is_list)

**Usage:** 

- fn = f_is_vnf();

**Description:** 

A factory that returns function literals equivalent to `is_vnf(a)`.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`a`                  | If given, replaces the argument.

---

### Function: f\_is\_bezier\_patch()

**Synopsis:** Returns a function to determine if a value is a Bezier Patch structure.

**Topics:** [Function Literals](Topics#function-literals), [Type Queries](Topics#type-queries)

**See Also:** [f\_is\_undef()](#function-f_is_undef), [f\_is\_bool()](#function-f_is_bool), [f\_is\_num()](#function-f_is_num), [f\_is\_int()](#function-f_is_int), [f\_is\_string()](#function-f_is_string), [f\_is\_list()](#function-f_is_list)

**Usage:** 

- fn = f_is_bezier_patch();

**Description:** 

A factory that returns function literals equivalent to `is_bezier_patch(a)`.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`a`                  | If given, replaces the argument.

---


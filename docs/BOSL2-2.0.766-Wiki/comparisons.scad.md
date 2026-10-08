# LibFile: comparisons.scad

Functions for comparisons with lists, ordering and sorting

To use, add the following lines to the beginning of your file:

    include <BOSL2/std.scad>

## File Contents

1. [Section: List comparison operations](#section-list-comparison-operations)
    - [`approx()`](#function-approx) – Returns true if two values are equal to within a small epsilon value.
    - [`all_zero()`](#function-all_zero) – Returns true if the value(s) given are approximately zero.
    - [`all_nonzero()`](#function-all_nonzero) – Returns true if the value(s) given are not approximately zero.
    - [`all_positive()`](#function-all_positive) – Returns true if the value(s) given are greater than zero.
    - [`all_negative()`](#function-all_negative) – Returns true if the value(s) given are less than zero.
    - [`all_nonpositive()`](#function-all_nonpositive) – Returns true if the value(s) given are less than or equal to zero.
    - [`all_nonnegative()`](#function-all_nonnegative) – Returns true if the value(s) given are greater than or equal to zero.
    - [`all_equal()`](#function-all_equal) – Returns true if all items in a list are approximately equal to each other.
    - [`are_ends_equal()`](#function-are_ends_equal) – Returns true if the first and last items in a list are approximately equal.
    - [`is_increasing()`](#function-is_increasing) – Returns true if every item in a list is greater than the previous item.
    - [`is_decreasing()`](#function-is_decreasing) – Returns true if every item in a list is less than the previous item.
    - [`compare_vals()`](#function-compare_vals) – Compares two values, possibly of different type.
    - [`compare_lists()`](#function-compare_lists) – Compares two lists of values, possibly of different type.

2. [Section: Finding the index of the minimum or maximum of a list](#section-finding-the-index-of-the-minimum-or-maximum-of-a-list)
    - [`min_index()`](#function-min_index) – Returns the index of the minimum value in the given list.
    - [`max_index()`](#function-max_index) – Returns the index of the maximum value in the given list.

3. [Section: Dealing with duplicate list entries](#section-dealing-with-duplicate-list-entries)
    - [`find_approx()`](#function-find_approx) – Finds the indexes of the item(s) in the given list that are approximately the given value.
    - [`deduplicate()`](#function-deduplicate) – Returns a list with all consecutive duplicate values removed.
    - [`deduplicate_indexed()`](#function-deduplicate_indexed) – Takes a list of indices into a list of values, and returns a list of indices whose values are not consecutively the same.
    - [`list_wrap()`](#function-list_wrap) – Returns a list whose last value is the same as the first.
    - [`list_unwrap()`](#function-list_unwrap) – Removes the last item of a list if its first and last values are equal.
    - [`unique()`](#function-unique) – Returns a sorted list with all duplicates removed.
    - [`unique_count()`](#function-unique_count) – Returns a sorted list of unique items with counts.
    - [`unique_approx()`](#function-unique_approx) – Returns a subset whose retained items are pairwise separated by a tolerance.
    - [`unique_approx_indexed()`](#function-unique_approx_indexed) – Returns indices of a subset whose retained items are separated by more than a tolerance.

4. [Section: Sorting](#section-sorting)
    - [`sort()`](#function-sort) – Returns a sorted list.
    - [`sortidx()`](#function-sortidx) – Returns a list of sorted indices into a list.
    - [`group_sort()`](#function-group_sort) – Returns a sorted list of groups of values.
    - [`group_data()`](#function-group_data) – Groups list data by integer group numbers.
    - [`list_smallest()`](#function-list_smallest) – Returns the `k` smallest values in the list, in arbitrary order.
    - [`list_largest()`](#function-list_largest) – Returns the `k` largest values in the list, in arbitrary order.


## Section: List comparison operations


### Function: approx()

**Synopsis:** Returns true if two values are equal to within a small epsilon value.

**Topics:** [Comparisons](Topics#comparisons)

**See Also:** [all\_zero()](#function-all_zero), [all\_nonzero()](#function-all_nonzero)

**Usage:** 

- test = approx(a, b, [eps])

**Description:** 

Compares two numbers, vectors, or matrices.  Returns true if they are closer than `eps` to each other.
Results are undefined if `a` and `b` are of different types, or if vectors or matrices contain non-numbers.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`a`                  | First value.
`b`                  | Second value.
`eps`                | The maximum allowed difference between `a` and `b` to consider as "no difference". Default: 1e-9.

**Example 1:** 

    include <BOSL2/std.scad>
    test1 = approx(-0.3333333333,-1/3);  // Returns: true
    test2 = approx(0.3333333333,1/3);    // Returns: true
    test3 = approx(0.3333,1/3);          // Returns: false
    test4 = approx(0.3333,1/3,eps=1e-3); // Returns: true
    test5 = approx(PI,3.1415926536);     // Returns: true
    test6 = approx([0,0,sin(45)],[0,0,sqrt(2)/2]);  // Returns: true

<br clear="all" /><br/>

---

### Function: all\_zero()

**Synopsis:** Returns true if the value(s) given are approximately zero.

**Topics:** [Comparisons](Topics#comparisons), [List Handling](Topics#list-handling)

**See Also:** [approx()](#function-approx), [all\_nonzero()](#function-all_nonzero)

**Usage:** 

- x = all_zero(x, [eps]);

**Description:** 

Returns true if its argument is approximately zero, to within `eps`.
If passed a nonempty list, returns true if all its entries are approximately zero.
Otherwise, returns false.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`x`                  | The value to check.
`eps`                | The maximum allowed variance.  Default: 1e-9

**Example 1:** 

    include <BOSL2/std.scad>
    a = all_zero(0);  // Returns: true.
    b = all_zero(1e-3);  // Returns: false.
    c = all_zero([0,0,0]);  // Returns: true.
    d = all_zero([0,0,1e-3]);  // Returns: false.
    e = all_zero(1,eps=1);       // Returns: true.
    f = all_zero([1],eps=1);     // Returns: true.
    g = all_zero(0,eps=0);       // Returns: true.

<br clear="all" /><br/>

---

### Function: all\_nonzero()

**Synopsis:** Returns true if the value(s) given are not approximately zero.

**Topics:** [Comparisons](Topics#comparisons), [List Handling](Topics#list-handling)

**See Also:** [approx()](#function-approx), [all\_zero()](#function-all_zero)

**Usage:** 

- test = all_nonzero(x, [eps]);

**Description:** 

Returns true if the absolute value of its argument is greater than `eps`.
If passed a nonempty list, returns true if all its entries have absolute value greater than `eps`.
Otherwise, returns false.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`x`                  | The value to check.
`eps`                | The maximum allowed variance.  Default: 1e-9

**Example 1:** 

    include <BOSL2/std.scad>
    a = all_nonzero(0);  // Returns: false.
    b = all_nonzero(1e-3);  // Returns: true.
    c = all_nonzero([0,0,0]);  // Returns: false.
    d = all_nonzero([0,0,1e-3]);  // Returns: false.
    e = all_nonzero([1e-3,1e-3,1e-3]);  // Returns: true.
    f = all_nonzero(1,eps=1);             // Returns: false.
    g = all_nonzero([1],eps=1);           // Returns: false.
    h = all_nonzero([0],eps=0);           // Returns: false.

<br clear="all" /><br/>

---

### Function: all\_positive()

**Synopsis:** Returns true if the value(s) given are greater than zero.

**Topics:** [Comparisons](Topics#comparisons), [List Handling](Topics#list-handling)

**See Also:** [approx()](#function-approx), [all\_zero()](#function-all_zero), [all\_nonzero()](#function-all_nonzero), [all\_negative()](#function-all_negative), [all\_nonpositive()](#function-all_nonpositive), [all\_nonnegative()](#function-all_nonnegative)

**Usage:** 

- test = all_positive(x,[eps]);

**Description:** 

Returns true if the argument is finite and greater than zero, within epsilon tolerance if desired.
If passed a list returns true if all the entries are finite positive numbers.
Otherwise, returns false.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`x`                  | The value to check.
`eps`                | Tolerance. Default: 0

**Example 1:** 

    include <BOSL2/std.scad>
    a = all_positive(-2);  // Returns: false.
    b = all_positive(0);  // Returns: false.
    c = all_positive(2);  // Returns: true.
    d = all_positive([0,0,0]);  // Returns: false.
    e = all_positive([0,1,2]);  // Returns: false.
    f = all_positive([3,1,2]);  // Returns: true.
    g = all_positive([3,-1,2]);  // Returns: false.

<br clear="all" /><br/>

---

### Function: all\_negative()

**Synopsis:** Returns true if the value(s) given are less than zero.

**Topics:** [Comparisons](Topics#comparisons), [List Handling](Topics#list-handling)

**See Also:** [approx()](#function-approx), [all\_zero()](#function-all_zero), [all\_nonzero()](#function-all_nonzero), [all\_positive()](#function-all_positive), [all\_nonpositive()](#function-all_nonpositive), [all\_nonnegative()](#function-all_nonnegative)

**Usage:** 

- test = all_negative(x, [eps]);

**Description:** 

Returns true if the argument is finite and less than zero, within epsilon tolerance if desired.
If passed a list, returns true if all the elements are finite negative numbers.
Otherwise, returns false.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`x`                  | The value to check.
`eps`                | tolerance.  Default: 0

**Example 1:** 

    include <BOSL2/std.scad>
    a = all_negative(-2);  // Returns: true.
    b = all_negative(0);  // Returns: false.
    c = all_negative(2);  // Returns: false.
    d = all_negative([0,0,0]);  // Returns: false.
    e = all_negative([0,1,2]);  // Returns: false.
    f = all_negative([3,1,2]);  // Returns: false.
    g = all_negative([3,-1,2]);  // Returns: false.
    h = all_negative([-3,-1,-2]);  // Returns: true.

<br clear="all" /><br/>

---

### Function: all\_nonpositive()

**Synopsis:** Returns true if the value(s) given are less than or equal to zero.

**Topics:** [Comparisons](Topics#comparisons), [List Handling](Topics#list-handling)

**See Also:** [approx()](#function-approx), [all\_zero()](#function-all_zero), [all\_nonzero()](#function-all_nonzero), [all\_positive()](#function-all_positive), [all\_negative()](#function-all_negative), [all\_nonnegative()](#function-all_nonnegative)

**Usage:** 

- all_nonpositive(x, [eps]);

**Description:** 

Returns true if its argument is finite and less than or equal to zero.
If passed a list, returns true if all the elements are finite non-positive numbers.
Otherwise, returns false.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`x`                  | The value to check.
`eps`                | tolerance.  Default: 0

**Example 1:** 

    include <BOSL2/std.scad>
    a = all_nonpositive(-2);  // Returns: true.
    b = all_nonpositive(0);  // Returns: true.
    c = all_nonpositive(2);  // Returns: false.
    d = all_nonpositive([0,0,0]);  // Returns: true.
    e = all_nonpositive([0,1,2]);  // Returns: false.
    f = all_nonpositive([3,1,2]);  // Returns: false.
    g = all_nonpositive([3,-1,2]);  // Returns: false.
    h = all_nonpositive([-3,-1,-2]);  // Returns: true.

<br clear="all" /><br/>

---

### Function: all\_nonnegative()

**Synopsis:** Returns true if the value(s) given are greater than or equal to zero.

**Topics:** [Comparisons](Topics#comparisons), [List Handling](Topics#list-handling)

**See Also:** [approx()](#function-approx), [all\_zero()](#function-all_zero), [all\_nonzero()](#function-all_nonzero), [all\_positive()](#function-all_positive), [all\_negative()](#function-all_negative), [all\_nonpositive()](#function-all_nonpositive)

**Usage:** 

- all_nonnegative(x, [eps]);

**Description:** 

Returns true if the finite number passed to it is greater than or equal to zero.
If passed a list, returns true if all the elements are finite non-negative numbers.
Otherwise, returns false.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`x`                  | The value to check.
`eps`                | tolerance.  Default: 0

**Example 1:** 

    include <BOSL2/std.scad>
    a = all_nonnegative(-2);  // Returns: false.
    b = all_nonnegative(0);  // Returns: true.
    c = all_nonnegative(2);  // Returns: true.
    d = all_nonnegative([0,0,0]);  // Returns: true.
    e = all_nonnegative([0,1,2]);  // Returns: true.
    f = all_nonnegative([0,-1,-2]);  // Returns: false.
    g = all_nonnegative([3,1,2]);  // Returns: true.
    h = all_nonnegative([3,-1,2]);  // Returns: false.
    i = all_nonnegative([-3,-1,-2]);  // Returns: false.

<br clear="all" /><br/>

---

### Function: all\_equal()

**Synopsis:** Returns true if all items in a list are approximately equal to each other.

**Topics:** [Comparisons](Topics#comparisons), [List Handling](Topics#list-handling)

**See Also:** [approx()](#function-approx), [all\_zero()](#function-all_zero), [all\_nonzero()](#function-all_nonzero), [all\_positive()](#function-all_positive), [all\_negative()](#function-all_negative), [all\_nonpositive()](#function-all_nonpositive), [all\_nonnegative()](#function-all_nonnegative)

**Usage:** 

- b = all_equal(vec, [eps]);

**Description:** 

Returns true if all of the entries in vec are equal to each other, or approximately equal to each other if eps is set.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`vec`                | vector to check
`eps`                | Set to tolerance for approximate equality.  Default: 0

---

### Function: are\_ends\_equal()

**Synopsis:** Returns true if the first and last items in a list are approximately equal.

**Topics:** [Comparisons](Topics#comparisons), [List Handling](Topics#list-handling)

**See Also:** [approx()](#function-approx), [all\_zero()](#function-all_zero), [all\_nonzero()](#function-all_nonzero), [all\_positive()](#function-all_positive), [all\_negative()](#function-all_negative), [all\_nonpositive()](#function-all_nonpositive), [all\_nonnegative()](#function-all_nonnegative)

**Usage:** 

- are_ends_equal(list, [eps]);

**Description:** 

Returns true if the first and last points in the given list are equal to within epsilon.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`list`               | list to check
`eps`                | Tolerance for approximate equality.  Default: 1e-9

---

### Function: is\_increasing()

**Synopsis:** Returns true if every item in a list is greater than the previous item.

**Topics:** [Comparisons](Topics#comparisons), [List Handling](Topics#list-handling)

**See Also:** [max\_index()](#function-max_index), [min\_index()](#function-min_index), [is\_decreasing()](#function-is_decreasing)

**Usage:** 

- bool = is_increasing(list, [strict]);

**Description:** 

Returns true if the list is (non-strictly) increasing, or strictly increasing if `strict=true`.
The list can be a list of any items that OpenSCAD can compare, or it can be a string, which gets
evaluated character by character.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`list`               | list (or string) to check
`strict`             | set to true to test that list is strictly increasing.  Default: false

**Example 1:** 

    include <BOSL2/std.scad>
    a = is_increasing([1,2,3,4]);  // Returns: true
    b = is_increasing([1,3,2,4]);  // Returns: false
    c = is_increasing([1,3,3,4]);  // Returns: true
    d = is_increasing([1,3,3,4],strict=true);  // Returns: false
    e = is_increasing([4,3,2,1]);  // Returns: false

<br clear="all" /><br/>

---

### Function: is\_decreasing()

**Synopsis:** Returns true if every item in a list is less than the previous item.

**Topics:** [Comparisons](Topics#comparisons), [List Handling](Topics#list-handling)

**See Also:** [max\_index()](#function-max_index), [min\_index()](#function-min_index), [is\_increasing()](#function-is_increasing)

**Usage:** 

- bool = is_decreasing(list, [strict]);

**Description:** 

Returns true if the list is (non-strictly) decreasing, or strictly decreasing if `strict=true`.
The list can be a list of any items that OpenSCAD can compare, or it can be a string, which gets
evaluated character by character.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`list`               | list (or string) to check
`strict`             | set to true to test that list is strictly decreasing.  Default: false

**Example 1:** 

    include <BOSL2/std.scad>
    a = is_decreasing([1,2,3,4]);  // Returns: false
    b = is_decreasing([4,2,3,1]);  // Returns: false
    c = is_decreasing([4,3,2,1]);  // Returns: true

<br clear="all" /><br/>

---

### Function: compare\_vals()

**Synopsis:** Compares two values, possibly of different type.

**Topics:** [Comparisons](Topics#comparisons), [List Handling](Topics#list-handling)

**See Also:** [approx()](#function-approx), [is\_increasing()](#function-is_increasing), [is\_decreasing()](#function-is_decreasing)

**Usage:** 

- test = compare_vals(a, b);

**Description:** 

Compares two values.  Lists are compared recursively.
Returns a negative value if a<b.  Returns a positive value if a>b.  Returns 0 if a==b.
If types are not the same, then undef < bool < nan < num < str < list < range.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`a`                  | First value to compare.
`b`                  | Second value to compare.

---

### Function: compare\_lists()

**Synopsis:** Compares two lists of values, possibly of different type.

**Topics:** [Comparisons](Topics#comparisons), [List Handling](Topics#list-handling)

**See Also:** [compare\_vals()](#function-compare_vals), [approx()](#function-approx), [is\_increasing()](#function-is_increasing), [is\_decreasing()](#function-is_decreasing)

**Usage:** 

- test = compare_lists(a, b)

**Description:** 

Compare contents of two lists using `compare_vals()`.
Returns a negative number if `a`<`b`.
Returns 0 if `a`==`b`.
Returns a positive number if `a`>`b`.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`a`                  | First list to compare.
`b`                  | Second list to compare.

---

## Section: Finding the index of the minimum or maximum of a list


### Function: min\_index()

**Synopsis:** Returns the index of the minimum value in the given list.

**Topics:** [List Handling](Topics#list-handling)

**See Also:** [max\_index()](#function-max_index), [is\_increasing()](#function-is_increasing), [is\_decreasing()](#function-is_decreasing)

**Usage:** 

- idx = min_index(vals);
- idxlist = min_index(vals, all=true);

**Description:** 

Returns the index of the first occurrence of the minimum value in the given list.
If `all` is true then returns a list of all indices where the minimum value occurs.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`vals`               | vector of values
`all`                | set to true to return indices of all occurrences of the minimum.  Default: false

**Example 1:** 

    include <BOSL2/std.scad>
    a = min_index([5,3,9,6,2,7,8,2,1]); // Returns: 8
    b = min_index([5,3,9,6,2,7,8,2,7],all=true); // Returns: [4,7]

<br clear="all" /><br/>

---

### Function: max\_index()

**Synopsis:** Returns the index of the maximum value in the given list.

**Topics:** [List Handling](Topics#list-handling)

**See Also:** [min\_index()](#function-min_index), [is\_increasing()](#function-is_increasing), [is\_decreasing()](#function-is_decreasing)

**Usage:** 

- idx = max_index(vals);
- idxlist = max_index(vals, all=true);

**Description:** 

Returns the index of the first occurrence of the maximum value in the given list.
If `all` is true then returns a list of all indices where the maximum value occurs.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`vals`               | vector of values
`all`                | set to true to return indices of all occurrences of the maximum.  Default: false

**Example 1:** 

    include <BOSL2/std.scad>
    max_index([5,3,9,6,2,7,8,9,1]); // Returns: 2
    max_index([5,3,9,6,2,7,8,9,1],all=true); // Returns: [2,7]

<br clear="all" /><br/>

---

## Section: Dealing with duplicate list entries


### Function: find\_approx()

**Synopsis:** Finds the indexes of the item(s) in the given list that are approximately the given value.

**Topics:** [List Handling](Topics#list-handling)

**See Also:** [in\_list()](lists.scad#function-in_list)

**Usage:** 

- idx = find_approx(val, list, [start=], [eps=]);
- indices = find_approx(val, list, all=true, [start=], [eps=]);

**Description:** 

Finds the first item in `list` that matches `val` to within `eps` tolerance, returning the index.  Returns `undef` if there is no match.
If `all=true` then returns all the items that agree within `eps` and returns the empty list if no such items exist.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`val`                | The value to search for.
`list`               | The list to search.

<abbr title="These args must be used by name, ie: name=value">By&nbsp;Name</abbr> | What it does
-------------------- | ------------
`start`              | The index to start searching from.  Default: 0
`all`                | If true, returns a list of all matching item indices.  Default: false
`eps`                | The maximum allowed floating point rounding error for numeric comparisons.  Default: 1e-9

**Example 1:** 

    include <BOSL2/std.scad>
    find_approx(3,[4,5,3.01,2,2.99], eps=0.1);  // Returns 2
    find_approx(9,[4,5,3.01,2,2.99], eps=0.1);  // Returns undef
    find_approx(3,[4,5,3.01,2,2.99], all=true, eps=0.1);  // Returns [2,4]
    find_approx(9,[4,5,3.01,2,2.99], all=true, eps=0.1);  // Returns []

<br clear="all" /><br/>

---

### Function: deduplicate()

**Synopsis:** Returns a list with all consecutive duplicate values removed.

**Topics:** [List Handling](Topics#list-handling)

**See Also:** [deduplicate\_indexed()](#function-deduplicate_indexed)

**Usage:** 

- list = deduplicate(list, [closed], [eps]);

**Description:** 

Removes consecutive duplicate items in a list.
When `eps` is zero, the comparison between consecutive items is exact.
Otherwise, comparisons use [`approx()`](#function-approx), including recursive comparison of numeric lists.
Unlike [`unique()`](#function-unique) only consecutive duplicates are removed and the list is *not* sorted.
If `closed` is true, the last and first entries are also compared as adjacent items.
If these comparisons would remove every item of nonempty input, one item is retained.
Empty input is returned unchanged.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`list`               | The list to deduplicate.
`closed`             | If true, treats first and last list entry as adjacent.  Default: false
`eps`                | The maximum tolerance between items.  Default: 1e-9

**Example 1:** 

    include <BOSL2/std.scad>
    a = deduplicate([8,3,4,4,4,8,2,3,3,8,8]);  // Returns: [8,3,4,8,2,3,8]
    b = deduplicate(closed=true, [8,3,4,4,4,8,2,3,3,8,8]);  // Returns: [8,3,4,8,2,3]
    c = deduplicate("Hello");  // Returns: "Helo"
    d = deduplicate([[3,4],[7,2],[7,1.99],[1,4]],eps=0.1);  // Returns: [[3,4],[7,1.99],[1,4]]
    e = deduplicate([[7,undef],[7,undef],[1,4],[1,4+1e-12]],eps=0);    // Returns: [[7,undef],[1,4],[1,4+1e-12]]
    f = deduplicate([7,7],closed=true);  // Returns: [7]
    g = deduplicate("aaa",closed=true); // Returns: "a"

<br clear="all" /><br/>

---

### Function: deduplicate\_indexed()

**Synopsis:** Takes a list of indices into a list of values, and returns a list of indices whose values are not consecutively the same.

**Topics:** [List Handling](Topics#list-handling)

**See Also:** [deduplicate()](#function-deduplicate)

**Usage:** 

- new_idxs = deduplicate_indexed(list, [indices], [closed], [eps]);

**Description:** 

Given a list, and a list of indices, removes consecutive indices corresponding to list values that are equal
or approximately equal.  If you omit the `indices` parameter then it defaults to the list `[0,...,len(list)-1]` so
the return value is the indices of the deduplication of the entire input list.  This is useful if you need to
remove the duplicates from list A and then remove the corresponding points from list B.  The `list` input
may itself have duplicates, so multiple distinct index values can correspond to the same list value.
When this happens, the index returned for a run of identical items will be the last index listed in the index list.
Comparisons match [`deduplicate()`](#function-deduplicate): exact equality when `eps` is zero, otherwise [`approx()`](#function-approx),
including recursive comparison of numeric lists.
If `closed` is true, the last and first selected entries are compared as adjacent items.
If no indices would survive from a nonempty selection, the last supplied index is retained.
An empty selection returns `[]`, including when the data is empty and `indices` is omitted.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`list`               | The list that the indices index into.
`indices`            | The list of indices to deduplicate.  Default: `count(len(list))`
`closed`             | If true, treats the last and first selected entries as adjacent, retaining one index if all would be removed. Default: false
`eps`                | Tolerance for recursive approximate comparisons; zero selects exact equality. Default: 1e-9

**Example 1:** 

    include <BOSL2/std.scad>
    a = deduplicate_indexed([8,6,4,6,3], [1,4,3,1,2,2,0,1]);  // Returns: [1,4,1,2,0,1]
    b = deduplicate_indexed([8,6,4,6,3], [1,4,3,1,2,2,0,1], closed=true);  // Returns: [1,4,1,2,0]
    c = deduplicate_indexed([[7,undef],[7,undef],[1,4],[1,4],[1,4+1e-12]],eps=0);    // Returns: [1,3,4]
    d = deduplicate_indexed([7,7],closed=true);          // Returns: [1]
    e = deduplicate_indexed([7,7,7],[2,0],closed=true);  // Returns: [0]
    f = deduplicate_indexed([]);                       // Returns: []
    g = deduplicate_indexed([1,2],[]);                 // Returns: []

<br clear="all" /><br/>

**Example 2:** Remove duplicates from `a` and then remove corresponding points from `b`.

    include <BOSL2/std.scad>
    a = [1, 1, 2, 3, 4, 4, 5, 5, 5];
    b = ["A", "B", "C", "D", "E", "F", "G", "H", "I"];
    ind = deduplicate_indexed(a,count(len(a)));  // Returns: [1,2,3,5,8]
    echo(select(a,ind));         // Displays:  [1,2,3,4,5]
    echo(select(b,ind));         // Displays:  ["B", "C", "D", "F", "I"]

<br clear="all" /><br/>

---

### Function: list\_wrap()

**Synopsis:** Returns a list whose last value is the same as the first.

**Topics:** [List Handling](Topics#list-handling), [Paths](Topics#paths)

**See Also:** [list\_unwrap()](#function-list_unwrap), [deduplicate()](#function-deduplicate)

**Usage:** 

- list_wrap(path, [eps]);

**Description:** 

Force a list to wrap around so that its last point is equal to its first point:  if the first and last entries are equal, simply returns the list unchanged.
Otherwise returns the list with the first point duplicated at the end of the list.  Comparisons are done to the tolerance `eps`.  Lists of length 0 or
1 are returned unchanged.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`list`               | list to unwrap
`eps`                | epsilon for comparison.  Default: 1e-9

---

### Function: list\_unwrap()

**Synopsis:** Removes the last item of a list if its first and last values are equal.

**Topics:** [List Handling](Topics#list-handling), [Paths](Topics#paths)

**See Also:** [list\_wrap()](#function-list_wrap), [deduplicate()](#function-deduplicate)

**Usage:** 

- list_unwrap(list, [eps]);

**Description:** 

If a list's last point matches its first point then delete the last point.  Inverse operation to [`list_wrap()`](#function-list_wrap).  Note that if the first/last points
are repeated then the output may still have the first point equal to the last point.  Comparisons are done to the tolerance `eps`.  If the list has
length 0 or 1 it is returned unchanged.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`list`               | list to unwrap
`eps`                | epsilon for comparison.  Default: 1e-9

---

### Function: unique()

**Synopsis:** Returns a sorted list with all duplicates removed.

**Topics:** [List Handling](Topics#list-handling)

**See Also:** [shuffle()](lists.scad#function-shuffle), [sort()](#function-sort), [sortidx()](#function-sortidx), [unique\_count()](#function-unique_count)

**Usage:** 

- ulist = unique(list);

**Description:** 

Given a string or a list returns the sorted string or the sorted list with all repeated items removed.
The sorting order of non homogeneous lists is the function `sort` order.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`list`               | The list to process.

**Example 1:** 

    include <BOSL2/std.scad>
    sorted = unique([5,2,8,3,1,3,8,7,5]);  // Returns: [1,2,3,5,7,8]
    sorted = unique("axdbxxc");  // Returns: "abcdx"
    sorted = unique([true,2,"xba",[1,0],true,[0,0],3,"a",[0,0],2]); // Returns: [true,2,3,"a","xba",[0,0],[1,0]]

<br clear="all" /><br/>

---

### Function: unique\_count()

**Synopsis:** Returns a sorted list of unique items with counts.

**Topics:** [List Handling](Topics#list-handling)

**See Also:** [shuffle()](lists.scad#function-shuffle), [sort()](#function-sort), [sortidx()](#function-sortidx), [unique()](#function-unique)

**Usage:** 

- sorted_counts = unique_count(list);

**Description:** 

Returns `[sorted,counts]` where `sorted` is a sorted list of the unique items in `list` and `counts` is a list such
that `counts[i]` gives the number of times that `sorted[i]` appears in `list`.
An empty list or empty string returns `[[],[]]`.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`list`               | The list to analyze.

**Example 1:** 

    include <BOSL2/std.scad>
    sorted = unique_count([5,2,8,3,1,3,8,3,5]);  // Returns: [ [1,2,3,5,8], [1,1,3,2,2] ]
    empty = unique_count("");                    // Returns: [[],[]]

<br clear="all" /><br/>

---

### Function: unique\_approx()

**Synopsis:** Returns a subset whose retained items are pairwise separated by a tolerance.

**Topics:** [List Handling](Topics#list-handling), [Comparisons](Topics#comparisons)

**See Also:** [unique\_approx\_indexed()](#function-unique_approx_indexed), [unique()](#function-unique), [deduplicate()](#function-deduplicate)

**Usage:** 

- ulist = unique_approx(data, [eps]);

**Description:** 

Returns a subset whose retained items are pairwise farther apart than `eps`.
For a vector of numbers, distance is the absolute difference and the result is sorted.
For a list of points, distance is Euclidean and retained points remain in input order.
This does not guarantee a minimal set of qualifying items:
an item can be discarded because it is close to another item that is also discarded.
This is a separated subset, not a clustering operation or a guarantee of representative coverage.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`data`               | A vector of numbers or a list of points of the same dimension.
`eps`                | Nonnegative minimum separation between retained items. Default: 1e-9

**Example 1:** 

    include <BOSL2/std.scad>
    unique_approx([0,0.9,1.8],eps=1);          // Returns: [0]
    unique_approx([[0,0],[0.9,0],[1.8,0]],eps=1); // Returns: [[0,0]]

<br clear="all" /><br/>

---

### Function: unique\_approx\_indexed()

**Synopsis:** Returns indices of a subset whose retained items are separated by more than a tolerance.

**Topics:** [List Handling](Topics#list-handling), [Comparisons](Topics#comparisons)

**See Also:** [unique\_approx()](#function-unique_approx), [unique()](#function-unique), [deduplicate\_indexed()](#function-deduplicate_indexed)

**Usage:** 

- indices = unique_approx_indexed(data, [eps]);

**Description:** 

Returns indices of a subset whose retained items are pairwise farther apart than `eps`.
For a vector of numbers, distance is the absolute difference and indices are in value-sorted order.
For a list of points, distance is Euclidean and returned indices are in input order.
As with [`unique_approx()`](#function-unique_approx), a discarded item need not be within `eps` of any retained item:
it can be discarded because it is close to another item that is also discarded.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`data`               | A vector of numbers or a list of points of the same dimension.
`eps`                | Nonnegative minimum separation between retained items. Default: 1e-9

**Example 1:** 

    include <BOSL2/std.scad>
    unique_approx_indexed([0,0.9,1.8],eps=1); // Returns: [0]

<br clear="all" /><br/>

---

## Section: Sorting


### Function: sort()

**Synopsis:** Returns a sorted list.

**Topics:** [List Handling](Topics#list-handling)

**See Also:** [shuffle()](lists.scad#function-shuffle), [sortidx()](#function-sortidx), [unique()](#function-unique), [unique\_count()](#function-unique_count), [group\_sort()](#function-group_sort)

**Usage:** 

- slist = sort(list, [idx]);

**Description:** 

Sorts the given list in lexicographic order. The sort is stable, meaning equivalent items do not change order.
If the input is a homogeneous simple list or a homogeneous
list of vectors (see function is_homogeneous), the sorting method uses the native comparison operator and is faster.
When sorting non-homogeneous list the elements are compared with `compare_vals`, with types ordered according to
`undef < boolean < nan < number < string < list < range`.  Comparison of lists is recursive.
When comparing vectors, homogeneous or not, the parameter `idx` may be used to select the components to compare.
Note that homogeneous lists of vectors may contain mixed types provided that for any two list elements
list[i] and list[j] satisfies  type(list[i][k])==type(list[j][k]) for all k.
Strings are allowed as any list element and are compared with the native operators although no substring
comparison is possible.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`list`               | The list to sort.
`idx`                | If given, do the comparison based just on the specified index, range or list of indices.

**Example 1:** 

    include <BOSL2/std.scad>
    // Homogeneous lists
    l1 = [45,2,16,37,8,3,9,23,89,12,34];
    sorted1 = sort(l1);  // Returns [2,3,8,9,12,16,23,34,37,45,89]
    l2 = [["oat",0], ["cat",1], ["bat",3], ["bat",2], ["fat",3]];
    sorted2 = sort(l2); // Returns: [["bat",2],["bat",3],["cat",1],["fat",3],["oat",0]]
    // Non-homegenous list
    l3 = [[4,0],[7],[3,9],20,[4],[3,1],[8]];
    sorted3 = sort(l3); // Returns: [20,[3,1],[3,9],[4],[4,0],[7],[8]]

<br clear="all" /><br/>

---

### Function: sortidx()

**Synopsis:** Returns a list of sorted indices into a list.

**Topics:** [List Handling](Topics#list-handling)

**See Also:** [shuffle()](lists.scad#function-shuffle), [sort()](#function-sort), [group\_sort()](#function-group_sort), [unique()](#function-unique), [unique\_count()](#function-unique_count)

**Usage:** 

- idxlist = sortidx(list, [idx]);

**Description:** 

Given a list, sort it as function `sort()`, and returns
a list of indexes into the original list in that sorted order.
The sort is stable, so equivalent items do not change order.
If you iterate the returned list in order, and use the list items
to index into the original list, then you are accessing the original
values in sorted order.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`list`               | The list to sort.
`idx`                | If given, do the comparison based just on the specified index, range or list of indices.

**Example 1:** 

    include <BOSL2/std.scad>
    lst = ["d","b","e","c"];
    idxs = sortidx(lst);  // Returns: [1,3,0,2]
    ordered = select(lst, idxs);   // Returns: ["b", "c", "d", "e"]

<br clear="all" /><br/>

**Example 2:** 

    include <BOSL2/std.scad>
    lst = [
        ["foo", 88, [0,0,1], false],
        ["bar", 90, [0,1,0], true],
        ["baz", 89, [1,0,0], false],
        ["qux", 23, [1,1,1], true]
    ];
    idxs1 = sortidx(lst, idx=1); // Returns: [3,0,2,1]
    idxs2 = sortidx(lst, idx=0); // Returns: [1,2,0,3]
    idxs3 = sortidx(lst, idx=[1,3]); // Returns: [3,0,2,1]

<br clear="all" /><br/>

---

### Function: group\_sort()

**Synopsis:** Returns a sorted list of groups of values.

**Topics:** [List Handling](Topics#list-handling)

**See Also:** [group\_data()](#function-group_data), [shuffle()](lists.scad#function-shuffle), [sort()](#function-sort), [sortidx()](#function-sortidx), [unique()](#function-unique), [unique\_count()](#function-unique_count)

**Usage:** 

- ulist = group_sort(list,[idx]);

**Description:** 

Given a list of numbers, sorts the list into a sequence of lists, where each list contains any repeated values.
If there are no repeated values, the output is a list of singleton lists. Empty input returns `[]`.
If you apply [`flatten()`](lists.scad#function-flatten) to the output, the result is a simple sorted list.

When the input is a list of lists, the sorting is done based on index `idx` of the entries in `list`.
In this case, `list[i][idx]` must be a number for every `i`, and the entries in `list` are grouped
together in the output if they match at index `idx`.  This function can be used to group together
items that are tagged with the same index.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`list`               | The list to sort.
`idx`                | If input is a list of lists, index to sort on.  Default: 0.

**Example 1:** 

    include <BOSL2/std.scad>
    sorted = group_sort([5,2,8,3,1,3,8,7,5]);  // Returns: [[1],[2],[3,3],[5,5],[7],[8,8]]
    // Next example returns: [ [[2,"b"],[2,"e"]], [[3,"d"]], [[5,"a"],[5,"c"]] ]
    sorted2 = group_sort([[5,"a"],[2,"b"], [5,"c"], [3,"d"], [2,"e"] ], idx=0);

<br clear="all" /><br/>

---

### Function: group\_data()

**Synopsis:** Groups list data by integer group numbers.

**Topics:** [List Handling](Topics#list-handling)

**See Also:** [group\_sort()](#function-group_sort), [shuffle()](lists.scad#function-shuffle), [sort()](#function-sort), [sortidx()](#function-sortidx), [unique()](#function-unique), [unique\_count()](#function-unique_count)

**Usage:** 

- groupings = group_data(groups, values);

**Description:** 

Given a list of integer group numbers, and an equal-length list of values,
returns a list of groups with the values sorted into the corresponding groups.
For example: if you have a groups index list of `[2,3,2]` and values of `["A","B","C"]`, then
the values `"A"` and `"C"` are put in group 2, and `"B"` is in group 3.
Groups that have no values grouped into them are empty lists. Therefore, the
above would return `[[], [], ["A","C"], ["B"]]`

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`groups`             | A list of integer group index numbers.
`values`             | A list of values to sort into groups.

**Example 1:** 

    include <BOSL2/std.scad>
    groups = group_data([1,2,0], ["A","B","C"]);  // Returns [["C"],["A"],["B"]]

<br clear="all" /><br/>

**Example 2:** 

    include <BOSL2/std.scad>
    groups = group_data([1,3,1], ["A","B","C"]);  // Returns [[],["A","C"],[],["B"]]

<br clear="all" /><br/>

---

### Function: list\_smallest()

**Synopsis:** Returns the `k` smallest values in the list, in arbitrary order.

**Topics:** [List Handling](Topics#list-handling)

**See Also:** [group\_sort()](#function-group_sort), [shuffle()](lists.scad#function-shuffle), [sort()](#function-sort), [sortidx()](#function-sortidx), [unique()](#function-unique), [unique\_count()](#function-unique_count)

**Usage:** 

- small = list_smallest(list, k)

**Description:** 

Returns a set of the k smallest items in list in arbitrary order.  The items must be
mutually comparable with native OpenSCAD comparison operations.
You get "undefined operation" errors if you provide invalid input.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`list`               | list to process
`k`                  | number of items to return

---

### Function: list\_largest()

**Synopsis:** Returns the `k` largest values in the list, in arbitrary order.

**Topics:** [List Handling](Topics#list-handling)

**See Also:** [group\_sort()](#function-group_sort), [shuffle()](lists.scad#function-shuffle), [sort()](#function-sort), [sortidx()](#function-sortidx), [unique()](#function-unique), [unique\_count()](#function-unique_count), [list\_smallest()](#function-list_smallest)

**Usage:** 

- big = list_largest(list, k)

**Description:** 

Returns a set of the k largest items in list in arbitrary order.  The items must be
mutually comparable with native OpenSCAD comparison operations.
You get "undefined operation" errors if you provide invalid input.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`list`               | list to process
`k`                  | number of items to return

---


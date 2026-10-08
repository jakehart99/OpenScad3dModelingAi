# LibFile: version.scad

File that provides functions to manage versioning.

To use, add the following lines to the beginning of your file:

    include <BOSL2/std.scad>

## File Contents

1. [Section: BOSL Library Version Functions](#section-bosl-library-version-functions)
    - [`bosl_version()`](#function-bosl_version) – Returns the BOSL2 version as a list.
    - [`bosl_version_num()`](#function-bosl_version_num) – Returns the BOSL2 version as a float.
    - [`bosl_version_str()`](#function-bosl_version_str) – Returns the BOSL2 version as a string.
    - [`bosl_required()`](#module-bosl_required) – Asserts that the current version of the library is at least the given version.

2. [Section: Generic Version Functions](#section-generic-version-functions)
    - [`version_to_list()`](#function-version_to_list) – Splits a version into a list of integer version parts.
    - [`version_to_str()`](#function-version_to_str) – Coerces a version into a standard version string.
    - [`version_to_num()`](#function-version_to_num) – Coerces a version into a standard version float.
    - [`version_cmp()`](#function-version_cmp) – Compares two versions.
    - [`supports()`](#function-supports) – Checks if a language extension feature is supported.
    - [`assert_supported()`](#function-assert_supported) – Asserts that a language extension feature is supported.


## Section: BOSL Library Version Functions


### Function: bosl\_version()

**Synopsis:** Returns the BOSL2 version as a list.

**Topics:** [Versioning](Topics#versioning)

**See Also:** [bosl\_version\_num()](#function-bosl_version_num), [bosl\_version\_str()](#function-bosl_version_str), [bosl\_required()](#module-bosl_required)

**Usage:** 

- ver = bosl_version();

**Description:** 

Returns a list with three integer elements, [MAJOR,MINOR,REV],
representing the Major, Minor, and Build Revision numbers.
For example, version 2.1.43 will be returned as `[2,1,43]`.

---

### Function: bosl\_version\_num()

**Synopsis:** Returns the BOSL2 version as a float.

**Topics:** [Versioning](Topics#versioning)

**See Also:** [bosl\_version()](#function-bosl_version), [bosl\_version\_str()](#function-bosl_version_str), [bosl\_required()](#module-bosl_required)

**Usage:** 

- ver = bosl_version_num();

**Description:** 

Returns a floating point number of the version, formatted like M.mmrrrr where M is the major version number,
each m is a zero-padded digit of the minor version number, and each r is a zero-padded digit of the build
revision number.  For example, version 2.1.43 will be returned as `2.010043`.

---

### Function: bosl\_version\_str()

**Synopsis:** Returns the BOSL2 version as a string.

**Topics:** [Versioning](Topics#versioning)

**See Also:** [bosl\_version()](#function-bosl_version), [bosl\_version\_num()](#function-bosl_version_num), [bosl\_required()](#module-bosl_required)

**Usage:** 

- ver = bosl_version_str();

**Description:** 

Returns a string of the version, formatted like "MAJOR.MINOR.REV".
For example, version 2.1.43 will be returned as `"2.1.43"`.

---

### Module: bosl\_required()

**Synopsis:** Asserts that the current version of the library is at least the given version.

**Topics:** [Versioning](Topics#versioning)

**See Also:** [version\_to\_num()](#function-version_to_num), [version\_to\_str()](#function-version_to_str), [version\_to\_list()](#function-version_to_list), [version\_cmp()](#function-version_cmp)

**Usage:** 

- bosl_required(version);

**Description:** 

Given a version as a list, number, or string, asserts that the currently installed BOSL library is at least the given version.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`version`            | version required

---

## Section: Generic Version Functions


### Function: version\_to\_list()

**Synopsis:** Splits a version into a list of integer version parts.

**Topics:** [Versioning](Topics#versioning)

**See Also:** [version\_to\_num()](#function-version_to_num), [version\_to\_str()](#function-version_to_str), [version\_cmp()](#function-version_cmp), [bosl\_required()](#module-bosl_required)

**Usage:** 

- ver = version_to_list(x);

**Description:** 

Given a version string, number, or list, returns the list of version integers [MAJOR,MINOR,REVISION].

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`x`                  | version to convert

**Example 1:** 

    include <BOSL2/std.scad>
    v1 = version_to_list("2.1.43");  // Returns: [2,1,43]
    v2 = version_to_list(2.120234);  // Returns: [2,12,234]
    v3 = version_to_list([2,3,4]);   // Returns: [2,3,4]
    v4 = version_to_list([2,3,4,5]); // Returns: [2,3,4]

<br clear="all" /><br/>

---

### Function: version\_to\_str()

**Synopsis:** Coerces a version into a standard version string.

**Topics:** [Versioning](Topics#versioning)

**See Also:** [version\_to\_num()](#function-version_to_num), [version\_to\_list()](#function-version_to_list), [version\_cmp()](#function-version_cmp), [bosl\_required()](#module-bosl_required)

**Usage:** 

- str = version_to_str(version);

**Description:** 

Takes a version string, number, or list, and returns the properly formatter version string for it.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`version`            | version to convert

**Example 1:** 

    include <BOSL2/std.scad>
    v1 = version_to_str([2,1,43]);  // Returns: "2.1.43"
    v2 = version_to_str(2.010043);  // Returns: "2.1.43"
    v3 = version_to_str(2.340789);  // Returns: "2.34.789"
    v4 = version_to_str("2.3.89");  // Returns: "2.3.89"

<br clear="all" /><br/>

---

### Function: version\_to\_num()

**Synopsis:** Coerces a version into a standard version float.

**Topics:** [Versioning](Topics#versioning)

**See Also:** [version\_cmp()](#function-version_cmp), [version\_to\_str()](#function-version_to_str), [version\_to\_list()](#function-version_to_list), [bosl\_required()](#module-bosl_required)

**Usage:** 

- str = version_to_num(version);

**Description:** 

Takes a version string, number, or list, and returns the properly formatter version number for it.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`version`            | version to convert

**Example 1:** 

    include <BOSL2/std.scad>
    v1 = version_to_num([2,1,43]);   // Returns: 2.010043
    v2 = version_to_num([2,34,567]); // Returns: 2.340567
    v3 = version_to_num(2.120567);   // Returns: 2.120567
    v4 = version_to_num("2.6.79");   // Returns: 2.060079

<br clear="all" /><br/>

---

### Function: version\_cmp()

**Synopsis:** Compares two versions.

**Topics:** [Versioning](Topics#versioning)

**See Also:** [version\_to\_num()](#function-version_to_num), [version\_to\_str()](#function-version_to_str), [version\_to\_list()](#function-version_to_list), [bosl\_required()](#module-bosl_required)

**Usage:** 

- cmp = version_cmp(a,b);

**Description:** 

Given a pair of versions, in any combination of string, integer, or list, compares them, and returns the relative value of them.
Returns an integer <0 if a<b.  Returns 0 if a==b.  Returns an integer >0 if a>b.

**Example 1:** 

    include <BOSL2/std.scad>
    cmp1 = version_cmp(2.010034, "2.1.33");  // Returns: >0
    cmp2 = version_cmp(2.010034, "2.1.34");  // Returns: 0
    cmp3 = version_cmp(2.010034, "2.1.35");  // Returns: <0

<br clear="all" /><br/>

---

### Function: supports()

**Synopsis:** Checks if a language extension feature is supported.

**Topics:** [versioning](Topics#versioning)

**See Also:** [version\_to\_num()](#function-version_to_num), [version\_to\_str()](#function-version_to_str), [version\_to\_list()](#function-version_to_list), [version\_cmp()](#function-version_cmp), [bosl\_required()](#module-bosl_required)

**Usage:** 

- is_supported = supports(feature, [minlev]);

**Description:** 

Checks if a feature is supported by the running OpenSCAD interpreter, at a given level.
Returns true if the feature is supported at the given level, false otherwise.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`feature`            | name of the feature to check
`minlev`             | minimum level of support required (default: 1)

**Example 1:** 

    include <BOSL2/std.scad>
    assert(supports("simplify-op"), "simplify() not supported in this OpenSCAD interpreter");

<br clear="all" /><br/>

---

### Function: assert\_supported()

**Synopsis:** Asserts that a language extension feature is supported.

**Topics:** [Versioning](Topics#versioning)

**See Also:** [version\_to\_num()](#function-version_to_num), [version\_to\_str()](#function-version_to_str), [version\_to\_list()](#function-version_to_list), [version\_cmp()](#function-version_cmp), [bosl\_required()](#module-bosl_required)

**Usage:** 

- assert_supported(feature, [minlev]);

**Description:** 

Asserts that a feature is supported by the running OpenSCAD interpreter, at a
given level.  If the feature is not supported, an error is raised.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`feature`            | name of the feature to check

---


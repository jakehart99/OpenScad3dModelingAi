# LibFile: structs.scad

This file provides manipulation of "structs".  A "struct" is a data structure that
associates arbitrary keys with values and allows you to get and set values
by key.

To use, add the following lines to the beginning of your file:

    include <BOSL2/std.scad>

## File Contents

1. [Section: struct operations](#section-struct-operations)
    - [`struct_set()`](#function-struct_set) – Sets one or more key-value pairs in a struct.
    - [`struct_remove()`](#function-struct_remove) – Removes one or more keys from a struct.
    - [`struct_val()`](#function-struct_val) – Returns the value for an key in a struct.
    - [`struct_keys()`](#function-struct_keys) – Returns a list of keys for a struct.
    - [`echo_struct()`](#functionmodule-echo_struct) – Echoes the struct to the console in a formatted manner.
    - [`is_struct()`](#function-is_struct) – Returns true if the value is a struct.


## Section: struct operations


### Function: struct\_set()

**Synopsis:** Sets one or more key-value pairs in a struct.

**Topics:** [Data Structures](Topics#data-structures), [Dictionaries](Topics#dictionaries)

**See Also:** [struct\_remove()](#function-struct_remove), [struct\_val()](#function-struct_val), [struct\_keys()](#function-struct_keys), [echo\_struct()](#functionmodule-echo_struct), [is\_struct()](#function-is_struct)

**Usage:** 

- struct2 = struct_set(struct, key, value, [grow=]);
- struct2 = struct_set(struct, [key1, value1, key2, value2, ...], [grow=]);

**Description:** 

Sets the key(s) in the structure to the specified value(s), returning a new updated structure.  If a
key exists its value is changed, otherwise the key is added to the structure.  If `grow=false` then
it is an error to set a key not already defined in the structure.  If you specify the same key twice
that is also an error.  Note that key order will change when you change a key's value.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`struct`             | input structure.
`key`                | Key to set, or a flat alternating list `[key1,value1,key2,value2,...]`.
`value`              | Value to store when giving a single key and value.

<abbr title="These args must be used by name, ie: name=value">By&nbsp;Name</abbr> | What it does
-------------------- | ------------
`grow`               | Set to true to allow structure to grow, or false for new keys to generate an error.  Default: true

**Example 1:** Create a struct containing just one key-value pair

    include <BOSL2/std.scad>
    some_struct = struct_set([], "answer", 42);
    // 'some_struct' now contains a single value, 42, under one key, "answer".

<br clear="all" /><br/>

**Example 2:** Create a struct containing more than one key-value pair. Note that keys and values need not be the same type.

    include <BOSL2/std.scad>
    some_struct = struct_set([], ["answer", 42, 2, "two", "quote", "What a nice day"]);
    // 'some struct' now contains these key-value pairs:
    // answer: 42
    // 2: two
    // quote: What a nice day

<br clear="all" /><br/>

---

### Function: struct\_remove()

**Synopsis:** Removes one or more keys from a struct.

**Topics:** [Data Structures](Topics#data-structures), [Dictionaries](Topics#dictionaries)

**See Also:** [struct\_set()](#function-struct_set), [struct\_val()](#function-struct_val), [struct\_keys()](#function-struct_keys), [echo\_struct()](#functionmodule-echo_struct), [is\_struct()](#function-is_struct)

**Usage:** 

- struct2 = struct_remove(struct, key);

**Description:** 

Remove key or list of keys from a structure.  If you want to remove a single key which is a list
you must pass it as a singleton list, or struct_remove will attempt to remove the listed items as keys.
If you list the same item multiple times for removal it will be removed without error.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`struct`             | input structure
`key`                | a single key or list of keys to remove.

---

### Function: struct\_val()

**Synopsis:** Returns the value for an key in a struct.

**Topics:** [Data Structures](Topics#data-structures), [Dictionaries](Topics#dictionaries)

**See Also:** [struct\_set()](#function-struct_set), [struct\_remove()](#function-struct_remove), [struct\_keys()](#function-struct_keys), [echo\_struct()](#functionmodule-echo_struct), [is\_struct()](#function-is_struct)

**Usage:** 

- val = struct_val(struct, key, [default]);

**Description:** 

Returns the value for the specified key in the structure, or default value if the key is not present

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`struct`             | input structure
`key`                | key whose value to return
`default`            | default value to return if key is not present.  Default: undef

---

### Function: struct\_keys()

**Synopsis:** Returns a list of keys for a struct.

**Topics:** [Data Structures](Topics#data-structures), [Dictionaries](Topics#dictionaries)

**See Also:** [struct\_set()](#function-struct_set), [struct\_remove()](#function-struct_remove), [struct\_val()](#function-struct_val), [echo\_struct()](#functionmodule-echo_struct), [is\_struct()](#function-is_struct)

**Usage:** 

- keys = struct_keys(struct);

**Description:** 

Returns a list of the keys in a structure

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`struct`             | input structure

---

### Function/Module: echo\_struct()

**Synopsis:** Echoes the struct to the console in a formatted manner.

**Topics:** [Data Structures](Topics#data-structures), [Dictionaries](Topics#dictionaries)

**See Also:** [struct\_set()](#function-struct_set), [struct\_remove()](#function-struct_remove), [struct\_val()](#function-struct_val), [struct\_keys()](#function-struct_keys), [is\_struct()](#function-is_struct)

**Usage:** 

- echo_struct(struct, [name]);
- foo = echo_struct(struct, [name]);

**Description:** 

Displays a list of structure keys and values, one pair per line, for easier reading.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`struct`             | input structure
`name`               | optional structure name to list at the top of the output.  Default: ""

---

### Function: is\_struct()

**Synopsis:** Returns true if the value is a struct.

**Topics:** [Data Structures](Topics#data-structures), [Dictionaries](Topics#dictionaries)

**See Also:** [struct\_set()](#function-struct_set), [struct\_remove()](#function-struct_remove), [struct\_val()](#function-struct_val), [struct\_keys()](#function-struct_keys), [echo\_struct()](#functionmodule-echo_struct)

**Usage:** 

- bool = is_struct(struct);

**Description:** 

Returns true if the input is a list of pairs, false otherwise.

---


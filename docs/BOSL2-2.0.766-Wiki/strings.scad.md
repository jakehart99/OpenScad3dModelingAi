# LibFile: strings.scad

String manipulation and formatting functions.

To use, add the following lines to the beginning of your file:

    include <BOSL2/std.scad>

## File Contents

1. [Section: Extracting substrings](#section-extracting-substrings)
    - [`substr()`](#function-substr) – Returns a substring from a string.
    - [`suffix()`](#function-suffix) – Returns the last few characters of a string.

2. [Section: String Searching](#section-string-searching)
    - [`str_find()`](#function-str_find) – Finds a substring in a string.
    - [`substr_match()`](#function-substr_match) – Returns true if the string `pattern` matches the string `str`.
    - [`starts_with()`](#function-starts_with) – Returns true if the string starts with a given substring.
    - [`ends_with()`](#function-ends_with) – Returns true if the string ends with a given substring.
    - [`str_split()`](#function-str_split) – Splits a longer string wherever a given substring occurs.

3. [Section: String modification](#section-string-modification)
    - [`str_join()`](#function-str_join) – Joints a list of strings into a single string.
    - [`str_strip()`](#function-str_strip) – Strips given leading and trailing characters from a string.
    - [`str_pad()`](#function-str_pad) – Pads a string to a given length.
    - [`str_replace()`](#function-str_replace) – Replace all occurrences of the specified substring in a string with another string.
    - [`str_replace_char()`](#function-str_replace_char) – Replace specified character in a string with a string.
    - [`str_collapse_char()`](#function-str_collapse_char) – Collapse a specific repeating character in a string.
    - [`downcase()`](#function-downcase) – Lowercases all characters in a string.
    - [`upcase()`](#function-upcase) – Uppercases all characters in a string.

4. [Section: Random strings](#section-random-strings)
    - [`rand_str()`](#function-rand_str) – Create a randomized string.

5. [Section: Parsing strings into numbers](#section-parsing-strings-into-numbers)
    - [`parse_int()`](#function-parse_int) – Parse an integer from a string.
    - [`parse_float()`](#function-parse_float) – Parse a float from a string.
    - [`parse_frac()`](#function-parse_frac) – Parse a float from a fraction string.
    - [`parse_num()`](#function-parse_num) – Parse a float from a decimal or fraction string.

6. [Section: Formatting numbers into strings](#section-formatting-numbers-into-strings)
    - [`format_int()`](#function-format_int) – Formats an integer into a string, with possible leading zeros.
    - [`format_fixed()`](#function-format_fixed) – Formats a float into a string with a fixed number of decimal places.
    - [`format_float()`](#function-format_float) – Formats a float into a string with a given number of significant digits.
    - [`format()`](#function-format) – Formats multiple values into a string with a given format.

7. [Section: Checking character class](#section-checking-character-class)
    - [`is_lower()`](#function-is_lower) – Returns true if all characters in the string are lowercase.
    - [`is_upper()`](#function-is_upper) – Returns true if all characters in the string are uppercase.
    - [`is_digit()`](#function-is_digit) – Returns true if all characters in the string are decimal digits.
    - [`is_hexdigit()`](#function-is_hexdigit) – Returns true if all characters in the string are hexidecimal digits.
    - [`is_letter()`](#function-is_letter) – Returns true if all characters in the string are letters.


## Section: Extracting substrings


### Function: substr()

**Synopsis:** Returns a substring from a string.

**Topics:** [Strings](Topics#strings)

**See Also:** [suffix()](#function-suffix), [str\_find()](#function-str_find), [substr\_match()](#function-substr_match), [starts\_with()](#function-starts_with), [ends\_with()](#function-ends_with), [str\_split()](#function-str_split), [str\_join()](#function-str_join), [str\_strip()](#function-str_strip)

**Usage:** 

- newstr = substr(str, [pos], [len]);

**Description:** 

Returns a substring from a string start at position `pos` with length `len`, or
if `len` isn't given, the rest of the string.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`str`                | string to operate on
`pos`                | starting index of substring, or vector of first and last position.  Default: 0
`len`                | length of substring, or omit it to get the rest of the string.  If len is zero or less then the emptry string is returned.

**Example 1:** 

    include <BOSL2/std.scad>
    s1=substr("abcdefg",3,3);     // Returns "def"
    s2=substr("abcdefg",2);       // Returns "cdefg"
    s3=substr("abcdefg",len=3);   // Returns "abc"
    s4=substr("abcdefg",[2,4]);   // Returns "cde"
    s5=substr("abcdefg",len=-2);  // Returns ""

<br clear="all" /><br/>

---

### Function: suffix()

**Synopsis:** Returns the last few characters of a string.

**Topics:** [Strings](Topics#strings)

**See Also:** [str\_find()](#function-str_find), [substr\_match()](#function-substr_match), [starts\_with()](#function-starts_with), [ends\_with()](#function-ends_with), [str\_split()](#function-str_split), [str\_join()](#function-str_join), [str\_strip()](#function-str_strip)

**Usage:** 

- newstr = suffix(str,len);

**Description:** 

Returns the last `len` characters from the input string `str`.
If `len` is longer than the length of `str`, then the entirety of `str` is returned.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`str`                | The string to get the suffix of.
`len`                | The number of characters of suffix to get.

---

## Section: String Searching


### Function: str\_find()

**Synopsis:** Finds a substring in a string.

**Topics:** [Strings](Topics#strings)

**See Also:** [suffix()](#function-suffix), [substr\_match()](#function-substr_match), [starts\_with()](#function-starts_with), [ends\_with()](#function-ends_with), [str\_split()](#function-str_split), [str\_join()](#function-str_join), [str\_strip()](#function-str_strip)

**Usage:** 

- ind = str_find(str,pattern,[last=],[all=],[start=]);

**Description:** 

Searches input string `str` for the string `pattern` and returns the index or indices of the matches in `str`.
By default `str_find()` returns the index of the first match in `str`.  If `last` is true then it returns the index of the last match.
If the pattern is the empty string the first match is at zero and the last match is the last character of the `str`.
If `start` is set then the search begins at index start, working either forward and backward from that position.  If you set `start`
and `last` is true then the search finds the pattern if it begins at index `start`. If no match exists, returns `undef`.
If you set `all` to true then `str_find()` returns all of the matches as a list, or an empty list if there are no matches.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`str`                | String to search.
`pattern`            | string pattern to search for

<abbr title="These args must be used by name, ie: name=value">By&nbsp;Name</abbr> | What it does
-------------------- | ------------
`last`               | set to true to return the last match. Default: false
`all`                | set to true to return all matches as a list.  Overrides last.  Default: false
`start`              | index where the search starts

**Example 1:** 

    include <BOSL2/std.scad>
    a=str_find("abc123def123abc","123");   // Returns 3
    b=str_find("abc123def123abc","b");     // Returns 1
    c=str_find("abc123def123abc","1234");  // Returns undef
    d=str_find("abc","");                  // Returns 0
    e=str_find("abc123def123", "123", start=4);     // Returns 9
    f=str_find("abc123def123abc","123",last=true);  // Returns 9
    g=str_find("abc123def123abc","b",last=true);    // Returns 13
    h=str_find("abc123def123abc","1234",last=true); // Returns undef
    i=str_find("abc","",last=true);                 // Returns 3
    j=str_find("abc123def123", "123", start=8, last=true);  // Returns 3
    k=str_find("abc123def123abc","123",all=true);   // Returns [3,9]
    l=str_find("abc123def123abc","b",all=true);     // Returns [1,13]
    m=str_find("abc123def123abc","1234",all=true);  // Returns []
    n=str_find("abc","",all=true);                  // Returns [0,1,2]
    o=str_find("abd{{bz}}fij", "{{b}}", all=true);  // returns []

<br clear="all" /><br/>

---

### Function: substr\_match()

**Synopsis:** Returns true if the string `pattern` matches the string `str`.

**Topics:** [Strings](Topics#strings)

**See Also:** [suffix()](#function-suffix), [str\_find()](#function-str_find), [starts\_with()](#function-starts_with), [ends\_with()](#function-ends_with), [str\_split()](#function-str_split), [str\_join()](#function-str_join), [str\_strip()](#function-str_strip)

**Description:** 

Returns true if the string `pattern` matches the string `str` starting
at `str[start]`.  If the string is too short for the pattern, or
`start` is out of bounds – either negative or beyond the end of the
string – then substr_match returns false.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`str`                | String to search
`start`              | Starting index for search in str
`pattern`            | String pattern to search for

**Example 1:** 

    include <BOSL2/std.scad>
    a=substr_match("abcde",2,"cd");   // Returns true
    b=substr_match("abcde",2,"cx");   // Returns false
    c=substr_match("abcde",2,"cdef"); // Returns false
    d=substr_match("abcde",-2,"cd");  // Returns false
    e=substr_match("abcde",19,"cd");  // Returns false
    f=substr_match("abc",1,"");       // Returns true

<br clear="all" /><br/>

---

### Function: starts\_with()

**Synopsis:** Returns true if the string starts with a given substring.

**Topics:** [Strings](Topics#strings)

**See Also:** [suffix()](#function-suffix), [str\_find()](#function-str_find), [substr\_match()](#function-substr_match), [ends\_with()](#function-ends_with), [str\_split()](#function-str_split), [str\_join()](#function-str_join), [str\_strip()](#function-str_strip)

**Usage:** 

- bool = starts_with(str,pattern);

**Description:** 

Returns true if the input string (or list) `str` starts with the specified string (or list) pattern, `pattern`.
Otherwise returns false.  (If `str` is not a string or list then always returns false.)

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`str`                | String to search.
`pattern`            | String pattern to search for.

**Example 1:** 

    include <BOSL2/std.scad>
    b1=starts_with("abcdef","abc");  // Returns true
    b2=starts_with("abcdef","def");  // Returns false
    b3=starts_with("abcdef","");     // Returns true

<br clear="all" /><br/>

---

### Function: ends\_with()

**Synopsis:** Returns true if the string ends with a given substring.

**Topics:** [Strings](Topics#strings)

**See Also:** [suffix()](#function-suffix), [str\_find()](#function-str_find), [substr\_match()](#function-substr_match), [starts\_with()](#function-starts_with), [str\_split()](#function-str_split), [str\_join()](#function-str_join), [str\_strip()](#function-str_strip)

**Usage:** 

- bool = ends_with(str,pattern);

**Description:** 

Returns true if the input string (or list) `str` ends with the specified string (or list) pattern, `pattern`.
Otherwise returns false.  (If `str` is not a string or list then always returns false.)

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`str`                | String to search.
`pattern`            | String pattern to search for.

**Example 1:** 

    include <BOSL2/std.scad>
    b1=ends_with("abcdef","def");  // Returns true
    b2=ends_with("abcdef","de");   // Returns false
    b3=ends_with("abcdef","");     // Returns true

<br clear="all" /><br/>

---

### Function: str\_split()

**Synopsis:** Splits a longer string wherever a given substring occurs.

**Topics:** [Strings](Topics#strings)

**See Also:** [suffix()](#function-suffix), [str\_find()](#function-str_find), [substr\_match()](#function-substr_match), [starts\_with()](#function-starts_with), [ends\_with()](#function-ends_with), [str\_join()](#function-str_join), [str\_strip()](#function-str_strip)

**Usage:** 

- string_list = str_split(str, sep, [keep_nulls]);

**Description:** 

Breaks an input string into substrings using a separator or list of separators.  If keep_nulls is true
then two sequential separator characters produce an empty string in the output list.  If keep_nulls is false
then no empty strings are included in the output list.

If sep is a single string then each character in sep is treated as a delimiting character and the input string is
split at every delimiting character.  Empty strings can occur whenever two delimiting characters are sequential.
If sep is a list of strings then the input string is split sequentially using each string from the list in order.
If keep_nulls is true then the output length is equal to `len(sep)+1`, possibly with trailing null strings
if the string runs out before the separator list.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`str`                | String to split.
`sep`                | a string or list of strings to use for the separator
`keep_nulls`         | boolean value indicating whether to keep null strings in the output list.  Default: true

**Example 1:** 

    include <BOSL2/std.scad>
    s1=str_split("abc+def-qrs*iop","*-+");     // Returns ["abc", "def", "qrs", "iop"]
    s2=str_split("abc+*def---qrs**iop+","*-+");// Returns ["abc", "", "def", "", "", "qrs", "", "iop", ""]
    s3=str_split("abc      def"," ");          // Returns ["abc", "", "", "", "", "", "def"]
    s4=str_split("abc      def"," ",keep_nulls=false); // Returns ["abc", "def"]
    s5=str_split("abc+def-qrs*iop",["+","-","*"]);     // Returns ["abc", "def", "qrs", "iop"]
    s6=str_split("abc+def-qrs*iop",["-","+","*"]);     // Returns ["abc+def", "qrs*iop", "", ""]

<br clear="all" /><br/>

---

## Section: String modification


### Function: str\_join()

**Synopsis:** Joints a list of strings into a single string.

**Topics:** [Strings](Topics#strings)

**See Also:** [suffix()](#function-suffix), [str\_find()](#function-str_find), [substr\_match()](#function-substr_match), [starts\_with()](#function-starts_with), [ends\_with()](#function-ends_with), [str\_split()](#function-str_split), [str\_strip()](#function-str_strip)

**Usage:** 

- str = str_join(list, [sep]);

**Description:** 

Returns the concatenation of a list of strings, optionally with a
separator string inserted between each string on the list.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`list`               | list of strings to concatenate
`sep`                | separator string to insert.  Default: ""

**Example 1:** 

    include <BOSL2/std.scad>
    s1=str_join(["abc","def","ghi"]);         // Returns "abcdefghi"
    s2=str_join(["abc","def","ghi"], " + ");  // Returns "abc + def + ghi"

<br clear="all" /><br/>

---

### Function: str\_strip()

**Synopsis:** Strips given leading and trailing characters from a string.

**Topics:** [Strings](Topics#strings)

**See Also:** [suffix()](#function-suffix), [str\_find()](#function-str_find), [substr\_match()](#function-substr_match), [starts\_with()](#function-starts_with), [ends\_with()](#function-ends_with), [str\_split()](#function-str_split), [str\_join()](#function-str_join)

**Usage:** 

- str = str_strip(s,c,[start],[end]);

**Description:** 

Takes a string `s` and strips off all leading and/or trailing characters that exist in string `c`.
By default strips both leading and trailing characters.  If you set start or end to true then
it strips only the leading or trailing characters respectively. If you set start
or end to false then it strips only the trailing or leading characters.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`s`                  | The string to strip leading or trailing characters from.
`c`                  | The string of characters to strip.
`start`              | if true then strip leading characters
`end`                | if true then strip trailing characters

**Example 1:** 

    include <BOSL2/std.scad>
    s1=str_strip("--##--123--##--","#-");  // Returns: "123"
    s2=str_strip("--##--123--##--","-");   // Returns: "##--123--##"
    s3=str_strip("--##--123--##--","#");   // Returns: "--##--123--##--"
    s4=str_strip("--##--123--##--","#-",end=true);   // Returns: "--##--123"
    s5=str_strip("--##--123--##--","-",end=true);    // Returns: "--##--123--##"
    s6=str_strip("--##--123--##--","#",end=true);    // Returns: "--##--123--##--"
    s7=str_strip("--##--123--##--","#-",start=true); // Returns: "123--##--"
    s8=str_strip("--##--123--##--","-",start=true);  // Returns: "##--123--##--"
    s9=str_strip("--##--123--##--","#",start=true);  // Returns: "--##--123--##--"

<br clear="all" /><br/>

---

### Function: str\_pad()

**Synopsis:** Pads a string to a given length.

**Topics:** [Strings](Topics#strings)

**See Also:** [suffix()](#function-suffix), [str\_find()](#function-str_find), [substr\_match()](#function-substr_match), [starts\_with()](#function-starts_with), [ends\_with()](#function-ends_with), [str\_split()](#function-str_split), [str\_join()](#function-str_join), [str\_strip()](#function-str_strip)

**Usage:** 

- padded = str_pad(str, length, char, [left]);

**Description:** 

Pad the given string `str` with to length `length` with the specified character,
which must be a length 1 string.  If left is true then pad on the left, otherwise
pad on the right.  If the string is longer than the specified length the full string
is returned unchanged.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`str`                | string to pad
`length`             | length to pad to
`char`               | character to pad with.  Default: " " (space)
`left`               | if true, pad on the left side.  Default: false

**Example 1:** 

    include <BOSL2/std.scad>
    s1=str_pad("hello", 10, "*");            // Returns: "hello*****"
    s2=str_pad("hello", 10, "*", left=true); // Returns: "*****hello"

<br clear="all" /><br/>

---

### Function: str\_replace()

**Synopsis:** Replace all occurrences of the specified substring in a string with another string.

**Topics:** [Strings](Topics#strings)

**See Also:** [str\_find()](#function-str_find), [substr\_match()](#function-substr_match), [str\_replace\_char()](#function-str_replace_char)

**Usage:** 

- newstr = str_replace(str, search, replace);

**Description:** 

Replace every occurence of `search` in the input string
with the string `replace`, which can be any string.


**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`str`                | string to process
`search`             | single character string to search for
`replace`            | string that replaces all copies of `search`

**Example 1:** 

    include <BOSL2/std.scad>
    s1 = str_replace_char("abcdefgabcdefg","bc","XYZ");     // Returns: "aXYZdefgaXYZdefg"

<br clear="all" /><br/>

---

### Function: str\_replace\_char()

**Synopsis:** Replace specified character in a string with a string.

**Topics:** [Strings](Topics#strings)

**See Also:** [suffix()](#function-suffix), [str\_find()](#function-str_find), [substr\_match()](#function-substr_match), [starts\_with()](#function-starts_with), [ends\_with()](#function-ends_with), [str\_split()](#function-str_split), [str\_join()](#function-str_join), [str\_strip()](#function-str_strip)

**Usage:** 

- newstr = str_replace_char(str, char, replace);

**Description:** 

Replace every occurence of `char` (a single character string) in the input string
with the string `replace`, which can be any string.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`str`                | string to process
`char`               | single character string to search for
`replace`            | string that replaces all copies of `char`

**Example 1:** 

    include <BOSL2/std.scad>
    s1 = str_replace_char("abcdcba","c","_123_");     // Returns: "ab_123_d_123_ba"
    s2 = str_replace_char(" s t r i n g ", " ", "");  // Returns: "string"

<br clear="all" /><br/>

---

### Function: str\_collapse\_char()

**Synopsis:** Collapse a specific repeating character in a string.

**Topics:** [Strings](Topics#strings)

**See Also:** [str\_strip()](#function-str_strip)

**Usage:** 

- newstr = str_collapse_char(str, char);

**Description:** 

Collapse any repeated sequences of a specified character in the input string into a single character.
This is useful to collapse multiple sequental spaces in a string that spans multiple indented lines in your source code.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`str`                | string to process
`char`               | single character string to search for repetitions. Default: space character

**Example 1:** 

    include <BOSL2/std.scad>
    s1 = str_collapse_char("a-b--c---d----e", "-");  // Returns: "a-b-c-d-e"
    
    st = "abc
          def
          xyz";  // parsed as "abc      def      xyz"
    s2 = str_collapse_char(st);                      // Returns: "abc def xyz"

<br clear="all" /><br/>

---

### Function: downcase()

**Synopsis:** Lowercases all characters in a string.

**Topics:** [Strings](Topics#strings)

**See Also:** [suffix()](#function-suffix), [str\_find()](#function-str_find), [substr\_match()](#function-substr_match), [starts\_with()](#function-starts_with), [ends\_with()](#function-ends_with), [str\_split()](#function-str_split), [str\_join()](#function-str_join), [str\_strip()](#function-str_strip), [upcase()](#function-upcase)

**Usage:** 

- newstr = downcase(str);

**Description:** 

Returns the string with the standard ASCII upper case letters A-Z replaced
by their lower case versions.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`str`                | String to convert.

**Example 1:** 

    include <BOSL2/std.scad>
    s=downcase("ABCdef");   // Returns "abcdef"

<br clear="all" /><br/>

---

### Function: upcase()

**Synopsis:** Uppercases all characters in a string.

**Topics:** [Strings](Topics#strings)

**See Also:** [suffix()](#function-suffix), [str\_find()](#function-str_find), [substr\_match()](#function-substr_match), [starts\_with()](#function-starts_with), [ends\_with()](#function-ends_with), [str\_split()](#function-str_split), [str\_join()](#function-str_join), [str\_strip()](#function-str_strip), [downcase()](#function-downcase)

**Usage:** 

- newstr = upcase(str);

**Description:** 

Returns the string with the standard ASCII lower case letters a-z replaced
by their upper case versions.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`str`                | String to convert.

**Example 1:** 

    include <BOSL2/std.scad>
    s=upcase("ABCdef");   // Returns "ABCDEF"

<br clear="all" /><br/>

---

## Section: Random strings


### Function: rand\_str()

**Synopsis:** Create a randomized string.

**Topics:** [Strings](Topics#strings)

**See Also:** [suffix()](#function-suffix), [str\_find()](#function-str_find), [substr\_match()](#function-substr_match), [starts\_with()](#function-starts_with), [ends\_with()](#function-ends_with), [str\_split()](#function-str_split), [str\_join()](#function-str_join), [str\_strip()](#function-str_strip), [upcase()](#function-upcase), [downcase()](#function-downcase)

**Usage:** 

- str = rand_str(n, [charset], [seed]);

**Description:** 

Produce a random string of length `n`.  If you give a string `charset` then the
characters of the random string are drawn from that list, weighted by the number
of times each character appears in the list.  If you do not give a character set
then the string is generated with characters ranging from "0" to "z" (based on
character code).

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`n`                  | number of characters to produce
`charset`            | string to draw the characters from.  Default: characters from "0" to "z".
`seed`               | random number seed

---

## Section: Parsing strings into numbers


### Function: parse\_int()

**Synopsis:** Parse an integer from a string.

**Topics:** [Strings](Topics#strings)

**See Also:** [parse\_float()](#function-parse_float), [parse\_frac()](#function-parse_frac), [parse\_num()](#function-parse_num)

**Usage:** 

- num = parse_int(str, [base])

**Description:** 

Converts a string into an integer with any base up to 16.  Returns NaN if
conversion fails.  Digits above 9 are represented using letters A-F in either
upper case or lower case.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`str`                | String to convert.
`base`               | Base for conversion, from 2-16.  Default: 10

**Example 1:** 

    include <BOSL2/std.scad>
    parse_int("349");        // Returns 349
    parse_int("-37");        // Returns -37
    parse_int("+97");        // Returns 97
    parse_int("43.9");       // Returns nan
    parse_int("1011010",2);  // Returns 90
    parse_int("13",2);       // Returns nan
    parse_int("dead",16);    // Returns 57005
    parse_int("CEDE", 16);   // Returns 52958
    parse_int("");           // Returns 0

<br clear="all" /><br/>

---

### Function: parse\_float()

**Synopsis:** Parse a float from a string.

**Topics:** [Strings](Topics#strings)

**See Also:** [parse\_int()](#function-parse_int), [parse\_frac()](#function-parse_frac), [parse\_num()](#function-parse_num)

**Usage:** 

- num = parse_float(str);

**Description:** 

Converts a string to a floating point number.  Returns NaN if the
conversion fails.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`str`                | String to convert.

**Example 1:** 

    include <BOSL2/std.scad>
    parse_float("44");       // Returns 44
    parse_float("3.4");      // Returns 3.4
    parse_float("-99.3332"); // Returns -99.3332
    parse_float("3.483e2");  // Returns 348.3
    parse_float("-44.9E2");  // Returns -4490
    parse_float("7.342e-4"); // Returns 0.0007342
    parse_float("");         // Returns 0

<br clear="all" /><br/>

---

### Function: parse\_frac()

**Synopsis:** Parse a float from a fraction string.

**Topics:** [Strings](Topics#strings)

**See Also:** [parse\_int()](#function-parse_int), [parse\_float()](#function-parse_float), [parse\_num()](#function-parse_num)

**Usage:** 

- num = parse_frac(str,[mixed=],[improper=],[signed=]);

**Description:** 

Converts a string fraction to a floating point number.  A string fraction has the form `[-][# ][#/#]` where each `#` is one or more of the
digits 0-9, and there is an optional sign character at the beginning.
The full form is a sign character and an integer, followed by exactly one space, followed by two more
integers separated by a "/" character.  The leading integer and
space can be omitted or the trailing fractional part can be omitted.  If you set `mixed` to false then the leading integer part is not
accepted and the input must include a slash.  If you set `improper` to false then the fractional part must be a proper fraction, where
the numerator is smaller than the denominator.  If you set `signed` to false then the leading sign character is not permitted.
The empty string evaluates to zero.  Any invalid string evaluates to NaN.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`str`                | String to convert.

<abbr title="These args must be used by name, ie: name=value">By&nbsp;Name</abbr> | What it does
-------------------- | ------------
`mixed`              | set to true to accept mixed fractions, false to reject them.  Default: true
`improper`           | set to true to accept improper fractions, false to reject them.  Default: true
`signed`             | set to true to accept a leading sign character, false to reject.  Default: true

**Example 1:** 

    include <BOSL2/std.scad>
    parse_frac("3/4");     // Returns 0.75
    parse_frac("-77/9");   // Returns -8.55556
    parse_frac("+1/3");    // Returns 0.33333
    parse_frac("19");      // Returns 19
    parse_frac("2 3/4");   // Returns 2.75
    parse_frac("-2 12/4"); // Returns -5
    parse_frac("");        // Returns 0
    parse_frac("3/0");     // Returns inf
    parse_frac("0/0");     // Returns nan
    parse_frac("-77/9",improper=false);   // Returns nan
    parse_frac("-2 12/4",improper=false); // Returns nan
    parse_frac("-2 12/4",signed=false);   // Returns nan
    parse_frac("-2 12/4",mixed=false);    // Returns nan
    parse_frac("2 1/4",mixed=false);      // Returns nan

<br clear="all" /><br/>

---

### Function: parse\_num()

**Synopsis:** Parse a float from a decimal or fraction string.

**Topics:** [Strings](Topics#strings)

**See Also:** [parse\_int()](#function-parse_int), [parse\_float()](#function-parse_float), [parse\_frac()](#function-parse_frac)

**Usage:** 

- num = parse_num(str);

**Description:** 

Converts a string to a number.  The string can be either a fraction (two integers separated by a "/") or a floating point number.
Returns NaN if the conversion fails.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`str`                | string to process

**Example 1:** 

    include <BOSL2/std.scad>
    parse_num("3/4");    // Returns 0.75
    parse_num("3.4e-2"); // Returns 0.034

<br clear="all" /><br/>

---

## Section: Formatting numbers into strings


### Function: format\_int()

**Synopsis:** Formats an integer into a string, with possible leading zeros.

**Topics:** [Strings](Topics#strings)

**See Also:** [format\_fixed()](#function-format_fixed), [format\_float()](#function-format_float), [format()](#function-format)

**Usage:** 

- str = format_int(i, [mindigits]);

**Description:** 

Formats an integer number into a string.  This can handle larger numbers than `str()`.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`i`                  | The integer to make a string of.
`mindigits`          | If the number has fewer than this many digits, pad the front with zeros until it does.  Default: 1.

**Example 1:** 

    include <BOSL2/std.scad>
    str(123456789012345);  // Returns "1.23457e+14"
    format_int(123456789012345);  // Returns "123456789012345"
    format_int(-123456789012345); // Returns "-123456789012345"
    format_int(12,3);             // Returns 012

<br clear="all" /><br/>

---

### Function: format\_fixed()

**Synopsis:** Formats a float into a string with a fixed number of decimal places.

**Topics:** [Strings](Topics#strings)

**See Also:** [format\_int()](#function-format_int), [format\_float()](#function-format_float), [format()](#function-format)

**Usage:** 

- s = format_fixed(f, [digits]);

**Description:** 

Given a floating point number, formats it into a string with the given number of digits after the decimal point.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`f`                  | The floating point number to format.
`digits`             | The number of digits after the decimal to show.  Default: 6

---

### Function: format\_float()

**Synopsis:** Formats a float into a string with a given number of significant digits.

**Topics:** [Strings](Topics#strings)

**See Also:** [format\_int()](#function-format_int), [format\_fixed()](#function-format_fixed), [format()](#function-format)

**Usage:** 

- str = format_float(f,[sig]);

**Description:** 

Formats the given floating point number `f` into a string with `sig` significant digits.
Strips trailing `0`s after the decimal point.  Strips trailing decimal point.
If possible, the number is represented in `sig` significant digits without a mantissa.
If given a list of numbers, recursively prints each item in the list, returning a string like `[3,4,5]`

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`f`                  | The floating point number to format.
`sig`                | The number of significant digits to display.  Default: 12

**Example 1:** 

    include <BOSL2/std.scad>
    format_float(PI,12);  // Returns: "3.14159265359"
    format_float([PI,-16.75],12);  // Returns: "[3.14159265359, -16.75]"

<br clear="all" /><br/>

---

### Function: format()

**Synopsis:** Formats multiple values into a string with a given format.

**Topics:** [Strings](Topics#strings)

**See Also:** [format\_int()](#function-format_int), [format\_fixed()](#function-format_fixed), [format\_float()](#function-format_float)

**Usage:** 

- s = format(fmt, vals);

**Description:** 

Given a format string and a list of values, inserts the values into the placeholders in the format string and returns it.
Formatting placeholders have the following syntax:
- A leading `{` character to show the start of the placeholder.
- An integer index into the `vals` list to specify which value should be formatted at that place. If not given, the first placeholder uses index `0`, the second uses index `1`, etc.
- An optional `:` separator to indicate that what follows if a formatting specifier.  If not given, no formatting info follows.
- An optional `-` character to indicate that the value should be left justified if the value needs field width padding.  If not given, right justification is used.
- An optional `0` character to indicate that the field should be padded with `0`s.  If not given, spaces are used for padding.
- An optional integer field width, which the value should be padded to.  If not given, no padding is performed.
- An optional `.` followed by an integer precision length, for specifying how many digits to display in numeric formats.  If not give, 6 digits is assumed.
- An optional letter to indicate the formatting style to use. If not given, `s` is assumed, which does its generic best to format any data type.
- A trailing `}` character to show the end of the placeholder.

Formatting styles, and their effects are as follows:
- `s`: Converts the value to a string with `str()` to display.  This is very generic.
- `i` or `d`: Formats numeric values as integers.
- `f`: Formats numeric values with the precision number of digits after the decimal point.  NaN and Inf are shown as `nan` and `inf`.
- `F`: Formats numeric values with the precision number of digits after the decimal point.  NaN and Inf are shown as `NAN` and `INF`.
- `g`: Formats numeric values with the precision number of total significant digits.  NaN and Inf are shown as `nan` and `inf`.  Mantissas are demarked by `e`.
- `G`: Formats numeric values with the precision number of total significant digits.  NaN and Inf are shown as `NAN` and `INF`.  Mantissas are demarked by `E`.
- `b`: If the value logically evaluates as true, it shows as `true`, otherwise `false`.
- `B`: If the value logically evaluates as true, it shows as `TRUE`, otherwise `FALSE`.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`fmt`                | The formatting string, with placeholders to format the values into.
`vals`               | The list of values to format.

**Example 1:** 

    include <BOSL2/std.scad>
    format("The value of {} is {:.14f}.", ["pi", PI]);  // Returns: "The value of pi is 3.14159265358979."
    format("The value {1:f} is known as {0}.", ["pi", PI]);  // Returns: "The value 3.141593 is known as pi."
    format("We use a very small value {1:.6g} as {0}.", ["EPSILON", EPSILON]);  // Returns: "We use a very small value 1e-9 as EPSILON."
    format("{:-5s}{:i}{:b}", ["foo", 12e3, 5]);  // Returns: "foo  12000true"
    format("{:-10s}{:.3f}", ["plecostamus",27.43982]);  // Returns: "plecostamus27.440"
    format("{:-10.9s}{:.3f}", ["plecostamus",27.43982]);  // Returns: "plecostam 27.440"

<br clear="all" /><br/>

---

## Section: Checking character class


### Function: is\_lower()

**Synopsis:** Returns true if all characters in the string are lowercase.

**Topics:** [Strings](Topics#strings)

**See Also:** [is\_upper()](#function-is_upper), [is\_digit()](#function-is_digit), [is\_hexdigit()](#function-is_hexdigit), [is\_letter()](#function-is_letter)

**Usage:** 

- x = is_lower(s);

**Description:** 

Returns true if all the characters in the given string are lowercase letters. (a-z)

---

### Function: is\_upper()

**Synopsis:** Returns true if all characters in the string are uppercase.

**Topics:** [Strings](Topics#strings)

**See Also:** [is\_lower()](#function-is_lower), [is\_digit()](#function-is_digit), [is\_hexdigit()](#function-is_hexdigit), [is\_letter()](#function-is_letter)

**Usage:** 

- x = is_upper(s);

**Description:** 

Returns true if all the characters in the given string are uppercase letters. (A-Z)

---

### Function: is\_digit()

**Synopsis:** Returns true if all characters in the string are decimal digits.

**Topics:** [Strings](Topics#strings)

**See Also:** [is\_lower()](#function-is_lower), [is\_upper()](#function-is_upper), [is\_hexdigit()](#function-is_hexdigit), [is\_letter()](#function-is_letter)

**Usage:** 

- x = is_digit(s);

**Description:** 

Returns true if all the characters in the given string are digits. (0-9)

---

### Function: is\_hexdigit()

**Synopsis:** Returns true if all characters in the string are hexidecimal digits.

**Topics:** [Strings](Topics#strings)

**See Also:** [is\_lower()](#function-is_lower), [is\_upper()](#function-is_upper), [is\_digit()](#function-is_digit), [is\_letter()](#function-is_letter)

**Usage:** 

- x = is_hexdigit(s);

**Description:** 

Returns true if all the characters in the given string are valid hexadecimal digits. (0-9 or a-f or A-F))

---

### Function: is\_letter()

**Synopsis:** Returns true if all characters in the string are letters.

**Topics:** [Strings](Topics#strings)

**See Also:** [is\_lower()](#function-is_lower), [is\_upper()](#function-is_upper), [is\_digit()](#function-is_digit), [is\_hexdigit()](#function-is_hexdigit)

**Usage:** 

- x = is_letter(s);

**Description:** 

Returns true if all the characters in the given string are standard ASCII letters. (A-Z or a-z)

---


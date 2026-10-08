# LibFile: linalg.scad

This file provides linear algebra, with support for matrix construction,
solutions to linear systems of equations, QR and Cholesky factorizations, and
matrix inverse.

To use, add the following lines to the beginning of your file:

    include <BOSL2/std.scad>

## File Contents

1. [Section: Matrices](#section-matrices)

2. [Section: Matrix testing and display](#section-matrix-testing-and-display)
    - [`is_matrix()`](#function-is_matrix) – Check if input is a numeric matrix or tensor, optionally of specified size
    - [`is_matrix_symmetric()`](#function-is_matrix_symmetric) – Checks if matrix is symmetric
    - [`is_rotation()`](#function-is_rotation) – Check if a transformation matrix represents a rotation.
    - [`echo_matrix()`](#functionmodule-echo_matrix) – Print a matrix neatly to the console.

3. [Section: Matrix indexing](#section-matrix-indexing)
    - [`column()`](#function-column) – Extract a column from a matrix.
    - [`submatrix()`](#function-submatrix) – Extract a submatrix from a matrix

4. [Section: Matrix construction and modification](#section-matrix-construction-and-modification)
    - [`ident()`](#function-ident) – Return identity matrix.
    - [`diagonal_matrix()`](#function-diagonal_matrix) – Make a diagonal matrix.
    - [`transpose()`](#function-transpose) – Transpose a matrix
    - [`swap_columns()`](#function-swap_columns) – Swap two columns of a matrix
    - [`outer_product()`](#function-outer_product) – Compute the outer product of two vectors.
    - [`submatrix_set()`](#function-submatrix_set) – Takes a matrix as input and change values in a submatrix.
    - [`hstack()`](#function-hstack) – Make a new matrix by stacking matrices horizontally.
    - [`block_matrix()`](#function-block_matrix) – Make a new matrix from a block of matrices.

5. [Section: Solving Linear Equations and Matrix Factorizations](#section-solving-linear-equations-and-matrix-factorizations)
    - [`linear_solve()`](#function-linear_solve) – Solve Ax=b or, for overdetermined case, solve the least square problem.
    - [`linear_solve3()`](#function-linear_solve3) – Fast solution to Ax=b where A is 3x3.
    - [`matrix_inverse()`](#function-matrix_inverse) – General matrix inverse.
    - [`rot_inverse()`](#function-rot_inverse) – Invert 2d or 3d rotation transformations.
    - [`null_space()`](#function-null_space) – Return basis for the null space of A.
    - [`qr_factor()`](#function-qr_factor) – Compute QR factorization of a matrix.
    - [`lu_factor()`](#function-lu_factor) – Compute LU factorization of a matrix with pivoting.
    - [`back_substitute()`](#function-back_substitute) – Solve an upper triangular system, Rx=b.
    - [`cholesky()`](#function-cholesky) – Compute the Cholesky factorization of a matrix.

6. [Section: Matrix Properties: Determinants, Norm, Trace](#section-matrix-properties-determinants-norm-trace)
    - [`det2()`](#function-det2) – Compute determinant of 2x2 matrix.
    - [`det3()`](#function-det3) – Compute determinant of 3x3 matrix.
    - [`det4()`](#function-det4) – Compute determinant of 4x4 matrix.
    - [`determinant()`](#function-determinant) – compute determinant of an arbitrary square matrix.
    - [`norm_fro()`](#function-norm_fro) – Compute Frobenius norm of a matrix
    - [`matrix_trace()`](#function-matrix_trace) – Compute the trace of a square matrix.


## Section: Matrices

The matrix, a rectangular array of numbers which represents a linear transformation,
is the fundamental object in linear algebra.  In OpenSCAD a matrix is a list of lists of numbers
with a rectangular structure.  Because OpenSCAD treats all data the same, most of the functions that
index matrices or construct them will work on matrices (lists of lists) whose elements are not numbers but may be
arbitrary data: strings, booleans, or even other lists.  It may even be acceptable in some cases if the structure is non-rectangular.
Of course, linear algebra computations and solutions require true matrices with rectangular structure, where all the entries are
finite numbers.

Matrices in OpenSCAD are lists of row vectors.  However, a potential source of confusion is that OpenSCAD
treats vectors as either column vectors or row vectors as demanded by
context.  Thus both `v*M` and `M*v` are valid if `M` is square and `v` has the right length.  If you want to multiply
`M` on the left by `v` and `w` you can do this with `[v,w]*M` but if you want to multiply on the right side with `v` and `w` as
column vectors, you now need to use [`transpose()`](#function-transpose) because OpenSCAD doesn't adjust matrices
contextually:  `A=M*transpose([v,w])`.  The solutions are now columns of A and you must extract
them with [`column()`](#function-column) or take the transpose of `A`.

## Section: Matrix testing and display


### Function: is\_matrix()

**Synopsis:** Check if input is a numeric matrix or tensor, optionally of specified size

**Topics:** [Matrices](Topics#matrices)

**See Also:** [is\_matrix\_symmetric()](#function-is_matrix_symmetric), [is\_rotation()](#function-is_rotation)

**Usage:** 

- test = is_matrix(A, [m], [n], [square])
- test = is_matrix(A, [rank=], [shape=], [equal=])

**Description:** 

Returns true if A is a numeric matrix of height m and width n with finite entries.  If m or n
are omitted or set to undef then returns true for any positive dimension.
Alternatively, checks if A is a numerical rectangular array with `rank` levels of nesting
(a tensor of the specified rank).  The `shape` parameter specifies required dimensions at each
level, and may contain `undef` to leave a particular level unconstrained.  If you give `shape`
then the rank is determined from its length and you cannot give `rank`.

You cannot mix `m`, `n` and `square` with `rank`, `shape`, and `equal`.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`A`                  | The matrix to test.
`m`                  | If given, requires the matrix to have this height.
`n`                  | If given, requires the matrix to have this width.
`square`             | If true, matrix must have height equal to width. Default: false

<abbr title="These args must be used by name, ie: name=value">By&nbsp;Name</abbr> | What it does
-------------------- | ------------
`rank`               | Specify rank (nesting level) of A, a positive integer.  Default: 2
`shape`              | Nonempty list specifying required dimensions of A that may contain undef entries
`equal`              | If true, all dimensions of A must be equal.  Default: false

---

### Function: is\_matrix\_symmetric()

**Synopsis:** Checks if matrix is symmetric

**Topics:** [Matrices](Topics#matrices)

**See Also:** [is\_matrix()](#function-is_matrix), [is\_rotation()](#function-is_rotation)

**Usage:** 

- b = is_matrix_symmetric(A, [eps])

**Description:** 

Returns true if the input matrix is symmetric, meaning it approximately equals its transpose.
The matrix can have arbitrary entries.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`A`                  | matrix to test
`eps`                | epsilon for comparing equality.  Default: 1e-12

---

### Function: is\_rotation()

**Synopsis:** Check if a transformation matrix represents a rotation.

**Topics:** [Affine](Topics#affine), [Matrices](Topics#matrices), [Transforms](Topics#transforms)

**See Also:** [is\_matrix()](#function-is_matrix), [is\_matrix\_symmetric()](#function-is_matrix_symmetric)

**Usage:** 

- b = is_rotation(A, [dim], [centered])

**Description:** 

Returns true if the input matrix is a square affine matrix that is a rotation around any point,
or around the origin if `centered` is true.
The matrix must be 3x3 (representing a 2d transformation) or 4x4 (representing a 3d transformation).
You can set `dim` to 2 to require a 2d transform (3x3 matrix) or to 3 to require a 3d transform (4x4 matrix).

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`A`                  | matrix to test
`dim`                | if set, specify dimension in which the transform operates (2 or 3)
`centered`           | if true then require rotation to be around the origin.  Default: false

---

### Function/Module: echo\_matrix()

**Synopsis:** Print a matrix neatly to the console.

**Topics:** [Matrices](Topics#matrices)

**See Also:** [is\_matrix()](#function-is_matrix), [is\_matrix\_symmetric()](#function-is_matrix_symmetric), [is\_rotation()](#function-is_rotation)

**Usage:** 

- echo_matrix(M, [description], [sig], [sep], [eps]);
- dummy = echo_matrix(M, [description], [sig], [sep], [eps]),

**Description:** 

Display a numerical matrix in a readable columnar format with `sig` significant
digits.  Values smaller than eps display as zero.  If you give a description
it is displayed at the top.  You can change the space between columns by
setting `sep` to a number of spaces, which will use wide figure spaces the same
width as digits, or you can set it to any string to separate the columns.
Values that are NaN or INF will display as "nan" and "inf".  Values which are
otherwise non-numerica display as two dashes.  Note that this includes lists, so
a 3D array will display as a list of dashes.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`M`                  | matrix to display, which should be numerical
`description`        | optional text to print before the matrix
`sig`                | number of digits to display.  Default: 4
`sep`                | number of spaces between columns or a text string to separate columns.  Default: 1
`eps`                | numbers smaller than this display as zero.  Default: 1e-9

---

## Section: Matrix indexing


### Function: column()

**Synopsis:** Extract a column from a matrix.

**Topics:** [Matrices](Topics#matrices), [List Handling](Topics#list-handling), [Arrays](Topics#arrays)

**See Also:** [select()](lists.scad#function-select), [slice()](lists.scad#function-slice)

**Usage:** 

- list = column(M, i);

**Description:** 

Extracts entry `i` from each list in M, or equivalently column i from the matrix M, and returns it as a vector.
This function will return `undef` at all entry positions indexed by i not found in M.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`M`                  | The given list of lists.
`i`                  | The index to fetch

**Example 1:** 

    include <BOSL2/std.scad>
    M = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]];
    a = column(M,2);      // Returns [3, 7, 11, 15]
    b = column(M,0);      // Returns [1, 5, 9, 13]
    N = [ [1,2], [3], [4,5], [6,7,8] ];
    c = column(N,1);      // Returns [1,undef,5,7]
    data = [[1,[3,4]], [3, [9,3]], [4, [3,1]]];   // Matrix with non-numeric entries
    d = column(data,0);   // Returns [1,3,4]
    e = column(data,1);   // Returns [[3,4],[9,3],[3,1]]

<br clear="all" /><br/>

---

### Function: submatrix()

**Synopsis:** Extract a submatrix from a matrix

**Topics:** [Matrices](Topics#matrices), [Arrays](Topics#arrays)

**See Also:** [column()](#function-column), [block\_matrix()](#function-block_matrix), [submatrix\_set()](#function-submatrix_set)

**Usage:** 

- mat = submatrix(M, idx1, idx2);

**Description:** 

The input must be a list of lists (a matrix or 2d array).  Returns a submatrix by selecting the rows listed in idx1 and columns listed in idx2.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`M`                  | Given list of lists
`idx1`               | rows index list or range
`idx2`               | column index list or range

**Example 1:** 

    include <BOSL2/std.scad>
    M = [[ 1, 2, 3, 4, 5],
         [ 6, 7, 8, 9,10],
         [11,12,13,14,15],
         [16,17,18,19,20],
         [21,22,23,24,25]];
    submatrix(M,[1:2],[3:4]);  // Returns [[9, 10], [14, 15]]
    submatrix(M,[1], [3,4]));  // Returns [[9,10]]
    submatrix(M,1, [3,4]));  // Returns [[9,10]]
    submatrix(M,1,3));  // Returns [[9]]
    submatrix(M, [3,4],1); // Returns  [[17],[22]]);
    submatrix(M, [1,3],[2,4]); // Returns [[8,10],[18,20]]);
    A = [[true,    17, "test"],
         [[4,2],   91, false],
         [6,    [3,4], undef]];
    submatrix(A,[0,2],[1,2]);   // Returns [[17, "test"], [[3, 4], undef]]

<br clear="all" /><br/>

---

## Section: Matrix construction and modification


### Function: ident()

**Synopsis:** Return identity matrix.

**Topics:** [Affine](Topics#affine), [Matrices](Topics#matrices), [Transforms](Topics#transforms)

**See Also:** [IDENT](constants.scad#constant-ident), [submatrix()](#function-submatrix), [column()](#function-column)

**Usage:** 

- mat = ident(n);

**Description:** 

Create an `n` by `n` square identity matrix.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`n`                  | The size of the identity matrix square, `n` by `n`.

**Example 1:** 

    include <BOSL2/std.scad>
    mat = ident(3);
    // Returns:
    //   [
    //     [1, 0, 0],
    //     [0, 1, 0],
    //     [0, 0, 1]
    //   ]

<br clear="all" /><br/>

**Example 2:** 

    include <BOSL2/std.scad>
    mat = ident(4);
    // Returns:
    //   [
    //     [1, 0, 0, 0],
    //     [0, 1, 0, 0],
    //     [0, 0, 1, 0],
    //     [0, 0, 0, 1]
    //   ]

<br clear="all" /><br/>

---

### Function: diagonal\_matrix()

**Synopsis:** Make a diagonal matrix.

**Topics:** [Affine](Topics#affine), [Matrices](Topics#matrices)

**See Also:** [column()](#function-column), [submatrix()](#function-submatrix)

**Usage:** 

- mat = diagonal_matrix(diag, [offdiag]);

**Description:** 

Creates a square matrix with the items in the list `diag` on
its diagonal.  The off diagonal entries are set to offdiag,
which is zero by default.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`diag`               | A list of items to put in the diagnal cells of the matrix.
`offdiag`            | Value to put in non-diagonal matrix cells.

---

### Function: transpose()

**Synopsis:** Transpose a matrix

**Topics:** [Linear Algebra](Topics#linear-algebra), [Matrices](Topics#matrices)

**See Also:** [submatrix()](#function-submatrix), [block\_matrix()](#function-block_matrix), [hstack()](#function-hstack), [flatten()](lists.scad#function-flatten)

**Usage:** 

- M = transpose(M, [reverse]);

**Description:** 

Returns the transpose of the given input matrix.  The input can be a matrix with arbitrary entries or
a numerical vector.  If you give a vector then transpose returns it unchanged.
When reverse=true, the transpose is done across the secondary diagonal.  (See example below.)
By default, reverse=false.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`M`                  | matrix to transpose
`reverse`            | if true reflect across secondary diagonal.  Default: false

**Example 1:** 

    include <BOSL2/std.scad>
    M = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ];
    t = transpose(M);
    // Returns:
    // [
    //     [1, 4, 7],
    //     [2, 5, 8],
    //     [3, 6, 9]
    // ]

<br clear="all" /><br/>

**Example 2:** 

    include <BOSL2/std.scad>
    M = [
        [1, 2, 3],
        [4, 5, 6]
    ];
    t = transpose(M);
    // Returns:
    // [
    //     [1, 4],
    //     [2, 5],
    //     [3, 6],
    // ]

<br clear="all" /><br/>

**Example 3:** 

    include <BOSL2/std.scad>
    M = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ];
    t = transpose(M, reverse=true);
    // Returns:
    // [
    //  [9, 6, 3],
    //  [8, 5, 2],
    //  [7, 4, 1]
    // ]

<br clear="all" /><br/>

**Example 4:** Transpose on a list of numbers returns the list unchanged

    include <BOSL2/std.scad>
    transpose([3,4,5]);  // Returns: [3,4,5]

<br clear="all" /><br/>

**Example 5:** Transpose on non-numeric input

    include <BOSL2/std.scad>
    arr = [
        [  "a",  "b", "c"],
        [  "d",  "e", "f"],
        [[1,2],[3,4],[5,6]]
    ];
    t = transpose(arr);
    // Returns:
    // [
    //     ["a", "d", [1,2]],
    //     ["b", "e", [3,4]],
    //     ["c", "f", [5,6]],
    // ]

<br clear="all" /><br/>

---

### Function: swap\_columns()

**Synopsis:** Swap two columns of a matrix

**Topics:** [Linear Algebra](Topics#linear-algebra), [Matrices](Topics#matrices)

**See Also:** [submatrix()](#function-submatrix), [block\_matrix()](#function-block_matrix), [hstack()](#function-hstack), [flatten()](lists.scad#function-flatten)

**Usage:** 

- M = swap_columns(M, i, j);

**Description:** 

Returns a matrix where columns i and j are swapped.  The input must be a list of lists where each row has the same length.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`M`                  | matrix to transpose
`reverse`            | if true reflect across secondary diagonal.  Default: false

**Example 1:** 

    include <BOSL2/std.scad>
    M = [
          [1, 2, 3, 0, 1],
          [4, 5, 6, 0, 1],
          [7, 8, 9, 0, 1]
    ];
    S = swap_columns(M,1,3);
    // Returns
    // [
    //   [1, 0, 3, 2, 1],
    //   [4, 0, 6, 5, 1],
    //   [7, 0, 9, 8, 1]
    // ]

<br clear="all" /><br/>

---

### Function: outer\_product()

**Synopsis:** Compute the outer product of two vectors.

**Topics:** [Linear Algebra](Topics#linear-algebra), [Matrices](Topics#matrices)

**See Also:** [submatrix()](#function-submatrix), [determinant()](#function-determinant)

**Usage:** 

- x = outer_product(u,v);

**Usage:** 

- M = outer_product(u,v);

**Description:** 

Compute the outer product of two vectors, which is a matrix.

---

### Function: submatrix\_set()

**Synopsis:** Takes a matrix as input and change values in a submatrix.

**Topics:** [Matrices](Topics#matrices), [Arrays](Topics#arrays)

**See Also:** [column()](#function-column), [submatrix()](#function-submatrix)

**Usage:** 

- mat = submatrix_set(M, A, [m], [n]);

**Description:** 

Sets a submatrix of M equal to the matrix A.  By default the top left corner of M is set to A, but
you can specify offset coordinates m and n.  If A (as adjusted by m and n) extends beyond the bounds
of M then the extra entries are ignored.  You can pass in `A=[[]]`, a null matrix, and M will be
returned unchanged.  This function works on arbitrary lists of lists and the input M need not be rectangular in shape.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`M`                  | Original matrix.
`A`                  | Submatrix of new values to write into M
`m`                  | Row number of upper-left corner to place A at.  Default: 0
`n`                  | Column number of upper-left corner to place A at.  Default: 0

---

### Function: hstack()

**Synopsis:** Make a new matrix by stacking matrices horizontally.

**Topics:** [Matrices](Topics#matrices), [Arrays](Topics#arrays)

**See Also:** [column()](#function-column), [submatrix()](#function-submatrix), [block\_matrix()](#function-block_matrix)

**Usage:** 

- A = hstack(M1, M2)
- A = hstack(M1, M2, M3)
- A = hstack([M1, M2, M3, ...])

**Description:** 

Constructs a matrix by horizontally "stacking" together compatible matrices or vectors.  Vectors are treated as columns in the stack.
This command is the inverse of `column`.  Note: strings given in vectors are broken apart into lists of characters.  Strings given
in matrices are preserved as strings.  If you need to combine vectors of strings use [`list_to_matrix()`](lists.scad#function-list_to_matrix) as shown below to convert the
vector into a column matrix.  Also note that vertical stacking can be done directly with concat.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`M1`                 | If given with other arguments, the first matrix (or vector) to stack.  If given alone, a list of matrices/vectors to stack.
`M2`                 | Second matrix/vector to stack
`M3`                 | Third matrix/vector to stack.

**Example 1:** 

    include <BOSL2/std.scad>
    M = ident(3);
    v1 = [2,3,4];
    v2 = [5,6,7];
    v3 = [8,9,10];
    a = hstack(v1,v2);     // Returns [[2, 5], [3, 6], [4, 7]]
    b = hstack(v1,v2,v3);  // Returns [[2, 5,  8],
                           //          [3, 6,  9],
                           //          [4, 7, 10]]
    c = hstack([M,v1,M]);  // Returns [[1, 0, 0, 2, 1, 0, 0],
                           //          [0, 1, 0, 3, 0, 1, 0],
                           //          [0, 0, 1, 4, 0, 0, 1]]
    d = hstack(column(M,0), submatrix(M,idx(M),[1 2]));  // Returns M
    strvec = ["one","two"];
    strmat = [["three","four"], ["five","six"]];
    e = hstack(strvec,strvec); // Returns [["o", "n", "e", "o", "n", "e"],
                               //          ["t", "w", "o", "t", "w", "o"]]
    f = hstack(list_to_matrix(strvec,1), list_to_matrix(strvec,1));
                               // Returns [["one", "one"],
                               //          ["two", "two"]]
    g = hstack(strmat,strmat); //  Returns: [["three", "four", "three", "four"],
                               //            [ "five",  "six",  "five",  "six"]]

<br clear="all" /><br/>

---

### Function: block\_matrix()

**Synopsis:** Make a new matrix from a block of matrices.

**Topics:** [Matrices](Topics#matrices), [Arrays](Topics#arrays)

**See Also:** [column()](#function-column), [submatrix()](#function-submatrix)

**Usage:** 

- bmat = block_matrix([[M11, M12,...],[M21, M22,...], ... ]);

**Description:** 

Create a block matrix by supplying a matrix of matrices, which will
be combined into one unified matrix.  Every matrix in one row
must have the same height, and the combined width of the matrices
in each row must be equal. Strings will stay strings.

**Example 1:** 

    include <BOSL2/std.scad>
    A = [[1,2],
         [3,4]];
    B = ident(2);
    C = block_matrix([[A,B],[B,A],[A,B]]);
        // Returns:
        //        [[1, 2, 1, 0],
        //         [3, 4, 0, 1],
        //         [1, 0, 1, 2],
        //         [0, 1, 3, 4],
        //         [1, 2, 1, 0],
        //         [3, 4, 0, 1]]);
    D = block_matrix([[A,B], ident(4)]);
        // Returns:
        //        [[1, 2, 1, 0],
        //         [3, 4, 0, 1],
        //         [1, 0, 0, 0],
        //         [0, 1, 0, 0],
        //         [0, 0, 1, 0],
        //         [0, 0, 0, 1]]);
    E = [["one", "two"], [3,4]];
    F = block_matrix([[E,E]]);
        // Returns:
        //        [["one", "two", "one", "two"],
        //         [    3,     4,     3,     4]]

<br clear="all" /><br/>

---

## Section: Solving Linear Equations and Matrix Factorizations


### Function: linear\_solve()

**Synopsis:** Solve Ax=b or, for overdetermined case, solve the least square problem.

**Topics:** [Matrices](Topics#matrices), [Linear Algebra](Topics#linear-algebra)

**See Also:** [linear\_solve3()](#function-linear_solve3), [matrix\_inverse()](#function-matrix_inverse), [rot\_inverse()](#function-rot_inverse), [back\_substitute()](#function-back_substitute), [cholesky()](#function-cholesky)

**Usage:** 

- solv = linear_solve(A,b,[pivot])

**Description:** 

Solves the linear system Ax=b.  By default, uses the QR factorization, which is the slowest but most flexible
solution method.  If `A` is square and non-singular the unique solution is returned.  If `A` is overdetermined
the least squares solution is returned. If `A` is underdetermined, the minimal norm solution is returned.
If `A` is rank deficient or singular then linear_solve returns `[]`.  If `b` is a matrix that is compatible with `A`
then the problem is solved for the matrix valued right hand side and a matrix is returned.  Note that if you
want to solve Ax=b1 and Ax=b2 that you need to form the matrix `transpose([b1,b2])` for the right hand side and then
transpose the returned value.  If `pivot` is set to true (the default) then
pivoting is used in the QR factorization, which is slower but expected to be more accurate.

If `A` is a square matrix you can select `method="lu"` to use LU decomposition, which may be slightly faster than QR on small problems.

If `A` is symmetric and positive definite then `method="cholesky"` is faster than LU decomposition.
(About 5x faster than LU decomposition on large problems.)

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`A`                  | Matrix describing the linear system, which need not be square
`b`                  | right hand side for linear system, which can be a matrix to solve several cases simultaneously.  Must be consistent with A.
`pivot`              | if true use pivoting when computing the QR factorization.  Default: true
`method`             | Set to "qr", "lu" or "cholesky" to choose the solution method.  Default: "qr"

---

### Function: linear\_solve3()

**Synopsis:** Fast solution to Ax=b where A is 3x3.

**Topics:** [Matrices](Topics#matrices), [Linear Algebra](Topics#linear-algebra)

**See Also:** [linear\_solve()](#function-linear_solve), [matrix\_inverse()](#function-matrix_inverse), [rot\_inverse()](#function-rot_inverse), [back\_substitute()](#function-back_substitute), [cholesky()](#function-cholesky)

**Usage:** 

- x = linear_solve3(A,b)

**Description:** 

Fast solution to a 3x3 linear system using Cramer's rule (which appears to be the fastest
method in OpenSCAD).  The input `A` must be a 3x3 matrix.  Returns undef if `A` is singular.
The input `b` must be a 3-vector.  Note that Cramer's rule is not a stable algorithm, so for
the highest accuracy on ill-conditioned problems you may want to use the general solver, which is about ten times slower.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`A`                  | 3x3 matrix for linear system
`b`                  | length 3 vector, right hand side of linear system

---

### Function: matrix\_inverse()

**Synopsis:** General matrix inverse.

**Topics:** [Matrices](Topics#matrices), [Linear Algebra](Topics#linear-algebra)

**See Also:** [linear\_solve()](#function-linear_solve), [linear\_solve3()](#function-linear_solve3), [rot\_inverse()](#function-rot_inverse), [back\_substitute()](#function-back_substitute), [cholesky()](#function-cholesky)

**Usage:** 

- mat = matrix_inverse(A)

**Description:** 

Compute the matrix inverse of the square matrix `A`.  If `A` is singular, returns `undef`.
Note that if you just want to solve a linear system of equations you should NOT use this function.
Instead use [`linear_solve()`](#function-linear_solve), or use [`qr_factor()`](#function-qr_factor).  The computation
will be faster and more accurate.

---

### Function: rot\_inverse()

**Synopsis:** Invert 2d or 3d rotation transformations.

**Topics:** [Matrices](Topics#matrices), [Linear Algebra](Topics#linear-algebra), [Affine](Topics#affine)

**See Also:** [linear\_solve()](#function-linear_solve), [linear\_solve3()](#function-linear_solve3), [matrix\_inverse()](#function-matrix_inverse), [back\_substitute()](#function-back_substitute), [cholesky()](#function-cholesky)

**Usage:** 

- B = rot_inverse(A)

**Description:** 

Inverts a 2d (3x3) or 3d (4x4) rotation matrix.  The matrix can be a rotation around any center,
so it may include a translation.  This is faster and likely to be more accurate than using `matrix_inverse()`.

---

### Function: null\_space()

**Synopsis:** Return basis for the null space of A.

**Topics:** [Matrices](Topics#matrices), [Linear Algebra](Topics#linear-algebra)

**See Also:** [linear\_solve()](#function-linear_solve), [linear\_solve3()](#function-linear_solve3), [matrix\_inverse()](#function-matrix_inverse), [rot\_inverse()](#function-rot_inverse), [back\_substitute()](#function-back_substitute), [cholesky()](#function-cholesky)

**Usage:** 

- x = null_space(A)

**Description:** 

Returns an orthonormal basis for the null space of `A`, namely the vectors {x} such that Ax=0.
If the null space is just the origin then returns an empty list.

---

### Function: qr\_factor()

**Synopsis:** Compute QR factorization of a matrix.

**Topics:** [Matrices](Topics#matrices), [Linear Algebra](Topics#linear-algebra)

**See Also:** [linear\_solve()](#function-linear_solve), [linear\_solve3()](#function-linear_solve3), [matrix\_inverse()](#function-matrix_inverse), [rot\_inverse()](#function-rot_inverse), [back\_substitute()](#function-back_substitute), [cholesky()](#function-cholesky)

**Usage:** 

- qr = qr_factor(A,[pivot]);

**Description:** 

Calculates the QR factorization of the input matrix A and returns it as the list [Q,R,P].  This factorization can be
used to solve linear systems of equations.  The factorization is `A = Q*R*transpose(P)`.  If pivot is false (the default)
then P is the identity matrix and A = Q*R.  If pivot is true then column pivoting results in an R matrix where the diagonal
is non-decreasing.  The use of pivoting is supposed to increase accuracy for poorly conditioned problems, and is necessary
for rank estimation or computation of the null space, but it may be slower.

---

### Function: lu\_factor()

**Synopsis:** Compute LU factorization of a matrix with pivoting.

**Topics:** [Matrices](Topics#matrices), [Linear Algebra](Topics#linear-algebra)

**See Also:** [linear\_solve()](#function-linear_solve), [linear\_solve3()](#function-linear_solve3), [matrix\_inverse()](#function-matrix_inverse), [rot\_inverse()](#function-rot_inverse), [back\_substitute()](#function-back_substitute), [cholesky()](#function-cholesky)

**Usage:** 

- lt_u_p = lu_factor(A);

**Description:** 

Calculates the LU factorization of the input matrix A with pivoting [LT,U,p].  This factorization can be
used to solve linear systems of equations and is equivalent to Gaussian elimination.
The factorization is `select(A,p) = transpose(LT) * U`. The permutation `p` is an index list, not a matrix.
The LU decomposition only works on square,  nonsingular matrices.  If `A` is singular then returns undef.

---

### Function: back\_substitute()

**Synopsis:** Solve an upper triangular system, Rx=b.

**Topics:** [Matrices](Topics#matrices), [Linear Algebra](Topics#linear-algebra)

**See Also:** [linear\_solve()](#function-linear_solve), [linear\_solve3()](#function-linear_solve3), [matrix\_inverse()](#function-matrix_inverse), [rot\_inverse()](#function-rot_inverse), [cholesky()](#function-cholesky)

**Usage:** 

- x = back_substitute(R, b, [transpose]);

**Description:** 

Solves the problem Rx=b where R is an upper triangular square matrix.  The lower triangular entries of R are
ignored.  If transpose==true then instead solve transpose(R)*x=b.
You can supply a compatible matrix b and it will produce the solution for every column of b.  Note that if you want to
solve Rx=b1 and Rx=b2 you must set b to transpose([b1,b2]) and then take the transpose of the result.  If the matrix
is singular (e.g. has a zero on the diagonal) then it returns [].

---

### Function: cholesky()

**Synopsis:** Compute the Cholesky factorization of a matrix.

**Topics:** [Matrices](Topics#matrices), [Linear Algebra](Topics#linear-algebra)

**See Also:** [linear\_solve()](#function-linear_solve), [linear\_solve3()](#function-linear_solve3), [matrix\_inverse()](#function-matrix_inverse), [rot\_inverse()](#function-rot_inverse), [back\_substitute()](#function-back_substitute)

**Usage:** 

- L = cholesky(A);

**Description:** 

Compute the cholesky factor, L, of the symmetric positive definite matrix A.
The matrix L is lower triangular and `L * transpose(L) = A`.  If the A is
not symmetric then an error is displayed.  If the matrix is symmetric but
not positive definite then undef is returned.

---

## Section: Matrix Properties: Determinants, Norm, Trace


### Function: det2()

**Synopsis:** Compute determinant of 2x2 matrix.

**Topics:** [Matrices](Topics#matrices), [Linear Algebra](Topics#linear-algebra)

**See Also:** [det3()](#function-det3), [det4()](#function-det4), [determinant()](#function-determinant), [norm\_fro()](#function-norm_fro), [matrix\_trace()](#function-matrix_trace)

**Usage:** 

- d = det2(M);

**Description:** 

Rturns the determinant for the given 2x2 matrix.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`M`                  | The 2x2 matrix to get the determinant of.

**Example 1:** 

    include <BOSL2/std.scad>
    M = [ [6,-2], [1,8] ];
    det = det2(M);  // Returns: 50

<br clear="all" /><br/>

---

### Function: det3()

**Synopsis:** Compute determinant of 3x3 matrix.

**Topics:** [Matrices](Topics#matrices), [Linear Algebra](Topics#linear-algebra)

**See Also:** [det2()](#function-det2), [det4()](#function-det4), [determinant()](#function-determinant), [norm\_fro()](#function-norm_fro), [matrix\_trace()](#function-matrix_trace)

**Usage:** 

- d = det3(M);

**Description:** 

Returns the determinant for the given 3x3 matrix.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`M`                  | The 3x3 square matrix to get the determinant of.

**Example 1:** 

    include <BOSL2/std.scad>
    M = [ [6,4,-2], [1,-2,8], [1,5,7] ];
    det = det3(M);  // Returns: -334

<br clear="all" /><br/>

---

### Function: det4()

**Synopsis:** Compute determinant of 4x4 matrix.

**Topics:** [Matrices](Topics#matrices), [Linear Algebra](Topics#linear-algebra)

**See Also:** [det2()](#function-det2), [det3()](#function-det3), [determinant()](#function-determinant), [norm\_fro()](#function-norm_fro), [matrix\_trace()](#function-matrix_trace)

**Usage:** 

- d = det4(M);

**Description:** 

Returns the determinant for the given 4x4 matrix.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`M`                  | The 4x4 square matrix to get the determinant of.

**Example 1:** 

    include <BOSL2/std.scad>
    M = [ [6,4,-2,1], [1,-2,8,-3], [1,5,7,4], [2,3,4,7] ];
    det = det4(M);  // Returns: -1773

<br clear="all" /><br/>

---

### Function: determinant()

**Synopsis:** compute determinant of an arbitrary square matrix.

**Topics:** [Matrices](Topics#matrices), [Linear Algebra](Topics#linear-algebra)

**See Also:** [det2()](#function-det2), [det3()](#function-det3), [det4()](#function-det4), [norm\_fro()](#function-norm_fro), [matrix\_trace()](#function-matrix_trace)

**Usage:** 

- d = determinant(M);

**Description:** 

Returns the determinant for the given square matrix.

**Arguments:** 

<abbr title="These args can be used by position or by name.">By&nbsp;Position</abbr> | What it does
-------------------- | ------------
`M`                  | The NxN square matrix to get the determinant of.

**Example 1:** 

    include <BOSL2/std.scad>
    M = [ [6,4,-2,9], [1,-2,8,3], [1,5,7,6], [4,2,5,1] ];
    det = determinant(M);  // Returns: 2267

<br clear="all" /><br/>

---

### Function: norm\_fro()

**Synopsis:** Compute Frobenius norm of a matrix

**Topics:** [Matrices](Topics#matrices), [Linear Algebra](Topics#linear-algebra)

**See Also:** [det2()](#function-det2), [det3()](#function-det3), [det4()](#function-det4), [determinant()](#function-determinant), [matrix\_trace()](#function-matrix_trace)

**Usage:** 

- norm_fro(A)

**Description:** 

Computes frobenius norm of input matrix.  The frobenius norm is the square root of the sum of the
squares of all of the entries of the matrix.  On vectors it is the same as the usual 2-norm.
This is an easily computed norm that is convenient for comparing two matrices.

---

### Function: matrix\_trace()

**Synopsis:** Compute the trace of a square matrix.

**Topics:** [Matrices](Topics#matrices), [Linear Algebra](Topics#linear-algebra)

**See Also:** [det2()](#function-det2), [det3()](#function-det3), [det4()](#function-det4), [determinant()](#function-determinant), [norm\_fro()](#function-norm_fro)

**Usage:** 

- matrix_trace(M)

**Description:** 

Computes the trace of a square matrix, the sum of the entries on the diagonal.

---


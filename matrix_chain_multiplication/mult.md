# mult.py

## Problem Statement

You’re going to write a program called mult.c (or mult.cpp, mult.java or mult.py, depending on your language choice). This program will solve the matrix chain multiplication problem. It will read in the dimensions of a series of matrices and report the least expensive way to multiply them as a fully parenthesized product of matrices.

If there’s more than one equally good way to parenthesize the matrix chain, either answer is fine (I won’t test your program on inputs like this).

### Input Format

Input will be given on standard input. It will start with a positive integer, n. This gives the number of matrices that are to be multiplied. This will be followed by n + 1 positive integers, one value per line. The first value is the height of the first matrix in the chain. The next value is the height of the second matrix (and also the width of the first matrix). This will continue up to the last value, which gives the width of the last matrix.

The input for the simple example we looked at in class would be given as:

```
7
3
8
4
6
6
9
2
5
```

### Output

Print a single line of output (to standard out) giving fully parenthesized expression showing how the product should be computed in order to minimize computation cost. The names of the matrices will be written as M1 M2 ... Leave one space between matrices, parentheses and multiplication operators, and don’t put parentheses around individual matrices or around the entire expression. The output for the example above should look like:

`( M1 * ( M2 * ( M3 * ( M4 * ( M5 * M6 ) ) ) ) ) * M7`

## Solution Usage

The solution was written for use with Python 3.x. Three input and output files are provided, and they can be used as follows:

```
python3 mult.py < input_m1.txt > output.txt
diff output.txt expected_m1.txt 
```

Repeat for the other two input/output files. No output from calling `diff` means the files match exactly.
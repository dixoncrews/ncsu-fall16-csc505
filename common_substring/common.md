# common.py

## Problem Statement
Consider the two strings below. The first string has 28 substrings, all of them different. For example “abcd” and “cdef” are both four-character substrings of the first string. The second string has 36 substrings, but some of them are duplicates.

> abcdefg
> cdefabab

Your job is to develop a program (named common.c, common.cpp, common.java or common.py) that counts the number of different strings that are substrings of both of two input strings. For example, “f”, “ab” and “cde” are all substrings of the two strings above. The “ab” substring occurs twice in the second string, but you should only count it once.

Your program will read its input from standard input, one string per line. Input strings will consist of lower-case letters. As output, your program should simply print the number of different strings that are substrings of the two input strings.

__Sample Input__

> abcdefg
> cdefabab

__Sample Output__

> 13

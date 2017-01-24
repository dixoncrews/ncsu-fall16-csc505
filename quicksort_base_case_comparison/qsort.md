# qsort.py

## Problem Statement

In our presentation of quicksort, we assumed the base case was a one-element list. In practice, it may be faster to switch to a different sort when the list size gets small enough, without waiting until it reaches zero. You’re going to write a quicksort program, qsort.c, qsort.cpp, qsort.java or qsort.py, to let us examine this.

Your qsort program will read a sequence of 32-bit numbers form standard input. It will store them in an an array, sort them with quicksort, then print the sorted results to standard output, one value per line.

Your program will take a command-line argument, k. This will tell it when to change sorting strategies. When recursion reaches a list size of k or smaller, your quicksort will just sort the list using insertion sort, bubble sort or selection sort (your choice), rather than continuing to quicksort it recursively. This will let us easily experiment with different trade-off points between quicksort and an asymptotically slower sort that might actually be faster for small enough lists.

### Runtime Reporting

To get quicksort to take enough time to measure, we’re going to need large input lists of numbers, a million items or more. It takes so long to read and print a list of this size, the total execution time of our programs won’t be a good indication of how long they took to perform the sort (especially since all these time measurements will be a little noisy). So, we need to be able to measure the time for just part of our program. We’ll do this by measuring the elapsed time in milliseconds and reporting it to standard error. Using stderr here is nice since it will let us send our programs sorted output to a file (or to /dev/null) and still be able to see the execution time on the terminal.

The way to measure execution time in milliseconds depends on your implementation language. Use code like the following to measure the runtime for just your quicksort and report it in milliseconds to standard error.

## Solution Usage

The solution was written for use with Python 3.x (but will probably work with 2.x). Four input and output files are provided, and they can be used as follows (where 5 is the k-value):

```
python3 qsort.py 5 < input_s10.txt > output.txt
diff output.txt expected_s10.txt 
```

Repeat for the other input/output files. No output from calling `diff` means the files match exactly.
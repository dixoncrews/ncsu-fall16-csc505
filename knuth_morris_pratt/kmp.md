<p align="center">
    **Take me to the [SOLUTION](https://github.com/dixoncrews/ncsu-fall16-csc505/blob/master/knuth_morris_pratt/kmp.py)!**
</p>

# kmp.py

## Problem Statement

Let’s compare string searching algorithms, including the standard string search mechanism for your chosen programming language. Write a program called kmp.c (or kmp.cpp, kmp.java, kmp.py). This will compare the performance of the naive, O(nm) string search algorithm, the KMP string search algorithm and the standard string search technique for your language. We’ll say the standard way of doing a string search is the strstr() function if you’re in C. If you’re programming in C++, we’ll say it’s the find() method on stl::string. In Java, we’ll say it’s the indexOf() method on String, and in Python, we’ll say it’s the find() method on string.

### String Input

Your program will take one optional command-line argument giving the name of a file. This file should contain two lines, the first giving the text you’re supposed to search through (the haystack) and the second containing the pattern your supposed to look for (the needle). So, for example, if the program is run as follows (in python):

```
python kmp.py input_kmp1.txt
```

It will use the first two lines from the file `input_kmp1.txt` as its haystack and needle strings.

If no command-line argument is given, your program should use needle and haystack strings designed by you. Try to choose these strings so that KMP performs noticeably better than the other two string search techniques. These will need to be large strings if we’re going to see a performance difference, so you’ll definitely want to write some looping code to create these strings (rather than just trying to type them in).

For example, running the program like the following should cause it to use the strings you designed (if it’s in Java).

```
java kmp
```

### String Search

In your program, define two of your own functions to perform string searching. The first will be called `naive()`. It will take two parameters, the haystack string then the needle string. The naive algorithm will use the naive, O(nm) algorithm to find the first occurrence of needle in the haystack and return the integer index of the first character of its occurrence. If it doesn’t occur, your function will return -1.

You’ll also implement a function called `kmp()` that takes the same two parameters and returns the same value as `naive()`. Internally, `kmp()` will use the Knuth-Morris-Pratt algorithm to find the needle in the haystack.

### Performance Comparison

When your program is run, it will use all three algorithms to perform the string search. First it will report on the position of the needle reported by `naive()` and the runtime of the naive string search in milliseconds. See the sample execution for the expected output format.

Then, use the standard built-in technique for finding a substring in a large string (described above). Report the position where it finds the needle (or -1) and the running time of this string search.

Finally, use your KMP algorithm to do a string search and report where it finds the substring and how long it takes. For all three techniques, the location where it finds the first occurrence of needle should be the same (but, this will be good to test with), but the runtimes will probably be different.

### Sample Execution

If you run your program as follows (if it’s written in C or C++), it will report the results of the three string search techniques and their runtimes of the sample input file. Here, the input strings are too small for string searching to take more than a millisecond of execution time:

```
$ ./kmp input_kmp1.txt
found at: 60
naive search time: 0
found at: 60
standard search time: 0
found at: 60
kmp search time: 0
```

If you run your program as follows (if it’s written in Java), it will create a large string you designed to try to show a performance advantage for KMP. As you can see, for my program, the needle occurs at position 788124 in the haystack (so, obviously, I’m using large strings). For the strings I created, the built-in string search is faster than my naive solution, but KMP is even faster.

```
$ java kmp
found at: 788124
naive search time: 3401
found at: 788124
standard search time: 524
found at: 788124
kmp search time: 20
```

### Performance Report

In a file called, report.pdf, give a report explaining the strings you used to try to exhibit better performance from KMP compared to the other two string search techniques. Show the output of your program and briefly explain your results and any conclusions you can draw from them. This should take about half a page.

## Solution Usage

The solution was written for use with Python 2.x (but will probably work with 3.x). One input file is provided, and can be used as described in the above write-up. 
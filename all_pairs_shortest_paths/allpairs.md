# allpairs.py

## Problem Statement

You’re going to write a program, allpairs.c (or .cpp, .java, .py). This program will use the Floyd-Warshall algorithm to solve the all-pairs shortest paths problem.

We’ll be working with a graph that’s defined by a collection of words, each word representing a vertex. Words consist of lower-case letters, and there’s an edge between two words if the they have the same length and differ at just one character position. The weight of the edge is how far apart the differing letters are in alphabetic order. So, for example, the words “help” and “yelp” would be connected by an edge of weight 17 (since ’y’ is 17 characters away from ’h’ in the alphabet). There wouldn’t be an edge between “ram” and “arm”; although they contain the same letters, they differ in the first character position and in the second.

For this problem, you can use a dense graph representation if you want. It won’t hurt the storage cost or running time, since the resulting shortest path matrix will be a dense representation.

Your program will read a list of words and compute the shortest path matrix. To help prove you computed the whole matrix, you’ll print a simple statistic based on this matrix. For each word, w_i, compute the number of other words you can reach starting from w_i and traversing edges of the graph (this should require looking at a row of the shortest path matrix). Compute the average number of reachable words, averaged over all words in the list. Print this value rounded to two fractional digits.

Then, your program will respond to a sequence of queries. Each querry will give a pair of words from the list. In response, your program will print out the length of the shortest path from the first word to the second one, followed by the sequence of words on one such shortest path. If there isn’t a path, it will print the two words, followed by “ not reachable”. See the sample execution below for an example.

For each query, there may be multiple equally short paths. Your program can print out any one of them.

If you want, you can use the O(V 2) technique we developed in class for recovering a shortest path. Or, if you’d like 5 points of extra credit, you can implement a linear-time technique instead. To do this, as you fill in the table, keep a record of the value, k that achieves the shortest path between each pair of vertices. Then, when you need to recover a shortest path from some i to j, you can first check to see if there’s a direct edge. If not, you can lookup the vertex k that the path goes through. Then, recursively recover a shortest path from i to k and then from k to j.

### Input

Input will start with a positive integer n, giving the number of words on the list. This will be followed by n words, one per line. Words will consist only of lower-case letters, but they may be of different lengths.

The word list is followed by a non-negative integer, m, giving the number of queries. This will be followed by m lines, each line containing two words from the list.

For example, the first sample input file, input_ap1.txt contains:

```
9
ran
met
mat
rag
ram
hat
set
tag
rap
2
tag rap
set ran
```

## Solution Usage

The solution was written for use with Python 3.x (but will probably work with 2.x). Three input and output files are provided, and they can be used as follows:

```
python3 allpairs.py < input_ap1.txt > output.txt
diff output.txt expected_ap1.txt
```

Repeat for the other input/output files. No output from calling `diff` means the files match exactly. It's unlikely they will match exactly due to the issues discussed above where there may be multiple equally short paths.
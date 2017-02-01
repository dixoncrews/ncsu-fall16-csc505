# maxflow.py

## Problem Statement

You’ll be implementing the Edmonds-Karp algorithm for maximum flow.

### Graph Input

Input will come from standard input and will start with a pair of numbers, n and m, giving the number of vertices and a number of **directed** edges in the graph. These two numbers will be followed by m lines, each describing an edge with 3 integer values. The first two values on each line, i j, give the endpoints of the edge ( i and j in 0 . . . n − 1). The third value gives the non-negative integer weight of the edge from i to j. The value of n will always be two or greater. Vertex zero is always the source and vertex one is always the sink. The graph will never contain anti-parallel edges.

#### Sample Input

```
4 5
0 2 10
0 3 20
2 3 4
2 1 5
3 1 25
```

This describes a graph that looks like:

![Graph 1](https://raw.githubusercontent.com/dixoncrews/ncsu-fall16-csc505/master/max_network_flow/graph1.png "Graph 1")

### Program Output

The output of your program will describe the maximum flow from the source to the sink. First, you will print a line giving the the total value of the maximum flow (the total amount of commodity flowing from source to sink). Then, you will print the list of edges in the same order as in the input. For each edge, give the flow across that edge rather than its capacity. If there are multiple flows that produce the maximum, you can report any of them, as long as the flow you report is one you could get using BFS to find augmenting paths.

#### Sample Output

```
29
0 2 9
0 3 20
2 3 4
2 1 5
3 1 24
```

Along with the graph description above, this describes a flow that looks like:

![Graph 2](https://raw.githubusercontent.com/dixoncrews/ncsu-fall16-csc505/master/max_network_flow/graph2.png "Graph 2")

## Solution Usage

The solution was written for use with Python 3.x (but will probably work with 2.x). Three input and output files are provided, and they can be used as follows:

```
python3 maxflow.py < input_f1.txt > output.txt
diff output.txt expected_f1.txt
```

Repeat for the other input/output files. No output from calling `diff` means the files match exactly.
# dependency.py

## Problem Statement

When you’re teaching a new subject, you often have to think about dependency among the topics you need to cover. For example, it’s probably necessary to understand what a variable declaration is before you start trying to learn about scope, and it’s probably necessary to understand something about types before you can understand a variable declaration. Sometimes, there may be so much dependency that you have some sets of topics that can’t be presented in an order that satisfies the dependency. For example, topic A may require that you first understand B. Topic B may require that you first understand C and C may require that you first understand A. In cases like this, the best you can do is to try to introduce all of the topics at once during the same lecture. Your job is to write a program that finds sets of topics like this and reports them. This way, an instructor can think ahead a bit and try to anticipate lectures that will go a little bit long.

### Input Format

Input will be given on standard input. It will start with a positive integer, n. This gives the number of different topics that need to be covered in the course. The next n lines each give the name of a topic. All topic names are sequences of non-whitespace characters (so they should be easy to parse). The list of topics is followed by a non-negative integer m and a list m of dependencies between pairs of topics. A dependency is given as a pair of course topics where you must understand the first topic before you can understand the second. For example, if a dependency is given as:

```
types declarations
```

it means you have to understand types in order to understand declarations.

### Output

Print out all topic sets, S, where |S| > 1 where the topics in S must all be covered in the same lecture. List topics in each set on a single line, space separated and sorted in the same order they were given in the topic list at the start of the input. List sets of topics sorted by the order their first topic was given in the input.

## Solution Usage

The solution was written for use with Python 3.x (but will probably work with 2.x). Three input and output files are provided, and they can be used as follows:

```
python3 dependency.py < input_d1.txt > output.txt
diff output.txt expected_d1.txt
```

Repeat for the other input/output files. No output from calling `diff` means the files match exactly.
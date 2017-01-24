# mult.py
# Author: Dixon Crews
# CSC 505-001, Fall 2016
# Homework 3, #1

###############################################################################

# Import needed libraries
import sys

###############################################################################

# Define matrixChainOrder() function
# Algorithm taken from our textbook, p. 375
def matrixChainOrder(p):
    # Get n
    n = len(p) - 1
    
    # Define m table
    m = [[0 for x in range(n)] for x in range(n)]
            
    # Define s table
    s = [[0 for x in range(n+1)] for x in range(n+1)]
        
    # Main loop    
    for l in range(2, n+1):
        for i in range(n - l + 1):
            j = i + l - 1
            m[i][j] = sys.maxsize
            for k in range(i, j):
                q = m[i][k] + m[k+1][j] + p[i] * p[k+1] * p[j+1]
                if(q < m[i][j]):
                    m[i][j] = q
                    s[i+1][j+1] = k+1
    
    return m, s

# Define printOptimalParens() function
# Algorithm taken from our textbook, p. 377
# Modified slightly to meet this assignment's specifications
def printOptimalParens(s, i, j):
    if(i == j):
        print("M" + str(i),end="")
    else:
        printOptimalParensHelper(s, i, s[i][j])
        print(" * ",end="")
        printOptimalParensHelper(s, s[i][j] + 1, j)
        print() # print a newline

# Define the printOptimalParensHelper() function
# A helper function to print the parentheses
def printOptimalParensHelper(s, i, j):
    if(i == j):
        print("M" + str(i),end="")
    else:
        print("( ",end="")
        printOptimalParensHelper(s, i, s[i][j])
        print(" * ",end="")
        printOptimalParensHelper(s, s[i][j] + 1, j)
        print(" )",end="")

###############################################################################

# Create a list to store input values
inputList = []

# Read input from stdin
while True:
    try:
        number = int(input())
        inputList.append(number)
    except EOFError:
        break

# Get n from the input list
n = inputList[0]

# Remove n from the list
inputList = inputList[1:]

# Run algorithm, get m and s matrices back
m, s = matrixChainOrder(inputList)

# Print the optimal order
printOptimalParens(s, 1, n)
# allpairs.py
# Author: Dixon Crews
# CSC 505-001, Fall 2016
# Homework 4, #1

###############################################################################

# Import needed library
import sys

###############################################################################

# Define the getPath() function
# Implements the "linear time" extra credit option with ideas from
# https://en.wikipedia.org/wiki/Floyd-Warshall_algorithm#Path_reconstruction
def getPath(n, u, v):
    path = [u]
    while u != v:
        u = n[u][v]
        path.append(u)
    return path

# Define the floyd_warshall() function
# m is the adjacency matrix, n is the next matrix
def floyd_warshall(m, n):
    v = len(m[0])
    
    for i in range(v):
        m[i][i] = 0

    for k in range(v):
        for i in range(v):
            for j in range(v):
                if(m[i][k] + m[k][j] < m[i][j]):
                    m[i][j] = m[i][k] + m[k][j]
                    n[i][j] = n[i][k]
                    
###############################################################################

# Create lists to store input
words = []
queries = []

# Read input from stdin
while True:
    try:
        # Store everything in words list for now
        line = input()
        words.append(line)
    except EOFError:
        break

# Get n and m
n = int(words[0])
m = int(words[n+1])

# Clean up & separate into two lists
queries = words[n+2:]
words = words[1:n+1]

# Create adjacency matrix
adj = [[sys.maxsize for x in range(n)] for x in range(n)]

# Create next matrix
next = [[None for x in range(n)] for x in range(n)]

# Find edges
# For each word in the list
for word in words:    
    # Go through the rest of the words
    for in_word in [x for x in words if x != word]:
        # Check if the length is the same
        if(len(word) == len(in_word)):
            # Get differences
            differences = [i for i in range(len(word)) if word[i] != in_word[i]]
            
            # If different at only 1 character, we have an edge
            if(len(differences) == 1):
                # Compute weight
                weight = ord(word[differences[0]]) - ord(in_word[differences[0]])
                
                # If negative, make positive
                if(weight < 0):
                    weight *= -1
                
                # Insert edge into adjacency matrix
                i = words.index(word)
                j = words.index(in_word)
                adj[i][j] = weight
                adj[j][i] = weight
                
                # Insert into next matrix
                next[i][j] = j
                next[j][i] = i

# Run Floyd-Warshall
floyd_warshall(adj, next)

# Compute "average number of reachable words"
count = 0
for row in adj:
    count += len([x for x in row if x != sys.maxsize])

# Print out result
print(str(round(count/n, 2)))

# Run queries
for query in queries:
    split = query.split(" ")
    i = words.index(split[0])
    j = words.index(split[1])
    
    if(adj[i][j] == sys.maxsize):
        # No path
        print(query + " not reachable")
    else:
        # There is a path, find it
        strToPrint = str(adj[i][j])
        for v in getPath(next, i, j):
            strToPrint += " " + words[v]
        print(strToPrint)
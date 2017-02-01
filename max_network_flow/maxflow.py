# maxflow.py
# Author: Dixon Crews
# CSC 505-001, Fall 2016
# Homework 4, #2

###############################################################################

import sys

###############################################################################

# Define the EdmondsKarp() function
# References: 
# https://en.wikipedia.org/wiki/Edmonds-Karp_algorithm#Pseudocode
# https://brilliant.org/wiki/edmonds-karp-algorithm/
def EdmondsKarp(C, E, s, t):
    # C: Capacity matrix
    # E: Adjacency matrix
    # s: Source (always 0 for this problem)
    # t: Sink (always 1 for this problem)
    
    # Get n
    n = len(C)
    
    # Create a variable to store the max flow in, starts at 0
    f = 0
    
    # Create residual capacity matrix, F
    F = [[0 for x in range(n)] for x in range(n)]
    
    # Main loop, run "forever"
    while True:        
        m, P = bfs(E, C, s, t, F)
        if m == 0:
            break
            
        f += m
        
        v = t
        while v != s:
            u = P[v]
            F[u][v] = F[u][v] + m
            F[v][u] = F[v][u] - m
            v = u
            
    return f, F

# Define the bfs() function
def bfs(C, E, s, t, F):
    # C: Capacity matrix
    # E: Adjacency matrix
    # s: Source (always 0 for this problem)
    # t: Sink (always 1 for this problem)
    # F: Residual capacity matrix
    
    # Get n
    n = len(C)
    
    # Create P list
    P = [-1 for x in range(n)]
    P[s] = -2
    
    # Create M list
    M = [0 for x in range(n)]
    M[s] = sys.maxsize
    
    # Create a BFS queue with the source
    queue = [s]
    
    # Run BFS (taken from Wikipedia pseudocode)
    while (len(queue) > 0):
        u = queue.pop(0)
        for v in E[u]:
            if(C[u][v] - F[u][v] > 0 and P[v] == -1):
                P[v] = u
                M[v] = min(M[u], C[u][v] - F[u][v])
                if v != t:
                    queue.append(v)
                else:
                    return M[t], P
    return 0, P
        
###############################################################################

# Create list to store input
edges = []

# Read input from stdin
while True:
    try:
        # Store everything in edges list
        line = input()
        edges.append(line)
    except EOFError:
        break

# Get n and m
edges0split = edges[0].split(" ")
n = int(edges0split[0])
m = int(edges0split[1])

# Get edges
edges = edges[1:]

# Create adjacency matrix
E = [[] for _ in range(n)]

# Create capacity matrix
C = [[0]*n for _ in range(n)]

# Put edges into matrix
for edge in edges:
    split = edge.split(" ")
    u = int(split[0])
    v = int(split[1])
    capacity = int(split[2])
    
    E[u].append(v)
    C[u][v] = capacity

# Run Edmonds-Karp
maxFlow, F = EdmondsKarp(E, C, 0, 1)

# Print max flow
print(maxFlow)

# Print edges and flows on each edge
for edge in edges:
    split = edge.split(" ")
    print(split[0] + " " + split[1] + " " + str(F[int(split[0])][int(split[1])]))
# dependency.py
# Author: Dixon Crews
# CSC 505-001, Fall 2016
# Homework 3, #4

###############################################################################

# Import needed library
import operator

###############################################################################

# Define the Node class
# Follows the same guidelines as the algorithm from our book,
# giving nodes a color, "pi" which is the predecessor,
# d which is the discovey time, and f which is the finish time.
class Node:
    def __init__(self, value, color=None, pi=None, d=None, f=None):
        self.value = value
        self.adjNodes = []
        self.color = color
        self.pi = pi
        self.d = d
        self.f = f
        
###############################################################################

# Define the transpose() function
# This function reverses the directed edges in the given graph
def transpose(graph):
    # List of tuples representing edges
    # (a,b) = directed edge from a to b
    edges = []
    
    # Get all edges, then clear adjacency lists
    for node in graph:
        nodeObj = graph[node]
        for edge in nodeObj.adjNodes:
            edges.append((node,edge))
            
        nodeObj.adjNodes.clear()
        
    # Re-add all edges in reverse
    for edge in edges:
        graph[edge[1]].adjNodes.append(edge[0])

# Define the scc_dfs() function
# This function is used when finding SCCs, it uses the 
# reverseFinishingTime parameter to look at the vertices
# in that order. Follows the algorithm from our book, p. 604
def scc_dfs(graph, reverseFinishingTime):
    # Color every node white, predecessor = none
    for node in graph:
        graph[node].color = "white"
        graph[node].pi = None
    
    # Declare the global time variable, set to 0
    global time
    time = 0
    
    # List to hold our components
    components = []
    
    # Consider nodes in reverse finishing time
    for node in reverseFinishingTime:
        if(graph[node].color == "white"):
            # Visit node
            dfs_visit(graph, graph[node])
            
            # Get new components, add to our list
            # comp is a set of new components
            # This is not a super efficient way to do this,
            # but it works.
            comp = set()
            for item in graph:
                if(graph[item].color == "black"):
                    comp.add(item)
            
            # Don't include items we already found
            for item in components:
                comp = comp - item
            
            # Add the new components
            components.append(comp)
    
    return components

# Define the dfs() function
# Follows algorithm from p. 604 of textbook
def dfs(graph):
    for node in graph:
        graph[node].color = "white"
        graph[node].pi = None
        
    global time
    time = 0
    
    for node in graph:
        if(graph[node].color == "white"):
            dfs_visit(graph, graph[node])

# Define the dvs_visit() function
# Follows algorithm from p. 604 of textbook
def dfs_visit(graph, node):
    global time
    time += 1
    
    node.d = time
    node.color = "gray"
    
    for edge in node.adjNodes:
        if(graph[edge].color == "white"):
            graph[edge].pi = node.value
            dfs_visit(graph, graph[edge])
            
    node.color = "black"
    time = time + 1
    node.f = time

###############################################################################

# Create lists to store topics, dependencies
topics = []
dependencies = []

# Read input from stdin
while True:
    try:
        # Store everything in topics list for now
        line = input()
        topics.append(line)
    except EOFError:
        break

# Get n and m
n = int(topics[0])
m = int(topics[n+1])

# Clean up lists, separate into two lists
dependencies = topics[n+2:]
topics = topics[1:n+1]

# Store graph as dictionary
# keys = topic, value = Node object
graph = {}

# Add topics to dictionary
for item in topics:
    graph[item] = Node(item)

# Create edges in graph
for item in dependencies:
    split = item.split(" ")
    graph[split[0]].adjNodes.append(split[1])

# Call dfs()
dfs(graph)

# Call transpose(), reverse edges
transpose(graph)

# Get nodes in order of reverse finishing time
reverseFinishingTime = []

# Add to list as a tuple
# (topic, finishing time)
for node in graph:
    reverseFinishingTime.append((graph[node].value,graph[node].f))
    
# Sort in reverse order by finishing time
reverseFinishingTime.sort(key=operator.itemgetter(1), reverse=True)

# Get rid of finishing times in tuple
reverseFinishingTime = [x[0] for x in reverseFinishingTime]

# Call scc_dfs()
components = scc_dfs(graph, reverseFinishingTime)

# Find the strongly connected components in our components list
scc = []

for comp in components:
    # |S| > 1 condition
    if(len(comp) > 1):
        # Need to sort by order the topics appeared in input
        temp = []
        for item in comp:
            temp.append((item,topics.index(item)))
        temp.sort(key=operator.itemgetter(1))
        temp = [x[0] for x in temp]
        scc.append(temp)

# Sort first elements of SCC by order they appeared in input
scc2 = []
for item in scc:
    scc2.append((item,topics.index(item[0])))
scc2.sort(key=operator.itemgetter(1))
scc2 = [x[0] for x in scc2]

# And finally, print out!
for item in scc2:
    print(" ".join(item))
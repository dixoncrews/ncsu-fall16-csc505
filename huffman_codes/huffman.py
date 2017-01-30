# huffman.py
# Author: Dixon Crews
# CSC 505-001, Fall 2016
# Homework 3, #5

###############################################################################

# Import needed libraries
import math, sys, binascii

###############################################################################

# Node class
class Node():
    left = None
    right = None
    value = None
    freq = 0
    
    def __init__(self, v, f):
        self.value = v
        self.freq = f

###############################################################################

# Define the huffman() function
def huffman(h):
    # Algorithm from textbook, p. 431
    while len(h) > 1:
        # Get two smallest nodes
        x = heapRemoveMin(h)
        y = heapRemoveMin(h)
        
        # Create a new node with the sum of frequencies
        z = Node(None, x.freq + y.freq)
        
        # Set z.left and z.right to x and y
        z.left = x
        z.right = y
        
        # Re-insert to heap
        heapInsert(h, z)
    
    # Get codes
    # Code adapted from
    # http://www.techrepublic.com/article/huffman-coding-in-python/
    codes = {}
    
    def getCodes(s, node):
        if(node.value):
            if(not s):
                codes[node.value] = "0"
            else:
                codes[node.value] = s
        else:
            getCodes(s + "0", node.left)
            getCodes(s + "1", node.right)
        
    getCodes("", h[0])
    
    return codes

# Tri-nary heap functions
# Define the parent() function
def parent(i):
    return math.floor((i-1)/3)

# Define the left() function
def left(i):
    return (3*i + 1)

# Define the middle() function
def middle(i):
    return (3*i + 2)

# Define the right() function
def right(i):
    return (3*i + 3)
    
# Define the minChild() function
def minChild(arr, i):
    # Store some needed values
    length = len(arr)
    leftIdx = left(i)
    middleIdx = middle(i)
    rightIdx = right(i)
    
    # Create boolean indicators for each child
    hasLeft = (leftIdx < length)
    hasMiddle = (middleIdx < length)
    hasRight = (rightIdx < length)
    
    # Need to find the minimum child to swap with
    # Start at the left child
    if(hasLeft):
        minVal, minIdx = arr[leftIdx].freq, leftIdx
        
        # Check middle (if exists)
        if(hasMiddle):
            if(arr[middleIdx].freq < minVal):
                minVal, minIdx = arr[middleIdx].freq, middleIdx
            
            # Check right (if exists)
            if(hasRight):
                if(arr[rightIdx].freq < minVal):
                    minVal, minIdx = arr[rightIdx].freq, rightIdx
        
        return minIdx
    else:
        return 0

# Define the percolateUp() function
def percolateUp(arr, i):
    while i > 0 and arr[parent(i)].freq > arr[i].freq:
        arr[parent(i)], arr[i] = arr[i], arr[parent(i)]
        i = parent(i)

# Define the percolateDown() function
def percolateDown(arr, i):
    # Find the index of the minimum child (if any, 0 if none)
    minIdx = minChild(arr, i)
    
    # Go through the array and swap if needed
    while minIdx != 0 and arr[i].freq > arr[minIdx].freq:
        # Swap
        arr[i], arr[minIdx] = arr[minIdx], arr[i]
        
        # Re-assign i to be the index we swapped to
        i = minIdx
        
        # Find the next minimum child
        minIdx = minChild(arr, minIdx)
    
# Define the heapInsert() function
def heapInsert(arr, value):
    # Insert new element at the last position in the array
    arr.append(value)
    
    # Move the item into the correct position until the heap
    # order property is satisfied
    percolateUp(arr, len(arr) - 1)

# Define the heapRemoveMin() function
def heapRemoveMin(arr):
    # Check size
    if(len(arr) == 0):
        return None
        
    # Store root in temporary variable
    root = arr[0]
    
    # Move last element to root position
    arr[0] = arr[len(arr) - 1]
    
    # Delete last element from heap
    del arr[len(arr) - 1]
        
    # Move the root item into the correct position until the
    # heap order property is satisfied
    percolateDown(arr, 0)
    
    return root

###############################################################################

# Generate all of the hex values from 0 to 255
# and store them in a dictionary with 1 as the value
hexDict = {}
for hexValue in [hex(x)[2:].zfill(2) for x in range(256)]:
    hexDict[hexValue] = 1

# Create a dictionary to hold input 
inputDict = {}

# Read input from stdin
while 1:
    # Read 1 byte
    data = sys.stdin.buffer.read(1)
    
    # If we didn't get anything, we're at EOF
    if(not data):
        break
    
    # Increment count or add to the dictionary if new
    if(data in inputDict):
        inputDict[data] += 1
    else:
        inputDict[data] = 1

# Go through the input values we saw and update their counts in hexDict
for item in inputDict:
    hexDict[binascii.hexlify(item).decode('ascii')] = inputDict[item] + 1

# Add special EOF
hexDict['EOF'] = 1

# Insert into heap
heap = []
for item in hexDict:
    heapInsert(heap, Node(item, hexDict[item]))

# Find Huffman codes
huff = huffman(heap)

# Print out codes
for item in sorted(huff):
    if(item >= '21' and item <= '7e'):
        print('{:>3} {}'.format(binascii.unhexlify(item).decode("utf-8"), huff[item]))
    elif(item != 'EOF'):
        print('{:>3} {}'.format(item.upper(), huff[item]))

print('EOF', huff['EOF'])
# heap3.py
# Author: Dixon Crews
# CSC 505-001, Fall 2016
# Homework 2, #2

###############################################################################

# Import needed libraries
import math

###############################################################################

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
        minVal, minIdx = arr[leftIdx], leftIdx
        
        # Check middle (if exists)
        if(hasMiddle):
            if(arr[middleIdx] < minVal):
                minVal, minIdx = arr[middleIdx], middleIdx
            
            # Check right (if exists)
            if(hasRight):
                if(arr[rightIdx] < minVal):
                    minVal, minIdx = arr[rightIdx], rightIdx
        
        return minIdx
    else:
        return 0

# Define the percolateUp() function
def percolateUp(arr, i):
    while i > 0 and arr[parent(i)] > arr[i]:
        arr[parent(i)], arr[i] = arr[i], arr[parent(i)]
        i = parent(i)

# Define the percolateDown() function
def percolateDown(arr, i):
    # Find the index of the minimum child (if any, 0 if none)
    minIdx = minChild(arr, i)
    
    # Go through the array and swap if needed
    while minIdx != 0 and arr[i] > arr[minIdx]:
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

# define the heapRemoveMin() function
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

# Create heap list
heap = []

#Read commands from stdin
while True:
    try:
        command = input()
        if(command.startswith("add")):
            heapInsert(heap, int(command.split(" ")[1]))
        else:
            print(heapRemoveMin(heap))
    except EOFError:
        break

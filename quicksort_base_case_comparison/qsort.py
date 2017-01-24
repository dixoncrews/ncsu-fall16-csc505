# qsort.py
# Author: Dixon Crews
# CSC 505-001, Fall 2016
# Homework 2, #4

###############################################################################

# Import needed libraries
import time, sys

###############################################################################

# Define the getMilliseconds() function
def getMilliseconds():
    return int(round(time.time() * 1000))
    
# Define the selectionSort() function
def selectionSort(inputList):
    # Loop over whole list
    for idx in range(0, len(inputList)):
        # Set our minimum index to this index
        minIdx = idx
        
        # Loop over the rest of the list looking for a new minIdx
        for iidx in range(idx + 1, len(inputList)):
            if(inputList[iidx] < inputList[minIdx]):
                # Found a new minIdx
                minIdx = iidx
        
        # If we found a new min, swap the two values
        if minIdx != idx:
            inputList[minIdx], inputList[idx] = inputList[idx], inputList[minIdx]
    
    return inputList

# Define the qSort() function
def qSort(inputList, k):
    # Base case check
    if(len(inputList) <= k):
        if(k > 1):
            return selectionSort(inputList)
        else:
            return inputList
    else:
        # Create less, pivot, and more lists
        less = []
        pivot = []
        more = []
        
        # Pick the pivot as the last value in the list
        p = inputList[len(inputList)-1]
        
        # Go through the list, checking each value
        for i in inputList:
            if i < p:
                less.append(i)
            elif i > p:
                more.append(i)
            else:
                pivot.append(i)
        
        # Recursively qSort the less and more lists
        less = qSort(less, k)
        more = qSort(more, k)
        
        # Return the less, pivot, and more lists
        return less + pivot + more

###############################################################################

# Check command line argument
if(len(sys.argv) != 2):
    print("usage: python qsort.py <k>")
    exit(1)

# Get k
k = int(sys.argv[1])

# Create input list
inputList = []

# Read input list from stdin
while True:
    try:
        num = int(input())
        inputList.append(num)
    except EOFError:
        break

# Quicksort the list
t0 = getMilliseconds()
sortedList = qSort(inputList, k)
t1 = getMilliseconds()

# Print out the sorted list one number per line
for num in sortedList:
    print(num)

sys.stderr.write("%d\n" % (t1 - t0))
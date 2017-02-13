# kmp.py
# Author: Dixon Crews
# CSC 505-001, Fall 2016
# Homework 5, #2

###############################################################################

# Import needed modules
import sys, datetime, random, string

###############################################################################

# Define the genHaystackNeedle() function
# Uses randomness to generate a haystack and needle
def genHaystackNeedle():
    finalLen = 10000000 # Haystack length (approx)
    seqLen = 500 # Needle length
    maxJumpLen = 10000 # Max length of random characters to add
    
    # Get a random character sequence to be our needle
    needle = ''.join(random.choice(string.ascii_lowercase) for x in range(seqLen))
    
    # Generate haystack
    i = 0
    haystack = ""
    # Loop
    while i < finalLen:
        # Get a random length of random characters between 0 and maxJumpLen
        r = random.randint(0,maxJumpLen)
        
        # Add to haystack
        haystack += ''.join(random.choice(string.ascii_lowercase) for x in range(r))
        
        # Get a random number between 0 and 99 inclusive
        z = random.randint(0,99)
        
        # If z <= 29, add a piece of the needle to the haystack
        if(z <= 29):
            a = random.randint(0, seqLen/2)
            b = random.randint((seqLen/2) + 1, seqLen)
            haystack += needle[a:b]
            i += r + len(needle[a:b])
        elif(z == 99):
            # If z == 99, add the whole needle
            haystack += needle
            i += r + len(needle)
        else:
            # Otherwise just add the length of the random characters
            i += r
    
    return haystack, needle

# Define the naive() function
# Implements the O(nm) algorithm for string matching
def naive(haystack, needle):
    n = len(haystack)
    m = len(needle)
    
    # Outer loop
    for i in range(n - m + 1):
        for j in range(m):
            if(haystack[i+j] != needle[j]):
                break
        if(j == m-1):
            return i # Match found, return
    
    return -1 # Match not found, return -1

# Define the kmp_table() function
# Uses pseudocode from 
# https://en.wikipedia.org/wiki/Knuth-Morris-Pratt_algorithm
def kmp_table(needle):
    pos = 2
    cnd = 0
    T = [0 for x in range(len(needle))]
    
    T[0] = -1
    T[1] = 0
    
    while pos < len(needle):
        if(needle[pos - 1] == needle[cnd]):
            T[pos] = cnd + 1
            cnd += 1
            pos += 1
        elif(cnd > 0):
            cnd = T[cnd]
            T[pos] = 0
        else:
            T[pos] = 0
            pos += 1
            
    return T
    
# Define the kmp() function
# Uses pseudocode from 
# https://en.wikipedia.org/wiki/Knuth-Morris-Pratt_algorithm
def kmp(haystack, needle):
    m = 0
    i = 0
    t = kmp_table(needle)
    
    while m + i < len(haystack):
        if(needle[i] == haystack[m + i]):
            if(i == len(needle) - 1):
                return m
            i += 1
        else:
            if(t[i] > -1):
                m  = m + i - t[i]
                i = t[i]
            else:
                m += 1
                i = 0
    
    return -1

###############################################################################

# Check for command line arguments
cmd = True if len(sys.argv) > 1 else False

# Check if we're using arguments or not
if(cmd):
    # Read first two lines of file
    with open(sys.argv[1]) as f:
        content = [x.strip('\n') for x in f.readlines()]
    haystack = content[0]
    needle = content[1]
else:
    # Default haystack and needle
    haystack, needle = genHaystackNeedle()

# Run naive
t1 = datetime.datetime.now()
naiveResult = naive(haystack, needle)
t2 = datetime.datetime.now()

# Run built-in find()
t3 = datetime.datetime.now()
builtInResult = haystack.find(needle)
t4 = datetime.datetime.now()

# Run KMP
t5 = datetime.datetime.now()
kmpResult = kmp(haystack, needle)
t6 = datetime.datetime.now()

# Print results
print("found at: " + str(naiveResult))
print(int(round((t2 - t1).microseconds / 1000.0)))
print("found at: " + str(builtInResult))
print(int(round((t4 - t3).microseconds / 1000.0)))
print("found at: " + str(kmpResult))
print(int(round((t6 - t5).microseconds / 1000.0)))
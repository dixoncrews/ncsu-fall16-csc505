# common.py
# Author: Dixon Crews
# CSC 505-001, Fall 2016
# Homework 1, #6

# Function that returns a set() of all unique substrings of a string
def get_substrings(string):
    toReturn = set()
    for idx, char in enumerate(string):
        toReturn.add(char)
        
        for c in string[idx+1:]:
            char += c
            toReturn.add(char)
    
    return toReturn

# Collect two strings from standard input
string1 = raw_input()
string2 = raw_input()

# Call the function to get substrings
string1_substr = get_substrings(string1)
string2_substr = get_substrings(string2)

# Find number of different strings that are substrings of both input strings
# using set intersection
# https://docs.python.org/3/library/stdtypes.html#set.intersection
print len(string1_substr & string2_substr)

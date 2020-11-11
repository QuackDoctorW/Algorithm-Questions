# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 18:48:31 2020

@author: manyu
"""

from collections import defaultdict
#question find the largest substring between 2 lists
#creating input from random numbers
from random import randint
original = []
compare = []

count = 0
while count <20:
    original.append(randint(0,9))
    compare.append(randint(0,9))
    count+=1
  
print(len(original),original)
print(len(compare),compare)


# This part below is the solution
#logic is get index of an element of list from compare
#that list can be mapped to original
#look for consecutive chain in original, extend or remove, or start new 
#track the length and last index to look for longest
def check(original,compare):
    #setup indexdict
    original.append("END")  
    indexdict = defaultdict(set)
    for i in range(len(compare)):
        indexdict[compare[i]].add(i)
    best = (0,0) #(length,ending index)
    checks = defaultdict(list)
    for firstindex in indexdict[original[0]]:
        checks[firstindex+1].append(1)
    #test links    
    for indexlist in original[1:]:
        new = defaultdict(list)
        for check in checks:
            if check not in indexdict[indexlist]:
                for length in checks[check]:
                    if best[0] < length:
                        best = (length,check-1)
            else:
                for i in checks[check]:
                    new[check+1].append(i+1)
        checks = new
        for index in indexdict[indexlist]:
            if index not in checks:
                checks[index+1].append(1)  
    return compare[best[1]-best[0]+1:best[1]+1]

print(check(compare,original))
        
#testing
test_cases = [
  # No common subsequence
  ("abc", "def", ""),
  # Common subsequence of length 1
  ("abc", "cde", "c"),
  # Identical inputs
  ("abc", "abc", "abc"),
  # Identica input with repeating letter
  ("aaaaa", "aaaaa", "aaaaa"),
  # Lots of letter repetition
  ("aaabaabaaababa", "baaabaabaaaaba", "aaabaabaaa"),
  # Semi-repetitive subsequence
  ("ababacd", "babacd", "babacd"),
]

def run_tests(funct, test_casesyb):
    print(f"Testing {funct.__name__}:")
    all_pass = True
    for A,B,expected in test_cases:
      actual = funct(list(A),list(B))
      expected = list(expected)
      if actual != expected:
        print(f"Warning: A={A},B={B}, expected {expected} but was {actual}")
        all_pass = False
    if all_pass:
      print("Passed all test cases!")

run_tests(check, test_cases)



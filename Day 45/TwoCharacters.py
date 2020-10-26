'''

n this challenge, you will be given a string. You must remove characters until the string is made up of any two alternating characters. When you choose a character to remove, all instances of that character must be removed. Your goal is to create the longest string possible that contains just two alternating letters.

As an example, consider the string abaacdabd. If you delete the character a, you will be left with the string bcdbd. Now, removing the character c leaves you with a valid string bdbd having a length of 4. Removing either b or d at any point would not result in a valid string.

Given a string , convert it to the longest possible string  made up only of alternating characters. Print the length of string  on a new line. If no string  can be formed, print  instead.

Function Description

Complete the alternate function in the editor below. It should return an integer that denotes the longest string that can be formed, or  if it cannot be done.

alternate has the following parameter(s):

s: a string
Input Format

The first line contains a single integer denoting the length of .
The second line contains string .

Constraints

Output Format

Print a single integer denoting the maximum length of  for the given ; if it is not possible to form string , print  instead.

Sample Input

10
beabeefeab
Sample Output

5

'''

#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import combinations

def alternate(s):
    if len(s) <= 1:
        return 0
    
    # unique set of characters
    unique = set(s)
    longest = 0
    
    # find all possible pairs
    for pair in combinations(unique, 2):
        matches = [c for c in s if c in pair]
        # check if matched string alternates
        if all(c1 != c2 for c1, c2 in zip(matches, matches[1:])):
            longest = max(longest, len(matches))
    
    return longest

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input().strip())

    s = input()

    result = alternate(s)

    fptr.write(str(result) + '\n')

    fptr.close()

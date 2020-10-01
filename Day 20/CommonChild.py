'''

A string is said to be a child of a another string if it can be formed by deleting 0 or more characters from the other string. Given two strings of equal length, what's the longest string that can be constructed such that it is a child of both?
For example, ABCD and ABDC have two children with maximum length 3, ABC and ABD. They can be formed by eliminating either the D or C from both strings. Note that we will not consider ABCD as a common child because we can't rearrange characters and ABCD  ABDC.

Function Description

Complete the commonChild function in the editor below. It should return the longest string which is a common child of the input strings.
commonChild has the following parameter(s):
s1, s2: two equal length strings

Input Format
There is one line with two space-separated strings,  and .

Constraints
All characters are upper case in the range ascii[A-Z].

Output Format
Print the length of the longest string , such that  is a child of both  and .

Sample Input
HARRY
SALLY

Sample Output
2

'''
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the commonChild function below.
def commonChild(s1, s2):
    prev = [0] * (len(s2)+1)
    curr = [0] * (len(s2)+1)

    for r in s1:
        for j, c in enumerate(s2, 1):
            curr[j] = prev[j-1] + 1 if r == c else max(prev[j], curr[j-1])
        prev, curr = curr,prev

    return prev[-1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = commonChild(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()

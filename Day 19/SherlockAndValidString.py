'''
Sherlock considers a string to be valid if all characters of the string appear the same number of times. It is also valid if he can remove just  character at  index in the string, and the remaining characters will occur the same number of times. Given a string , determine if it is valid. If so, return YES, otherwise return NO.
For example, if , it is a valid string because frequencies are . So is  because we can remove one  and have  of each character in the remaining string. If  however, the string is not valid as we can only remove  occurrence of . That would leave character frequencies of .

Function Description
Complete the isValid function in the editor below. It should return either the string YES or the string NO.
isValid has the following parameter(s):
s: a string

Input Format
A single string .
 
Output Format
Print YES if string  is valid, otherwise, print NO.

Sample Input 0
aabbcd

Sample Output 0
NO
'''

#!/bin/python3

import math
import os
import random
import re
import sys

from collections import Counter
def isValid(s):

    C = Counter(s) ; V = list(C.values())
    F = Counter(V)
        
    if len(F) == 1 : return "YES"
    if len(F) > 2 : return "NO"

    if F[1] == 1 : return "YES"
    m, M = min(V), max(V)
    return "YES" if F[M] == 1 and M == m+1 else "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()

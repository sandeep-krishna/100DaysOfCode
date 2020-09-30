'''
A string is said to be a special string if either of two conditions is met:

All of the characters are the same, e.g. aaa.
All characters except the middle one are the same, e.g. aadaa.
A special substring is any substring of a string which meets one of those criteria. Given a string, determine how many special substrings can be formed from it.

For example, given the string , we have the following special substrings: .

Function Description
Complete the substrCount function in the editor below. It should return an integer representing the number of special substrings that can be formed from the given string.
substrCount has the following parameter(s):
n: an integer, the length of string s
s: a string

Input Format
The first line contains an integer, , the length of .
The second line contains the string .
Each character of the string is a lowercase alphabet, .

Output Format
Print a single line containing the count of total special substrings.

Sample Input 0
5
asasd

Sample Output 0
7 

'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the substrCount function below.
def substrCount(n, s):
    count = n
    for x in range(n): 
        y = x
        while y < n - 1:
            y += 1
            if s[x] == s[y]:
                count += 1
            else:
                if s[x:y] == s[y+1:2*y-x+1]:
                    count += 1
                break

    return count
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = substrCount(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()

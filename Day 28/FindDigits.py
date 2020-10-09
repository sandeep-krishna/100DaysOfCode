'''
An integer d is a divisor of an integer  if the remainder of n/d=0 .
Given an integer, for each digit that makes up the integer determine whether it is a divisor. Count the number of divisors occurring within the integer.
Note: Each digit is considered to be unique, so each occurrence of the same digit should be counted (e.g. for ,  is a divisor of  each time it occurs so the answer is ).

Function Description
Complete the findDigits function in the editor below. It should return an integer representing the number of digits of  that are divisors of .

findDigits has the following parameter(s):
n: an integer to analyze

Input Format
The first line is an integer, , indicating the number of test cases.
The  subsequent lines each contain an integer, .

Output Format
For every test case, count the number of digits in  that are divisors of . Print each answer on a new line.

Sample Input
2
12
1012

Sample Output
2
3

'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the findDigits function below.
def findDigits(N):
    return sum(d != 0 and N % d == 0 for d in map(int, str(N)))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = findDigits(n)

        fptr.write(str(result) + '\n')

    fptr.close()

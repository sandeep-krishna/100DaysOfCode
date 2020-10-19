'''
Given a set of distinct integers, print the size of a maximal subset of  where the sum of any  numbers in  is not evenly divisible by .
For example, the array  and . One of the arrays that can be created is . Another is . After testing all permutations, the maximum length solution array has  elements.
Function Description
Complete the nonDivisibleSubset function in the editor below. It should return an integer representing the length of the longest subset of  meeting the criteria.
nonDivisibleSubset has the following parameter(s):
S: an array of integers
k: an integer

Input Format
The first line contains  space-separated integers,  and , the number of values in  and the non factor.
The second line contains  space-separated integers describing , the unique values of the set.

Constraints
All of the given numbers are distinct.

Output Format
Print the size of the largest possible subset ().

Sample Input
4 3
1 7 2 4

Sample Output
3

'''


#!/bin/python3

import math
import os
import random
import re
import sys


def nonDivisibleSubset(k, S):
    res = [0 for i in range (0, k)]
    for i in S:
        res[i%k] += 1
    maxN = 1 if res[0]>0 else 0
    for i in range(1,k//2+1):
        if (i != k-i):
            maxN += max(res[i],res[k-i])
        else:
            maxN += 1
    return maxN

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)

    fptr.write(str(result) + '\n')

    fptr.close()

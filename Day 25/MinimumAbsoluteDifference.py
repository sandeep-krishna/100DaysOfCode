'''
Consider an array of integers, . We define the absolute difference between two elements,  and  (where ), to be the absolute value of .
Given an array of integers, find and print the minimum absolute difference between any two elements in the array. For example, given the array  we can create  pairs of numbers:  and . The absolute differences for these pairs are ,  and . The minimum absolute difference is .

Function Description
Complete the minimumAbsoluteDifference function in the editor below. It should return an integer that represents the minimum absolute difference between any pair of elements.
minimumAbsoluteDifference has the following parameter(s):
n: an integer that represents the length of arr
arr: an array of integers

Input Format
The first line contains a single integer , the size of .
The second line contains  space-separated integers .

Output Format
Print the minimum absolute difference between any two elements in the array.

Sample Input 0
3
3 -7 0

Sample Output 0
3
'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumAbsoluteDifference function below.
def minimumAbsoluteDifference(arr):
    if len(set(arr)) < len(arr):
        return 0
    a = sorted(arr)
    n = []
    for i,x in enumerate(arr[:-1]):
        s = abs(a[i+1]-a[i])
        n.append(s)
    return min(n)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

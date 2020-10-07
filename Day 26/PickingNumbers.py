'''
Given an array of integers, find the longest subarray where the absolute difference between any two elements is less than or equal to .

Function Description

Complete the pickingNumbers function in the editor below.
pickingNumbers has the following parameter(s):
int a[n]: an array of integers
Returns
Hint: the length of the longest subarray that meets the criterion

Input Format
The first line contains a single integer , the size of the array .
The second line contains  space-separated integers, each an .

Sample Input 0
6
4 6 5 3 3 1

Sample Output 0
3
'''

#!/bin/python3

import math
import os
import random
import re
import sys

def pickingNumbers(l):
    maximum=0
    for i in l:
        c=l.count(i)
        d=l.count(i-1)
        c=c+d
        if c > maximum:
            maximum=c
    return(maximum)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()

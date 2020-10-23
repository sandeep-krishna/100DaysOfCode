'''

Manasa is out on a hike with friends. She finds a trail of stones with numbers on them. She starts following the trail and notices that any two consecutive stones' numbers differ by one of two values. Legend has it that there is a treasure trove at the end of the trail. If Manasa can guess the value of the last stone, the treasure will be hers.

For example, assume she finds  stones and their differences are  or . We know she starts with a  stone not included in her count. The permutations of differences for the two stones would be  or . Looking at each scenario, stones might have  or  on them. The last stone might have any of , or  on its face.

Compute all possible numbers that might occur on the last stone given a starting stone with a  on it, a number of additional stones found, and the possible differences between consecutive stones. Order the list ascending.

Function Description

Complete the stones function in the editor below. It should return an array of integers representing all possible values of the last stone, sorted ascending.

stones has the following parameter(s):

n: an integer, the number of non-zero stones
a: one possible integer difference
b: another possible integer difference
Input Format

The first line contains an integer , the number of test cases.

Each test case contains  lines:
- The first line contains , the number of non-zero stones found.
- The second line contains , one possible difference
- The third line contains , the other possible difference.

Constraints

Output Format

Space-separated list of numbers which are the possible values of the last stone in increasing order.

Sample Input

2
3 
1
2
4
10
100
Sample Output

2 3 4 
30 120 210 300 

'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the stones function below.
def stones(n, a, b):
    return sorted(set([a*i+b*(n-1-i) for i in range(n)]))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input())

    for T_itr in range(T):
        n = int(input())

        a = int(input())

        b = int(input())

        result = stones(n, a, b)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()

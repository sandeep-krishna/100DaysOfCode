'''
The Utopian Tree goes through 2 cycles of growth every year. Each spring, it doubles in height. Each summer, its height increases by 1 meter.
A Utopian Tree sapling with a height of 1 meter is planted at the onset of spring. How tall will the tree be after  growth cycles?
For example, if the number of growth cycles is , the calculations are as follows:

Period  Height
0          1
1          2
2          3
3          6
4          7
5          14

Function Description
Complete the utopianTree function in the editor below.
utopianTree has the following parameter(s):
int n: the number of growth cycles to simulate
Returns
int: the height of the tree after the given number of cycles

Input Format
The first line contains an integer, , the number of test cases.
 subsequent lines each contain an integer, , the number of cycles for that test case.

Sample Input
3
0
1
4

Sample Output
1
2
7

'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the utopianTree function below.
def utopianTree(n):
    if n < 3:
        return n + 1
    if n % 2 == 0:
        return (utopianTree(n - 2) * 2) + 1
    else:
        return (utopianTree(n - 2) + 1) * 2

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = utopianTree(n)

        fptr.write(str(result) + '\n')

    fptr.close()

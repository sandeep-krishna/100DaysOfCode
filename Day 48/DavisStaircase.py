'''

Davis has a number of staircases in his house and he likes to climb each staircase , , or  steps at a time. Being a very precocious child, he wonders how many ways there are to reach the top of the staircase.
Given the respective heights for each of the  staircases in his house, find and print the number of ways he can climb each staircase, module  on a new line.
For example, there is  staircase in the house that is  steps high. Davis can step on the following sequences of steps:

1 1 1 1 1
1 1 1 2
1 1 2 1 
1 2 1 1
2 1 1 1
1 2 2
2 2 1
2 1 2
1 1 3
1 3 1
3 1 1
2 3
3 2
There are  possible ways he can take these  steps. 

Function Description
Complete the stepPerms function in the editor below. It should recursively calculate and return the integer number of ways Davis can climb the staircase, modulo 10000000007.
stepPerms has the following parameter(s):
n: an integer, the number of stairs in the staircase

Input Format
The first line contains a single integer, , the number of staircases in his house.
Each of the following  lines contains a single integer, , the height of staircase .


Output Format
For each staircase, return the number of ways Davis can climb it as an integer.

Sample Input
3
1
3
7

Sample Output
1
4
44

'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the stepPerms function below.
def stepPerms(n):
    f1, f2, f3 = 1, 2, 4
    for i in range(n-1):
        f1, f2, f3 = f2, f3, f1 + f2 + f3
    return f1
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = int(input())

    for s_itr in range(s):
        n = int(input())

        res = stepPerms(n)

        fptr.write(str(res) + '\n')

    fptr.close()

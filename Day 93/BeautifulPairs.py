'''

You are given two arrays,  and , both containing  integers.
A pair of indices  is beautiful if the  element of array  is equal to the  element of array . In other words, pair  is beautiful if and only if . A set containing beautiful pairs is called a beautiful set.
A beautiful set is called pairwise disjoint if for every pair  belonging to the set there is no repetition of either  or  values. For instance, if  and  the beautiful set  is not pairwise disjoint as there is a repetition of , that is .
Your task is to change exactly  element in  so that the size of the pairwise disjoint beautiful set is maximum.

Function Description
Complete the beautifulPairs function in the editor below. It should return an integer that represents the maximum number of pairwise disjoint beautiful pairs that can be formed.
beautifulPairs has the following parameters:
A: an array of integers
B: an array of integers

Input Format
The first line contains a single integer , the number of elements in  and .
The second line contains  space-separated integers .
The third line contains  space-separated integers .

Output Format
Determine and print the maximum possible number of pairwise disjoint beautiful pairs.
Note: You must first change  element in , and your choice of element must be optimal.

Sample Input 0
4
1 2 3 4
1 2 3 3

Sample Output 0
4


'''



#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulPairs function below.
def beautifulPairs(A, B):
    n=0
    for i in A:
        if i in B:
            B.remove(i)
            n+=1
    if n<len(A):
        return n+1
    else:
        return n-1
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    A = list(map(int, input().rstrip().split()))

    B = list(map(int, input().rstrip().split()))

    result = beautifulPairs(A, B)

    fptr.write(str(result) + '\n')

    fptr.close()

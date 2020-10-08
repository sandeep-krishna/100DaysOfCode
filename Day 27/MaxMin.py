'''
You will be given a list of integers, , and a single integer . You must create an array of length  from elements of  such that its unfairness is minimized. Call that array . Unfairness of an array is calculated as

Where:
- max denotes the largest integer in 
- min denotes the smallest integer in 

As an example, consider the array  with a  of . Pick any two elements, test .

Testing for all pairs, the solution  provides the minimum unfairness.
Note: Integers in  may not be unique.
Function Description
Complete the maxMin function in the editor below. It must return an integer that denotes the minimum possible value of unfairness.
maxMin has the following parameter(s):
k: an integer, the number of elements in the array to create
arr: an array of integers .

Input Format
The first line contains an integer , the number of elements in array .
The second line contains an integer .
Each of the next  lines contains an integer  where .

Output Format
An integer that denotes the minimum possible value of unfairness.

Sample Input 0
7
3
10
100
300
200
1000
20
30

Sample Output 0
20

'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxMin function below.
def maxMin(k, A):
    A = sorted(A, reverse=True)
    answer = min(A[i]-A[i+k-1] for i in range(n-k+1))
    return(answer)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    k = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = maxMin(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()

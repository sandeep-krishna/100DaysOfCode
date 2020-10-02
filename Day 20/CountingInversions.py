'''
In an array, , the elements at indices  and  (where ) form an inversion if . In other words, inverted elements  and  are considered to be "out of order". To correct an inversion, we can swap adjacent elements.
For example, consider the dataset . It has two inversions:  and . To sort the array, we must perform the following two swaps to correct the inversions:
Given  datasets, print the number of inversions that must be swapped to sort each dataset on a new line.

Function Description

Complete the function countInversions in the editor below. It must return an integer representing the number of inversions required to sort the array.
countInversions has the following parameter(s):
arr: an array of integers to sort .

Input Format
The first line contains an integer, , the number of datasets.
Each of the next  pairs of lines is as follows:
The first line contains an integer, , the number of elements in .
The second line contains  space-separated integers, .
Constraints

Output Format
For each of the  datasets, return the number of inversions that must be swapped to sort the dataset.

Sample Input
2  
5  
1 1 1 2 2  
5  
2 1 3 1 2

Sample Output
0  
4  

'''

#!/bin/python3

import math
import os
import random
import re
import sys

count = 0

def mergesort2(A):
    global count
    if len(A) > 1:
        n = len(A)
        m = int(n/2)
        L = A[:m]
        R = A[m:n]

        mergesort2(L)
        mergesort2(R)

        i = 0
        j = 0
        k = 0
        n1 = m
        n2 = n-m

        while i < n1 and j < n2:
            if L[i] <= R[j]:
                A[k] = L[i]
                i += 1
                k += 1
            else:
                A[k] = R[j]
                j += 1
                k += 1
                count += n1-i

        while i < n1:
            A[k] = L[i]
            i+=1
            k+=1 
        while j < n2:
            A[k] = R[j]
            j+=1
            k+=1


# Complete the countInversions function below.
def countInversions(arr):
    global count
    count = 0
    mergesort2(arr)
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = countInversions(arr)

        fptr.write(str(result) + '\n')

    fptr.close()

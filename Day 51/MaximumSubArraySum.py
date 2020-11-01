'''

We define the following:

A subarray of array  of length  is a contiguous segment from  through  where .
The sum of an array is the sum of its elements.
Given an  element array of integers, , and an integer, , determine the maximum value of the sum of any of its subarrays modulo . For example, Assume  and . The following table lists all subarrays and their moduli:

		sum	%2
[1]		1	1
[2]		2	0
[3]		3	1
[1,2]		3	1
[2,3]		5	1
[1,2,3]		6	0
The maximum modulus is .

Function Description

Complete the maximumSum function in the editor below. It should return a long integer that represents the maximum value of .

maximumSum has the following parameter(s):

a: an array of long integers, the array to analyze
m: a long integer, the modulo divisor
Input Format

The first line contains an integer , the number of queries to perform.

The next  pairs of lines are as follows:

The first line contains two space-separated integers  and (long), the length of  and the modulo divisor.
The second line contains  space-separated long integers .
Constraints

 the sum of  over all test cases 
Output Format

For each query, return the maximum value of  as a long integer.

Sample Input

1
5 7
3 3 9 9 5
Sample Output

6

'''
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maximumSum function below.
import itertools 
def maximumSum(a, m):
    a=list(itertools.accumulate(a))
    a=list(map(lambda i:i%m,a))
    d={}
    for idx,b in enumerate(a):
        d[b]=idx
    a.sort()
    ans1=a[len(a)-1]
    i=0
    j=1
    min_diff=m
    while j<len(a):
        if abs(a[i]-a[j])<min_diff and d[a[j]]<d[a[i]]:
            min_diff=abs(a[i]-a[j])
        i+=1
        j+=1
    return max(ans1,m-min_diff)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input())

    for q_itr in range(q):
        nm = input().split()

        n = int(nm[0])

        m = int(nm[1])

        a = list(map(int, input().rstrip().split()))

        result = maximumSum(a, m)

        fptr.write(str(result) + '\n')

    fptr.close()

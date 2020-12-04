'''

We define  to be a permutation of the first  natural numbers in the range . Let  denote the value at position  in permutation  using -based indexing.

P is considered to be an absolute permutation if  holds true for every .

Given  and , print the lexicographically smallest absolute permutation . If no absolute permutation exists, print -1.

For example, let  giving us an array . If we use  based indexing, create a permutation where every . If , we could rearrange them to :

pos[i]	i	|Difference|
3	1	2
4	2	2
1	3	2
2	4	2
Function Description

Complete the absolutePermutation function in the editor below. It should return an integer that represents the smallest lexicographically smallest permutation, or  if there is none.

absolutePermutation has the following parameter(s):

n: the upper bound of natural numbers to consider, inclusive
k: the integer difference between each element and its index
Input Format

The first line contains an integer , the number of test cases.
Each of the next  lines contains  space-separated integers,  and .

Constraints

Output Format

On a new line for each test case, print the lexicographically smallest absolute permutation. If no absolute permutation exists, print -1.

Sample Input

3
2 1
3 0
3 2
Sample Output

2 1
1 2 3
-1

'''


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the absolutePermutation function below.
def absolutePermutation(n, k):
    if k == 0:
        return [i+1 for i in range(n)]
    elif n % (2*k) != 0 or 2*k > n: 
        return [-1]
    return [(i+1)+(1 if (i//k)%2==0 else -1)*k for i in range(n)]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        result = absolutePermutation(n, k)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()

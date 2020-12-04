'''

Madison, is a little girl who is fond of toys. Her friend Mason works in a toy manufacturing factory . Mason has a 2D board  of size  with  rows and  columns. The board is divided into cells of size  with each cell indicated by it's coordinate . The cell  has an integer  written on it. To create the toy Mason stacks  number of cubes of size  on the cell .

Given the description of the board showing the values of  and that the price of the toy is equal to the 3d surface area find the price of the toy.

image

Input Format

The first line contains two space-separated integers  and  the height and the width of the board respectively.

The next  lines contains  space separated integers. The  integer in  line denotes .

Constraints

Output Format

Print the required answer, i.e the price of the toy, in one line.

Sample Input 0

1 1
1
Sample Output 0

6


'''


#!/bin/python3

import math
import os
import random
import re
import sys

def surfaceArea(A):
    a = [[0] * (len(A[0]) + 2)]
    for row in A:
        a.append([0] + row + [0])
    a.append([0] * (len(A[0]) + 2))
    
    ans = len(A) * len(A[0]) * 2
    
    for i in range(1, len(a)):
        for j in range(1, len(a[i])):
            ans += abs(a[i][j] - a[i-1][j])
            ans += abs(a[i][j] - a[i][j-1])
    return ans

    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    HW = input().split()

    H = int(HW[0])

    W = int(HW[1])

    A = []

    for _ in range(H):
        A.append(list(map(int, input().rstrip().split())))

    result = surfaceArea(A)

    fptr.write(str(result) + '\n')

    fptr.close()

'''

Given a 2D array of digits or grid, try to find the occurrence of a given 2D pattern of digits. For example, consider the following grid:

1234567890  
0987654321  
1111111111  
1111111111  
2222222222  
Assume we need to look for the following 2D pattern array:

876543  
111111  
111111
The 2D pattern begins at the second row and the third column of the grid. The pattern is said to be present in the grid.

Function Description

Complete the gridSearch function in the editor below. It should return YES if the pattern exists in the grid, or NO otherwise.

gridSearch has the following parameter(s):

G: the grid to search, an array of strings
P: the pattern to search for, an array of strings
Input Format

The first line contains an integer , the number of test cases.

Each of the  test cases is represented as follows:
The first line contains two space-separated integers  and , indicating the number of rows and columns in the grid .
This is followed by  lines, each with a string of  digits representing the grid .
The following line contains two space-separated integers,  and , indicating the number of rows and columns in the pattern grid .
This is followed by  lines, each with a string of  digits representing the pattern .

Constraints





Output Format

Display YES or NO, depending on whether  is present in .

Sample Input

2
10 10
7283455864
6731158619
8988242643
3830589324
2229505813
5633845374
6473530293
7053106601
0834282956
4607924137
3 4
9505
3845
3530
15 15
400453592126560
114213133098692
474386082879648
522356951189169
887109450487496
252802633388782
502771484966748
075975207693780
511799789562806
404007454272504
549043809916080
962410809534811
445893523733475
768705303214174
650629270887160
2 2
99
99
Sample Output

YES
NO

'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the gridSearch function below.
def gridSearch(G, P):
    h = len(P)
    w = len(P[0])
    for i,row in enumerate(G[:-h+1]):
        for j,col in enumerate(row[:-w+1]):
            if col == P[0][0]:
                if [G[k][j:j+w] for k in range(i, i+h)] == P:
                    return "YES"
    else:
        return "NO"
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        RC = input().split()

        R = int(RC[0])

        C = int(RC[1])

        G = []

        for _ in range(R):
            G_item = input()
            G.append(G_item)

        rc = input().split()

        r = int(rc[0])

        c = int(rc[1])

        P = []

        for _ in range(r):
            P_item = input()
            P.append(P_item)

        result = gridSearch(G, P)

        fptr.write(result + '\n')

    fptr.close()

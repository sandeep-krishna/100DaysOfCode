'''

Consider a matrix where each cell contains either a  or a . Any cell containing a  is called a filled cell. Two cells are said to be connected if they are adjacent to each other horizontally, vertically, or diagonally. In the following grid, all cells marked X are connected to the cell marked Y.

XXX
XYX  
XXX    
If one or more filled cells are also connected, they form a region. Note that each cell in a region is connected to zero or more cells in the region but is not necessarily directly connected to all the other cells in the region.

Given an  matrix, find and print the number of cells in the largest region in the matrix. Note that there may be more than one region in the matrix.

For example, there are two regions in the following  matrix. The larger region at the top left contains  cells. The smaller one at the bottom right contains .

110
100
001
Function Description

Complete the connectedCell function in the editor below. It should return an integer that denotes the area of the largest region.

connectedCell has the following parameter(s):
- matrix: a 2D array of integers where  represents the  row of the matrix

Input Format

The first line contains an integer , the number of rows in the matrix.
The second line contains an integer , the number of columns in the matrix.
Each of the next  lines contains  space-separated integers .

Constraints

Output Format

Print the number of cells in the largest region in the given matrix.

Sample Input

4
4
1 1 0 0
0 1 1 0
0 0 1 0
1 0 0 0
Sample Output

5


'''


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the connectedCell function below.
def connectedCell(matrix):
    
    largest = 0 
    
    def find(temp,i,j):
        
        if 0<=i<len(matrix) and 0<=j<len(matrix[0]):
            if matrix[i][j] == 1:
                matrix[i][j] = 0 
                temp+=1
                try:
                    if matrix[i+1][j] == 1:
                        temp = find(temp,i+1,j)
                except:
                    pass
                try:
                    if matrix[i-1][j] == 1:
                        temp = find(temp,i-1,j)
                except:
                    pass
                try:
                    if matrix[i][j+1] == 1:
                        temp = find(temp,i,j+1)
                except:
                    pass
                try:
                    if matrix[i][j-1] == 1:
                        temp = find(temp,i,j-1)
                except:
                    pass

                try:
                    if matrix[i+1][j+1] == 1:
                        temp = find(temp,i+1,j+1)
                except:
                    pass
                try:
                    if matrix[i-1][j-1] == 1:
                        temp = find(temp,i-1,j-1)
                except:
                    pass
                try:
                    if matrix[i-1][j+1] == 1:
                        temp = find(temp,i-1,j+1)
                except:
                    pass
                try:
                    if matrix[i+1][j-1] == 1:
                        temp = find(temp,i+1,j-1)
                except:
                    pass
        return temp

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            temp = 0 
            if matrix[i][j] == 1:
                temp = find(temp,i,j)
            largest = max(temp,largest)

    return largest

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    m = int(input())

    matrix = []

    for _ in range(n):
        matrix.append(list(map(int, input().rstrip().split())))

    result = connectedCell(matrix)

    fptr.write(str(result) + '\n')

    fptr.close()

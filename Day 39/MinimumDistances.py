'''
We define the distance between two array values as the number of indices between the two values. Given , find the minimum distance between any pair of equal elements in the array. If no such value exists, print .
For example, if , there are two matching pairs of values: . The indices of the 's are  and , so their distance is . The indices of the 's are  and , so their distance is .

Function Description
Complete the minimumDistances function in the editor below. It should return the minimum distance between any two matching elements.
minimumDistances has the following parameter(s):
a: an array of integers

Input Format
The first line contains an integer , the size of array .
The second line contains  space-separated integers .

Output Format
Print a single integer denoting the minimum  in . If no such value exists, print .

Sample Input
6
7 1 3 4 1 7

Sample Output
3
'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumDistances function below.
def  minimumDistances(n,A):
    for d in range(1, n):
        for i in range(n - d):
            if A[i] == A[i+d]:
                return d
    return -1
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    a = list(map(int, input().rstrip().split()))
    result = minimumDistances(len(a),a)
    fptr.write(str(result) + '\n')
    fptr.close()
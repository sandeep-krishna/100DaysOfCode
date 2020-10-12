'''
You will be given an array of integers and a target value. Determine the number of pairs of array elements that have a difference equal to a target value.
For example, given an array of [1, 2, 3, 4] and a target value of 1, we have three values meeting the condition: , , and .

Function Description
Complete the pairs function below. It must return an integer representing the number of element pairs having the required difference.
pairs has the following parameter(s):
k: an integer, the target difference
arr: an array of integers
Input Format
The first line contains two space-separated integers  and , the size of  and the target value.
The second line contains  space-separated integers of the array .

Constraints
Each integer  will be unique

Output Format
An integer representing the number of pairs of integers whose difference is .

Sample Input
5 2  
1 5 3 4 2  

Sample Output
3

'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the pairs function below.
def pairs(k, arr):
    myDict = {item : 1 for index, item in enumerate(arr)}        
    count = 0
    for each in myDict:
        if each + k in myDict:
            count += 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()

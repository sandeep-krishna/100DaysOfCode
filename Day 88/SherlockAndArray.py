'''

Watson gives Sherlock an array of integers. His challenge is to find an element of the array such that the sum of all elements to the left is equal to the sum of all elements to the right.

The answer is  since left and right sum to .
You will be given arrays of integers and must determine whether there is an element that meets the criterion. If there is, return YES. Otherwise, return NO.

Function Description
Complete the balancedSums function in the editor below.

balancedSums has the following parameter(s):
int arr[n]: an array of integers
Returns
string: either YES or NO

Input Format
The first line contains , the number of test cases.
The next  pairs of lines each represent a test case.
- The first line contains , the number of elements in the array .
- The second line contains  space-separated integers  where .

Constraints

Sample Input 0
2
3
1 2 3
4
1 2 3 3

Sample Output 0
NO
YES

'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the balancedSums function below.
def balancedSums(a):
    # Complete this function
    summy=sum(a)
    l=len(a)
    lefty=0
    for i in range(len(a)):
        current=a[i]
        summy-=current
        if lefty==summy:
            return 'YES'
        lefty+=current
    return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = balancedSums(arr)

        fptr.write(result + '\n')

    fptr.close()

'''

Numeros the Artist had two lists that were permutations of one another. He was very proud. Unfortunately, while transporting them from one exhibition to another, some numbers were lost out of the orignal list. Can you find the missing numbers?

Example
The  array is the orginal list. The numbers missing are .
Notes
If a number occurs multiple times in the lists, you must ensure that the frequency of that number in both lists is the same. If that is not the case, then it is also a missing number.
Return the missing numbers sorted ascending.
Only include a missing number once, even if it is missing multiple times.
The difference between the maximum and minimum numbers in the original list is less than or equal to .

Function Description
Complete the missingNumbers function in the editor below. It should return a sorted array of missing numbers.

missingNumbers has the following parameter(s):
int arr[n]: the array with missing numbers
int brr[m]: the original array of numbers

Input Format
There will be four lines of input:
 - the size of the first list, 
The next line contains  space-separated integers 
 - the size of the second list, 
The next line contains  space-separated integers 

Sample Input
10
203 204 205 206 207 208 203 204 205 206
13
203 204 204 205 206 207 205 208 203 206 205 206 204

Sample Output
204 205 206

'''


#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
# Complete the missingNumbers function below.
def missingNumbers(arr, brr):
    a = Counter(arr)
    b = Counter(brr)
    return sorted((b - a).keys())

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    m = int(input())

    brr = list(map(int, input().rstrip().split()))

    result = missingNumbers(arr, brr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

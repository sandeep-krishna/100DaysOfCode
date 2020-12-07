'''

Palindromes are strings that read the same from the left or right, for example madam or 0110.

You will be given a string representation of a number and a maximum number of changes you can make. Alter the string, one digit at a time, to create the string representation of the largest number possible given the limit to the number of changes. The length of the string may not be altered, so you must consider 's left of all higher digits in your tests. For example  is valid,  is not.

Given a string representing the starting number and a maximum number of changes allowed, create the largest palindromic string of digits possible or the string -1 if it's impossible to create a palindrome under the contstraints.

Function Description
Complete the highestValuePalindrome function in the editor below. It should return a string representing the largest value palindrome achievable, or -1.
highestValuePalindrome has the following parameter(s):
s: a string representation of an integer
n: an integer that represents the length of the integer string
k: an integer that represents the maximum number of changes allowed

Input Format
The first line contains two space-separated integers,  and , the number of digits in the number and the maximum number of changes allowed.
The second line contains an -digit string of numbers.

Constraints
Each character  in the number is an integer where .

Output Format
Print a single line with the largest number that can be made by changing no more than  digits. If this is not possible, print -1.

Sample Input 0
4 1
3943

Sample Output 0
3993

Sample Input 1
6 3
092282

Sample Output 1
992299

Sample Input 2
4 1
0011

Sample Output 2
-1

'''


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the highestValuePalindrome function below.
def highestValuePalindrome(s, n, k):
    
    if (n == 1):
        if (k == 1):
            return '9'
        else:
            return '-1'
    arr = list(s)
    changes = [0 for _ in range(n)]
    for i in range(int(n / 2) + (n & 1)):
        if (arr[i] != arr[n - 1 - i]):
            arr[i] = arr[n - 1 - i] = max(arr[i], arr[n - 1 - i])
            changes[i] += 1
            k -= 1
        if (k < 0):
            return '-1'
    for i in range(int(n / 2) + (n & 1)):
        if (arr[i] == arr[n - 1 - i]):
            if (arr[i] != '9'):
                if (changes[i] == 1 or i == (n - 1 - i)):
                    cost = 1
                else:
                    cost = 2
                if (k >= cost):
                    arr[i] = arr[n - 1 - i] = '9'
                    k -= cost
    return ''.join(arr)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    s = input()

    result = highestValuePalindrome(s, n, k)

    fptr.write(result + '\n')

    fptr.close()

'''

Consider a string, , of  lowercase English letters where each character,  (, denotes the letter at index  in . We define an  palindromic tuple of  to be a sequence of indices in  satisfying the following criteria:

, meaning the characters located at indices  and  are the same.
, meaning the characters located at indices  and  are the same.
, meaning that , , , and  are ascending in value and are valid indices within string .
Given , find and print the number of  tuples satisfying the above conditions. As this value can be quite large, print it modulo .

Input Format

A single string denoting .

Constraints

It is guaranteed that  only contains lowercase English letters.
Output Format

Print the the number of  tuples satisfying the conditions in the Problem Statement above. As this number can be very large, your answer must be modulo .

Sample Input 0

kkkkkkz
Sample Output 0

15

'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the shortPalindrome function below.
def create(n):
    l = [0] * 26 ** n
    return l
# Complete the shortPalindrome function below.
def shortPalindrome(s):
    l1, l2, l3 = create(1), create(2), create(3)
    ret = 0
    for c in s:
        n = ord(c) - ord('a')
    
        for i in range(26):
            ret += l3[n*26*26+i*26+i] % 1000000007
            l3[i*26*26+n*26+n] += l2[i * 26 + n]
            l2[i * 26 + n] += l1[i]
        l1[n] += 1
       
    return ret % 1000000007

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = shortPalindrome(s)

    fptr.write(str(result) + '\n')

    fptr.close()

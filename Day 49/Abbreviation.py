'''
You can perform the following operations on the string, :

Capitalize zero or more of 's lowercase letters.
Delete all of the remaining lowercase letters in .
Given two strings,  and , determine if it's possible to make  equal to  as described. If so, print YES on a new line. Otherwise, print NO.
For example, given  and , in  we can convert  and delete  to match . If  and , matching is not possible because letters may only be capitalized or discarded, not changed.

Function Description
Complete the function  in the editor below. It must return either  or .
abbreviation has the following parameter(s):
a: the string to modify
b: the string to match

Input Format
The first line contains a single integer , the number of queries.
Each of the next  pairs of lines is as follows:
- The first line of each query contains a single string, .
- The second line of each query contains a single string, .

Constraints
String  consists only of uppercase and lowercase English letters, ascii[A-Za-z].
String  consists only of uppercase English letters, ascii[A-Z].

Output Format
For each query, print YES on a new line if it's possible to make string  equal to string . Otherwise, print NO.

Sample Input
1
daBcd
ABC

Sample Output
YES
'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the abbreviation function below.

def abbreviation(a, b):
    n=len(a)
    m=len(b)
    dp=[[0]*(m+1) for _ in range(n+1)]
    dp[0][0]=1
    i=1
    while i<n+1:    
        if a[i-1].isupper():
            break
        else:
            dp[i][0]=1
        i+=1
    for i in range(1,n+1):
        for j in range(1,m+1):
            if a[i-1]==b[j-1]:
                dp[i][j]=dp[i-1][j-1]
            elif a[i-1].islower() and a[i-1].upper()==b[j-1]:
                dp[i][j]=dp[i-1][j-1] or dp[i-1][j]
            elif a[i-1].isupper():
                dp[i][j]=0
            else:
                dp[i][j]=dp[i-1][j]
    return  "YES" if dp[-1][-1] else "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        a = input()

        b = input()

        result = abbreviation(a, b)

        fptr.write(result + '\n')

    fptr.close()

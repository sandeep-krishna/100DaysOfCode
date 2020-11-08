'''

A weighted string is a string of lowercase English letters where each letter has a weight. Character weights are  to  from  to  as shown below:

image

We define the following terms:

The weight of a string is the sum of the weights of all the string's characters. For example:

image

A uniform string consists of a single character repeated zero or more times. For example, ccc and a are uniform strings, but bcb and cd are not.
Given a string, , let  be the set of weights for all possible uniform contiguous substrings of string . You have to answer  queries, where each query  consists of a single integer, . For each query, print Yes on a new line if ; otherwise, print No instead.

Note: The  symbol denotes that  is an element of set .

Function Description

Complete the weightedUniformStrings function in the editor below. It should return an array of strings, either Yes or No, one for each query.

weightedUniformStrings has the following parameter(s):

s: a string
queries: an array of integers
Input Format

The first line contains a string , the original string.
The second line contains an integer , the number of queries.
Each of the next  lines contains an integer , the weight of a uniform subtring of  that may or may not exist.

Constraints

 will only contain lowercase English letters, ascii[a-z].
Output Format

Print  lines. For each query, print Yes on a new line if . Otherwise, print No.

Sample Input 0

abccddde
6
1
3
12
5
9
10
Sample Output 0

Yes
Yes
Yes
Yes
No
No

'''

#!/bin/python3

import sys


s = input().strip()
n = int(input().strip())

sorted(s)

a_set = set()
prev = ''

count = 0
for c in s:
    if c != prev:
        count = 1
        prev = c
    else:
        count +=1
    a_set.add(count * (ord(c) - 96))

for a0 in range(n):
    x = int(input().strip())
    print("Yes" if x in a_set else "No")
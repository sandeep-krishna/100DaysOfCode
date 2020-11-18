'''

You are given a range . You are required to find the number of integers  in the range such that  where  is equal to the sum of digits of  in its hexadecimal (or base 16) representation.
For example,  ( in hexadecimal is written as ). You are aksed  such questions. 

Input format
The first line contains a positive integer  denoting the number of questions that you are asked.
Each of the next  lines contain two integers  and  denoting the range of questions.

Output Format
For each test case, you are required to print exactly  numbers as the output. 

SAMPLE INPUT 
3
1 3
5 8
7 12

SAMPLE OUTPUT 
2
4
6

'''

import math

def convertHexa(n):
    total = 0
    for i in hex(n).lstrip("0x").rstrip("L"):
        total += int(i, 16)

    return total


T = int(input())
for _ in range(T):
    L, R = input().split()
    count = 0

    for i in range(int(L), int(R)+1):
        if math.gcd(i, convertHexa(i)) > 1:
            count += 1

    print (count)
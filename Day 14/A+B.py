'''
A + B

Problem Description
Given a series of integer pairs  and , output the sum of  and .

Input Format
Each line contains two integers,  and . One input file may contain several pairs  where .

Output Format
Output a single integer per line - The sum of  and .


SAMPLE INPUT 
1 2
2 5
10 14
SAMPLE OUTPUT 
3
7
24
'''

from sys import stdin
sums = []
for i in stdin:
     data = list(map(int, i.split()))
     sums.append(sum(data))
print(*sums,sep="\n")
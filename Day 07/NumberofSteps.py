'''
Number of steps

You are given two arrays  and . In each step, you can set  if . Determine the minimum number of steps that are required to make all 's equal.

Input format

First line: n
Second line: a1,a2,a3,a4....,an
Third line: b1,b2,b3,b4,....,bn
Output format
Print the minimum number of steps that are required to make all 's equal. If it is not possible, then print -1.

Sample input

2
5 6
4 3

Sample output

-1

SAMPLE INPUT 
5
5 7 10 5 15
2 2 1 3 5
SAMPLE OUTPUT 
8
'''

def steps(a, b, n):
    
    a_min = min(a)
    count = 0
    i = 0
    while i < n:
       while a[i] > a_min:
           a[i] = a[i] - b[i]
           count = count+1
       
       if a[i] == a_min:
           i=i+1
           continue
       
       if a[i] < b[i]:
           count = -1
           break
       
       if a[i] < a_min:
           a_min = a[i]
           i = 0
           continue

       i = i+1
    print(count)

n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

steps(a, b, n)
'''
You are given n inputs and two numbers x and y. check whether all the given numbers lies in range of x and y. (x <= y). 
If the condition is true print YES else print NO.

Input Format:
First line contains N, X, Y seperated by space.
Next Line contains n integers.

SAMPLE INPUT 
5 1 5
1 2 3 4 5

SAMPLE OUTPUT 
YES

'''

n,x,y=map(int,input().split())
l=list(map(int,input().split()))
l.sort()
if(l[0]>=x and l[-1]<=y):
    print('YES')
else:
    print('NO')
'''
Find the Pattern

The pattern challenge is back again with more complexity. Can you solve it??

Input 1:
3
2224 5262 223

Output 1:
5485

Input 2:
11
170 368 472 298 22 139 370 1061 162 1073 491

Output 2:
1095

SAMPLE INPUT 
3
2224 5262 223

SAMPLE OUTPUT 
5485
'''
x=int(input())
A=list(map(int,input().split()))
print(max(A)+min(A))
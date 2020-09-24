'''
Minimum Steps

There are three integers k,m,n. You have to convert the number k to m by performing the given operations:

Multiply k by n
 Decrease k by 2.
 Decrease k by 1.
You have to perform the above operations to convert the integer from k to m and find the minimum steps.

Note: You can perform the operations in any order.

Input : 
First-line contains the number of test cases T.
The next T line contains three space-separated integers k, m, and n.

Output : 
Print minimum no. of steps as output in a new line for each test case.

SAMPLE INPUT 
2
3 10 2
11 6 2
SAMPLE OUTPUT 
3
3
'''
def rec(a,b,c):
    if a>=b:
        return ((a-b)//2+(a-b)%2)
    if b%c==0:
        return (1+rec(a,b//c,c))
    else:
        x=(b//c+1)*c;
        return ((x-b)//2+(x-b)%2+rec(a,x,c))


 

for _ in range(int(input())):
    a,b,c=map(int,input().split())
    print(rec(a,b,c))
   
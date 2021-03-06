'''

You are given a stack of N integers. In one operation, you can either pop an element from the stack or push any popped element into the stack. You need to maximize the top element of the stack after performing exactly K operations. If the stack becomes empty after performing K operations and there is no other way for the stack to be non-empty, print -1.

Input format :
The first line of input consists of two space-separated integers N and K.
The second line of input consists N space-separated integers denoting the elements of the stack. The first element represents the top of the stack and the last element represents the bottom of the stack.

Output format :
Print the maximum possible top element of the stack after performing exactly K operations.

SAMPLE INPUT 
6 4
1 2 4 3 3 5

SAMPLE OUTPUT 
4

'''


n,k=map(int,input().split())
arr=[int(x) for x in input().split()]

if k==n or (n==1 and k%2==1):
    print(-1)
elif k>n:
    print(max(arr))
else:
    t=-1
    for i in range(0,k-1):
        t=max(t,arr[i])
    ans=max(t,arr[k])
    print(ans)
    
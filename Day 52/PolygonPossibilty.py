'''
You are given length of n sides, you need to answer whether it is possible to make n sided convex polygon with it.

Input : -
First line contains ,no .of testcases.
For each test case , first line consist of single integer ,second line consist of  spaced integers, size of each side.

Output : -
For each test case print "Yes" if it is possible to make polygon or else "No" if it is not possible.

SAMPLE INPUT 
2
3
4 3 2 
4
1 2 1 4 
SAMPLE OUTPUT 
Yes
No

'''

for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    total=sum(arr)
    flag=1
    for i in arr:
        if total-i <= i:
            flag=0
            break

    print ("Yes" if flag==1 else "No")
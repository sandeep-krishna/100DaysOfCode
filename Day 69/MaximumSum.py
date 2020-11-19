'''

You are given an array of integers , you need to find the maximum sum that can be obtained by picking some non-empty subset of the array. If there are many such non-empty subsets, choose the one with the maximum number of elements. Print the maximum sum and the number of elements in the chosen subset.

Input:
The first line contains an integer , denoting the number of elements of the array. Next line contains  space-separated integers, denoting the elements of the array.

Output:
Print  space-separated integers, the maximum sum that can be obtained by choosing some subset and the maximum number of elements among all such subsets which have the same maximum sum.

SAMPLE INPUT 
5
1 2 -4 -2 3

SAMPLE OUTPUT 
6 3


'''

n=int(input())
a=list(map(int,input().split()))
b=[]
s=0
c=0

for i in range(n):
    if(a[i]>=0):
        s+=a[i]
        c=c+1

if(s==0 and c==0):
    print(max(a),end=" ")
    print("1")
else:
    print(s,end=" ")
    print(c)
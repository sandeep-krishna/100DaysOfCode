'''


You are given an array A of N integers. Now, two functions  and  are defined:

F(X) : This is the smallest number Z such that X<Z<N and A|X| < A|Z|

G(X) : This is the smallest number Z such that X<Z<N and A|X| > A|Z|

Now, you need to find for each index i of this array , where  . If such a number does not exist, for a particular index i, output 1 as its answer. If such a number does exist, output 

Input :
The first line contains a single integer N denoting the size of array A. Each of the next N lines contains a single integer, where the integer on the  line denotes .

Output :
Print N space separated integers on a single line, where the  integer denotes  or 1, if  does not exist.

SAMPLE INPUT 
8
3
7
1
7
8
4
5
2

SAMPLE OUTPUT 
1 4 4 4 -1 2 -1 -1

'''
arr = []
n = int(input())
a, b, s1, s2 = dict(), dict(), [], []
for i in range(n):
    arr.append(int(input()))
    x = arr[i]
    while(s1!=[] and s1[-1][0]<x):
        a[s1.pop()[1]] = i
    s1.append((x, i))
    while(s2!=[] and s2[-1][0]>x):
        b[s2.pop()[1]] = i
    s2.append((x, i))
for i in range(n):
    if i in a:
        if a[i] in b:
            print(arr[b[a[i]]], end = " ")
        else:
            print(-1, end = " ")
    else:
        print(-1, end = " ")
print()


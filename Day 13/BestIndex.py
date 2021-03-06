'''
Best Index

You are given an array  of  elements. Now you need to choose the best index of this array . An index of the array is called best if the special sum of this index is maximum across the special sum of all the other indices.

To calculate the special sum for any index  , you pick the first element that is  and add it to your sum. Now you pick next two elements i.e.  and  and add both of them to your sum. Now you will pick the next  elements and this continues till the index for which it is possible to pick the elements. For example:

If our array contains  elements and you choose index to be  then your special sum is denoted by -
 , beyond this its not possible to add further elements as the index value will cross the value .

Find the best index and in the output print its corresponding special sum. Note that there may be more than one best indices but you need to only print the maximum special sum.

Input
First line contains an integer  as input. Next line contains  space separated integers denoting the elements of the array .
Output
In the output you have to print an integer that denotes the maximum special sum


SAMPLE INPUT 
6
-3 2 3 -4 3 1
SAMPLE OUTPUT 
3

'''
N = int(input())
ns = [int(n) for n in input().split()]
k = 2
start = 1
 
while start <= N:
    start += k
    k += 1
    
start -= k - 1
k -= 2
s = sum(ns[:start])
ms = s
 
for i in range(1, N):
    s -= ns[i - 1]
    
    if start < N:
        s += ns[start]
        start += 1
    else:
        k -= 1
        s -= sum(ns[N - k:N])
        start -= k
        
    if s > ms:
        ms = s
print(ms)
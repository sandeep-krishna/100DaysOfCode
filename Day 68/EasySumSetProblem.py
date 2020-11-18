'''

In this problem, we define "set" is a collection of distinct numbers. For two sets  and , we define their sum set is a set . In other word,  set  contains all elements which can be represented as sum of an element in  and an element in . Given two sets , your task is to find set  of positive integers less than or equals  with maximum size such that . It is guaranteed that there is unique such set.

Input Format
The first line contains  denoting the number of elements in set , the following line contains  space-separated integers  denoting the elements of set .
The third line contains  denoting the number of elements in set , the following line contains  space-separated integers  denoting the elements of set .

Output Format
Print all elements of  in increasing order in a single line, separated by space.

SAMPLE INPUT 
2
1 2
3
3 4 5

SAMPLE OUTPUT 
2 3

'''

n = int(input())
a = list(map(int, input().split()))
m = int(input())
c = list(map(int, input().split()))
b = []

maximum_a = max(a)
maximum_c = max(c)
for i in range(abs(maximum_a-maximum_c)+1):
    count = 0
    for j in a:
        if i+j in c:
            count += 1
        if count == n:
            b.append(i)
b.sort()

print(" ".join(map(str, b)))
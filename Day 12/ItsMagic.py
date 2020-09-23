'''
It's Magic

Sussutu is a world-renowned magician. And recently, he was blessed with the power to remove EXACTLY ONE element from an array.
Given, an array A (index starting from 0) with N elements. Now, Sussutu CAN remove only that element which makes the sum of ALL the remaining elements exactly divisible by 7.
Throughout his life, Sussutu was so busy with magic that he could never get along with maths. Your task is to help Sussutu find the first array index of the smallest element he CAN remove.

Input:
The first line contains a single integer N.
Next line contains N space separated integers Ak , 0 < k < N.

Output:
Print a single line containing one integer, the first array index of the smallest element he CAN remove, and -1 if there is no such element that he can remove!

Constraints:
1 < N < 105
0 < Ak < 109

SAMPLE INPUT 
5
14 7 8 2 4
SAMPLE OUTPUT 
1
Explanation
Both 14 and 7 are valid answers, but since 7 is the smallest, the required array index is 1.
'''

n=int(input())
m=list(map(int,input().split()))
y=sum(m)
l=[]
for i in range(n):
    k=y-m[i]
    if(k%7==0):
        l.append(m[i])

if(len(l)==0):
    print('-1')
else:
    print(m.index(min(l)))
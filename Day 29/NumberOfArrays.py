'''
You are given an array A. You need to divide this array into exactly K non-empty segments and check whether the minimum element S amongst the maximum elements amongst all segments is less than Q or not.
In other words, if we store the maximum element of each of the segment in an array P, then you have to check if minimum element in P is less than Q or not.

Input:
First line of input contains number of testcases, T
First line of each testcase contains three integers: N denoting number of elements in array A, K denoting number of segments and Q.
Second line of each testcase contains N space-separated integers,  , , ... .

Output:
For each testcase, if S is less than Q, print S, else print  (without quotes).
Answer for each test case should come in a new line.


SAMPLE INPUT 
1
5 5 2
1 2 3 4 5

SAMPLE OUTPUT 
1

Explanation
We can divide the complete array into 5 segments ---1, 2, 3, 4, 5. The minimum number among this number is 1 which is less than 2.
'''

for _ in range(int(input())):
     n,k,q=map(int,input().split())
     a=list(map(int,input().split()))
     if(k==1):
          if(max(a)<q):
              print(max(a))
          else:
              print('NO')
     elif(min(a)<q):
         print(min(a))
     else:
         print('NO')
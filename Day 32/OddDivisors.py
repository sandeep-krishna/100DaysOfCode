'''
You are given a positive integer N.f(N) . is the greatest odd divisor of N. 

Find the sum .
Input format
The first line of the input contains a single integer   denoting the number of test cases. The description of  test cases follows.
The first line of each test case contains two integers  and  .

Output format
For each value of , print the value of  in a separate line.

SAMPLE INPUT 
5
1 100
110 30
12345 100000007
10 28383
100 5

SAMPLE OUTPUT 
1
18
50804693
36
4

'''
for _ in range(int(input())):
    
     n,m=map(int,input().split());
     s=0 

     while(n>0):
         s+=((n+1)//2)**2;n//=2

     print(s%m)
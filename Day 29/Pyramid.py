'''
You are given T test cases. For each test case you are given an integer n. For every test case you need to print a pyramid made up of symbol '*' of height n in new line.

SAMPLE INPUT 
2
1
3
SAMPLE OUTPUT 
*

  *
 ***
*****

'''

for _ in range(int(input())):
    n=int(input())
    for i in range(1,n+1):
        print(' '*(n-i),'*'*(2*i-1),sep='')
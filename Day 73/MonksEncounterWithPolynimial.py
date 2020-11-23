'''

Our monk, while taking a stroll in the park, stumped upon a polynomial ( A X2 + B X +C ) lying on the ground. The polynomial was dying! Being considerate, our monk tried to talk and revive the polynomial. The polynomial said:
I have served my purpose, and shall not live anymore. Please fulfill my dying wish. Find me the least non-negative integer Xo, that shall make my value atleast K i.e., A Xo2 + B Xo + C >= K .

Help our Monk fulfill the polynomial's dying wish!


Input:
The first line contains an integer T. T test cases follow.
Each test case consists of four space-separated integers A, B, C and K.

Output:
For each test case, output the answer in a new line.

Constraints:
1 ≤ T ≤ 105
1 ≤ A,B,C ≤ 105
1 ≤ K ≤ 1010

SAMPLE INPUT 
3
3 4 5 6
3 4 5 5
3 4 5 150

SAMPLE OUTPUT 
1
0
7


'''


import math
import sys
n= int(input())
for i in range(n):
    m=sys.stdin.readline()
    v=(m.split(' '))
    
    a= int(v[0])
    b= int(v[1])
    c= int(v[2])
    k= int(v[3])
    
    c=c-k
    if a==0:
        r1= (k-c)/b
        r2= (k-c)/b
    else:
        if ((b*b)-(4*a*c))<0:
            r1=0
            r2=0
        else:
            r1=(-b+math.sqrt((b*b)-4*a*c))/(2*a)
            r2=(-b-math.sqrt((b*b)-4*a*c))/(2*a)
            r1=math.ceil(r1)
            r2=math.ceil(r2)
    if r1<0 and r2<0:
        print (0)
    else:
        if r2>=r1 and r1<0:
            print(r2)
        else:
            print (r1)
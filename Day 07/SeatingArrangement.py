'''
Akash and Vishal are quite fond of travelling. They mostly travel by railways. They were travelling in a train one day and they got interested in the seating arrangement of their compartment. The compartment looked something like


So they got interested to know the seat number facing them and the seat type facing them. The seats are denoted as follows :

Window Seat : WS
Middle Seat : MS
Aisle Seat : AS

You will be given a seat number, find out the seat number facing you and the seat type, i.e. WS, MS or AS.

INPUT
First line of input will consist of a single integer T denoting number of test-cases. Each test-case consists of a single integer N denoting the seat-number.

OUTPUT
For each test case, print the facing seat-number and the seat-type, separated by a single space in a new line.

CONSTRAINTS
1<=T<=105
1<=N<=108
SAMPLE INPUT 
2
18
40
SAMPLE OUTPUT 
19 WS
45 AS
'''

def seat(a):
    c = (a // 6)
    if c % 2 == 0:
        if a % 6 == 0:
            ans = (str(a - 11)+' ' +'WS')
        elif a % 6 == 1:
            ans = (str(a + 11)+' '+  'WS')
        elif a % 6 == 2:
            ans = (str(a + 9)+' '+ 'MS')
        elif a % 6 == 3:
            ans = (str(a + 7)+' '+ 'AS')
        elif a % 6 == 4:
            ans = (str(a + 5)+' '+ 'AS')
        elif a % 6 == 5:
            ans = (str(a + 3)+' '+ 'MS')

    if c % 2 != 0:
        if a % 6 == 0:
            ans = (str(a + 1)+' '+ 'WS')
        if a % 6 == 1:
            ans = (str(a - 1)+' '+ 'WS')
        if a % 6 == 2:
            ans = (str(a - 3)+' '+ 'MS')
        if a % 6 == 3:
            ans = (str(a - 5)+' '+ 'AS')
        if a % 6 == 4:
            ans = (str(a - 7)+' '+ 'AS')
        if a % 6 == 5:
            ans = (str(a - 9)+ ' ' +'MS')
    print(ans)



for _ in range(int(input())):
    a = int(input())
    seat(a)

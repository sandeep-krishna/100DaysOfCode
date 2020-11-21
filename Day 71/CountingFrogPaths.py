'''

There is a frog initially placed at the origin of the coordinate plane. In exactly  second, the frog can either move up  unit, move right  unit, or stay still. In other words, from position , the frog can spend  second to move to:
After  seconds, a villager who sees the frog reports that the frog lies on or inside a square of side-length  with coordinates , , , . Calculate how many points with integer coordinates on or inside this square could be the frog's position after exactly  seconds

Input Format:
The first and only line of input contains four space-separated integers: , , , and .

Output Format:
Print the number of points with integer coordinates that could be the frog's position after  seconds.

Constraints:
Note that the Expected Output Feature for Custom Invocation is not supported for this contest. 

SAMPLE INPUT 
2 2 3 6
SAMPLE OUTPUT 
6

'''

X,Y,s,T=list(map(int,input().split()))
c=0
for i in range(X,X+s+1):
    for j in range(Y,Y+s+1):
        if(i+j<=T):
            c+=1

print(c)


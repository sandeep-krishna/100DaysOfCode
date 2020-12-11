'''

KnightL  is a chess piece that moves in an L shape. We define the possible moves of  as any movement from some position  to some  satisfying either of the following:

 and , or
 and 
Note that  and  allow for the same exact set of movements. For example, the diagram below depicts the possible locations that  or  can move to from its current location at the center of a  chessboard:

image

Observe that for each possible movement, the Knight moves  units in one direction (i.e., horizontal or vertical) and  unit in the perpendicular direction.

Given the value of  for an  chessboard, answer the following question for each  pair where :

What is the minimum number of moves it takes for  to get from position  to position ? If it's not possible for the Knight to reach that destination, the answer is -1 instead.
Then print the answer for each  according to the Output Format specified below.

Input Format

A single integer denoting .

Constraints

Output Format

Print exactly  lines of output in which each line  (where ) contains  space-separated integers describing the minimum number of moves  must make for each respective  (where ). If some  cannot reach position , print -1 instead.

For example, if , we organize the answers for all the  pairs in our output like this:

(1,1) (1,2)
(2,1) (2,2)
Sample Input 0

5
Sample Output 0

4 4 2 8
4 2 4 4
2 4 -1 -1
8 4 -1 1

'''


from collections import deque

def valid(x,y):

    if x>=n or x<0 or y>=n or y<0:
        return False
    if vi[x][y]:
        return False
    
    return True

def BFS(x,y,p,qq):
    q=deque()
    vi[x][y]=True
    q.append([x,y])
    
    dx=[p,p,-p,-p,-qq,-qq,qq,qq]
    dy=[qq,-qq,qq,-qq,p,-p,p,-p]
    
    while q:
        A=q.popleft()
    
        X=A[0]
        Y=A[1]
       
        for i in range(8):
            newX=X+dx[i]
            newY=Y+dy[i]
            
            if valid(newX,newY):
                q.append([newX,newY])
                dis[newX][newY]=dis[X][Y]+1
                if newX==n-1 and newY==n-1:
                    return 1
                vi[newX][newY]=True

        
    return 0

n=int(input())
for i in range(1,n):
    for j in range(1,n):
        vi=[[False for i in range(n+1)] for i in range(n+1)]
        dis=[[0 for  i in range(n+1)] for  i in range(n+1)]
        c=BFS(0,0,i,j)
        
        if c:
            print(dis[n-1][n-1],end=' ')
        else:
            print(-1,end=' ' )
    print()
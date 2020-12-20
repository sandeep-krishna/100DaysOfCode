'''

Ron and Hermione are deep in the Forbidden Forest collecting potion ingredients, and they've managed to lose their way. The path out of the forest is blocked, so they must make their way to a portkey that will transport them back to Hogwarts.

Consider the forest as an  grid. Each cell is either empty (represented by .) or blocked by a tree (represented by ). Ron and Hermione can move (together inside a single cell) LEFT, RIGHT, UP, and DOWN through empty cells, but they cannot travel through a tree cell. Their starting cell is marked with the character , and the cell with the portkey is marked with a . The upper-left corner is indexed as .

.X.X......X
.X*.X.XXX.X
.XX.X.XM...
......XXXX.
In example above, Ron and Hermione are located at index  and the portkey is at . Each cell is indexed according to Matrix Conventions.

Hermione decides it's time to find the portkey and leave. They start along the path and each time they have to choose a direction, she waves her wand and it points to the correct direction. Ron is betting that she will have to wave her wand exactly  times. Can you determine if Ron's guesses are correct?

The map from above has been redrawn with the path indicated as a series where  is the starting point (no decision in this case),  indicates a decision point and  is just a step on the path:

.X.X.10000X
.X*0X0XXX0X
.XX0X0XM01.
...100XXXX.
There are three instances marked with  where Hermione must use her wand.

Note: It is guaranteed that there is only one path from the starting location to the portkey.

Function Description

Complete the countLuck function in the editor below. It should return a string, either  if Ron is correct or  if he is not.

countLuck has the following parameters:

matrix: a list of strings, each one represents a row of the matrix
k: an integer that represents Ron's guess
Input Format

The first line contains an integer , the number of test cases.

Each test case is described as follows:
The first line contains  space-separated integers  and , the number of forest matrix rows and columns.
Each of the next  lines contains a string of length  describing a row of the forest matrix.
The last line contains an integer , Ron's guess as to how many times Hermione will wave her wand.

Constraints

There will be exactly one  and one  in the forest.
Exactly one path exists between  and .
Output Format

On a new line for each test case, print  if Ron impresses Hermione by guessing correctly. Otherwise, print .

Sample Input

3
2 3
*.M
.X.
1
4 11
.X.X......X
.X*.X.XXX.X
.XX.X.XM...
......XXXX.
3
4 11
.X.X......X
.X*.X.XXX.X
.XX.X.XM...
......XXXX.
4
Sample Output

Impressed
Impressed
Oops!


'''
def countLuck(matrix, k):
    turns = 0
    ron = positionRon(grid)
    size = findLargestRegion(grid, ron[0], ron[1], turns)
    if size==k:
        return "Impressed"
    return "Oops!"

def positionRon(matrix):
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 'M':
                return [i,j]


def findLargestRegion(grid, row, col, turns):
    if row<0 or row>=rows or col<0 or col>=cols:
        return None
    elif grid[row][col]=='X':
        return None
    elif grid[row][col]=='*':
        return turns
    path = 0
    if not row-1<0:
        if grid[row-1][col]=='.' or grid[row-1][col]=='*':
            path += 1
    if not row+1>=rows:
        if grid[row+1][col]=='.' or grid[row+1][col]=='*':
            path += 1
    if not col-1<0:
        if grid[row][col-1]=='.' or grid[row][col-1]=='*':
            path += 1
    if not col+1>=cols:
        if grid[row][col+1]=='.' or grid[row][col+1]=='*':
            path += 1

    
    if path>1:
        turns+=1
        grid[row][col]='1'
    else:
        grid[row][col]='0'
    for x in [[row-1, col], [row+1, col], [row, col-1], [row, col+1]]:
        r = x[0]
        c = x[1]
        if r<0 or r>=rows or c<0 or c>=cols:
            continue
        if grid[r][c] == '1' or grid[r][c] == '0':
            continue
        size = findLargestRegion(grid, r, c, turns)   #RECURSION CALL!
        if size==None:
            continue
        else:
            return size



t = int(input())
for _ in range(t):
    rows, cols = map(int,input().split(' ')) 
    grid = []
    for i in range(rows):
        grid.append(list(input()))
    k = int(input())
    print(countLuck(grid,k))
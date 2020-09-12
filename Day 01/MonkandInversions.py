"""
**Problem**
Monk and Inversions
Monk's best friend Micro, who happen to be an awesome programmer, got him an integer matrix M of size  for his birthday. Monk is taking coding classes from Micro. They have just completed array inversions and Monk was successful in writing a program to count the number of inversions in an array. Now, Micro has asked Monk to find out the number of inversion in the matrix M. Number of inversions, in a matrix is defined as the number of unordered pairs of cells  such that .
Monk is facing a little trouble with this task and since you did not got him any birthday gift, you need to help him with this task.

Input:
First line consists of a single integer T denoting the number of test cases.
First line of each test case consists of one integer denoting N. Following N lines consists of N space separated integers denoting the matrix M.

Output:
Print the answer to each test case in a new line.

"""
#Solution

for _ in range(int(input())):
    N = int(input())
    arr = []
    for k in range(N):
        arr.append(list(map(int,input().strip().split(" "))))
    x = []
    y= []
    for i in range(N):
        for j in range(N):
            x.append((i,j))
            y.append((i,j))
    
    count = 0
    for i,j in x:
        for p,q in y:
            if i<=p and j<=q:
                if(arr[i][j]) > (arr[p][q]):
                    count +=1
    
    print (count)
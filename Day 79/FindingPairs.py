'''

Given an array A of N numbers, find the number of distinct pairs (i, j) such that j >=i and A[i] = A[j].
First line of the input contains number of test cases T. Each test case has two lines, first line is the number N, followed by a line consisting of N integers which are the elements of array A.
For each test case print the number of distinct pairs.

Constraints
1 <= T <= 10
1 <= N <= 10^6
-10^6 <= A[i] <= 10^6 for 0 <= i < N

SAMPLE INPUT 
3
4
1 2 3 4
3
1 2 1
5
1 1 1 1 1

SAMPLE OUTPUT 
4
4
15

'''

i = int(input())
for x in range(0, i):
    j = input()
    l = list(map(int, input().strip().split(" ")))
    minimum = min(l)
    if minimum < 0: 
        l = [i + abs(minimum) for i in l]
    numbers = [0]*(max(l) + 1)
    for k in l:
        numbers[k] += 1#Counting sort
    result = 0
    for j in numbers:
        if j > 0:
            result += j + (j*(j-1))/2# i + nC2, where i is the number, n is count
    print(int(result))
 '''
You are given an array of  integers. The task is to partition the array into an arbitrary number of groups (subarrays) such that bitwise  of beauties of the groups is maximized.
The beauty of a group (subarray) is defined by the bitwise  of all the numbers belonging to that group (subarray).

 

Input format
First line of the input contains the number of test cases  .
Each test case has 2 lines. First line of the test case is the size of the array . Second line has the array elements separated by space.

 

Output format
For each test case, output a single number, the maximum value achievable for the given array.

SAMPLE INPUT 
2
7
4 1 2 5 2 1 6
3
1 2 4

SAMPLE OUTPUT 
7
7

'''

t= int(input())
while t > 0:
    n = int(input())
    a = list(map(int, input().split()))[:n]
    x = 0
    for i in range(n):
        x ^= a[i]
    maxm = x
    y = 0
    z = 0
    for j in range(n):
        y ^= a[j]
        z = y & (y ^ x)
        if z > maxm:
            maxm = z
    print(maxm)
    t -= 1
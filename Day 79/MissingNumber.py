'''

You are given an array A. You can decrement any element of the array by 1. This operation can be repeated any number of times. A number is said to be missing if it is the smallest positive number which is a multiple of 2 that is not present in the array A. You have to find the maximum missing number after all possible decrements of the elements.

Input Format:
The first line of input contains T denoting number if test cases.
The first line of each test case contains N, the size of the array.
The second line of each test case contains N space seperated intergers.

Output Format:
Print the answer for each test case in a new line.

SAMPLE INPUT 
2
6
1 3 3 3 6 7
3
3 0 2

SAMPLE OUTPUT 
8
4

'''

def Solve (arr):
    arr.sort()
    st=2
    for v in arr:
        if v>=st : 
            st+=2
    return st

T = int(input())

for _ in range(T):

    n = int(input())
    arr = list(map(int, input().split()))
    out_ = Solve(arr)
    print (out_)
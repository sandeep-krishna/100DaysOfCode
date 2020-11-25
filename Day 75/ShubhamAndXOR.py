'''

You are given an array of n integer numbers , , .. ,. Calculate the number of pair of indices  such that  <  and  xor 

Input format
- First line: n denoting the number of array elements
- Second line: n space separated integers , , .. ,.

Output format
Output the required number of pairs.

SAMPLE INPUT 
5
1 3 1 4 3

SAMPLE OUTPUT 
2

'''

def sort(arr, n):
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

n = int(input())
arr = list(map(int, input().rstrip().split()))

sort(arr, n)
count = 0
for k in range(n-1):
    if arr[k] == arr[k+1]:
        count = count+1

print(count)
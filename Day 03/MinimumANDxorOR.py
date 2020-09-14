'''
*** Problem ***
Minimum AND xor OR
Given an array  of  integers. Find out the minimum value of the following expression for all valid .

, where .

Input format

First line: A single integer  denoting the number of test cases
For each test case:
First line contains a single integer , denoting the size of the array.
Second line contains  space separated integers 
Output format

For each test case, print a single line containing one integer that represents the minimum value of the given expression

'''

# Solution
def maxAndXor(arr, n): 
  
    ans = float('inf') 
    arr.sort() 
    for i in range(n - 1): 

        ans = min(ans, arr[i] ^ arr[i + 1]) 
  
    return ans 
  
if __name__ == '__main__': 

    for _ in range(int(input())):
          
        N = int(input())
        arr = list(map(int, input().strip().split()))

        print(maxAndXor(arr, N)) 
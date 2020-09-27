'''
Set numbers

You are given the binary representation of a number. You must consider the highest number of set bits in the binary representation to complete your task. For example,  is represented as  in binary and it contains four set bits (1-bits).
You are also given a number  and your task is to determine the number that is less than or equal to  and contains the maximum number of set bits in its binary representation. 
In other words, print a number  that is less than or equal to  such that the number of set bits in the binary representation of  must be maximum

Input format
First line: An integer  denoting the number of test cases
For each test case:
First line: An integer 

Output format
For each test case, print the answer on a new line denoting a number  that is less than or equal to  such that the number of set bits in the binary representation of  must be maximum.  

SAMPLE INPUT 
1
345
SAMPLE OUTPUT 
255
Explanation
The number 255 (< 345) has most number of set bits.
'''
for _ in range(int(input())):
    x = bin(int(input()))
    if all(i == '1' for i in x[2:]):
        print (int(x, 2))
    else:
        print(int('1' * len(x[3:]), 2))
"""
*** Problem ***
Cyclic shift
A large binary number is represented by a string  of size  and comprises of  and . You must perform a cyclic shift on this string.
 The cyclic shift operation is defined as follows:

If the string  is , then after performing one cyclic shift, the string becomes .
You performed the shift infinite number of times and each time you recorded the value of the binary number represented by the string.
 The maximum binary number formed after performing (possibly ) the operation is . Your task is to determine the number of cyclic shifts that can be performed such that the value represented by the string  will be equal to  for the  time.

Input format

First line: A single integer  denoting the number of test cases
For each test case:
First line: Two space-separated integers  and 
Second line:  denoting the string
Output format

For each test case, print a single line containing one integer that represents the number of cyclic shift operations performed such that the value represented by string  is equal to  for the  time.

"""
#Solution
def cycle(a,k):
    i = bin(int(a,2))[2:].zfill(len(a))
    b=i[1:]+i[0]
    maxi = i
    while b!=i: 
        if b>maxi:
            maxi = b
        b= b[1:]+b[0]
    c=0
    b=i
    if i!=maxi:
        while b!=maxi:
            b= b[1:]+b[0]
            c+=1

    b = maxi[1:]+maxi[0]
    d=1
    while b!=maxi:
        d+=1
        b= b[1:]+b[0]
    return c+d*(k-1)
    
for i in range(int(input())):
    n,k = map(int,input().split())
    a = input()
    print(cycle(a,k))

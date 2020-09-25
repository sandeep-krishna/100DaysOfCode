'''
Digit Problem

This time your task is simple.

Given two integers X and K, find the largest number that can be formed by changing digits at atmost K places in the number X.

Input:
First line of the input contains two integers X and K separated by a single space.

Output:
Print the largest number formed in a single line.

SAMPLE INPUT 
4483 2
SAMPLE OUTPUT 
9983

Explanation
First two digits of the number are changed to get the required number.
'''

x, k = map(int, input().split())
x = list(str(x))
for i in range(len(x)):
    if k!= 0:
        if x[i] != '9':
            x[i] = '9'
            k -= 1
        else:
            continue
print(''.join(x))
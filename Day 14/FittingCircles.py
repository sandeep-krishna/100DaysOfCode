'''
Fitting circles

You are given a rectangle of length  and width . You are required to determine a circle that contains the maximum circumference that fits inside the rectangle. This type of circle is called a big circle. Your task is to determine the maximum number of big circles that can fit inside the rectangle. 

Input format
First line: An integer t denoting the number of test cases
First line of each test case: Integers a and b

Output format
For each test case, print the answer on a new line denoting the maximum number of big circles that can fit in the provided rectangle.  

SAMPLE INPUT 
1
40 10
SAMPLE OUTPUT 
4
Explanation
4 circles of radius 10 can fit inside the rectangle.

'''

for i in range(int(input())):
    a, b = map(int, input().split())
    print(max(a, b) // min(a, b))
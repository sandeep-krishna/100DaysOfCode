'''
Given a sequence of  integers,  where each element is distinct and satisfies . For each  where , find any integer  such that  and print the value of  on a new line.

Function Description
Complete the permutationEquation function in the editor below. It should return an array of integers that represent the values of .
permutationEquation has the following parameter(s):
p: an array of integers

Input Format
The first line contains an integer , the number of elements in the sequence.
The second line contains  space-separated integers  where .

Output Format

For each  from  to , print an integer denoting any valid  satisfying the equation  on a new line.
Sample Input 0
3
2 3 1

Sample Output 0
2
3
1
'''

n = int(input())
numbers = [int(num) for num in input().split()]

for x in range(n):
    print(numbers.index(numbers.index(x + 1) + 1) + 1)
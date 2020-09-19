'''
Find Product

You have been given an array A of size N consisting of positive integers. You need to find and print the product of all the number in this array Modulo .

Input Format:
The first line contains a single integer N denoting the size of the array. The next line contains N space separated integers denoting the elements of the array

Output Format:
Print a single integer denoting the product of all the elements of the array Modulo .

SAMPLE INPUT 
5
1 2 3 4 5
SAMPLE OUTPUT 
120
'''

n= int(input())
A = list(map(int,input().split()))
answer =1
for i in A:
    answer = ( answer * i) % (pow(10,9)+7)
print (answer)
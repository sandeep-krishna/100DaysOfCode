'''
Divisible
You are given an array  of size  that contains integers. Here,  is an even number. You are required to perform the following operations:

Divide the array of numbers in two equal halves
Note: Here, two equal parts of a test case are created by dividing the array into two equal parts.
Take the first digit of the numbers that are available in the first half of the array (first 50% of the test case)
Take the last digit of the numbers that are available in the second half of the array (second 50% of the test case)
Generate a number by using the digits that have been selected in the above steps
Your task is to determine whether the newly-generated number is divisible by .

Input format

First line: A single integer  denoting the size of array 
Second line:  space-separated integers denoting the elements of array 
Output format
If the newly-generated number is divisible by , then print . Otherwise, print .

Constraints
 

SAMPLE INPUT 
6
15478 8452 8232 874 985 4512
SAMPLE OUTPUT 
OUI
Explanation
The first digit of 15478 is 1.
The first digit of 8452 is 8.
The first digit of 8232 is 8.
The last digit of 874 is 4.
The last digit of 985 is 5.
The last digit of 4512 is 2.
The newly generated number will be 188452 which is divisible by 11. 
'''
n=int(input())
a=list(map(int,input().split()))
h=int(n/2)
b1=""
res=""

for i in range(h):
   cur=a[i]
   b1=str(cur)
   res+=b1[0]

for i in range(h,n):
   cur=a[i]
   b1=str(cur)
   res+=b1[-1]

if int(res)%11 == 0:
   print('OUI')
else:
   print('NON')


#One liner
def solve (A):
    return "OUI" if int("".join([A[i][0] if i<len(A)//2 else A[i][-1] for i in range(N)]))%11==0 else "NON"
N = int(input())
A = input().split()
out_ = solve(A)
print (out_)
'''

Divisibility

You are provided an array  of size  that contains non-negative integers. Your task is to determine whether the number that is formed by selecting the last digit of all the N numbers is divisible by .
Note: View the sample explanation section for more clarification.

Input format

First line: A single integer  denoting the size of array 
Second line:  space-separated integers.
Output format
If the number is divisible by , then print . Otherwise, print .

SAMPLE INPUT 
5
85 25 65 21 84
SAMPLE OUTPUT 
No

Explanation
Last digit 85 of  is 5.
Last digit 25 of  is 5.
Last digit 65 of  is 5.
Last digit 21 of  is 1.
Last digit 84 of  is 4.
Therefore the number 55514 formed is  which is not divisible by 10 .
'''

N = int(input())
data = [int(x) for x in input().split()]

if(data[-1]%10==0):
    print("Yes")

else:
    print("No")
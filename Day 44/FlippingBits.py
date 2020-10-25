'''
You will be given a list of 32 bit unsigned integers. Flip all the bits ( and ) and print the result as an unsigned integer.

For example, your decimal input . We're working with 32 bits, so:



Function Description
Complete the flippingBits function in the editor below. It should return the unsigned decimal integer result.
flippingBits has the following parameter(s):
n: an integer

Input Format
The first line of the input contains , the number of queries.
Each of the next  lines contain an integer, , to process.

Output Format
Output one line per element from the list with the decimal value of the resulting unsigned integer.

Sample Input 0
3
2147483647
1
0

Sample Output 0
2147483648
4294967294
4294967295

'''

#!/bin/python3

import math
import os
import random
import re
import sys


#Complete the flippingBits function below.
def flippingBits(n):
    # ^ = bitwise XOR
    return n ^ 4294967295


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        result = flippingBits(n)

        fptr.write(str(result) + '\n')

    fptr.close()

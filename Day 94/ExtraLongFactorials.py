'''

The factorial of the integer , written , is defined as:

Calculate and print the factorial of a given integer.

For example, if , we calculate  and get .

Function Description

Complete the extraLongFactorials function in the editor below. It should print the result and return.

extraLongFactorials has the following parameter(s):

n: an integer
Note: Factorials of  can't be stored even in a  long long variable. Big integers must be used for such calculations. Languages like Java, Python, Ruby etc. can handle big integers, but we need to write additional code in C/C++ to handle huge values.

We recommend solving this challenge using BigIntegers.

Input Format

Input consists of a single integer 

Constraints


Output Format

Print the factorial of .

Sample Input
25

Sample Output
15511210043330985984000000


'''


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the extraLongFactorials function below.
def extraLongFactorials(n):
    cache = {}
    def rec(n):
        if n in cache:
            return cache[n]
        if n == 1:
            return 1
        result = n * rec(n-1)
        cache[n] = result
        return result
    return rec(n)

if __name__ == '__main__':
    n = int(input())

    print(extraLongFactorials(n))

'''

Lexicographical order is often known as alphabetical order when dealing with strings. A string is greater than another string if it comes later in a lexicographically sorted list.

Given a word, create a new word by swapping some or all of its characters. This new word must meet two criteria:

It must be greater than the original word
It must be the smallest word that meets the first condition
For example, given the word , the next largest word is .

Complete the function biggerIsGreater below to create and return the new string meeting the criteria. If it is not possible, return no answer.

Function Description

Complete the biggerIsGreater function in the editor below. It should return the smallest lexicographically higher string possible from the given string or no answer.

biggerIsGreater has the following parameter(s):

w: a string
Input Format

The first line of input contains , the number of test cases.
Each of the next  lines contains .

Constraints

 will contain only letters in the range ascii[a..z].
Output Format

For each test case, output the string meeting the criteria. If no answer exists, print no answer.

Sample Input 0

5
ab
bb
hefg
dhck
dkhc
Sample Output 0

ba
no answer
hegf
dhkc
hcdk

'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the biggerIsGreater function below.
def biggerIsGreater(w):
    # Converting str into list for easier access
    word = list(w)
    i = j = l = len(word) - 1
    while i > 0 and word[i - 1] >= word[i]:
        i -= 1
    if i <= 0:
        return 'no answer'
    while word[j] <= word[i - 1]:
        j -= 1
    word[i - 1], word[j] = word[j], word[i - 1]
    word[i:] = word[l:i - 1:-1]
    return ''.join(word)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

        fptr.write(result + '\n')

    fptr.close()

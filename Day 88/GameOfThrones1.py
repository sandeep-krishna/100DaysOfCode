'''

Dothraki are planning an attack to usurp King Robert's throne. King Robert learns of this conspiracy from Raven and plans to lock the single door through which the enemy can enter his kingdom.

But, to lock the door he needs a key that is an anagram of a palindrome. He starts to go through his box of strings, checking to see if they can be rearranged into a palindrome.
For example, given the string , one way it can be arranged into a palindrome is .

Function Description
Complete the gameOfThrones function below to determine whether a given string can be rearranged into a palindrome. If it is possible, return YES, otherwise return NO.
gameOfThrones has the following parameter(s):
s: a string to analyze

Input Format
A single line which contains , the input string.

Constraints
 |s| 
 contains only lowercase letters in the range 

Output Format
A single line which contains YES or NO.

Sample Input 0
aaabbbb

Sample Output 0
YES

'''


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the gameOfThrones function below.
def gameOfThrones(s):
    a = set(s)
    li = [1 for ele in a if s.count(ele) % 2 == 1]
    if sum(li) > 1:
        return "NO"
    return "YES"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = gameOfThrones(s)

    fptr.write(result + '\n')

    fptr.close()
        
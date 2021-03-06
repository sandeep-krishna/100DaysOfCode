'''

Julius Caesar protected his confidential information by encrypting it using a cipher. Caesar's cipher shifts each letter by a number of letters. If the shift takes you past the end of the alphabet, just rotate back to the front of the alphabet. In the case of a rotation by 3, w, x, y and z would map to z, a, b and c.

Original alphabet:      abcdefghijklmnopqrstuvwxyz
Alphabet rotated +3:    defghijklmnopqrstuvwxyzabc
For example, the given cleartext  and the alphabet is rotated by . The encrypted string is .

Note: The cipher only encrypts letters; symbols, such as -, remain unencrypted.

Function Description

Complete the caesarCipher function in the editor below. It should return the encrypted string.

caesarCipher has the following parameter(s):

s: a string in cleartext
k: an integer, the alphabet rotation factor
Input Format

The first line contains the integer, , the length of the unencrypted string.
The second line contains the unencrypted string, .
The third line contains , the number of letters to rotate the alphabet by.

Constraints

 n is a valid ASCII string without any spaces.

Output Format

For each test case, print the encoded string.

Sample Input

11
middle-Outz
2
Sample Output

okffng-Qwvb

'''


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the caesarCipher function below.
def caesarCipher(s, k):
    alphabets = [i for i in 'abcdefghijklmnopqrstuvwxyz']
    alphabets += alphabets*k
    s = [i for i in s]

    for i in range(len(s)):
        if s[i].isalpha() ==True:
            if s[i].isupper():
                 s[i] = alphabets[alphabets.index(s[i].lower())+k].upper()
            else:
                 s[i] = alphabets[alphabets.index(s[i].lower())+k]

    return "".join(s)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    k = int(input())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()

'''

An English text needs to be encrypted using the following encryption scheme.
First, the spaces are removed from the text. Let  be the length of this text.
Then, characters are written into a grid, whose rows and columns have the following constraints:

For example, the sentence , after removing spaces is  characters long.  is between  and , so it is written in the form of a grid with 7 rows and 8 columns.

ifmanwas  
meanttos          
tayonthe  
groundgo  
dwouldha  
vegivenu  
sroots
Ensure that 
If multiple grids satisfy the above conditions, choose the one with the minimum area, i.e. .
The encoded message is obtained by displaying the characters in a column, inserting a space, and then displaying the next column and inserting a space, and so on. For example, the encoded message for the above rectangle is:

imtgdvs fearwer mayoogo anouuio ntnnlvt wttddes aohghn sseoau

You will be given a message to encode and print.

Function Description

Complete the encryption function in the editor below. It should return a single string composed as described.

encryption has the following parameter(s):

s: a string to encrypt
Input Format

One line of text, the string 

Constraints


 is comprised only of characters in the range ascii[a-z].

Output Format

Print the encoded message on one line as described.

Sample Input

haveaniceday
Sample Output 0

hae and via ecy

'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the encryption function below.
def encryption(s):
    n = 0
    st = math.ceil(math.sqrt(len(s)))
    res = ""

    for i in range(n, st, 1):
        res += s[n::st]+" "
        n += 1

    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()

'''

Sami's spaceship crashed on Mars! She sends a series of SOS messages to Earth for help.

NASA_Mars_Rover.jpg

Letters in some of the SOS messages are altered by cosmic radiation during transmission. Given the signal received by Earth as a string, , determine how many letters of Sami's SOS have been changed by radiation.

For example, Earth receives SOSTOT. Sami's original message was SOSSOS. Two of the message characters were changed in transit.

Function Description

Complete the marsExploration function in the editor below. It should return an integer representing the number of letters changed during transmission.

marsExploration has the following parameter(s):

s: the string as received on Earth
Input Format

There is one line of input: a single string, .

Note: As the original message is just SOS repeated  times, 's length will be a multiple of .

Constraints

 will contain only uppercase English letters, ascii[A-Z].
Output Format

Print the number of letters in Sami's message that were altered by cosmic radiation.

Sample Input 0

SOSSPSSQSSOR
Sample Output 0

3


'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the marsExploration function below.
def marsExploration(s):
    return sum(s[i] != "SOS"[i%3] for i in range(len(s)))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()

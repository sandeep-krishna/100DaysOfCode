'''
Given a string, , we define some operations on the string as follows:
a.  denotes the string obtained by reversing string . Example: 
b.  denotes any string that's a permutation of string . Example: 
c.  denotes any string that's obtained by interspersing the two strings  & , maintaining the order of characters in both. For example,  & , one possible result of  could be , another could be , another could be  and so on.
Given a string  such that  for some string , find the lexicographically smallest .
For example, . We can split it into two strings of . The reverse is  and we need to find a string to shuffle in to get . The middle two characters match our reverse string, leaving the  and  at the ends. Our shuffle string needs to be . Lexicographically , so our answer is .
Function Description
Complete the reverseShuffleMerge function in the editor below. It must return the lexicographically smallest string fitting the criteria.
reverseShuffleMerge has the following parameter(s):
s: a string

Input Format
A single line containing the string .

Constraints
 contains only lower-case English letters, ascii[a-z]
Output Format
Find and return the string which is the lexicographically smallest valid .

Sample Input 0
eggegg

Sample Output 0
egg

'''
#!/bin/python3

import math
import os
import random
import re
import sys
import collections

# Complete the reverseShuffleMerge function below.
def frequency(s):
    res = collections.defaultdict(int)
    for char in s:
        res[char] += 1
    return res

# Complete the reverseShuffleMerge function below.
def reverseShuffleMerge(s):
    char_freq = frequency(s)
    used_chars = collections.defaultdict(int)
    remain_chars = dict(char_freq)
    res = []
    
    def can_use(char):
        return (char_freq[char] // 2 - used_chars[char]) > 0
    
    def can_pop(char):
        needed_chars = char_freq[char] // 2
        return used_chars[char] + remain_chars[char] - 1 >= needed_chars
    
    for char in reversed(s):
        if can_use(char):
            while res and res[-1] > char and can_pop(res[-1]):
                removed_char = res.pop()
                used_chars[removed_char] -= 1
            
            used_chars[char] += 1
            res.append(char)
        
        remain_chars[char] -= 1
    
    return "".join(res)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = reverseShuffleMerge(s)

    fptr.write(result + '\n')

    fptr.close()

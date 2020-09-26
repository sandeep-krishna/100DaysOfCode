'''
One String No Trouble

A string  is called a good string if and only if two consecutive letters are not the same. For example,  and   are good while  and  are not.
You are given a string . Among all the good substrings of  ,print the size of the longest one.

Input format
A single line that contains a string  ().

Output format
Print an integer that denotes the size of the longest good substring of .

SAMPLE INPUT 
ab

SAMPLE OUTPUT 
2

Explanation
The complete string is good so the answer is .
'''

s = input()
count = 1
ans = []
for i in range(len(s)-1):
       if s[i]!=s[i+1]:
               count+=1
       elif (s[i]==s[i+1]):
               ans.append(count)
               count = 1
print(max(max(ans),count)) if ans else print(count)
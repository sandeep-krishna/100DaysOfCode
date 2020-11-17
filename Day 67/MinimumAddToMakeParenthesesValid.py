'''

Given a string S of '(' and ')' parentheses, we add the minimum number of parentheses ( '(' or ')', and in any positions ) so that the resulting parentheses string is valid.

Formally, a parentheses string is valid if and only if:
It is the empty string, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
Given a parentheses string, return the minimum number of parentheses we must add to make the resulting string valid.

SAMPLE INPUT 
()))((

SAMPLE OUTPUT 
4

'''

s=input()
stack=[]
count=0

for i in s:
    if i == '(':
        stack.append(i)
    else:
        count +=1


    if len(stack)>0 and stack[-1]=='(' and i == ')':
        stack.pop()
        count -=1

print(len(stack)+count)
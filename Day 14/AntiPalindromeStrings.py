'''
Anti-palindrome strings

You are given a string  containing only lowercase alphabets. You can swap two adjacent characters any number of times (including 0).

A string is called anti-palindrome if it is not a palindrome. If it is possible to make a string anti-palindrome, then find the lexicographically smallest anti-palindrome. Otherwise, print .

Input format
The first line contains a single integer  denoting the number of test cases. The description of  test cases follows.
Each line contains a string  of lower case alphabets only.

Output format
For each test case, print the answer in a new line.

Constraints
contains only lowercase alphabets.

SAMPLE INPUT 
4
bpc
pp
deep
zyx
SAMPLE OUTPUT 
bcp
-1
deep
xyz

Explanation
In the first test case, you can create "bcp" which is not a palindrome and it is a lexicographically-smallest string.
In the second test case, you cannot form any anti palindrome.

'''

for _ in range(int(input())):
      x=list(input())
      if x[::]==x[::-1]:
           print(-1)
      else:
           print(''.join(sorted(x)))
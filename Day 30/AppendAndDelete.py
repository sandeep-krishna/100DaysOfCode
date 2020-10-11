'''

You have a string of lowercase English alphabetic letters. You can perform two types of operations on the string:

Append a lowercase English alphabetic letter to the end of the string.
Delete the last character in the string. Performing this operation on an empty string results in an empty string.
Given an integer, , and two strings,  and , determine whether or not you can convert  to  by performing exactly  of the above operations on . If it's possible, print Yes. Otherwise, print No.

For example, strings  and . Our number of moves, . To convert  to , we first delete all of the characters in  moves. Next we add each of the characters of  in order. On the  move, you will have the matching string. If there had been more moves available, they could have been eliminated by performing multiple deletions on an empty string. If there were fewer than  moves, we would not have succeeded in creating the new string.

Function Description

Complete the appendAndDelete function in the editor below. It should return a string, either Yes or No.

appendAndDelete has the following parameter(s):

s: the initial string
t: the desired string
k: an integer that represents the number of operations
Input Format

The first line contains a string , the initial string.
The second line contains a string , the desired final string.
The third line contains an integer , the number of operations.

Output Format
Print Yes if you can obtain string  by performing exactly  operations on . Otherwise, print No.

Sample Input 0
hackerhappy
hackerrank
9

Sample Output 0
Yes

'''

s = input().strip()
t = input().strip()
k = int(input().strip())

numSameChars = min(len(s), len(t))
for i in range(len(t)):
    if s[:i] != t[:i]:
        numSameChars = i-1
        break

diff = len(s)-numSameChars + len(t)-numSameChars
print('Yes' if (diff <= k and diff%2 == k%2) or len(s) + len(t) < k else 'No')
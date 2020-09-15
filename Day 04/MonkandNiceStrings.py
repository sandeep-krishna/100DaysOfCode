'''
*** Problem ***

Monk and Nice Strings
Monk's best friend Micro's birthday is coming up. Micro likes Nice Strings very much, so Monk decided to gift him one. Monk is having N nice strings, so he'll choose one from those. But before he selects one, he need to know the Niceness value of all of those. Strings are arranged in an array A, and the Niceness value of string at position i is defined as the number of strings having position less than i which are lexicographicaly smaller than . Since nowadays, Monk is very busy with the Code Monk Series, he asked for your help.
Note: Array's index starts from 1.

Input:
First line consists of a single integer denoting N.
N lines follow each containing a string made of lower case English alphabets.

Output:
Print N lines, each containing an integer, where the integer in  line denotes Niceness value of string .
'''

# Solution

n = int(input())
a = []
for i in range(n):
    a.append(input())
    ans = 0
    for j in a:
        if j < a[i]:
            ans += 1
    print(ans)
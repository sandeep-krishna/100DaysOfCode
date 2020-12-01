'''

You are given a string S. S consists of several words separated by one or more spaces. Word consists of Latin letters as well as other symbols (but not spaces).
In each word which starts from lowercase Latin letter replace starting letter with uppercase Latin letter.

Input
The only line contains S

Output
Output one line with modified string S.

Constraints
1 <= length of S <= 30 000

SAMPLE INPUT 
Wish you were here

SAMPLE OUTPUT 
Wish You Were Here

'''

ip = input()
ans = ip[0].upper()
for i in range(1,len(ip)):
    if ip[i] != " " and ip[i-1] == " ":
        ans += ip[i].upper()
    else:
        ans += ip[i]
print(ans)
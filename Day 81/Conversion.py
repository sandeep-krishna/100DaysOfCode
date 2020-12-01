'''

Given a string, convert it into its number form .

A or a -> 1
B or b -> 2
C or c -> 3
. . .
Z or z -> 26
space -> $

Input:
test cases, t
string , s
Output:

Desired O/p
Constraints: string length <=200

SAMPLE INPUT 
2
AMbuj verma
Aaaa bBBB

SAMPLE OUTPUT 
11322110$22518131
1111$2222

'''

for i in range(int(input())):
    s=input()
    ans=""
    for i in range(len(s)):
        if(s[i].islower()):
            x=ord(s[i])-ord('a')+1
            ans+=str(x)

        elif s[i].isupper():
            x=ord(s[i])-ord('A')+1
            ans+=str(x)
        else:
            ans+='$'
    print(ans)


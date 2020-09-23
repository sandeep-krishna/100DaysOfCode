'''

Ali and Helping innocent people

Arpasland has surrounded by attackers. A truck enters the city. The driver claims the load is food and medicine from Iranians. Ali is one of the soldiers in Arpasland. He doubts about the truck, maybe it's from the siege. He knows that a tag is valid if the sum of every two consecutive digits of it is even and its letter is not a vowel. 
Determine if the tag of the truck is valid or not.
We consider the letters "A","E","I","O","U","Y" to be vowels for this problem.

Input Format
The first line contains a string of length 9. The format is "DDXDDD-DD", where D stands for a digit (non zero) and X is an uppercase english letter.

Output Format
Print "valid" (without quotes) if the tag is valid, print "invalid" otherwise (without quotes)

SAMPLE INPUT 
12X345-67
SAMPLE OUTPUT 
invalid
Explanation
The tag is invalid because the sum of first and second digit of it is odd (also the sum of 4'th and 5'th, 5'th and 6'th and 8'th and 9'th are odd).
'''

s=input().upper()
vow=['A','E','I','O','U','Y']
count=0
if (int(s[0])+int(s[1]))%2==0 and (int(s[3])+int(s[4]))%2==0 and (int(s[4])+int(s[5]))%2==0 and (int(s[7])+int(s[8]))%2==0:
    for i in range(0,len(vow)):
        if s[2]==vow[i]:
            count=1
            break

    if count==1:
        print("invalid")

    else:
        print("valid")

else:
    print("invalid")
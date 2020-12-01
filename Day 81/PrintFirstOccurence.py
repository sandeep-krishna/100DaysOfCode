'''

Given a string containing only lower case letters ,print first occurrence of all the letters present in that order only.
Input :
Test cases, t
string ,s

Output :
Desired Output

Constraint :
string length <=200

SAMPLE INPUT 
2
aasdvasvavda
sajhags

SAMPLE OUTPUT 
asdv
sajhg

'''

for i in range(int(input())):
    print("".join(list(dict.fromkeys(input()))))
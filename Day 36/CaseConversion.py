'''
You are given a string  in the camel case format. Your task is to convert this string into the snake case format.

Examples of the camel case strings are as follows:

ComputerHope
FedEx
WordPerfect
Note: In the camel case string, the first character may or may not be capitalized.

Examples of the snake case strings are as follows:

computer_hope
fed_ex
word_perfect
Input format

First line:  denotes the number of test cases
Next  lines: String 
Output format
For each test case, print the snake case format of the given camel case in the string  in a new line.

Constraints


, where  indicates the length of string 

String  is made of lower and upper case English alphabets

SAMPLE INPUT 
6
HackerEarth
primeCheck
OddOrEven
random
getRandom
macOS
SAMPLE OUTPUT 
hacker_earth
prime_check
odd_or_even
random
get_random
mac_o_s
'''

def caseConversion (s):
    k=list(s)
    m=[]
    for i in range(len(k)):
        if(i!=0):
            if(k[i].isupper()):
                m.append("_")
                j=k[i].lower()
                m.append(j)
            else:
                m.append(k[i])
        else:
            g=k[i].lower()
            m.append(g)
    return "".join(m)
for _ in range(int(input())):
    s = input()
    out_ = caseConversion(s)
    print (out_)

 
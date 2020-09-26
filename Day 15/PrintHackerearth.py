from collections import Counter
'''
As a beginner to the programming, Mishki came to Hackerearth platform, to become a better programmer. She solved some problems and felt very confident. Later being a fan of Hackerearth, she gave a problem to her friends to solve. They will be given a string containing only lower case characters (a-z), and they need to find that by using the characters of the given string, how many times they can print "hackerearth"(without quotes). As they are new to programming world, please help them.

Input:
The first line will consists of one integer N denoting the length of string.
Next line will contain the string  containing only lower case characters.

Output:
Print one integer, denoting the number of times her friends can print "hackerearth" (without quotes).

Each character of string  will be in range 
SAMPLE INPUT 
13
aahkcreeatrha
SAMPLE OUTPUT 
1
'''

n=int(input())
s=input()
l=Counter(s)
h=l['h']//2
a=l['a']//2
c=l['c']
k=l['k']
e=l['e']//2
r=l['r']//2
t=l['t']

print(min(h,a,c,k,e,r,t))
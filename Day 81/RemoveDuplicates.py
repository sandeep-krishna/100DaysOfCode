'''

input:
Input contain a single string S.

Output:
Print the string S with no any duplicate characters.

Constraints:
Test Files 1 to 5:
1<=|S|<=100
Test Files 6 to 10:
1<=|S|<=100000

Sample Output #1
hacker

Sample Output #1
hacker

Sample Input #2
hackerearth

Sample Output #2
hackert

Sample Input #3
programming

Sample Output #3
progamin

SAMPLE INPUT 
iloveprogramming

SAMPLE OUTPUT 
iloveprgamn

'''


print("".join(list(dict.fromkeys(input()))))
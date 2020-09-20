'''
Seven Segment Display

You all must have seen a seven segment display.If not here it is:
Alice got a number written in seven segment format where each segment was creatted used a matchstick.

Example: If Alice gets a number 123 so basically Alice used 12 matchsticks for this number.

Alice is wondering what is the numerically largest value that she can generate by using at most the matchsticks that she currently possess.Help Alice out by telling her that number.

Input Format:
First line contains T (test cases).
Next T lines contain a Number N.

Output Format:
Print the largest possible number numerically that can be generated using at max that many number of matchsticks which was used to generate N.

SAMPLE INPUT 
2
1
0
SAMPLE OUTPUT 
1
111

Explanation
If you have 1 as your number that means you have 2 match sticks.You can generate 1 using this.

If you have 0 as your number that means you have 6 match sticks.You can generate 111 using this.
'''
d = {'0' :6,'1':2,'2':5,'3':5,'4':4,'5': 5,'6':6,'7':3,'8':7,'9': 6} 

for _ in range(int(input())):
    stick = 0
    one=0
    for ch in input():
        stick += d[ch]
        one = stick // 2
    if stick % 2:
        ans = '7' + '1'*(one-1)
    else:
        ans = '1'*one
    print(ans)


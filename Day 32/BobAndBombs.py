'''
Bob and Khatu are brave soldiers in World War 3. They have spotted an enemy troop which is planting bombs. They sent message to the command centre containing characters W and B where W represents a wall and B represents a Bomb. They asked command to tell them how many walls will be destroyed if all bombs explode at once. One bomb can destroy 2 walls on both sides.

Input:
First line of input contains number of test cases T. Each test case contains a single string which contains two type of chars 'W' and 'B'.

Output:
For each test case print the total number of destroyed wall.

Constraints:
1 ≤ T ≤ 10
1 ≤ |S| ≤ 105

SAMPLE INPUT 
3
WBW
WWBWWBW
BWWWBWBWW

SAMPLE OUTPUT 
2
5
6

'''

t = int(input())
for _ in range(t):
    s = list(input())
    count=0
    for i in range(len(s)):
        if s[i] == "B":
            if i - 2 >= 0 and s[i-2]=="W":
                s[i-2]="_"
                count+=1
            if i - 1 >= 0 and s[i-1]=="W":
                s[i-1]="_"
                count+=1
            if i+1 <len(s) and s[i+1]=="W":
                s[i+1]="_"
                count+=1
            if i+2<len(s) and s[i+2]=="W":
                s[i+2]="_"
                count+=1
    print(count)
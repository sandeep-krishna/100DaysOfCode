'''

Alice and Bob are very good friends. They keep on playing some strange games. Today Alice came up with a new game, in which each player gets  cards at the start. Each card has it's value printed on it.
The game proceeds as each player chooses a random card and shows it's value. The player having card with higher value wins. As Alice came up with this game, he wants to ensure his win. So he starts to increase value of some cards using an algorithm. To increase the value of a card by , the running time of algorithm is  seconds.
Find the minimum running time of algorithm, ensuring the win of Alice.

Input:
First line of input contains an integer  denoting the number of TestCases.
First line of Each testcase contains two Integers  and .
Next two lines of each TestCase contains  integers, each denoting value of cards of Alice and Bob respectively.
    
Output:
Print a single line for each TestCase, running time of algorithm to ensure the win for Alice.  
    
SAMPLE INPUT 
3
5 3
8 9 10 23 4
7 9 2 3 13
6 8
8 99 23 1 3 0
9 32 22 45 3 2
3 2
1 1 0
5 8 9

SAMPLE OUTPUT 
75
1560
56

'''



for i in range(int(input())):
   n,k=map(int,input().split())
   alice=list(map(int,input().split()))
   bob=list(map(int,input().split()))
   c=max(bob)+1
   ans=0
   for i in alice:
       if(i<c):
           d=c-i
           d*=k
           ans+=d
   print(ans)
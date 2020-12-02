'''

Moriarty is planning to plant a bomb in the city. City is organized in such a way that only similar continuous blocks gets affected by such attacks. Moriarty have the information of the arrangement of blocks. Help him to calculate maximum number of blocks that can be destroyed.

INPUT
First line of input contains N denoting number of blocks.
Then for following N space separated number denotes type of block.


OUTPUT
Output maximum number of blocks that can be destroyed by Moriarty.
Note: Blocks are of only 2 types (0 or 1). And City is considered to be linear.


CONSTRAINTS
1<= N <= 10^8

SAMPLE INPUT 
5
0 1 1 0 1

SAMPLE OUTPUT 
2

'''

n=int(input())
a=''.join(input().split())
x=max (a.split("1"))
y=max (a.split("0"))
 
print(max(len(x),len(y)))
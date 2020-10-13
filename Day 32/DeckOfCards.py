'''
Heman, Anil and Soubhik are playing a fun card game. They have an orderd deck of N cards numbered from 1 to N with the card 1 at the top and card N at the bottom.

Heman and Anil both perform an operation on the deck as long as there is exactly 1 card on the deck. Heman will throw away the card on the top and then Anil moves the card that is now on the top of the deck to the bottom. Soubhik has to find number on the final card left in the deck, your job is to help him to do so.

Input:
The first line contains a number T denoting the number of test cases.
Each of the next T lines contains a number N denoting the number of cards.

Output:
For each test case print the required answer in a new line.

SAMPLE INPUT 
5
2
3
5
8
4

SAMPLE OUTPUT 
2
2
2
8
4
'''
for _ in range(int(input())):
     n=int(input());s=1
     while(n!=1):
          if(2**s>n):break
          s+=1
     s-=1

     if(n==1):
         print(n)

     elif(2**s==n):
         print(n)

     else:
         print((n-2**s)*2)
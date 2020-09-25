'''
City Travel

You are going from City A to City B. The distance between A and B is  km. In the most days, you can go at most  km one day. But there are  exceptions, in the  th day, you can go at most  km.
 You need to find out the minimum number of days required to reach city  from city . 

Input Format
First line contains three integers, .
The  th line contains two integers .
It's guaranteed any two  are different. Note that  is not sorted.

Output Format
One integer represents the answer.

SAMPLE INPUT 
21 5 2
2 4
4 8

SAMPLE OUTPUT 
4

Explanation

In the first day, you walked km.
In the second day, you walked km.
In the third day, you walked km.
In the fourth day, you walked km and arrived.
'''

import math 
if __name__ == "__main__": 
   S,X,N = map(int,input().split()) 
   days = 0 
   distance = S 
   TY = [] 
   defDays = math.ceil(S/X) 
   for i in range(N): 
       TY.append(list(map(int,input().split()))) 
    
   TY.sort() 
   i = 0 
   pas = 0 
   while distance > 0: 
       if i <N: 
           if TY[i][0]-1 == days: 
               distance -= TY[i][1] 
               days += 1 
               i += 1 
           else: 
               Ti = TY[i][0] 
               Tj = TY[i-1][0]+1 if i>0 else 1 
               yGap = (Ti - Tj)*X 
               if yGap<distance: 
                   distance -= yGap 
                   days += yGap//X 
               else: 
                   i=N 
       else: 
           days += math.ceil(distance/X) 
           distance -= X*math.ceil(distance/X) 
    
   print(days)
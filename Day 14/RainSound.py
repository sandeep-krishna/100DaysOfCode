'''
Rain sound
You like the sound of rain only if the sound ranges from  to  units. Every cloud makes  unit of sound. Determine the minimum and the maximum number of clouds that can produce the sound in the provided range.

Input format
First line: One integer  denoting the number of test cases
Next  lines: Three integers  and  denoting the provided range of the rain sound and the units of sound produced by each cloud

Output format
In  lines, print two space-separated integers that represent the minimum and the maximum number of the clouds that can produce the sound in the provided range.
Note: Print  if no answer is available.

SAMPLE INPUT 
3
5 10 3
7 12 4
50 60 1

SAMPLE OUTPUT 
2 3
2 3
50 60
'''

import math
for _ in range(int(input())):
    l,r,s = map(int,input().split())
    x=math.ceil(l/s)
    y=math.floor(r/s)
    if (x>y):
        print(-1,-1)
    else:
        print(x,y)
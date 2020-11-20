'''

You have  rectangles. A rectangle is golden if the ratio of its sides is in between , both inclusive. Your task is to find the number of golden rectangles.

Input format

First line: Integer  denoting the number of rectangles
Each of the  following lines: Two integers  denoting the width and height of a rectangle
Output format

Print the answer in a single line.
Constraints



SAMPLE INPUT 
5
10 1
165 100
180 100
170 100
160 100

SAMPLE OUTPUT 
3

'''

n = int(input())
a = [list(map(int,input().split())) for i in range(n)]
print(sum(1 for i in a if max(i)/min(i)>=1.6 and max(i)/min(i)<=1.7))
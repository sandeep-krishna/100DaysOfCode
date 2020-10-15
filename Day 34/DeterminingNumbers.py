'''
You are given an array of integers. The special property of the array is that exactly two different elements occur once while other elements occur twice.
You are required to determine those two elements.

Input format
First line: Integer  denoting the number of elements in the array
Second line:  space-separated integers denoting the values in the array

Output format
Print two space-separated integers that occur once in the array in ascending order.


SAMPLE INPUT 
8
1 2 3 4 5 5 3 4

SAMPLE OUTPUT 
1 2

Explanation
The numbers other than 1 and 2 occur twice, hence, the answer is 1 and 2.
'''


from collections import Counter
int(input())
array = tuple(map(int, input().split()))
elements = []
counts = Counter(array)
for key in counts:
        if counts[key]==1:
                elements.append(key)
elements.sort()
for ele in elements:
          print(ele, end=' ')
#HackerRank
'''
Frequency Queries
You are given  queries. Each query is of the form two integers described below:
-1 x  : Insert x in your data structure.
-2 y  : Delete one occurence of y from your data structure, if present.
-3 z : Check if any integer is present whose frequency is exactly . If yes, print 1 else 0.

The queries are given in the form of a 2-D array  of size  where  contains the operation, and  contains the data element. For example, you are given array . The results of each operation are:

Operation   Array   Output
(1,1)       [1]
(2,2)       [1]
(3,2)                   0
(1,1)       [1,1]
(1,1)       [1,1,1]
(2,1)       [1,1]
(3,2)                   1
Return an array with the output: .

Function Description
Complete the freqQuery function in the editor below. It must return an array of integers where each element is a  if there is at least one element value with the queried number of occurrences in the current array, or 0 if there is not.
freqQuery has the following parameter(s):
queries: a 2-d array of integers

Input Format
The first line contains of an integer , the number of queries.
Each of the next  lines contains two integers denoting the 2-d array .


Output Format
Return an integer array consisting of all the outputs of queries of type .

Sample Input 
8
1 5
1 6
3 2
1 10
1 10
1 6
2 5
3 2

Sample Output 
0
1
'''

#!/bin/python3

import math
import os
import random
import re
import sys
import collections
# Complete the freqQuery function below.
def freqQuery(queries):
    count = dict()
    result = list()
    for q in queries: 
        if q[0] == 1:
            try:
                count[q[1]] += 1
            except:
                count[q[1]] = 1

        elif q[0] == 2:
            try:
                count[q[1]] -= 1
                if count[q[1]] == 0:
                    del count[q[1]]
            except:
                continue
        
        else:
            if q[1] in set(count.values()):
                result.append('1')
            else:
                result.append('0')
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()

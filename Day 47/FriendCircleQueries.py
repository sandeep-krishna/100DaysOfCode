'''

The population of HackerWorld is . Initially, none of the people are friends with each other. In order to start a friendship, two persons  and  have to shake hands, where . The friendship relation is transitive, that is if  and  shake hands with each other,  and friends of  become friends with  and friends of .

You will be given  queries. After each query, you need to report the size of the largest friend circle (the largest group of friends) formed after considering that query.

For example, your list of queries is:

1 2
3 4
2 3
First,  and  shake hands, forming a circle of . Next,  and  do the same. Now there are two groups of  friends. When  and  become friends in the next query, both groups of friends are added together to make a circle of  friends. We would print

2
2
4
Function Description

Complete the function maxCircle in the editor below. It must return an array of integers representing the size of the maximum circle of friends after each query.

maxCircle has the following parameter(s):

queries: an array of integer arrays, each with two elements indicating a new friendship

Input Format
The first line contains an integer, , the number of queries to process.
Each of the next  lines consists of two space-separated integers denoting the 2-D array

Output Format
Return an integer array of size , whose value at index  is the size of largest group present after processing the  query.

Sample Input 0
2
1 2
1 3

'''


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxCircle function below.
def maxCircle(queries):
    elems  = {} # reference for which set they are in
    groups = {} # collection of the sets
    results = []
    maxl = 0
    for a,b in queries:
        if a not in elems:
            groups[a] = set([a])
            elems[a] = a
        if b not in elems:
            groups[b] = set([b])
            elems[b] = b
        if elems[a] != elems[b]:
            a,b =elems[a],elems[b]
            if len(groups[b])>len(groups[a]): a,b=b,a
            groups[a] |= groups[b]
            for p in groups[b]: elems[p] = a
            del groups[b]
        maxl = max(maxl, len(groups[elems[a]]))
        results.append(maxl)
    return results

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = maxCircle(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()

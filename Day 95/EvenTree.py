'''


You are given a tree (a simple connected graph with no cycles).
Find the maximum number of edges you can remove from the tree to get a forest such that each connected component of the forest contains an even number of nodes.
As an example, the following tree with  nodes can be cut at most  time to create an even forest.


Function Description
Complete the evenForest function in the editor below. It should return an integer as described.
evenForest has the following parameter(s):
t_nodes: the number of nodes in the tree
t_edges: the number of undirected edges in the tree
t_from: start nodes for each edge
t_to: end nodes for each edge, (Match by index to t_from.)
Input Format

The first line of input contains two integers  and , the number of nodes and edges.
The next  lines contain two integers  and  which specify nodes connected by an edge of the tree. The root of the tree is node .

Constraints
Note: The tree in the input will be such that it can always be decomposed into components containing an even number of nodes.  is the set of positive even integers.

Output Format
Print the number of removed edges.

Sample Input 1
Undirected Graph: t
2
1
3
4
5
6
7
8
9
10

 
10 9
2 1
3 1
4 3
5 2
6 1
7 2
8 6
9 8
10 8


Sample Output 1
2


'''



#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

# Complete the evenForest function below.
def createGraph(t_from,t_to):
    d = defaultdict(set)
    for u,v in zip(t_from,t_to):
        d[v].add(u)
    return d

def countNodes(d,node,count):
    if node not in d or len(d[node]) == 0:
        return count
    for nei in d[node]:
        count = countNodes(d,nei,count+1)
    return count



def evenForest(t_nodes, t_edges, t_from, t_to):
    d = createGraph(t_from,t_to)
    countDict = {}
    for i in range(1,t_nodes+1):
        count = countNodes(d,i,1)
        countDict[i] = count
    ans = -1
    for i in countDict.values():
        if i >= 2 and i % 2 == 0:
            ans += 1
    return ans

    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t_nodes, t_edges = map(int, input().rstrip().split())

    t_from = [0] * t_edges
    t_to = [0] * t_edges

    for i in range(t_edges):
        t_from[i], t_to[i] = map(int, input().rstrip().split())

    res = evenForest(t_nodes, t_edges, t_from, t_to)

    fptr.write(str(res) + '\n')

    fptr.close()

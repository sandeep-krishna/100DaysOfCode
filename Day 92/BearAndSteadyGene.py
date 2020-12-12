'''

A gene is represented as a string of length  (where  is divisible by ), composed of the letters , , , and . It is considered to be steady if each of the four letters occurs exactly  times. For example,  and  are both steady genes.

Bear Limak is a famous biotechnology scientist who specializes in modifying bear DNA to make it steady. Right now, he is examining a gene represented as a string . It is not necessarily steady. Fortunately, Limak can choose one (maybe empty) substring of  and replace it with any string of the same length.

Modifying a large substring of bear genes can be dangerous. Given a string , can you help Limak find the length of the smallest possible substring that he can replace to make  a steady gene?

Note: A substring of a string  is a subsequence made up of zero or more contiguous characters of .

As an example, consider . The substring  just before or after  can be replaced with  or . One selection would create .

Function Description

Complete the  function in the editor below. It should return an integer that represents the length of the smallest substring to replace.

steadyGene has the following parameter:

gene: a string
Input Format

The first line contains an interger  divisible by , that denotes the length of a string .
The second line contains a string  of length .

Constraints

 is divisible by 
Subtask

 in tests worth  points.
Output Format
Print the length of the minimum length substring that can be replaced to make  stable.

Sample Input
8  
GAAATAAA

Sample Output
5

'''


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the steadyGene function below.
from collections import Counter

def balanced(l,d):
    ans=True
    for k,v in d.items():
        if v>l:
            ans=False
            break
    return ans        


def steadyGene(gene):
    l=len(gene)//4
    gene_count=Counter(gene)
    start=0
    end=0
    count=10**6
    while(start<n and end <n):
        if not balanced(l,gene_count):
            gene_count[gene[end]]-=1
            end+=1
        else:
            count=min(count,end-start)
            gene_count[gene[start]]+=1
            start+=1    
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    gene = input()

    result = steadyGene(gene)

    fptr.write(str(result) + '\n')

    fptr.close()

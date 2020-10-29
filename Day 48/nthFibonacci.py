'''

The Fibonacci Sequence

The Fibonacci sequence appears in nature all around us, in the arrangement of seeds in a sunflower and the spiral of a nautilus for example.

The Fibonacci sequence begins with  and  as its first and second terms. After these first two elements, each subsequent element is equal to the sum of the previous two elements.

Programmatically:

Given n, return the nth number in the sequence.

As an example, . The Fibonacci sequence to  is . With zero-based indexing, .

Function Description

Complete the recursive function  in the editor below. It must return the  element in the Fibonacci sequence.

fibonacci has the following parameter(s):
n: the integer index of the sequence to return

Input Format
The input line contains a single integer, n.

Output Format
Locked stub code in the editor prints the integer value returned by the  function.

Sample Input
3  

Sample Output
2

'''

def fibonacci(n):
    if n > 1:
        return fibonacci(n - 1) + fibonacci(n - 2)
    else:
        return n

n = int(input())
print(fibonacci(n))
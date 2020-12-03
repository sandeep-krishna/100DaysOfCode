'''

In this challenge you need to print the string that accompanies each integer in a list sorted by the integers. If two strings are associated with the same integer, they must be printed in their original order so your sorting algorithm should be stable. There is one other twist. The first half of the strings encountered in the inputs are to be replaced with the character "".

Insertion Sort and the simple version of Quicksort are stable, but the faster in-place version of Quicksort is not since it scrambles around elements while sorting.

In this challenge, you will use counting sort to sort a list while keeping the order of the strings preserved.

For example, if your inputs are  you could set up a helper array with three empty arrays as elements. The following shows the insertions:

i	string	converted	list
0				[[],[],[]]
1 	a 	-		[[-],[],[]]
2	b	-		[[-],[-],[]]
3	c			[[-,c],[-],[]]
4	d			[[-,c],[-,d],[]]
The result is then printed:  .

Function Description

Complete the countSort function in the editor below. It should construct and print out the sorted strings.

countSort has the following parameter(s):

arr: a 2D array where each arr[i] is comprised of two strings: x and s.
Note: The first element of each , , must be cast as an integer to perform the sort.

Input Format

The first line contains , the number of integer/string pairs in the array .
Each of the next  contains  and , the integers (as strings) with their associated strings.

Constraints


 is even


 consists of characters in the range 

Output Format

Print the strings in their correct order, space-separated on one line.

Sample Input

20
0 ab
6 cd
0 ef
6 gh
4 ij
0 ab
6 cd
0 ef
6 gh
0 ij
4 that
3 be
0 to
1 be
5 question
1 or
2 not
4 is
2 to
4 the
Sample Output

- - - - - to be or not to be - that is the question - - - -

'''


n = int(input())

ar = []
for i in range(n):
    if i < n//2:
        numX, striX = input().strip().split()
        ar.append((int(numX),'-'))
    else:
        numX,striX = input().strip().split()
        ar.append((int(numX),striX))

ar.sort(key=lambda tup: tup[0]) 
print(*[x[1] for x in ar])
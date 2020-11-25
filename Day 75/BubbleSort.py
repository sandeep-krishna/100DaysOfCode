'''

You are given arrays . What will return the next function  in the next picture.

Link to the image: https://ibb.co/vzFR5kr

Input format
The first line contains the integer  () denoting the number of elements of array .
The second line contains  positive integers () denoting the elements of the array.
Note: It is guaranteed that all elements of array  are different.

Output format
Print an integer that denotes the answer to the question.

SAMPLE INPUT 
5
1 3 2 5 4

SAMPLE OUTPUT 
2

'''


def sort(s):
    k = 0
    swap = True
    while swap!=False:
        swap = False
        k+=1
        for i in range(len(s)-1):
            if s[i]>s[i+1]:
                s[i], s[i+1] = s[i+1], s[i]
                swap = True
    return k

n = int(input())
m = list(map(int, input().split()))
print(sort(m))
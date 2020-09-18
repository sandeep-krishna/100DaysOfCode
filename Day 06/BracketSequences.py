"""
A bracket sequence is a string that contains only characters '(' and ')'.

A correct bracket sequence is a bracket sequence that can be transformed into a correct arithmetic expression by inserting characters '1' and '+' between the original characters of the sequence. For example, bracket sequences '()()' and '(())' are correct. The resulting expressions of these sequences are: '(1)+(1)' and '((1+1)+1)'. However, '(', ')(', and '(' are incorrect bracket sequences. 

You are given a bracket sequence , where  denotes the type of 's bracket (open or close). It is not mandatory that  is necessarily correct. Your task is to determine the number of 's such that  is a correct bracket sequence.

Input format

The single line contains sequence .

Output format 

Print the number of shifts denoting the correct bracket sequence.

SAMPLE INPUT 
)()()(
SAMPLE OUTPUT 
3
Explanation
For all , shift of string will be ()()(), which is correct bracket sequence. Since, answer is 3

"""
def solve(s):
    p=0
    t=0
    res = 0
    for i in s:
        if(i=='('):
            p+=1
        else:
            p-=1;
        if (p<t):
            t=p
            res = 0
        if(t==p):
            res+=1
    if p:
        return 0
    else:
        return res
s= input()
print(solve(s))

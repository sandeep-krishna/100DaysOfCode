'''

You are given a binary string, (string which contains 0's and 1's), You have to perform several operations on this string, in one operation choose a non-empty even length substring containing only 0's or only 1's and remove it from the string.
Your goal is to minimize the final length of the string after performing several operations.It is possible that the final string may become empty, in that case print "KHALI" without quotes.
And it can be proved that there is always an unique string with minimal length after performing the operations.

Input:
First line of input contains an intger T denoting number of testcases.
Next T lines of input contains a binary string S.

Output:
for each testcase print the required minimal string.
Constraints:
1 <= T <= 10
1 <= |S|  <= 105
 

SAMPLE INPUT 
2
101001
1001

SAMPLE OUTPUT 
10
KHALI

'''


for i in range(int(input())):
    stack = []
    binary_string = input()
    for binary_char in binary_string:
        if len(stack) > 0:
            if binary_char == stack[-1]:
                stack.pop()
            else:
                stack.append(binary_char)
        else:
            stack.append(binary_char)


    if len(stack) > 0:
        print(''.join(stack))
    else:
        print('KHALI')


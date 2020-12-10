'''

Madam Hannah Otto, the CEO of Reviver Corp., is fond of palindromes, or words that read the same forwards or backwards. She thinks palindromic brand names are appealing to millennials.
As part of the marketing campaign for the company's new juicer called the Rotator™, Hannah decided to push the marketing team's palindrome-searching skills to a new level with a new challenge.
In this challenge, Hannah provides a string  consisting of lowercase English letters. Every day, for  days, she would select two integers  and , take the substring  (the substring of  from index  to index ), and ask the following question:
Consider all the palindromes that can be constructed from some of the letters from . You can reorder the letters as you need. Some of these palindromes have the maximum length among all these palindromes. How many maximum-length palindromes are there?

For example, if ,  and , then we have,
Your job as the head of the marketing team is to answer all the queries. Since the answers can be very large, you are only required to find the answer modulo .
Complete the functions initialize and answerQuery and return the number of maximum-length palindromes modulo .

Input Format
The first line contains the string .
The second line contains a single integer .
The  of the next  lines contains two space-separated integers ,  denoting the  and  values Anna selected on the  day.

Constraints
Here,  denotes the length of .

Subtasks
For 30% of the total score:
For 60% of the total score:

Output Format
For each query, print a single line containing a single integer denoting the answer.

Sample Input 0
week
2
1 4
2 3

Sample Output 0
2
1

'''


def initialize(s):
    n, z = len(s), ord('a')
    S, F, I = [[0] * L for _ in range(n + 1)], [1] * n, [1] * n
    for i, v in enumerate(s, 1):
        for j in range(L):          # 2D array of character counts
            S[i][j] = S[i - 1][j] + (j == ord(v) - z)
    for i in range(1, n):
        F[i] = F[i - 1] * i % M     # modular factorial
        I[i] = pow(F[i], M - 2, M)  # modular inverse of factorial
    return(S, F, I)
    
def answerQuery(l, r):
    c, s, d = 0, 0, 1
    for j in [S[r][i] - S[l - 1][i] for i in range(L)]:
        c += j % 2                  # count of center characters
        s += j // 2                 # count of side characters
        d *= I[j // 2]              # "denominators"
    return((c or 1) * F[s] * d % M)

import os
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    L, M = 26, 1000000007
    S, F, I = initialize(input())
    for _ in range(int(input())):
        result = answerQuery(*map(int, input().split()))
        fptr.write(str(result) + '\n')
    fptr.close()
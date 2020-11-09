'''

A numeric string, , is beautiful if it can be split into a sequence of two or more positive integers, , satisfying the following conditions:

 for any  (i.e., each element in the sequence is  more than the previous element).
No  contains a leading zero. For example, we can split  into the sequence , but it is not beautiful because  and  have leading zeroes.
The contents of the sequence cannot be rearranged. For example, we can split  into the sequence , but it is not beautiful because it breaks our first constraint (i.e., ).
The diagram below depicts some beautiful strings:


You must perform  queries where each query consists of some integer string . For each query, print whether or not the string is beautiful on a new line. If it's beautiful, print YES x, where  is the first number of the increasing sequence. If there are multiple such values of , choose the smallest. Otherwise, print NO.

Function Description
Complete the separateNumbers function in the editor below. It should print a string as described above.

separateNumbers has the following parameter:
s: an integer value represented as a string

Input Format
The first line contains an integer , the number of strings to evaluate.
Each of the next  lines contains an integer string  to query.

Output Format
For each query, print its answer on a new line (i.e., either YES x where  is the smallest first number of the increasing sequence, or NO).

Sample Input 0
7
1234
91011
99100
101103
010203
13
1

Sample Output 0
YES 1
YES 9
YES 99
NO
NO
NO
NO

'''


for _ in range(int(input())):
    s = input()
    l = len(s)
    for i in range(1, l//2 + 1):
        check = s[:i]
        add = int(check)
        while check in s:
            add += 1
            check += f'{add}'
            if check == s:
                break
        else:
            continue
        print('YES', s[:i])
        break
    else:
        print('NO')
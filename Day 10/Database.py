'''
Database

Rahul is a good student  but has less coding skill, and he is placed in a company "datora" this year. And as his first task he has been given to write some code to organize a database table from user input as similar to SQL table shows in command prompt (terminal). He has to code as requirements.

1. There are only four data types

    (a). "string" contains only alphabets without space.

    (b). "integer" contains only numeric

    (c). "date" which contain "dd/mm/yyyy" format

    (d). "boolean" which contain one of two values "true" or "false"

2. all field data should fit into its corresponding cell

3. string ,date and boolean are stored in table as left aligned with a space and integer is right alligned with a space

But you know he is weak in coding so you have to help him to do so.

Constraints

First line of input define number of tables T, 1<= T <=200

For each T first line will have two integer separeted by a space m and n, m is the number attributes, n is the number of touples

Next line contains m number of strings defining name of each attribute

Next n line will contain exactly m number of values (string, integer, date, boolean)

 

Note

No string will be length of more than 30 characters and integer more than 20 digits

 

To see sample output better click on the download link on the right upper corener of the sample output section.

SAMPLE INPUT 
1
5 2
name dob f_name date amount 
AnshulKumar 07/07/1995 Tamal 30/02/2019 20000 
RahulKumar 07/02/1995 Manish 31/03/2019 16000 
SAMPLE OUTPUT 
+-------------+------------+--------+------------+--------+
| name        | dob        | f_name | date       | amount |
+-------------+------------+--------+------------+--------+
| AnshulKumar | 07/07/1995 | Tamal  | 30/02/2019 |  20000 |
| RahulKumar  | 07/02/1995 | Manish | 31/03/2019 |  16000 |
+-------------+------------+--------+------------+--------+

 '''

def p(l,m):
    ans = '+'
    for i in l:
        print('+'.ljust(i+3,'-'),end='')
    print('+')
 
for _ in range(int(input())):
    m, n = [int(i) for i in input().split()]
    a = input().split()
    details = [a]
    for r in range(n):
        details.append(input().split())
    z = zip(*details)
    master = []
    for i in z:
        master.append(i)
 
    lengths = []
    for i in master:
        l = max([len(st) for st in i])
        lengths.append(l)
 
    for k in range(n+1):
        ans = '| '.ljust(1)
        wid = 0
        if k == 0:
            p(lengths, m)
        for i in master:
            s = i[k]
            if s.isdigit():
                ans += s.rjust(lengths[wid],' ') + ' | '
            else:
                ans += s.ljust(lengths[wid],' ') + ' | '
            wid += 1
        print(ans)
        if k == 0 or k == n:
            p(lengths, m)
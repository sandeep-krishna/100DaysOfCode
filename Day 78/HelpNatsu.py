'''

Natsu wishes to find Igneel, the dragon who is like a father to him. But in order to find him he has to complete certain number of tasks. Tasks are defined by string of lowercase english alphabets and he may be asked to complete a same task more than once. He has a list of N tasks. But he wants to complete the tasks which occur multiple times together. Also he wants to complete the tasks which occurs least frequently first. If two tasks have same frequency the lexicographicaly smaller will be completed first. Help him prepare such a list representing frequency of tasks and task name separated by a space.

Constraints:
1 ≤ T ≤ 10
1 ≤ N ≤ 10000
1 ≤ | Task| ≤ 10

Input:
First line contains the number of test cases T. For each of the T test cases first line is number N the number of Tasks followed by N strings of lowercase english alphabet.

Output:
For each test case output the list as explained above.

SAMPLE INPUT 
1
10
abcd
bcd
abc
abc
abc
bcd
bge
dbaa
bcd
bge

SAMPLE OUTPUT 
1 abcd
1 dbaa
2 bge
3 abc
3 bcd

'''


t=int(input())
for i in range(t):
    a=[]
    n=int(input())

    for i in range(n):
        s=input()
        a.append(s)
    d={}

    for i in a:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1

    t=sorted(zip(d.values(),d.keys()))

for k,l in t:

    print(k,l)
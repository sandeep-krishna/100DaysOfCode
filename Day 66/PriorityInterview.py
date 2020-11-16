'''

Microsoft has come to hire interns from your college. N students got shortlisted out of which few were males and a few females. All the students have been assigned talent levels. Smaller the talent level, lesser is your chance to be selected. Microsoft wants to create the result list where it wants the candidates sorted according to their talent levels, but there is a catch. This time Microsoft wants to hire female candidates first and then male candidates.
the task is to create a list where first all female candidates are sorted in a descending order and then male candidates are sorted in a descending order.

Input Format
The first line contains an integer N denoting the number of students. Next, N lines contain two space-separated integers, ai and bi.
The first integer,  ai will be either 1(for a male candidate) or 0(for female candidate).
The second integer, bi will be the candidate's talent level.

Output Format
Output   space-separated integers, which first contains the talent levels of all female candidates sorted in descending order and then the talent levels of male candidates in descending order.

SAMPLE INPUT 
5
0 3
1 6
0 2
0 7
1 15

SAMPLE OUTPUT 
7 3 2 15 6

'''

n=int(input())
l=[[y for y in input().split()] for i in range(n)]
girl=[]
boy=[]

for i in range(n):
     if (int(l[i][0]) != 0):
         boy.append(int(l[i][1]))
     else:
           girl.append(int(l[i][1]))

girl.sort(reverse=True)
boy.sort(reverse=True)
result=[]
result.extend(girl)
result.extend(boy)
print(' '.join(str(i) for i in result))
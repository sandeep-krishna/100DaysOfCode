'''

Students have become secret admirers of SEGP. They find the course exciting and the professors amusing. After a superb Mid Semester examination its now time for the results. The TAs have released the marks of students in the form of an array, where arr[i] represents the marks of the ith student.
Since you are a curious kid, you want to find all the marks that are not smaller than those on its right side in the array.

Input Format
The first line of input will contain a single integer n denoting the number of students.
The next line will contain n space separated integers representing the marks of students.

Output Format
Output all the integers separated in the array from left to right that are not smaller than those on its right side.

Constraints
1 <= n <= 1000000
0 <= arr[i] <= 10000

SAMPLE INPUT 
6
16 17 4 3 5 2
SAMPLE OUTPUT 
17 5 2

'''

n=int(input())
arr=list(map(int,input().split()))
sol=[arr[-1]]

for i in range(n-2,-1,-1):
   if arr[i]>=sol[-1]:
       sol.append(arr[i])

sol=sol[::-1]

print(*sol)

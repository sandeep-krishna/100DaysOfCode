'''

Coders here is a simple task for you, you have given an array of size N and an integer M.
Your task is to calculate the difference between maximum sum and minimum sum of N-M elements of the given array.

Constraints:
1<=t<=10
1<=n<=1000
1<=a[i]<=1000

Input:
First line contains an integer T denoting the number of testcases.
First line of every testcase contains two integer N and M.
Next line contains N space separated integers denoting the elements of array

Output:
For every test case print your answer in new line

SAMPLE INPUT 
1
5 1
1 2 3 4 5

SAMPLE OUTPUT 
4

'''

def sorting(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if(arr[j]>arr[j+1]):
                arr[j],arr[j+1]=arr[j+1],arr[j];
    
    return arr;

t=int(input())
for i in range(t):
    m,n=map(int,input().split())
    arr=list(map(int,input().split()))
    sortedArr=sorting(arr)
    f1=sum(arr[:m-n])
    f2=sum(arr[::-1][:m-n])
    print(abs(f1-f2))


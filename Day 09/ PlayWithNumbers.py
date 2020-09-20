'''
 Play with numbers

 You are given an array of n numbers and q queries. For each query you have to print the floor of the expected value(mean) of the subarray from L to R.
First line contains two integers N and Q denoting number of array elements and number of queries.
Next line contains N space seperated integers denoting array elements.
Next Q lines contain two integers L and R(indices of the array).


print a single integer denoting the answer.

 :

1<= N ,Q,L,R <= 10^6

1<= Array elements <= 10^9

NOTE
Use Fast I/O

'''
x = list(map(int,input().split()))

a = list(map(int,input().split()))

b = [a[0]]

for i in range (1, len(a)):

    b.append(a[i]+b[-1])

for i in range (0,x[1]):
    c = list(map(int,input().split()))
    if c[0] == 1:
        print(b[c[1]-1]//(c[1]))
    else:
        print((b[c[1]-1] - b[c[0] - 2])//((c[1] - c[0])+1))
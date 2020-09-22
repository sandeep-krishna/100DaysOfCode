'''
Minimize Cost

You are given an array of numbers  which contains positive as well as negative numbers . The cost of the array can be defined as 
 C(X), where T is the transfer array which contains N zeros initially.
You need to minimize this cost . You can transfer value from one array element to another if and only if the distance between them is at most K.
Also, transfer value can't be transferred further.
Say array contains  and 
if we transfer 3 from  element to  , the array becomes
Original Value 

Transferred value 

 which is minimum in this case

Note :

Only positive value can be transferred

It is not necessary to transfer whole value i.e partial transfer is also acceptable. This means that if you have  then you can distribute the value 5 across many other array elements provided that they finally sum to a number less than equal to 5. For example 5 can be transferred in chunks of smaller values say 2 , 3 but their sum should not exceed 5.

Input:

First line contains N and K separated by space

Second line denotes an array of size N

Output

Minimum value of C(X)

SAMPLE INPUT 
3 2
3 -1 -2
SAMPLE OUTPUT 
0

'''

def Solve (k, arr):
    sum1=0
    counter=0
    m=k

    for i in arr:
        if(i>=0):
            counter+=1
            sum1+=i
            m=k

        else:
            if(counter==0):
                return abs(sum(arr)+i)

            else:
                m-=1
                if(m<0):
                    sum1+=abs(i)
                else:
                    sum1+=i
    return abs(sum1)

n,k = map(int, input().split())
arr = map(int, input().split())
out_ = Solve(k, arr)
print (out_)
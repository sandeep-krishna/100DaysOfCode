def cycle(a,k):
    i = bin(int(a,2))[2:].zfill(len(a))
    b=i[1:]+i[0]
    maxi = i
    while b!=i: 
        if b>maxi:
            maxi = b
        b= b[1:]+b[0]
    c=0
    b=i
    if i!=maxi:
        while b!=maxi:
            b= b[1:]+b[0]
            c+=1

    b = maxi[1:]+maxi[0]
    d=1
    while b!=maxi:
        d+=1
        b= b[1:]+b[0]
    return c+d*(k-1)
    
for i in range(int(input())):
    n,k = map(int,input().split())
    a = input()
    print(cycle(a,k))
'''

It's a holiday season for all school students around the world! Unfortunately, Mahamba is busy preparing for International Olympiad in Informatics, which will be held in Tehran, Iran. He is now facing a new challenge from his teacher Aceka, and it goes something like this:
You have a string x of length N, which consists of small English letters. You have to find the number of indexes a, b, c and d, such that  and , as well as .
He is baffled and definitely needs some help. So, you, the best programmer in Lalalandia, decided to give him a hand!

Input format
The first line contains the number N - the length of a string x. The second line contains the string x itself.

Output format
The first and only line should contain the answer to the problem.

Constraints
The string x only contains small English letters.

SAMPLE INPUT 
5
ababa

SAMPLE OUTPUT 
2

'''

def counter(a,b):
    temp = a+b
    lnt= len(temp)
    temp.sort()
    # check = False
    # dc = False
    ca=[]
    cb= []
    counta= 0
    countb = 0
    for i  in range(len(a)):
    	
    	j= temp.index(a[i])
    	ca.append(lnt - len(a)-j+i)
    for i  in range(len(b)):
    	
    	j= temp.index(b[i])
    	cb.append(lnt - len(b)-j+i)
    
    # print(ca,cb)
    # ca.append(len(temp)-i-1)
    # check = False
    
    for i in range(len(ca)-1):
        for j in range(i+1, len(ca)):
            counta += ca[j]*(ca[i]-ca[j])
        
    for i in range(len(cb)-1):
        for j in range(i+1, len(cb)):
            countb += cb[j]*(cb[i]-cb[j])
    
    
    total = counta + countb
    return total
    
 
 
n= int(input())
l= list(input())
d= {}
for i in range(n):
    if l[i] in d:
        d[l[i]].append(i)
 
    else: d[l[i]] = [i]   
final = 0
run =[x for x in d]
for i in range(len(run)-1):
    for j in range(i+1, len(run)):
        final += counter(d[run[i]], d[run[j]])
    
 
 
for x in d:
    ln= len(d[x])
    if ln>=4:
        final+=((ln)*(ln-1)*(ln-2)*(ln-3))//24
print(final)

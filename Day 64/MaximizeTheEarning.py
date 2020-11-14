'''

Napoleon choosed a city for Advertising his company's product. There are  streets in that city. Each day he travels one street. There are  buildings in a street which are located at points . Each building has some height(Say  meters). Napoleon stands at point . His height is . Now Napoleon starts communicating with the people of each building. He can communicate with people of a particular building only if he can see that building. If he succeed to communicate with any particular building then his boss gives him . i.e. if he communicates with  buildings in a day, then he will earn . Now Napoleon wants to know his maximum Earning for each day.

Note: All the points are on Strainght Line and Napoleon is always standing at point 0.

Input:
First line of input contains an integer , denoting no of streets in the city.
Details for each street is described in next two lines.
First line contains two integers  and  denoting no of buildings in the Street and earning on communicating with a building.
Second line contains  integers, denoting height of  building.

Output:
Print  Lines, each containing maximum earning in  street.
    
SAMPLE INPUT 
2
6 3
8 2 3 11 11 10
5 12
12 20 39 45 89

SAMPLE OUTPUT 
6
60

'''

s=int(input())
for i in range(s):
    n,r=map(int,input().split())
    h=list(map(int,input().split()))
    b=h[0]
    count=1
    for i in range(n):
        if(b<h[i]):
            count+=1
            b=h[i]
    print(count*r)

'''

Sam among his friends wants to go to watch a movie in Armstord Cinema.
There is something special about Armstord cinema whenever people come in the group here. They will get seats accordingly their heights. Sam as a curious guy always wants to sit in the middle as cinema has the best view from the middle.
Now, Sam as the leader of his group decides who will join him for the movie.
Initially, he has  friends with him ( including him).
You are given  numbers that represent the heights of Sam's friends.
You are given the height of Sam as well.

Now, Sam can do two operations:
1. He can call a new friend of height .
2. He can cancel any of his friend invitations.

Each operation will cost him a unit time.
He wants to do this as soon as possible.

Input format
The first line contains T, where T is the test case.
Each test case contain two lines,
The first line contains two space-separated integer ,  where  is the total number of Sam's friend and  is Sam height.
The second line contains  space-separated integers that represent the height of Sam's friend.

Output format
Print the required answer for each test case in a new line.

Note:
Sam should always sit in middle and there's an equal number of persons in his left and right.
Height of Sam is always unique.      

SAMPLE INPUT 
2
3 2
4 3 1
1 5
6


SAMPLE OUTPUT 
1
1

'''

from bisect import bisect_left
tc = int(input())
for _ in range(tc):
    s,n = map(int,input().split(" "))
    arr = sorted(list(map(int,input().split(" "))))
    res = bisect_left(arr,n)
    arr.insert(res,n)
    print(abs(len(arr[:res]) - len(arr[res+1:])))
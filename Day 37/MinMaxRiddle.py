'''
Given an integer array of size , find the maximum of the minimum(s) of every window size in the array. The window size varies from  to .
For example, given , consider window sizes of  through . Windows of size  are . The maximum value of the minimum values of these windows is . Windows of size  are  and their minima are . The maximum of these values is . Continue this process through window size  to finally consider the entire array. All of the answers are .

Function Description
Complete the riddle function in the editor below. It must return an array of integers representing the maximum minimum value for each window size from  to .
riddle has the following parameter(s):
arr: an array of integers
Input Format
The first line contains a single integer, , the size of .
The second line contains  space-separated integers, each an .


Output Format
Single line containing  space-separated integers denoting the output for each window size from  to .

Sample Input 0
4
2 6 1 12

Sample Output 0
12 2 1 1

'''

def solve():
        global H
        mx = [0] * len(H)

        H.append(0)
        stack= list()
        for i, h in enumerate(H):
                li = i
                while stack and h < stack[-1][0]:
                        lh, li = stack.pop()
                        for j in range(1, i - li + 1):
                                mx[j - 1] = max(mx[j - 1], lh)

                stack.append((h, li))
        return ' '.join(map(str, mx))

if __name__ == '__main__':
        import os
        fp = open(os.environ['OUTPUT_PATH'], 'w')

        _ = int(input())
        H = list(map(int, input().split()))
        sol = solve()

        fp.write(str(sol) + '\n')

        fp.close()
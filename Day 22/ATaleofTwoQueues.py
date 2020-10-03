'''
A queue is an abstract data type that maintains the order in which elements were added to it, allowing the oldest elements to be removed from the front and new elements to be added to the rear. This is called a First-In-First-Out (FIFO) data structure because the first element added to the queue (i.e., the one that has been waiting the longest) is always the first one to be removed.

A basic queue has the following operations:

Enqueue: add a new element to the end of the queue.
Dequeue: remove the element from the front of the queue and return it.
In this challenge, you must first implement a queue using two stacks. Then process  queries, where each query is one of the following  types:

1 x: Enqueue element  into the end of the queue.
2: Dequeue the element at the front of the queue.
3: Print the element at the front of the queue.
For example, a series of queries might be as follows:


Function Description
Complete the put, pop, and peek methods in the editor below. They must perform the actions as described above.

Input Format
The first line contains a single integer, , the number of queries.
Each of the next  lines contains a single query in the form described in the problem statement above. All queries start with an integer denoting the query , but only query  is followed by an additional space-separated value, , denoting the value to be enqueued.



Output Format
For each query of type , return the value of the element at the front of the fifo queue on a new line.

Sample Input
10
1 42
2
1 14
3
1 28
3
1 60
1 78
2
2

Sample Output
14
14
'''

class MyQueue(object):
    def __init__(self):
        self.inward = []
        self.outward = []
    
    def peek(self):
        if not self.outward:
            self.outward = list(reversed(self.inward))
            self.inward = []
        return self.outward[-1]         
        
    def pop(self):
        head = self.peek()
        del self.outward[-1]
        return head
        
    def put(self, value):
        self.inward.append(value)

queue = MyQueue()
t = int(input())
for line in range(t):
    values = map(int, input().split())
    values = list(values)
    if values[0] == 1:
        queue.put(values[1])        
    elif values[0] == 2:
        queue.pop()
    else:
        print(queue.peek())
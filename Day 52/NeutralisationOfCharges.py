'''

In a parallel universe, there are not just two charges like positive and negative, but there are  charges represented by   english alphabets.
Charges have a property of killing each other or in other words neutralizing each other if they are of same charge and next to each other.
You are given a string  where each  represents a charge, where .
You need to output  of final string followed by string after which no neutralizing is possible.

SAMPLE INPUT 
12
aaacccbbcccd
SAMPLE OUTPUT 
2
ad

'''

n = int(input())
arr = [char for char in input()]
stack = []
for c in arr:
    if len(stack)==0:
        stack.insert(0, c)
    else:
        if c==stack[0]:
            stack.pop(0)
        else:
            stack.insert(0, c)

stack.reverse()
print(len(stack))       
print("".join(stack))

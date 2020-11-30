'''

David has invited his girlfriend Patricia to the cinema to see the latest Ciro Guerra movie, after a long time they have agreed to see the 7 PM movie. When David prepares to pay, he realizes that the serial number on the ticket is a yellow number, so he decides not to use it and finally Patricia must pay for the cinema.
A yellowish number refers to any number that reads the same from left to right.
For this problem it is required to verify if a number is capicúa.

Entry
The first line consists of the number of cases T such that. Later there will be T lines, each with a number N, such that. It is ensured that the numbers do not have leading zeros.

Departure
T lines must be printed, on each line “YES” must be printed if the number is capicúa or “NO” otherwise, all without quotation marks.

SAMPLE INPUT 
5
11111
8785878
51875
224614
547745

SAMPLE OUTPUT 
YES
YES
NO
NO
YES

'''

for _ in range(int(input())):
    s=input()
    if s==s[::-1]:
        print('YES')
    else:
        print('NO')

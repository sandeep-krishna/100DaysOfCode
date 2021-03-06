'''
 Cipher
 
 Indian army is going to do a surprise attack on one of its enemies country. The President of India, the Supreme Commander of the Indian Army will be sending an alert message to all its commanding centers. As enemy would be monitoring the message, Indian army is going to encrypt(cipher) the message using basic encryption technique. A decoding key 'K' (number) would be sent secretly.

You are assigned to develop a cipher program to encrypt the message. Your cipher must rotate every character in the message by a fixed number making it unreadable by enemies.

Given a single line of string 'S' containing alpha, numeric and symbols, followed by a number '0<=N<=1000'. Encrypt and print the resulting string.

Note: The cipher only encrypts Alpha and Numeric. (A-Z, a-z, and 0-9) . All Symbols, such as - , ; %, remain unencrypted.

SAMPLE INPUT 
All-convoYs-9-be:Alert1.
4
SAMPLE OUTPUT 
Epp-gsrzsCw-3-fi:Epivx5.
Explanation
First line contains the string to convert. S

Second line contains the number, encrypt key. K

A becomes E, Y becomes C, 9 becomes 3,

-, . unchanged.

'''

s = input()
t = int(input())
k = t
out = ""

for i in s:
    if i.isalnum():
        if i.isupper():
            k %= 26
            if ord(i)+k > ord('Z'):
                out += chr(ord('A')+ord(i)+k-ord('Z')-1)
            else:
                out += chr(ord(i)+k)
            k = t
        elif i.islower():
            k %= 26
            if ord(i)+k > ord('z'):
                out += chr(ord('a')+ord(i)+k-ord('z')-1)
            else:
                out += chr(ord(i)+k)
            k = t
        elif i.isnumeric():
            k %= 10
            if int(i)+k > 9:
                out += str(int(i)+k-10)
            else:
                out += str(int(i)+k)
            k = t

    else:
        out += i
print(out)
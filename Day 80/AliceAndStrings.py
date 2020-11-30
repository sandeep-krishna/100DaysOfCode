'''

Two strings  and  comprising of lower case English letters are compatible if they are equal or can be made equal by following this step any number of times:
Select a prefix from the string  (possibly empty), and increase the alphabetical value of all the characters in the prefix by the same valid amount. For example if the string is  and we select the prefix  then we can convert it to  by increasing the alphabetical value by 1. But if we select the prefix  then we cannot increase the alphabetical value.
Your task is to determine if given strings  and  are compatible.

Input format
First line: String  
Next line: String 

Output format
For each test case, print  if string  can be converted to string  , otherwise print .

SAMPLE INPUT 
abaca
cdbda

SAMPLE OUTPUT 
YES

'''

str1, str2 = input(),input()
if (len(str1)==len(str2)):
       for i in range(len(str1)):
                  if (str1[i]>str2[i]):
                            print('NO')
                            break
       else:
            print('YES')
else:
      print('NO')


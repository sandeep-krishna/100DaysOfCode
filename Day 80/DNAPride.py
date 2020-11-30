'''

Everyone is familiar with Pratik's obsession with DNA and how much he likes to find the correct pair for the nucleotide bases. One day Samim found him exaggerating about his knowledge of DNA bases. So Samim challenged Pratik about finding the correct base pair for the given DNA sequence and show the result. Also he secretly introduced some of RNA nucleotide bases to test Pratik. Now initially he accepted the challenge but soon found out about how big the sequence actually was, so he came to you ask him for your in finding the sequence and keep his pride about the knowledge of DNA molecules.
You are given a string that contains the nucleotide bases of DNA and RNA, you are needed to find the correct pair for all the bases and print the corresponding sequence obtained. In case the sequence contains a RNA base, print "Error RNA nucleobases found!" (without quotes).

INPUT FORMAT
The first line of input contains T, the no of test cases. The next line of input contains N, the no of bases in each of the DNA sequence The line after that contains the DNA sequence.

OUTPUT FORMAT
For each test case output your answer on a new line.

SAMPLE INPUT 
3
2
AG
4
ATGC
6
UGCACT

SAMPLE OUTPUT 
TC
TACG
Error RNA nucleobases found!


'''

for _ in range(int(input())):
        n,s = int(input()), input()
        temp = ""
        for i in range(n):
            if (s[i]=='G'):
               temp+='C'

            elif (s[i]=='A'):
               temp+='T'

            elif (s[i]=='T'):
               temp+='A'

            elif (s[i]=='C'):
               temp+='G'

            elif (s[i]=='U'):
               print('Error RNA nucleobases found!')
               break

        else:
           print(temp)
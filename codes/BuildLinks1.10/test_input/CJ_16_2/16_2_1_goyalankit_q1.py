#!/usr/bin/env python

num = {0:'ZERO',1:'ONE',2:'TWO',3:'THREE',4:'FOUR',5:'FIVE',6:'SIX',7:'SEVEN',8:'EIGHT',9:'NINE'}

ref = {'Z':0,'W':2,'U':4,'X':6,'G':8,'F':5,'O':1,'T':3,'V':7,'I':9}

inFile = open('in.txt','r')
outFile = open('out.txt','w')
t = int(inFile.readline())

for test in range(1,t+1,1):
    string = inFile.readline()[:-1]
    string = list(string)
    chars = ['Z','W','U','X','G','F','O','T','V','I']
    numlist = []
    for char in chars:
        total = string.count(char)
        for i in range(total):
            numlist.append(ref[char])
            for x in num[ref[char]]:
                string.remove(x)

    numlist.sort()
    f = ''
    for a in numlist:
        f += str(a)
    outFile.write('Case #{}: {}\n'.format(test,f))

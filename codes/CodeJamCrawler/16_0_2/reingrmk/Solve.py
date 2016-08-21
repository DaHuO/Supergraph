#!/bin/python

def writeLine(case, answer) :
    outF.write('Case #'+str(case+1)+': '+answer+'\n')

filename = 'B-large'

inF = open(filename+'.in', 'r')
outF = open(filename+'.out', 'w')

n = int(inF.readline())

for case in range(n) :
    read = inF.readline().strip()[::-1]
    b = True
    count = 0
    for s in read :
        if s == '+' :
            if not b :
                count += 1
                b = True
        elif s == '-' :
            if b :
                count += 1
                b = False
        else :
            print('WTF')
    writeLine(case, str(count))




#!/bin/python

def writeLine(case, answer) :
    outF.write('Case #'+str(i+1)+': '+answer+'\n')

inF = open('A-large.in', 'r')
outF = open('a-large.out', 'w')

n = int(inF.readline())

for i in range(n) :
    start = count = inF.readline().strip()
    if count == '0' :
        writeLine(i, 'INSOMNIA')
        continue
    sleep = [1,1,1,1,1,1,1,1,1,1]
    while sum(sleep) != 0 :
        for j in count :
            sleep[int(j)] = 0
        count = str(int(count)+int(start))
    writeLine(i, str(int(count)-int(start)))
    


























# 1 2 3 4 5 6 7 8 9 0
# 2 4 6 8 10 12 14 16 18 
# 3 6 9 12 15 18 21 24 27 30



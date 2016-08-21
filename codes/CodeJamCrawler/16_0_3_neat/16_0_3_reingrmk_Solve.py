#!/bin/python2

def writeLine(number, divisors) :
    outF.write(str(number))
    for i in divisors :
        outF.write(' '+str(i))
    outF.write('\n')

# filename = 'C-small-attempt1'
filename = 'C-large'

inF = open(filename+'.in', 'r')
outF = open(filename+'.out', 'w')
outF.write('Case #1:\n')
inF.readline()

read = inF.readline().strip().split()
n = int(read[0])
j = int(read[1])

# num = '1'+(14*'0')+'1'
num = '1'+((n-2)*'0')+'1'
count = 0
primenumbers = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]

while count < j :
    divisors = list()
    
    for b in range(2,11) :
        i = int(num, b)
        for p in primenumbers[:10] :
            if i % p == 0 :
                divisors.append(p)
                break
        else :
            break
    else :
        writeLine(num, divisors)
        count += 1
    num = format(int(num,2)+int('10',2), 'b')

    




# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 19:27:27 2016

@author: Bluefish_
"""
def getDigits(number, digitSet):
    while number!=0:
        digit = number % 10
        digitSet.add(digit)
        number = number // 10

infile = open("A-large.in",'r')
outfile = open("out-large.txt",'w')
inputs = int(infile.readline())
for i in range(inputs):
    n = int(infile.readline())
    if n==0:
        outfile.write("Case #"+str(i+1)+": INSOMNIA\n")
    else:
        ten = set([])
        counter = 1
        number = n
        while len(ten)!=10:
            getDigits(number,ten)
            counter += 1
            number = n * counter
        number = (counter-1)*n
        outfile.write("Case #"+str(i+1)+": "+str(number)+"\n")
infile.close()
outfile.close()
    
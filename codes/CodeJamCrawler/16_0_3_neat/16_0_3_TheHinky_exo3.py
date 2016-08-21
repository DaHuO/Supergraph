#!/usr/bin/python
# coding: utf-8

import sys
import os
import re
import datetime
import argparse
import math

class Exo3Coin(object):

    samplebegin = '100001'
    sampleend   = '1000000'
    #samplebegin = '100011'
    #sampleend   = '100111'

    smallbegin = '1000000000000001' 
    smallend   = '10000000000000000'

    filename = 'A-small-attempt3.in'
    filenameout = 'output3.txt'

    Tcase = 0
    bases = [2,3,4,5,6,7,8,9,10]
    def __init__(self):
        self.exosolution3()

    def exosolution3(self):
        with open(self.filename, 'r') as f:
             read_data = f.readlines()

        with open(self.filenameout, 'w') as fileout:
            for index,row in enumerate(read_data):
                if index == 0 :
                    self.Tcase = row
                else:
                    if index > self.Tcase:
                        print "Erreur too big"
                    else:
                        self.parse_data(row, index, fileout)

    def parse_data(self, linetoparse, testcaseid, fileout):
        outputstring = ""
        numberofcases = 0
        maxcases = int(linetoparse.split(' ')[1])
        print maxcases
        for i in range(int(self.smallbegin,2), int(self.smallend,2)):
#        for i in range(int(self.samplebegin,2), int(self.sampleend,2)):
            allprimes = True
            dividors = []
            binary = bin(i).split('b')[1]
            #print binary
            if binary[-1:] == '0':
                continue
            for j in self.bases:
                #print j
                #print bin(i).split('b')[1]
                n=int(binary, j)
                prime,dividor = self.isprime(n)
                if prime:
                    allprimes = False
                    break
                else:
                    dividors.append(dividor)
            #print allprimes
            if allprimes:
                outputstring += self.getfullline(i, dividors) + '\n'
                numberofcases = numberofcases + 1
                print self.getfullline(i, dividors)
            if numberofcases >= maxcases:
                break      
        stringtowrite = "Case #" + str(testcaseid) + ":\n" + str(outputstring) 
        #print stringtowrite
        fileout.write(stringtowrite)

    def isprime(self,number):
        prime = False
        dividor = 0
        if number % 2 == 0 and number > 2:
	    return prime, 2
        for i in range(3, int(math.sqrt(number)+1), 2):
            #print "RESTANT" + str(number % i)
	    #print int(math.sqrt(number)+1)
            if number % i == 0:
		#print str(number) + '/' + str(i)
                dividor = i
                break
        if dividor == 0:
            prime = True
        return prime, dividor

    def getfullline(self, number, dividors):
        numberbin = bin(number).split('b')[1] 
        out = numberbin
        for j in dividors:
            out = out + ' ' + str(j)
        return out
### MAIN ###
if __name__ == "__main__":
    foo = Exo3Coin()

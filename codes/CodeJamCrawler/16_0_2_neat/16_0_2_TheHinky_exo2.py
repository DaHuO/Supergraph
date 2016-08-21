#!/usr/bin/python
# coding: utf-8

import sys
import os
import re
import datetime
import argparse
import math

class Exo2Pancake(object):

    filename = 'B-large.in'
    filenameout = 'output2big.txt'

    def __init__(self):
        self.exosolution2()

    def exosolution2(self):
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
        signS = list(linetoparse.strip())
        flip = 0
        lenstring = len(signS)
        print lenstring
        for i in range(0, lenstring):
            if signS[lenstring - (i+1)] == '+':
                continue
            flip = flip + 1
            for j in range(i, lenstring ):
                if signS[lenstring - (j+1)] == '-':
                    signS[lenstring - (j+1)] = '+'
                else:
                    signS[lenstring - (j+1)] = '-'
        print signS
        stringtowrite = "Case #" + str(testcaseid) + ": " + str(flip) + '\n' 
        #print stringtowrite
        fileout.write(stringtowrite)

### MAIN ###
if __name__ == "__main__":
    foo = Exo2Pancake()

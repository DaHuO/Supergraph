#!/usr/bin/python
# coding: utf-8

import sys
import os
import re
import datetime
import argparse


class Exo1Sheep(object):

    listcase = []
    Tcase = 0
    filename = "A-large.in"
    filenameout = "outputbig.txt"
    def __init__(self):
        self.exosolution1()

    def init_listclass(self):
        for i in range (0,10):
            if str(i) not in self.listcase:
                self.listcase.append(str(i))

    def exosolution1(self):
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
        self.init_listclass()
        count = int(linetoparse.strip())
        outputcount = ""
        loopcounter = 1
        if count == 0:
            outputcount = 'INSOMNIA'
        else:
            while(1):
                insidecount = count * loopcounter
                toremove = []
                for i in self.listcase:
                    if i in str(insidecount):
         #               print "Removing" + i
                        toremove.append(i)
                for removing in toremove:
                    self.listcase.remove(removing)
                if not self.listcase:
                    outputcount=insidecount
                    break
                else:
                    loopcounter = loopcounter + 1
        stringtowrite = "Case #" + str(testcaseid) + ": " + str(outputcount) + "\n"
        #print stringtowrite
        fileout.write(stringtowrite)


### MAIN ###
if __name__ == "__main__":
    foo = Exo1Sheep()

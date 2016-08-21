# -*- coding: utf-8 -*-

# just copy a whole bunch of these just in case
import time
import sys, traceback, ast
import fileinput
import os
import re
import httplib
import codecs
import HTMLParser
import math
import operator

inputFile = "A-large.in"

outputFile = "output.txt"
outFile = open(outputFile, mode='w')

def runSolution(inFile):
    
    lines = open(inFile, mode='r').readlines()
    ln = 0 #ln = line number
    
    cases = int(lines[ln])
    ln += 1
    for i in range(0, cases):
        caseInput = []
        linesInCase = 1
        
        for j in range(0, linesInCase):
            caseInput.append(lines[ln].strip())
            ln += 1
        #ln += 1 #skip blank line in input
        
        case = formatCaseInput(caseInput)
        output = getCaseOutput(case)
        
        print "Case #" + str(i+1) + ": " + output
        outFile.write("Case #" + str(i+1) + ": " + output + '\n')
        
    outFile.close()
        

def formatCaseInput(caseInput):
    line = caseInput[0]
    splitln = line.split(" ")
    x = int(splitln[0])

    #print case
    return x

def getCaseOutput(case):
    print str(case)
    val = doCase(case)
    return str(val)

def doCase(stuff):
    n = stuff;
    value = 0;
    seenValues = {};
    
    digits = {};
    tries = 0;
    
    isDone = False
    while isDone == False:
        tries += 1;
        value += n;
        if (value in seenValues):
            return "INSOMNIA"
        seenValues[value] = value;
        
        for digit in str(value):
            digits[digit] = 1;
        if len(digits) > 9:
            return value;

        if tries > 1000000:
            isDone = True;

    return "INSOMNIA"
    
runSolution(inputFile)

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

inputFile = "B-large.in"

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

    return line

def getCaseOutput(case):
    val = doCase(case)
    return str(val)

def doCase(stuff):
    stack = stuff;

    flips = 0;
    done = False
    while done == False:
        #print stack;
        if "-" not in stack:
            done = True;
        else:
            newStack = "";
            
            lastMinus = stack.rfind("-");
            i = 0;
            while i < len(stack):
                if i <= lastMinus:
                    if stack[i] == "+":
                        newStack += '-';
                    else:
                        newStack += '+';
                else:
                    newStack += stack[i]
                i += 1;

            stack = newStack;
            flips += 1;
        
    return flips    
runSolution(inputFile)

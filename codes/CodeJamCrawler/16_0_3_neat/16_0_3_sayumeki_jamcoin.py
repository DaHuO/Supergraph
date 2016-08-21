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
import copy
import random
import operator

inputFile = "input.txt"

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
        
        print "Case #" + str(i+1) + ": "
        outFile.write("Case #" + str(i+1) + ": " + '\n')
        for thing in output:
            str2 = "";
            for digit in thing[0]:
                str2 += str(digit);
            str2 += " "
            for factor in thing[1]:
                str2 += str(factor) + " ";
            print str2;
            outFile.write(str2);
        
    outFile.close()
        

def formatCaseInput(caseInput):
    line = caseInput[0]

    case = [16, 50]
    return case

def getCaseOutput(case):
    val = doCase(case)
    return val;

def doCase(stuff):
    neededLength = stuff[0];
    neededCoins = stuff[1];
    coins = [];

    currentCoin = [1];
    while len(currentCoin) < neededLength - 1:
        currentCoin.append(0);
    currentCoin.append(1);
    
    while len(coins) < neededCoins:
        if random.random() < 0:
            print "Testing " + str(currentCoin)
        coinFactors = [];

        #print currentCoin;
        base = 2;
        while base <= 10:
            value = valueInBase(currentCoin, base)
            factorOfValue = thefactorOfValue(value);
            if factorOfValue != -1:
                coinFactors.append(factorOfValue);
            base += 1;

        if len(coinFactors) == 9:
            coins.append([copy.deepcopy(currentCoin), coinFactors]);
            print([copy.deepcopy(currentCoin), coinFactors])

        currentCoin = getNextCoin(currentCoin);

    return coins;

def getNextCoin(coin):
    coinPos = len(coin) - 2;
    while coin[coinPos] == 1:
        coin[coinPos] = 0;
        coinPos -= 1;
    coin[coinPos]= 1;
    return coin;

def valueInBase(coin, base):
    value = 0;
    baseValue = 1;
    for i in reversed(coin):
        value += i * baseValue;
        
        baseValue *= base;
    return value;

def thefactorOfValue(value):
    test = 2;
    while test < math.sqrt(value) + 1:            
        if value % test == 0:
            #print str(value) + " " + str(test);
            return test;
        test += 1;
    return -1;
                                
runSolution(inputFile)

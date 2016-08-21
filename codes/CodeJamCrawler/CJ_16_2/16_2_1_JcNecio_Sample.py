#!/bin/bash

INDECES = [0, 8, 3, 2, 6, 7, 5, 4, 9, 1]
DIGITS = ["ZERO", "EIGHT", "THREE", "TWO", "SIX", "SEVEN", "FIVE" , "FOUR", "NINE", "ONE"]
LETTERS = ["Z", "E", "R", "O", "N", "T", "W", "H", "F", "U", "I", "V", "S", "X", "G"]

def printer(line):
        counts = dict((LETTERS[i], line.count(LETTERS[i])) for i in range(0, len(LETTERS)))
        retVal = []
        for i in DIGITS:
                while everythingAvailable(i, counts):
                        retVal.append(INDECES[DIGITS.index(i)])
                        removeOneFromLetters(i, counts)
        return retVal

def everythingAvailable(word, letters):
        for i in list(word):
                if letters[i] < word.count(i):
                        return False
        return True

def removeOneFromLetters(word, letters):
        for i in list(word):
                letters[i] = letters[i] - 1;
                
for i in range(1, int(raw_input()) + 1):
        l = printer(raw_input())
        print("Case #%d: %s" % (i , (''.join(str(x) for x in sorted(l)))))
        

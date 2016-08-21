#!/usr/bin/python

import sys
import io
import array

f = open(sys.argv[1],'r')
w = io.open(sys.argv[1][:-3]+".out", 'w', newline='')
t = int(f.readline())

def getLetterIndex(x):
	return {
		'Z': 0,
		'E': 1,
		'R': 2,
		'O': 3,
		'N': 4,
		'T': 5,
		'W': 6,
		'H': 7,
		'F': 8,
		'U': 9,
		'I': 10,
		'V': 11,
		'S': 12,
		'X': 13,
		'G': 14
	}[x]

def getUniqueDigit(x):
	return {
		'Z': 0,
		'W': 2,
		'U': 4,
		'X': 6,
		'G': 8,
		'O': 1,
		'R': 3,
		'F': 5,
		'S': 7,
		'I': 9
	}[x]

def getLetters(x):
	return {
		'Z': 'ZERO',
		'W': 'TWO',
		'U': 'FOUR',
		'X': 'SIX',
		'G': 'EIGHT',
		'O': 'ONE',
		'R': 'THREE',
		'F': 'FIVE',
		'S': 'SEVEN',
		'I': 'NINE'
	}[x]
chars = ['Z','W','U','X','G','O','R','F','S','I']
totalChars = 0
for case in range(t):
	s = f.readline()
	phoneNumberArray = [0]*10
	letters = [0]*15
	for c in s:
		if(c == '\n'):
			break;
		letters[getLetterIndex(c)] += 1
		totalChars += 1
	for c in chars:
		count = letters[getLetterIndex(c)]
		if (count == 0):
			continue
		stringRep = getLetters(c)
		for l in stringRep:
			letters[getLetterIndex(l)] -= count
		phoneNumberArray[getUniqueDigit(c)] += count
		totalChars -= len(stringRep)*count
	w.write("Case #" + str(case+1) + ": ")
	for i in range(len(phoneNumberArray)):
		for j in range(phoneNumberArray[i]):
			w.write(str(i))
	w.write("\n")
		


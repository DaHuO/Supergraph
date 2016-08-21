'''
Created on Mar 13, 2016

Codejam template

@author: Ozge
'''
from itertools import groupby
filepath = ''
fileprefix = 'A-large' #Change

filepathname = filepath + fileprefix
infilename = filepathname + '.in'
outfilename = filepathname + '.out'
lines = open(infilename, 'rU').read().split("\n")
outfile = open(outfilename, 'w+')

tcases = int(lines[0]) 
linestart = 1 # check if parameters exists on more lines: N, M, L etc

def solve(word):
	letters=list(word)
	fl=letters[0]
	str=fl
	for i in range(1, len(letters)):
		if fl==letters[i]:
			str=letters[i]+str
			fl=letters[i]
		if fl<letters[i]:
			str=letters[i]+str
			fl=letters[i]
		if fl>letters[i]:
			str=str+letters[i]
			fl=str[0]

	return str	

		
for testcase in range(1, tcases+1): #change the value to the line number where the first case starts
   out = solve(lines[testcase]) #Assign solved value
   casestr = 'Case #'+str(testcase)+': '+out
   outfile.write(casestr+"\n")
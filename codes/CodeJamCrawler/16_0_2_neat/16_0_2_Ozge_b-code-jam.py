'''
Created on Mar 13, 2016

Codejam template

@author: Ozge
'''
from itertools import groupby
filepath = ''
fileprefix = 'B-large' #Change

filepathname = filepath + fileprefix
infilename = filepathname + '.in'
outfilename = filepathname + '.out'
lines = open(infilename, 'rU').read().split("\n")
outfile = open(outfilename, 'w+')

tcases = int(lines[0]) #this never chaneges
linestart = 1 # this might change if there are parameters N, M, L etc

def solve3(p):
	pancakes= list(p)
	lp=[x[0] for x in groupby(pancakes)]
	m=count(lp,'-')
	if lp[0]=='+':
		counter=2*m
	else:
		counter=2*m-1
	return counter	

def count(list,str):
	count=0
	for i in list:
		if i==str:
			count+=1
	return count
		
for testcase in range(1, tcases+1): #change the value to the line number where the first case starts
   out = solve3(lines[testcase]) #Assign solved value
   casestr = 'Case #'+str(testcase)+': '+str(out)
   outfile.write(casestr+"\n")
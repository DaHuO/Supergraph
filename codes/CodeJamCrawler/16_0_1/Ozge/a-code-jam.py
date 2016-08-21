'''
Created on Mar 13, 2016

Codejam template

@author: Ozge
'''

filepath = ''
fileprefix = 'A-large' #Change

filepathname = filepath + fileprefix
infilename = filepathname + '.in'
outfilename = filepathname + '.out'
lines = open(infilename, 'rU').read().split("\n")
outfile = open(outfilename, 'w+')

tcases = int(lines[0]) #this never chaneges
linestart = 1 # this might change if there are parameters N, M, L etc
res= [0,0,0,0,0,0,0,0,0,0]
def solve(number, counter, sum):
	global res
	if number==0:
		return "INSOMNIA"
	else:
		num=number*counter #1
		numcopy=num #1
		while num>0:
			digit=num%10
			if res[digit]==0:
				res[digit]=1
				sum=sum+1
			num//=10
		if sum==10:
			return numcopy
		else:
			return solve(number, counter+1, sum) 
   
def checksum(sum):
	if sum<10:
		False
	else:
		True

for testcase in range(1, tcases+1): #change the value to the line number where the first case starts
    out = solve(int(lines[testcase]), 1, 0) #Assign solved value
    casestr = 'Case #'+str(testcase)+': '+str(out)
    res= [0,0,0,0,0,0,0,0,0,0]
    outfile.write(casestr+"\n")
#!/usr/bin/python2
from sets import Set
def countflip(string):
	print("string :::::: " +string)

	short=[]
	count=0
	for i in string:
		if len(short) ==0 or short[-1] != i:
			short.append(i)
		else:
			print "i %s short %s"%(i,short) 
	print "short %s"%short
	index =1
	for i in short:
		if i == "-":
			count +=1
		elif count>0 and index!=len(short):
			count +=1
		index+=1
	if count>0 and short[0]=="+":
		count +=1
	return count

#lines = open("A-large.in").readlines()
lines = open("B-large.in").readlines()

f = open('ouput.txt', 'w')
t = int(lines[0])
for i in range(1,t+1):
	string = lines[i]
	flips = countflip(string.replace("\n",""))
	print("string %s %s flip %s"%(string,len(string),flips))
	f.write("Case #%s: %s"%(i,flips))
	if (i<t):
		f.write("\n")
f.close()
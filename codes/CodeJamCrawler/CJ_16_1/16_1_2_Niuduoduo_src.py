#! /usr/bin/env python

from numpy import *

def get_stream(file):
	for line in file:
		for token in line.strip().split():
			yield token
 
def get_int(stream):
	retour = int(stream.next())
	return retour

def get_str(stream):
	retour = str(stream.next())
	return retour
 
def get_solution(stream):

#mise ne forme
#=============

	#n
	n = get_int(stream)
	m=[]
	dnj=[]
	for i in xrange(2*n-1):
		for j in xrange(n):
			l = get_int(stream)
			dnj.append(l)
	ens = set(dnj)

	
#traitement
#==========

	a =[]

	for i in ens :
		if dnj.count(i)%2 == 1:
			a.append(i)
	a.sort()
	s=""
	for x in xrange(n):
		s += str(a[x]) + ' '
	return s

def main(path): 
	print "Fonction main\n"
	file = open(path, 'r')
	outfile = open(path + '.out', 'w')
	stream = get_stream(file)  
	cases = get_int(stream)
	  
	solution = []
	for case in range(0, cases):
		solution = get_solution(stream)
		buffer = "Case #" + str(case+1) + ": " + str(solution) + "\n"
		outfile.write( buffer )
		#print buffer
 
	outfile.close()

print "Appel traitement\n"
main("in")




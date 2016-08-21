#! /usr/bin/env python
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

	#s
	s = get_str(stream)
	print s

#traitement
#==========
	m=s[0]
	a=''
	#print m
	#Boucle
	for l in s:
		#print "l = " + l
		#print "m = " + m
		#print "a avant = " + a
		if a == '':
			a=l
		elif l >= a[0]:
			a = l+a
		else :
			a = a+l
		#print "a apres =  " + a + '\n'
		m=l

	return a

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
		print buffer
 
	outfile.close()

print "Appel traitement\n"
main("in")




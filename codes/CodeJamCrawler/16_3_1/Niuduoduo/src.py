#! /usr/bin/env python
import string

def get_stream(file):
	for line in file:
		for token in line.strip().split():
			yield token
 
def get_int(stream):
	retour = int(stream.next())
	return retour
 
def get_solution(stream):

#Mise ne forme
	n=get_int(stream)
	l = [[string.ascii_uppercase[i],get_int(stream)] for i in xrange(n)]
#	print n
#	print l

#Traitement
	s = ""
	while True:
		amax = max(l, key=lambda x: x[1])[1]
#		print amax
		if amax ==0: break
		
		nmax = 0
		for i in l:
			if i[1]==amax: nmax+=1
#		print nmax
		
		x = ""
		for i in l:
			if i[1]==amax:
				x+=str(i[0])
				i[1]-=1
				if nmax != 2:break
		s+= x + ' '
#		print s
		
#		print " " 

	return s

def main(path): 
	print "Fonction main\n"
	file = open(path, 'r')
	outfile = open('out', 'w')
	stream = get_stream(file)  
	cases = get_int(stream)

	solution = []
	for case in range(0, cases):
                        solution = get_solution(stream)
                        buffer = "Case #" + str(case+1) + ": " + str(solution) + "\n"
                        outfile.write( buffer )
                        print buffer
 
	outfile.close()

main("in")




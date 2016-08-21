import numpy as np
import collections

def letterCount(word):
	d = collections.defaultdict(int)
	for c in word:
		d[c] += 1
	return d

def removeLetters(d,string,num):
	for char in string:
		d[char]=d[char]-num
	return d

N = raw_input('')
for i in np.arange(0,int(N),1):
	seq = raw_input('')
	d = letterCount(seq)
	#print d
	numbers = np.zeros(10, dtype = int)

	# COUNT R 
	# Remove ZERO
	#print "Numer of Z:", d['Z'] 
	numbers[0]=d['Z']
	d = removeLetters(d,"ZERO",d['Z'])

	# Count W 
	#print "Numer of W:", d['W'] 
	# Remove TWO
	numbers[2]=d['W']
	d = removeLetters(d,"TWO",d['W'])

	# Count X
	# Remove SIX
	#print "Numer of X:", d['X'] 
	numbers[6]=d['X']
	d = removeLetters(d,"SIX",d['X'])

	# Count G 
	# Remove EIGHT
	#print "Numer of G:", d['G'] 
	numbers[8]=d['G']
	d = removeLetters(d,"EIGHT",d['G'])


	# Count U
	# Remove FOUR
	#print "Numer of U:", d['U'] 
	numbers[4]=d['U']
	d = removeLetters(d,"FOUR",d['U'])


	# Count H 
	# Remove THREE
	#print "Numer of H:", d['H'] 
	numbers[3]=d['H']
	d = removeLetters(d,"THREE",d['H'])

	# Count F
	# Remove FIVE
	#print "Numer of F:", d['F'] 
	numbers[5]=d['F']
	d = removeLetters(d,"FIVE",d['F'])

	# Count I 
	# Remove NINE
	#print "Numer of I:", d['I'] 
	numbers[9]=d['I']
	d = removeLetters(d,"NINE",d['I'])


	# COUNT V
	# Remove SEVEN
	#print "Numer of V:", d['V'] 
	numbers[7]=d['V']
	d = removeLetters(d,"SEVEN",d['V'])
	
	# COUNT O
	# Remove ONE
	#print "Numer of O:", d['O'] 
	numbers[1]=d['O']
	d = removeLetters(d,"ONE",d['O'])

	#print numbers
	final = ""
	print "CASE #" + str(i+1) +":",
	for j in np.arange(0,10,1):
		for k in np.arange(0,numbers[j],1):
			final = final + str(j) 
	print final



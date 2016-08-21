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

def flip(pile,rang):
	retour = []
	for i in range(0,len(pile)):
		if 0<=i and i<=rang:
			if pile[rang-i]==0 : retour.append(1)
			else               : retour.append(0)
		else:
			retour.append(pile[i])
		#print retour
	return retour		

def get_solution(stream):

#mise ne forme
#=============

	#plus moins
	plus_moins = get_str(stream)
	pile = []
 	#print "plus_moins = " + plus_moins
	for c in plus_moins:
		if c=="+": pile.append(1)
		else: pile.append(0)
	#print pile

#traitement
#==========
	if   sum(pile) == 0        : return 1
	elif sum(pile) == len(pile): return 0
	else:
		fin = False
		ctr=0
		while not fin:
			indice = -1
			for f in pile:
				indice+=1
				if indice > 0:
					if (f - prev_f) != 0:
						print "rang  :" + str(indice-1)
						print "avant : " + str(pile)
						pile = flip(pile,indice-1)
						print "apres : " + str(pile)
						ctr+=1
						if sum(pile) == len(pile): return ctr
						elif sum(pile) == 0: return ctr+1
						else: break
				prev_f = f


def main(path): 
	#print "Fonction main\n"
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




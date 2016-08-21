import os, sys

def evacuation(liste):
	somme=sum(liste)
	evac=""
	while(sum(liste) > 0):
		m = max(liste)
		indices = [i for i, j in enumerate(liste) if j == m]
		# si deux max atteints
		evac = evac + chr(65+indices[0])
		liste[indices[0]] = liste[indices[0]] - 1
		if(len(indices)==2):
			evac = evac + chr(65+indices[1])
			liste[indices[1]] = liste[indices[1]] - 1
		evac = evac + (" ")
		
	return evac

#def func(param):
#if(cond):
#while(cond):
#for c in range(0,10) : 0-9

# Lecture de l'entree
fichier = open(sys.argv[1])
T = fichier.readline()
cpt = 0

while(cpt < int(T)):
	N = fichier.readline().rstrip('\n')
	mot = fichier.readline().rstrip('\n')
	l = [N] * 0
	l = mot.split(' ')
	l = list(map(int, l))
	cpt+=1	
	print("Case #",cpt,": ",evacuation(l), sep='')

fichier.close()

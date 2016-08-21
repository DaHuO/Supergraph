import os
import sys

os.chdir('C:\\Users\Rémi\Documents\Informatique\Google Code Jam\Problem D')

def small_input (K,C,S):
	result='1'
	for i in range(K):
		if (i>0): result=result+' '+str(i+1)
	return result

def base (liste,b):
	result=0
	for i in range(len(liste)):
		result=result*b
		result=result+int(liste[i])
	return result+1

def large_input (K,C,S):
	if (K>C*S): return 'IMPOSSIBLE'
	result=''
	n=0
	while (n<K):
		liste=[]
		for i in range(C):
			if (n<K): liste.extend([n])
			else: liste.extend([K-1])
			n=n+1
		result=result+' '+str(base(liste,K))
	return result
	


output = open('Output.txt','w')
Case=0
with open("Input.txt", "r") as txt:
	for line in txt:
		if (Case==0):
			Case=Case+1
		else:
			K, C, S=map(int, line.split())
			output.write('Case #'+str(Case)+': '+large_input(K,C,S)+'\n')
			Case=Case+1
output.close()



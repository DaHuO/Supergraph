import os
import sys
import math

os.chdir('C:\\Users\Rémi\Documents\Informatique\Google Code Jam\Problem C')

def base2 (number):
	result=''
	i=0
	reading=number
	while (reading>0):
		if (reading%2==1):
			result='1'+result
		else: result='0'+result
		i=i+1
		reading=reading//2
	return result

def base (string,b):
	result=0
	for i in range(len(string)):
		result=result*b
		if (string[i]=='1'): result=result+1
	return result

def liste_prime_numbers (n): # Recherche et impression de nombres premiers
	liste=[0]*(n+1)
	max=math.sqrt(n)
	root=2
	prime=open('Liste de nombres premiers.txt','w')
	while (root<=max):
		if(liste[root]==0):
			prime.write(str(root)+'\n')
			indice=2*root
			while(indice<=n):
				liste[indice]=1
				indice=indice+root
		root=root+1
	prime.close()

def prime_numbers ():
	with open("Liste de nombres premiers.txt", "r") as txt:
		for line in txt:
			print(int(line))

output = open('Output.txt','w')
output.write('Case #1:'+'\n')
found=0
for N in range(2**31+1,2**32,2):
	string=base2(N)
	diviseurs=[0]*11
	b=2
	while (b<=10):
		n=base(string,b)
		with open("Liste de nombres premiers.txt", "r") as txt:
			for line in txt:
				if (n%int(line)==0):
					diviseurs[b]=int(line)
					break
		if (diviseurs[b]==0): b=99
		else: b=b+1
	if (b<99):
		output.write(string+' '+str(diviseurs[2])+' '+str(diviseurs[3])+' '+str(diviseurs[4])+' '+str(diviseurs[5])+' '+str(diviseurs[6])+' '+str(diviseurs[7])+' '+str(diviseurs[8])+' '+str(diviseurs[9])+' '+str(diviseurs[10])+'\n')
		found=found+1
	if (found>=500): break
output.close()


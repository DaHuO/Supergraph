import os
import sys

os.chdir('C:\\Users\Rémi\Documents\Informatique\Google Code Jam\Problem A')

def allseen(list):
	accu=True
	for i in range(10):
		if (list[i]==0): accu=False
	return accu

def sheep(N):
	if (N==0): return 0
	dgseen=[0]*10
	current=0
	while (not allseen(dgseen)):
		current=current+N
		for digit in str(current):
			dgseen[int(digit)]=1
	return current


output = open('Large output.txt','w')
Case=0
with open("Large input.txt", "r") as txt:
	for N in txt:
		if (Case==0):
			Case=Case+1
		else:
			result=sheep(int(N))
			if (result==0): output.write('Case #'+str(Case)+': '+'INSOMNIA'+'\n')
			else: output.write('Case #'+str(Case)+': '+str(result)+'\n')
			Case=Case+1
output.close()


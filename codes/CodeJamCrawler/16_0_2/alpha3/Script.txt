import os
import sys

os.chdir('C:\\Users\Rémi\Documents\Informatique\Google Code Jam\Problem B')

def pancakes(string):
	position='+'
	accu=0
	for i in range(len(string)):
		if (string[len(string)-i-1] != '\n' and string[len(string)-i-1] != position):
			accu=accu+1
			if (position=='+'): position='-'
			else: position='+'
	return accu


output = open('Output.txt','w')
Case=0
with open("Input.txt", "r") as txt:
	for line in txt:
		if (Case==0):
			Case=Case+1
		else:
			result=pancakes(line)
			output.write('Case #'+str(Case)+': '+str(result)+'\n')
			Case=Case+1
output.close()



import re

def numFlips(pancakes,numPancakes):
	flips = 0
	ri = numPancakes - 1
	while(pancakes[ri] != '-' and ri >= 0):
		ri -= 1
	if(ri < 0):
		return 0 
	if(pancakes[0] == '+'):
		pancakes = flip(pancakes,1)
		flips += 1
	pancakes = flip(pancakes,ri + 1)
	flips += 1
	return numFlips(pancakes,ri + 1) + flips
	
def flip(pancakes, bottom):
	b = bottom - 1
	return re.sub(r'[+]|[-]',lambda m: '+' if m.group(0) == '-' else '-',pancakes[b::-1]) + pancakes[bottom:]

def clump(string):
	return re.sub(r'([+]+)|([-]+)',lambda m: '+' if m.group(0)[0] == '+' else '-',string)

with open("B-large.in",'r') as fileI:
	fileO = open("output2.txt","w")
	T = int(fileI.readline())
	for j in range(T):
		pancakes = clump(fileI.readline())
		fileO.write("Case #" + str(j + 1) + ": " + str(numFlips(pancakes,len(pancakes))) + "\n")
	fileO.closed
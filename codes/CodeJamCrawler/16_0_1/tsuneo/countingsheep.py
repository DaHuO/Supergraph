import re

found = {}

def init():
	for i in xrange(10):
		found[i] = 0

def allmatch():
	return found[0] and found[1] and found[2] and found[3] and found[4] and found[5] and found[6] and found[7] and found[8] and found[9]

def count(input):
	input = int(input)
	if (input == 0):
		return 'INSOMNIA'
	init()
	number = input
	while (not(allmatch())):
		check(number)
		number += input
	return number-input

def check(number):
	for i in found:
		if (found[i]==0):
			if (match(str(i),str(number))):
				found[i] = 1

def match(digit,number):
	return re.search(digit,number)

file = open('A-large.in','r')
input =  file.read().split('\n')
input_number = input.pop(0)
output = open('output','w')
for line in input:
	if (line != ''):
		print count(line)
		output.write("Case #"+str(input.index(line)+1)+": "+str(count(line))+'\n')
output.close()
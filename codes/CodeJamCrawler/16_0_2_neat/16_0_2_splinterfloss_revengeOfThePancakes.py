import os

def isDone(pancakes):
	for pancake in pancakes:
		if pancake == 0:
			return False
	return True

def flip(pancake):
	if pancake == 0:
		return 1
	else:
		return 0

def getNumFlips(pancakes):
	flips = 0
	for i in xrange(len(pancakes)-1, -1, -1):
		if(pancakes[i] == 0):
			flips+=1
			for i in xrange(0, i):
				pancakes[i] = flip(pancakes[i])
	return flips

with open('input.txt') as input_file:
    testCases = input_file.readlines()
numTestCases = testCases[0]
testCases.remove(numTestCases)
output_filename= 'output.txt'
if os.path.exists(output_filename):
	os.remove(output_filename)
for i in range(0, len(testCases)):
	binary_list = []
	for pancake in testCases[i].rstrip():
		if pancake == '+':
			binary_list.append(1)
		else:
			binary_list.append(0)
 	numFlips = getNumFlips(binary_list)
	
	
	with open(output_filename, 'a') as output_file:
		output_file.write('Case #' + str(i+1) + ': ' + str(numFlips) + '\n')










# Eric Montijo
# Google Code Jam qualification round 4/9/2016

import array

# Open input/output files
#fin = open('qB-small-input-test.txt','r')
fin = open('B-large.in','r')
fout = open('output.txt','w')
num_inputs = int(fin.readline())

for i in range (0, num_inputs): # Visit each input stack
	moves = 0
	pattern = fin.readline().rstrip()
	# print('pattern=',pattern)
	
	lastChar = pattern[0]
	for j in range(1,len(pattern)):
		# print(pattern[j])
		# print('j=',j, ' p[j]=',pattern[j], ' lastchar=',lastChar)
		if(pattern[j] != lastChar):
			moves += 1
			lastChar = pattern[j]
			# print('move made')
	if(lastChar == '-'):
		moves += 1
		# print('lastchar=-, add 1 move')
	
	# print('Moves used: ' + str(moves) + '\n')
	outputLine = 'Case #' + str(i+1) + ': ' + str(moves) + '\n'
	fout.write(outputLine)

fin.close()
fout.close()

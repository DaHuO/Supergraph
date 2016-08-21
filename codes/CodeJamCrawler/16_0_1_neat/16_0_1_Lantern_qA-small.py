# Eric Montijo
# Google Code Jam qualification round 4/9/2016

# Open input/output files
# fin = open('qA-small-input-test.txt','r')
fin = open('A-large.in','r')
fout = open('output.txt','w')
num_inputs = int(fin.readline())

for i in range (0, num_inputs): # Visit each input
	base = int(fin.readline().rstrip())
	
	if(base > 0): # INSOMNIA only happens on a 0
		digitsLeft = ["0","1","2","3","4","5","6","7","8","9"]
		mult = 1
		
		# (brute force) try each product until we see every digit
		while(len(digitsLeft) > 0):
			product = str(base*mult)
			# print('product=', product, '\ndigitsLeft: ',digitsLeft)
			
			j = 0
			numLeft = len(digitsLeft)
			while(j < numLeft):
				for k in range(0, len(product)):
					# print(digitsLeft[j], ' ', product[k])
					if(digitsLeft[j] == product[k]): # match: remove digit
						digitsLeft.pop(j)
						numLeft -= 1
						break # move onto next digit
				else:
					j += 1
			mult += 1
			
		outputLine = 'Case #' + str(i+1) + ': ' + str(product)
	else:
		outputLine = 'Case #' + str(i+1) + ': INSOMNIA'
	# print(outputLine)
	fout.write(outputLine + '\n')

fin.close()
fout.close()

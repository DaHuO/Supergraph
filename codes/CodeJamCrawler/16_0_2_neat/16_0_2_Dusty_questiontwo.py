fileout = open('output.out', 'w')
filein = open('B-large.in', 'r')

N = int(filein.readline()) #Number of cases
for i in range(N):
	pancakes = list(reversed(list(filein.readline().strip())))
	count = 0
	for pancakeInd in range(len(pancakes)):
		if(pancakes[pancakeInd] == '-'):
			for x in range(pancakeInd, len(pancakes)):
				if(pancakes[x]=='+'):
					pancakes[x] = '-'
				else:
					pancakes[x] = '+'
			count += 1
	fileout.write('Case #'+str(i+1)+': '+str(count)+'\n')




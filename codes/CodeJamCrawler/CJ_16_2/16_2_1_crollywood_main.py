TEST_NAME = 'A-large'

def main():
	solutions = []
	with open(TEST_NAME+'.in', 'r') as f:
		rows = int(f.readline())
		for i in range(rows):
			result = ''
			tc = f.readline().strip()
			
			abc = getAbc(tc)
			result = getSolution(abc)
			
			solutions.append(result)
	
	with open(TEST_NAME+'.out', 'w') as f:
		counter = 1
		for line in solutions:
			f.write("Case #{0}: {1}\n".format(str(counter), line))
			counter += 1

def getAbc(tc):
	ABC = 'QWERTZUIOPASDFGHJKLYXCVBNM'
	res = {}
	for l in ABC:
		res[l] = 0
	for l in tc:
		res[l] += 1
	return res	

def getSolution(abc):
	res = []
	zeros, abc = extractZeros(abc)
	twos, abc = extractTwos(abc)
	sixes, abc = extractSixes(abc)
	eights, abc = extractEights(abc)
	sevens, abc = extractSevens(abc)
	fives, abc = extractFives(abc)
	fours, abc = extractFours(abc)
	threes, abc = extractThrees(abc)
	nines, abc = extractNines(abc)
	ones, abc = extractOnes(abc)
	
	res += ['0']*zeros + ['1']*ones + ['2']*twos + ['3']*threes + ['4']*fours + ['5']*fives + ['6']*sixes + ['7']*sevens + ['8']*eights + ['9']*nines
	return ''.join(res)
	
def extractZeros(abc):
	count = abc['Z']
	abc['Z'] -= count
	abc['E'] -= count
	abc['R'] -= count
	abc['O'] -= count
	return count, abc
	
def extractTwos(abc):
	count = abc['W']
	abc['T'] -= count
	abc['W'] -= count
	abc['O'] -= count
	return count, abc
	
def extractSixes(abc):
	count = abc['X']
	abc['S'] -= count
	abc['I'] -= count
	abc['X'] -= count
	return count, abc
	
def extractEights(abc):
	count = abc['G']
	abc['E'] -= count
	abc['I'] -= count
	abc['G'] -= count
	abc['H'] -= count
	abc['T'] -= count
	return count, abc
	
def extractSevens(abc):
	count = abc['S']
	abc['S'] -= count
	abc['E'] -= count
	abc['V'] -= count
	abc['E'] -= count
	abc['N'] -= count
	return count, abc

def extractFives(abc):
	count = abc['V']
	abc['F'] -= count
	abc['I'] -= count
	abc['V'] -= count
	abc['E'] -= count
	return count, abc

def extractFours(abc):
	count = abc['F']
	abc['F'] -= count
	abc['O'] -= count
	abc['U'] -= count
	abc['R'] -= count
	return count, abc
	
def extractThrees(abc):
	count = abc['R']
	abc['T'] -= count
	abc['H'] -= count
	abc['R'] -= count
	abc['E'] -= count
	abc['E'] -= count
	return count, abc
	
def extractNines(abc):
	count = abc['I']
	abc['N'] -= count
	abc['I'] -= count
	abc['N'] -= count
	abc['E'] -= count
	return count, abc
	
def extractOnes(abc):
	count = abc['O']
	abc['O'] -= count
	abc['N'] -= count
	abc['E'] -= count
	return count, abc
	
main()




























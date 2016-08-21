numTest = 0
inputs = [] 
largestLimit = 10**6


def calc(castNum, input):
	
	if input <= 0:
		print 'Case #%d: %s' % (castNum, 'INSOMNIA')
		return 'Case #%d: %s' % (castNum, 'INSOMNIA')
	
	aSet = set()
	
	for i in range(1, largestLimit):
		incNum = input*i;
		if isinstance(incNum, int) == False:
			print 'Case #%d: %s' % (castNum, 'INSOMNIA')
			return 'Case #%d: %s' % (castNum, 'INSOMNIA')
		
		aString = str(incNum)
		cList = list(aString)
		for c in cList:
			n = int(c)
			aSet.add(n)
		
		if len(aSet) == 10:
			print 'Case #%d: %d' % (castNum, incNum)
			return 'Case #%d: %d' % (castNum, incNum)
	

def main():
	f = open("A-large.in", 'r')
	numTest = int(f.readline())
	while True:
		line = f.readline()
		if not line: break
		inputs.append(int(line))
	f.close()
	
	print 'numtest : ' + str(numTest)
	
	f = open("output_large_test1.txt", 'w')
	
	for i in range(0, len(inputs)):
		output = calc(i+1, inputs[i])
		f.write(output + '\n')
	f.close()
	
if __name__ == "__main__":
    main()
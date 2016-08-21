threshold = 10**6

def isPrime(n):
	if n == 2 or n == 3:
		return True
	if n < 2 or n%2 == 0:
		return False
	if n < 9:
		return True
	if n%3 == 0:
		return False
	r = int(n**0.5)
	f = 5
	while f <= r and f < threshold:
		if n%f == 0:
			return False
		if n%(f+2) == 0:
			return False
		f +=6
	return True    

def increment(aList):
	currPos = len(aList) - 2
	while currPos >= 0:
		c = aList[currPos]
		if c == '0':
			aList[currPos] = '1'
			return True
		elif c == '1':
			aList[currPos] = '0'
		currPos = currPos - 1
	return False
			

def calc(n, j):
	maxNum = 2**n
	count = 0
	outputList = []
	
	numList = ['1']
	for i in range(0, n-2):
		numList.append(str('0'))
	numList.append(str('1'))
	numStr = ''.join(numList)
	currNum = long(numStr, 2)
	#print 'maxNum ' + str(maxNum)
	
	while currNum < maxNum and count < j:
		#print 'jamstr ' + numStr
		#print 'currNum ' + str(currNum)
		
		if increment(numList) == False:
			break
		numStr = ''.join(numList)
		currNum = long(numStr, 2)
		isEligible = True
		
		numBaseList = []
		
		for i in range(2, 11):
			num = long(numStr, i)
			#print 'Base ' + str(i) + ' => ' + str(num)
			if (isPrime(num)):
				#print 'PRIME'
				isEligible = False
				break
			else:
				numBaseList.append(num)
				#print 'NOT PRIME'
		
		if isEligible == True:
			#print 'found!!!'
			count = count + 1
			outputStr = numStr
			for i in numBaseList:
				divider = 2
				while divider < long(i/2):
					if (i % divider == 0):
						outputStr = outputStr + ' ' + str(divider)
						break
					divider = divider + 1
			outputList.append(outputStr)
	
	return outputList

def main():
	f = open("C-large.in", 'r')
	numTest = int(f.readline())
	print '# of test : ' + str(numTest)
	
	elements = str(f.readline()).split()
	n = elements[0]
	j = elements[1]
	f.close()
	
	print 'N ' + n
	print 'J ' + j
	outputList = calc(int(n), int(j))
	
	f = open("output_large_test3.txt", 'w')
	f.write('Case #1:\n')
	
	for e in outputList:
		print e
		f.write(e + '\n')
	print 'output size ' + str(len(outputList))
	f.close()

if __name__ == "__main__":
    main()
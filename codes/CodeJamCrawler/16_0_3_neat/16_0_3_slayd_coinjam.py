import sys,math

def isprime(n):
    '''
    check if integer n is a prime, return True or False
    '''
    # 2 is the only even prime
    if n == 2:
        return True
    # integers less than 2 and even numbers other than 2 are not prime
    elif n < 2 or not n & 1:
        return False
    # loop looks at odd numbers 3, 5, 7, ... to sqrt(n)
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True

def getFirstDivisor( n ) :

	i = 2
	while i < n :
		if n % i == 0 :
			return i
		i = i + 1

	return -1

def getLastDivisor( n ) :
	divisors = []
	for i in range(2,n) :
		if n % i == 0 :
			divisors.append(i)
	if len( divisors ) == 0 :
		return -1

	return divisors[-1]

def convert( s, n ) :
	i = 0
	result = 0
	for j in s[::-1] :
		result = result + int(j) * int ( math.pow(n,i) )
		i = i + 1

	return result

def getInputList( length ) :
	list = []
	realLen = length - 2;
	max = pow(2, realLen)
	
	for i in range(0, max) :
		s = str( bin(i) )[2:]
		if len(s) < realLen : 
			temp = ''
			for j in range(0, realLen- len(s) ) :
				temp = temp + '0'

			s = temp + s

		s = '1' + s + '1'
		list.append(s)

	return list

def getResult(inputLength, minimunResult) :
	print inputLength
	print minimunResult

	list = getInputList(inputLength)
	count = minimunResult;
	
	result = []
	resultDivisor = []
	for i in list :
		print i
		sub = []
		for j in range(2,11) : 
			sub.append( convert(i, j ))

		divisorList = []
		for j in sub :
			if isprime(j) :
				break

			r = getFirstDivisor(j)

			if r < 0 :
				break;

			divisorList.append(r)

		if len(sub) == len(divisorList) :
			#success
			result.append(i)
			resultDivisor.append(divisorList)
			count = count - 1;
			if ( count == 0 ) :
				break

	return (result, resultDivisor)



with open('C-small-attempt1.in') as f :
	line = f.read().splitlines()

	num = line[0]
	length = int(line[1].split(' ')[0])
	count = int(line[1].split(' ')[1])

	result = getResult(length, count)

	resultList = result[0]
	resultDivisorList = result[1]


	with open('result.txt', 'w') as resultFile :
	
		resultFile.write('Case #' + num  + ":\n")
		for i in range(0, len(resultList)) :
			resultFile.write( resultList[i])
			for j in range(0, len(resultDivisorList[i])) :
				resultFile.write(' ')
				resultFile.write( str( resultDivisorList[i][j] ))
			resultFile.write('\n')








primes = [2]
def isPrime(n):
	global primes
	#return True if is prime, otherwise return a valid divisor 
	for i in range(2,int(n**0.5)+1):
		if (i in primes and n%i==0):
			return i
		if (i>primes[-1] and isPrime(i)==True):
			primes.append(i)
			if n%i==0:
				return i
	return True


def convertToBase10(n, base):
    number = []
    negative = False

    # If n is a negative number (it's a string at this moment of the code)..
    # then replace the minus sign with a blank character to correctly convert string to int...
    # so the algorithm can continue.
    if n[0] == '-':
        n = n.replace('-', '')
        negative = True

    for i in n:
        number.append(int(i))

    number = number[::-1]
    if negative:
        for i in range(len(number)):
            number[i] = number[i] * -1
            number[i] = number[i] * (base ** i)
    else:
        for i in range(len(number)):
            number[i] = number[i] * (base ** i)

    return sum(number)


def increment(number, length):
	bNumber = int(number, base=2)
	incremented = bNumber+1
	incremented = format(incremented, "b")
	if len(incremented)>length:
		return False
	padded = "0"*(length-len(incremented))+incremented
	return padded

def coinJam(N, J):
	#iterate through all combinations and test if they are valid
	results = []
	current = "0"*(N-2)
	while current!=False and len(results)<J:
		value = "1"+current+"1"
		#print value
		result = [value]
		for i in range(2, 11):
			number = convertToBase10(value, i)
			#print number
			divisor = isPrime(number)
			if divisor==True:
				#print primes
				break
			result.append(divisor)
		if len(result) ==10:
			results.append(result)
			print result
		current = increment(current,N-2)
	return results

print coinJam(16, 50)
	



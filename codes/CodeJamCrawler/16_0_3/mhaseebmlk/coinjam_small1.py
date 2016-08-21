import itertools
import time

def genCoins(length):
	coins = []
	bitStrings = ["".join(seq) for seq in itertools.product("01", repeat=length)] 
	for x in xrange(0,len(bitStrings)):
		if ((bitStrings[x]).startswith('1')) and ((bitStrings[x]).endswith('1'))  :
			coins.append(bitStrings[x])
	return coins
def toBase(base,bitString):
	i = len(bitString) - 1
	exponent = 0
	value = 0
	while (i>=0):
		value += ((base**exponent)*(int(bitString[i])))
		exponent += 1
		i -= 1
	# print '---> Base:',base,'Value:',value
	return value
def isPrime(value):
	# # print str(value)+'-------:'
	for i in range(1, int(value**0.5) + 1):
		if (value%i == 0) and (i!=1) and (i!=value):
			return (False,i)

	return (True,1)



def isJamCoin(bitString):
	divisors = []
	for base in xrange(2,11):
		res = isPrime(toBase(base,bitString))

		# if it is not prime then add the divisor to the divisors list
		if not (res[0]):
			divisors.append(res[1])
			# print 'Base: '+(str(base)),bitString+' result: '+(str(res[0])),res[1],'Value of this bitString is: ',(toBase(base,bitString))
		else:
			# print 'The bitString '+bitString+' is not a isJamCoin'
			# print 'Base: '+(str(base)),bitString+' result: '+(str(res[0])),res[1],'Value of this bitString is: ',(toBase(base,bitString))
			return (False,-1)
	# print 'The bitString '+bitString+' is a isJamCoin. Check the divisors array'
	return (True,divisors)

def main():
	testCases = raw_input()
	(n,j) = ((raw_input()).split(' '))
	coins = genCoins((int(n)))
	j = int(j)
	count = 0
	print ('Case #'+(str(1))+':')
	for x in xrange(0,len(coins)):
		if (count==j):
			break
		res = isJamCoin(coins[x])
		if res[0] == True:
			count += 1
			print coins[x], 
			for x in xrange(0,len(res[1])):
				print res[1][x],
			print

if __name__ == '__main__':
	start_time = time.time()
	main()
	print("--- %s seconds ---" % (time.time() - start_time))
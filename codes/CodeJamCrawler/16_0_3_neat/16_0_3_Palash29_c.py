#import math
# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
def getnum(jc,k):
	numb = 0
	factor = 1
	while jc!=0:
		numb += (jc&1)*factor
		jc = jc>>1
		factor = factor*k
	return numb

def isPrime(num):
	i=2
	j = 1000 #math.sqrt(num)
	# While j = 1000 does not disqualify the jam coin candidate invalid, it allows us to 
	# move on the next possible candidate without too much computation/time penalty.
	# If at all we weren't able to get required number of jam coins, we could have used 
	# couple of ways to improve upon the heuristics
	# 1. Increase the max_divisor threshold for failed jam coin candidates, in increasing
	# offsets.
	while i < j:
		if(num%i==0):
			return i
		i = i+1
	else:
		return -1

T = int(input())  # read a line with a single integer

for i in range(1, T + 1):
	n, m = [int(s) for s in input().split(" ")]  # read a list of integers, 2 in this case
	print("Case #{}:".format(i))
	#bits from numbered from 0 to n-1
	#loop until we find m jamcoins
	jc = 2**(n-1)+1
	j=0
	divisor = [-1,-1,-1,-1,-1,-1,-1,-1,-1]
	while (j < m) and (jc < 2**n):
		for k in range(2,11):
			num = getnum(jc,k)
			#print("jc ={}, base = {}, num  = {}".format(jc,k,num))
			divisor[k-2] = isPrime(num)
			if divisor[k-2] == -1:
				break
			#if num%100 == 1:
			#	print("{} not jamcoin".format(num))
		else:
			print(num,divisor[0],divisor[1],divisor[2],divisor[3],divisor[4],divisor[5],divisor[6],divisor[7],divisor[8])
			j = j + 1
		jc = jc + 2
		
  #for each bit from 1 to n-2 we will continue toggling bits in increasing value.
  #Generate next possible candidate for jamcoin
  #Convert current candidate in each of the bases from 2 to 10.
  #For each base, check if the number is prime, break if a divisor is found, save the divisor.
  #If for any base a prime is found abort checking primality of current candidate for next bases
  #If success, print jamcoin with divisors for each bases
  #increment m
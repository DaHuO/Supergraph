import math

def jamcoin_base(jamcoin,base):
	jamcoin_len=len(jamcoin)

	num = 1 

	mul = base
	for i in range(jamcoin_len):
		num += jamcoin[jamcoin_len-1-i] * mul
		mul *= base
	num += mul

	return num

def primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in xrange(3,n,2) if sieve[i]]

def check_jamcoin(jamcoin):

	divisors = list()

	for base in range(2,11):
		base_num=jamcoin_base(jamcoin,base)

		#print base,base_num	
		sqrt_base_num=int(math.sqrt(base_num))
		p_i = 0
		while p[p_i] <= sqrt_base_num:
			if base_num % p[p_i] == 0:
				divisors.append(p[p_i])
				break
			p_i += 1

		# prime number here
		if p[p_i] > sqrt_base_num:
			return divisors

	return divisors
	

for t in range(input()):
	N,J = map(int,raw_input().split())

	print "Case #%d:" %(t+1)

	p=primes(int(math.sqrt(10**N))+1)

	#print N,J

	jamcoin=[0 for i in range(N-2)]

	jamcoin_cnt = 0
	for i in range(2**(N-2)):

		num=i

		#generate the jamcoin
		for j in range(N-2):
			jamcoin[N-3-j]=num % 2
			num /= 2

		#print jamcoin,len(check_jamcoin(jamcoin))

		divisor = check_jamcoin(jamcoin)
		if len(divisor) == 9:
			print jamcoin_base(jamcoin,10)," ".join(map(str,divisor))
			jamcoin_cnt += 1
			if (jamcoin_cnt >= J):
				break
		
		#print i,jamcoin,jamcoin_base(jamcoin,2)


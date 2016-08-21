
def primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * (n/2)
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i/2]:
            sieve[i*i/2::i] = [False] * ((n-i*i-1)/(2*i)+1)
    return [2] + [2*i+1 for i in xrange(1,n/2) if sieve[i]]

p = primes(65536+10)
T = int(raw_input())

def find(number):
	sqrt = number ** 0.5

	answer = 0
	for i in p:
		if i > sqrt:
			break
		if not number % i:
			answer = i
			break
	return answer


for i in xrange(1, T+1):
	print 'Case #1:'

	N, J = map(int, raw_input().split())

	begin = int('1'+'0'*(N-2)+'1', 2)
	end   = int('1'*N, 2)

	founded = 0
	for i in xrange(begin, end+1, 2):
		binary = bin(i)[2:]

		res = []
		for k in xrange(2, 11):
			number = int(binary, k)

			ans = find(number)
			res.append(ans)
			if not ans: break

		if res[-1] != 0:
			print binary, ' '.join(map(str, res))
			founded += 1

		if founded == J:
			break

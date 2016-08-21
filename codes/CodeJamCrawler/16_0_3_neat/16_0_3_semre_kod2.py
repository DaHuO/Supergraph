
def primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * (n/2)
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i/2]:
            sieve[i*i/2::i] = [False] * ((n-i*i-1)/(2*i)+1)
    return [2] + [2*i+1 for i in xrange(1,n/2) if sieve[i]]

p = primes(65536+10)

T = int(raw_input())

N,J = map(int,raw_input().split())


s = int('1' + '0'*(N-2) + '1',2)

end  = int('1'*N,2)
print end
found = 0

print "Case #1:"
for i in xrange(s,end+1,2):

	if found >= J:
		break
	b = bin(i)[2:]
	res = []
	for j in xrange(2,11):
		n = int(b,j)
		flag = False
		for k in p:
			if k*k > n:
				break
			if not n % k:
				flag = True
				res.append(k)
				break



		if not flag:
			break

	if not flag:
		continue

	st = b
	for r in res:
		st += " " + str(r)
	print st
	found += 1

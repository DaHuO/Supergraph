import itertools

# From http://stackoverflow.com/questions/2897297/speed-up-bitstring-bit-operations-in-python
def prime_numbers(limit=1000000):
    '''Prime number generator. Yields the series
    2, 3, 5, 7, 11, 13, 17, 19, 23, 29 ...
    using Sieve of Eratosthenes.
    '''
    yield 2
    sub_limit = int(limit**0.5)
    flags = [True, True] + [False] * (limit - 2)
    # Step through all the odd numbers
    for i in range(3, limit, 2):
        if flags[i]:
            continue
        yield i
        # Exclude further multiples of the current prime number
        if i <= sub_limit:
            for j in range(i*i, limit, i<<1):
                flags[j] = True

def f():
	n, j = tuple(map(int, input().split()))
	c = 0
	for i in list(itertools.product("01", repeat=n-2)):
		s = '1'+''.join(i)+'1'
		o = [s]
		b = [int(s, x) for x in range(2,11)]
		f = False
		for k in b:
			f = False
			for kk in e:
				if k % kk == 0:
					o.append(kk)
					f = True
					break
			if not f: break
		if f:
			for k in o:
				print(k, end=' ')
			print()
			c = c + 1
		if c == j: break

e = list(prime_numbers(256));
for i in range(int(input())):
	print("Case #{0}:".format(i+1))
	f()

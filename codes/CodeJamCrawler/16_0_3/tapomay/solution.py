N = int(input())

def isNotPrime(n):
	if n == 2:
		return -1
	if n % 2 == 0:
		return 2
	i = 3
	while (i*i) <= n:
		if n%i == 0:
			return i
		i = i + 2
	return -1

def getDiv(decval, base):
	bn = bin(decval)[2:]
	val = int(bn, base)
	ret = isNotPrime(val)
	# print('getdiv:' + str(decval) + ":" + str(base) + ":" + str(ret))
	return ret
	
def coinJam(size, count):
	base = 1 << (size-1) | 1
	num = 0
	found = 0
	while found < count:
		b = num << 1
		bn = base | b
		divs = []
		for i in range(2,11):
			d = getDiv(bn, i)
			if d == -1:
				break
			else:
				divs = divs + [d]
		if len(divs) == 9:
			print (bin(bn)[2:] + ' ' + ' '.join(map(str, divs)))
			found = found + 1
		# else:
		# 	print('discard: ' + bin(bn))
		num = num + 1
	
for i in range(1, N+1):
	M = input()
	Mtup = M.split()
	size = int(Mtup[0])
	count = int(Mtup[1])
	print('Case #' + str(i) + ':')
	coinJam(size, count)


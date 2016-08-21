
def to_b10(origin, old_base):
	val = 0
	k = 0
	for i in xrange(len(origin)-1, -1,-1):
		val += int(origin[i])*pow(old_base, k)
		k += 1
	return val

def foo(N, J):
	num = [0 for i in xrange(N)]
	num[0] = num[N-1] = 1
	count = 0
	div_list = []
	while count < J:
		b = 2
		div = 0
		tmp = ["".join(map(str, num))]
		while b < 11:
			num_int = to_b10(num, b)
			divisor = to_b10("11", b)
			if num_int % divisor != 0:
				break
			else:
				tmp.append(divisor)
			b += 1
		if b == 11:
			div_list.append(tmp)
			count += 1
		# increment num
		i = N-2
		while num[i] != 0 and i > 0:
			i -= 1
		num[i] = 1
		i += 1
		while i < 15:
			num[i] = 0
			i += 1
	for item in div_list:
		for x in item:
			print x,
		print

import sys
f = open(sys.argv[1], 'r')				
N = int(f.readline().strip())
print "Case #1:"
for case in xrange(1, N+1):
	[n,j] = map(int, f.readline().strip().split(' '))
	foo(n,j)
	#print n,j
	#sieve = [False in xrange()]	
		

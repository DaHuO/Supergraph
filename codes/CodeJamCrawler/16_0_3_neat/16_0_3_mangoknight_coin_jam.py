import itertools

T = int(raw_input())
N, J = raw_input().split(' ')
N = int(N)
J = int(J)

def is_it_prime(x):
	x = int(x)
	for i in xrange(2, 10001):
		if(x % i == 0):
			return i
	return 0


def check(x):
	ans = []
	for i in range(2, 11):
		y = int(str(x), i)
		a = is_it_prime(y)
		if not a:
			return 0
		else:
			ans.append(str(a))
	return ans


for t in range(T):
	print "Case #" + str(t + 1) + ":"
	count = 0
	for i in itertools.product(['0', '1'], repeat=N-2):
		i = ''.join(i)
		i = '1' + str(i) + '1'
		#print i
		a = check(i)
		if not a:
			continue
		else:
			print i + ' ' + ' '.join(a)
			count += 1
			if count == J: break

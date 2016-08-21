import math
import sys

def main():
	T = input()
	for tt in range(T):
		s = raw_input()
		K, C, S = (int(x) for x in s.split(' '))

		if S<K:
			print 'Case #{0}: IMPOSSIBLE'.format(tt+1)
			continue

		r = []
		step = int(math.pow(K, C-1))
		for i in range(0,K):
			r.append(1+i*step)

		sys.stdout.write('Case #{0}: '.format(tt+1))
		for i in r:
			sys.stdout.write('{0} '.format(i))

		print


main()
import sys
from decimal import Decimal


def tie(probs):
	K = len(probs)
	f = [0 for _ in range(K+1)]
	f[0] = 1
	for i, p in enumerate(probs):
		for j in reversed(range(1, min(i+1, K/2)+1)):
			f[j] = f[j-1] * p + f[j] * (1-p)
		f[0] = f[0] * (1-p)
		# print i, p, f
	return f[K/2], probs


def calc():
	N, K = [int(_) for _ in raw_input().split()]
	probs = [float(_) for _ in raw_input().split()]
	# Small BEGIN
	from itertools import combinations
	ans = 0
	for tt, ps in enumerate(combinations(probs, K)):
		#if tt % 1000 == 0:
		#	print >> sys.stderr, t, tt
		ans = max(ans, tie(ps)[0])
	return ans
	# Small END
	''' Big
	f = [[[0 for j in range(N+1)] for i in range(N+1)] for ii in range(N+1)]
	f[0][0][0] = (None, 1, 0)
	for ii1, p in enumerate(probs):
		ii = ii1 + 1
		print '=====', ii, '====='
		for i in range(N+1):
			for j in range(N+1):
				# f[ii][i][j] = max(f[ii-1][i-1][j-1] * p + f[ii-1][i-1][j] * (1-p), f[ii-1][i][j])
				l, m, r = _, f[ii-1][i-1][j-1][1] * p + f[ii-1][i-1][j][2] * (1-p), _
				f[ii][i][j] = (l, m, r)
				l, m, r = _, f[ii-1][i-1][j-1][0] * p + f[ii-1][i-1][j][1] * (1-p), _
				if m > f[ii][i][j][1]:
					f[ii][i][j] = (l, m, r)
				l, m, r = _, f[ii-1][i][j][1], _
				if m > f[ii][i][j][1]:
					f[ii][i][j] = (l, m, r)
				print f[ii][i][j],
			print
	'''
	return f[N][K][K/2]


def main():
	# print tie([0.5, 0.5])
	# print tie([0.0, 1])
	# print tie([0.5, 0.75])
	# print tie([0.5, 1])
	# print tie([1, 0.75])
	# raise
	global t
	T = input()
	for t in range(T):
		ans = calc()
		print 'Case #%d: %s'%(t+1, ans)


if __name__ == '__main__':
	main()

import sys
import random

def compress(s):
	r=''
	for i in xrange(len(s)):
		if i == len(s)-1 or s[i] != s[i+1]:
			r+=s[i]
	return r

def solve(s):
	s = map(lambda x: 1 if x == '+' else -1, compress(s))
	if len(s)==1:
		if s[0]==1: return 0
		else: return 1
	if s[-1]==1:
		s=s[0:-1]
	return len(s)

'''def solve_stupid(s):
	minstep = 999999
	def inverse(s): return map(lambda x: -1 if x == 1 else 1, s)
	for i in xrange(1000):
		ss = map(lambda x: 1 if x == '+' else -1, s)
		steps = 0
		while True:
			if sum(ss)==len(ss):
				minstep = min(minstep, steps)
				break
			j = random.randrange(0, len(ss))
			ss[0:j+1] = list(reversed(inverse(ss[0:j+1])))
			steps = steps+1
	return minstep'''

def gen_random(n):
	s = ''
	for i in xrange(n):
		s += '+' if random.randrange(0,2)==1 else '-'
	return s

T=int(sys.stdin.readline())
for i in xrange(1,T+1):
	s = sys.stdin.readline().strip()
	print('Case #%d: %d' % (i, solve(s)))

'''while True:
	s = gen_random(6)
	print('Random test: %s' % s)
	n, m = solve(s), solve_stupid(s)
	print('%d %d' % (n,m))
	if n > m: break'''
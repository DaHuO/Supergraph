from sage.all import *

def check(x):
	proof = []
	for i in xrange(2, 11):
		xi = int(x, i)
		numy, _ = factor(xi)[0]
		if numy == xi: return None
		proof.append(numy)
	return proof

def generate(N, J):
	result = []
	i = 0
	while len(result) < N:
		cur = '1' + bin(i)[2:].rjust(J-2, '0') + '1'
		ans = check(cur)
		if ans: result.append((cur, ans))
		i += 1
	return result

raw_input()
print 'Case #1:'
J, N = map(int, raw_input().split())
for x, proof in generate(N, J):
	print x, ' '.join(map(str, proof))
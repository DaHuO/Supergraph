#! /usr/bin/python

T = int(raw_input())

def iterateOneStep(probs, p):
	probs = [0.0] + probs + [0.0]
	return [(1.0 - p)*probs[i] + p*probs[i - 1] for i in range(1, len(probs))]

for t in range(1, T+1):

	N, K = [int(inp) for inp in raw_input().split()]
	P = sorted([float(inp) for inp in raw_input().split()])

	maxP = 0.0
	for k in range(K + 1):
		distrib = [1.0]
		for i in range(k):
			distrib = iterateOneStep(distrib, P[i])
		for j in range(K - k):
			distrib = iterateOneStep(distrib, P[N - 1 - j])
		if maxP < distrib[K/2]:
			maxP = distrib[K/2]

	print 'Case #' + str(t) + ': ' + str(maxP)
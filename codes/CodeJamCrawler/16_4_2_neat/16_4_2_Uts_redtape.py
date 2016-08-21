import itertools

def tie_probability(probabilities):
	K = len(probabilities)
	total_p = 0
	yes_voters = itertools.combinations(range(K), K/2)
	for yes_voter in yes_voters:
		tie_p = 1
		for i, p in enumerate(probabilities):
			if i in yes_voter:
				tie_p *= p
			else:
				tie_p *= 1-p
		total_p += tie_p
	return total_p

def solve(K, probabilities):
	winner = 0
	combos = itertools.combinations(probabilities, K)
	for combo in combos:
		tie_prob = tie_probability(combo)
		if tie_prob > winner:
			winner = tie_prob
	return winner

T = int(raw_input())
for t in range(1, T+1):
	N, K = [int(i) for i in raw_input().split()]
	probabilities = [float(i) for i in raw_input().split()]
	print "Case #%d: %f" % (t, solve(K, probabilities))


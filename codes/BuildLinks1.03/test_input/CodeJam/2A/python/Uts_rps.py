import sys
import pdb

winners = {'P': 'PR', 'R': 'RS', 'S' : 'PS'}
orderings = ['PRS', 'PSR', 'SPR', 'SRP', 'RSP', 'RPS']

def solve(N, R, P, S):
	best = presolve(N, 'R')
	if (R, P, S) == (best.count('R'), best.count('P'), best.count('S')):
		return best
	best = presolve(N, 'P')
	if (R, P, S) == (best.count('R'), best.count('P'), best.count('S')):
		return best
	best = presolve(N, 'S')
	if (R, P, S) == (best.count('R'), best.count('P'), best.count('S')):
		return best
	return 'IMPOSSIBLE'

def bits(n):
    while n:
        b = n & (~n+1)
        yield b
        n ^= b

def presolve(N, matchup):
	if N == 0:
		return matchup
	new_matchup = ''
	for j in range(len(matchup)):
		ordering = orderings[(N-1) % 6]
		winner = winners[matchup[j]]
		if ordering.index(winner[0]) > ordering.index(winner[1]):
			winner = winner[::-1]
		new_matchup += winner
	return presolve(N-1, new_matchup)

T = int(raw_input())
for t in range(1, T+1):
	N, R, P, S = [int(i) for i in raw_input().split()]
	print "Case #%d: %s" % (t, solve(N, R, P, S))


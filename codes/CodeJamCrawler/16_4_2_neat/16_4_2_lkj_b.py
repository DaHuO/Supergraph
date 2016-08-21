from itertools import combinations

def tiep(subs):
	tieprob = 0
	for sj in combinations(range(0,len(subs)), len(subs)//2):
		p = 1
		for i in range(len(subs)):
			if i in sj:
				p *= subs[i]
			else:
				p *= (1-subs[i])
		tieprob += p
	return tieprob
	
def solve(n,k,yesp):
	maxp = 0
	maxinds = None
	for J in combinations(yesp,k):
		tieprob = tiep(J)
		if tieprob > maxp:
			maxp = tieprob
			maxinds = J
	#print('maxp for this choice:', maxinds)
	return maxp

tc = int(input())
for t in range(1,tc+1):
	n,k = [int(x) for x in input().split()]
	yesp = [float(x) for x in input().split()]
	print('Case #{}: {}'.format(t,solve(n,k,yesp)))

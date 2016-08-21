import itertools

def f(n,k,ps):
	sums = [1]
	used = [0] * n
	for i in range(k//2):
		a,b = chooseBest2(ps, used, sums, i*2)
		used[a] = 1
		used[b] = 1
		p2 = ps[a] * ps[b]
		p1 = (ps[a]*(1-ps[b]) + ps[b]*(1-ps[a]))
		p0 = (1-ps[a])*(1-ps[b])
		#print(a,b,p0,p1,p2)
		
		
		if (i == 0):
			sums = [p0,p1,p2]
			continue

		nextSums = [0] * (i*2 + 3)
		nextSums[0] = sums[0]*p0
		nextSums[1] = sums[1]*p0+sums[0]*p1

		for j in range(2,len(nextSums)-2):
			nextSums[j] = sums[j]*p0 + sums[j-1]*p1 + sums[j-2]*p2
		nextSums[-2] = sums[-2]*p2 + sums[-1]*p1
		nextSums[-1] = sums[-1]*p2
		sums = nextSums
	#print(sums)
	return sums[k//2]

def f2(n,k,ps):
	best = 0
	for c in itertools.combinations(ps, k):
		val = bruteForce(c)
		if val > best:
			best = val
	return best


def bruteForce(x):
	ans = 0
	for use in itertools.product((0,1), repeat = len(x)):
		
		if sum(use) == len(x)//2:
			p = 1
			for i in range(len(x)):
				if use[i]:
					p *= x[i]
				else:
					p *= 1-x[i]
			ans += p
	return ans


def chooseBest2(ps, used, currentDiff, numUsed):
	if numUsed == 0:
		best = 0,0
		bestVal = 0
		for i in range(len(ps)):
			for j in range(i+1, len(ps)):
				if not used[i] and not used[j]:
					val = ps[i]*(1-ps[j]) + ps[j]*(1-ps[i])
					if val > bestVal:
						best = i,j
						bestVal = val
		return best
	oneLess = currentDiff[numUsed//2]
	twoLess = currentDiff[numUsed//2 - 1]
	zeroLess = currentDiff[numUsed//2+1]
	best = 0,0
	bestVal = 0
	for i in range(len(ps)):
		for j in range(i+1, len(ps)):
			if not used[i] and not used[j]:

				val = ps[i] * ps[j] * twoLess
				val += (ps[i]*(1-ps[j]) + ps[j]*(1-ps[i])) * oneLess
				val += (1-ps[i])*(1-ps[j]) * zeroLess
				if val > bestVal:
					best = i,j
					bestVal = val
	return best




n = int(input())
for i in range(n):
	n,k = list(map(int,input().split()))
	ps = list(map(float,input().split()))
	x = f2(n,k,ps)
	y = f(n,k,ps)
	#if (x != y):
	#	print(n,k,ps,x,y)
	print("Case #{0}: {1}".format(i+1, x))
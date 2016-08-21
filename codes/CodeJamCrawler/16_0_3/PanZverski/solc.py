import math

bs = range(2, 11)
pows = [[b ** i for i in range(0, 32)] for b in bs]
sols_cnt = 0

def sol(n, need):
	sums = [(b[n - 1] + 1) for b in pows]
	path = ['1'] + ['0'] * (n - 2) + ['1']
	def get_divs():
		ans = []
		for s in sums:
			d = 2
			gr = min(16, s - 1)
#			gr = int(math.sqrt(s)) + 1
			while d <= gr and (s % d) != 0:
				d = d + 1
			if d > gr:
				return None
			ans.append(d)
		return ans

	def gen(i):
		global sols_cnt
		if sols_cnt == need:
			return
		if i == n - 1:
			divs = get_divs()
			if divs:
				print ''.join(path), ' '.join(map(str, divs))
				sols_cnt = sols_cnt + 1
		else:
			cnt = gen(i + 1)
			path[i] = '1'
			for j in range(0, len(pows)):
				sums[j] = sums[j] + pows[j][n - 1 - i];
			gen(i + 1)
			path[i] = '0'
			for j in range(0, len(pows)):
				sums[j] = sums[j] - pows[j][n - 1 - i];
	gen(1)

tests = input()
for test in range(1, tests + 1):
	n, j = map(int, raw_input().split())
	print "Case #%d:" % (test)
	sol(n, j)

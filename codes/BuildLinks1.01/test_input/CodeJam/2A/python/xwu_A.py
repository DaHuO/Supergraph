import sys
from collections import Counter


m = {
	'P': 'PR',
	'R': 'RS',
	'S': 'PS',
}
ans = {}


def dfs(i, c, n):
	if i >= n:
		return c
	else:
		c2 = m[c]
		l = dfs(i+1, c2[0], n)
		r = dfs(i+1, c2[1], n)
		return min(l+r, r+l)


def prep():
	global ans
	for n in range(1, 12+1):
		for s in 'PRS':
			init = s
			s = dfs(0, s, n)
			cc = Counter(s)
			cand = (cc['R'], cc['P'], cc['S'])
			ans[cand] = min(ans.get(cand, 'Z'), s)
			# print n, init, cand, ans[cand][:10]


def calc():
	n, r, p, s = (int(_) for _ in raw_input().split())
	return ans.get((r, p, s), 'IMPOSSIBLE')


def main():
	prep()
	T = input()
	for t in range(T):
		ans = calc()
		print 'Case #%d: %s'%(t+1, ans)


if __name__ == '__main__':
	main()

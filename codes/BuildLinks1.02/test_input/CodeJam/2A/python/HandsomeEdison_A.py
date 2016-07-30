# -*- coding: utf-8 -*-
# @Author: zeyuan.shang
# @Date:   2016-05-08 17:01:08
# @Last Modified by:   zeyuan.shang
# @Last Modified time: 2016-05-28 22:55:22
def solve(N, R, P, S):
	if R < 0 or P < 0 or S < 0:
		return ('IMPOSSIBLE', -1)

	if N == 0:
		if R > 0:
			return ('R', 0)
		elif P > 0:
			return ('P', 0)
		elif S > 0:
			return ('S', 0)

	a = (P + S - R) / 2
	b = (P + R - S) / 2
	c = (S + R - P) / 2

	P -= a
	S -= c
	R -= b

	string, result = solve(N - 1, R, P, S)
	if result == -1:
		return (string, result)
	else:
		new_string = ''
		for c in string:
			if c == 'P':
				new_string += 'PR'
			elif c == 'R':
				new_string += 'SR'
			elif c == 'S':
				new_string += 'PS'
			else:
				print 'Fuck!'

	return (new_string, result)

def resort(ans):
	n = len(ans)
	if n == 2:
		return ''.join(sorted(ans))
	else:
		left = resort(ans[:n / 2])
		right = resort(ans[n / 2:])
		lr = left + right
		rl = right + left
		if lr < rl:
			return lr
		else:
			return rl

if __name__ == "__main__":
	T = input()
	for i in xrange(1, T + 1):
		N, R, P, S = map(int, raw_input().split())
		ans, res = solve(N, R, P, S)
		if res != -1:
			ans = resort(ans)
		print 'Case #{}: {}'.format(i, ans)

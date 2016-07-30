def expand(s):
	anss = ''
	for i in s:
		if i == 'R':
			anss += 'RS'
		elif i == 'P':
			anss += 'PR'
		else:
			anss += 'PS'
	return anss

def game(s):
	if len(s) == 1:
		return s
	else:
		s1 = s[:len(s)/2]
		s2 = s[len(s)/2:]
		s1 = game(s1)
		s2 = game(s2)
		if s1<s2:
			return s1+s2
		else:
			return s2+s1
te = input()
for qe in range(1, te+1):

	n, r, p, s = map(int, raw_input().split())

	ans = []
	ss = 'S'
	for i in range(n):
		ss = expand(ss)

	if ss.count('P') == p and ss.count('S') == s and ss.count('R') == r:
		ans.append(ss)


	rr = 'R'
	for i in range(n):
		rr = expand(rr)

	if rr.count('P') == p and rr.count('S') == s and rr.count('R') == r:
		ans.append(rr)


	pp = 'P'
	for i in range(n):
		pp = expand(pp)

	if pp.count('P') == p and pp.count('S') == s and pp.count('R') == r:
		ans.append(pp)

	ans = [game(ii) for ii in ans]
	
	if len(ans) == 0:
		AAA = 'IMPOSSIBLE'
	else:
		AAA = sorted(ans)[0]

	print 'Case #{}: {}'.format(qe, AAA)
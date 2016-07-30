def f(n,r,p,s):
	p1 = expand('R', n)
	p2 = expand('P', n)
	p3 = expand('S', n)
	poss = [p1,p2,p3]
	#print(poss)
	possAns = []
	for i in poss:
		if i.count('R') == r and i.count('S') == s and i.count('P') == p:
			possAns.append(i)
	if len(possAns) == 0:
		return "IMPOSSIBLE"
	possAns.sort()
	return possAns[0]


e = dict()
e['R'] = 'RS'
e['P'] = 'PR'
e['S'] = 'PS'

d = {}
def expand(l, layers):
	if layers == 0:
		return l
	if (l,layers) in d:
		return d[(l,layers)]
	s = e[l]
	a = expand(s[0], layers - 1)
	b = expand(s[1], layers - 1)
	if (a<b):
		ans = a+b
	else:
		ans = b+a
	d[(l,layers)] = ans
	return ans




n = int(input())
for i in range(n):
	x = f(*map(int,input().split()))
	print("Case #{0}: {1}".format(i+1, x))
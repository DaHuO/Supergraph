def solve(p):
	p.reverse()
	i = 0
	ans = 0
	while i < len(p):
		a = p[i]
		if a == '-':
			j = len(p)-1
			if p[j] == '+':
				while p[j] == '+':
					j-=1
				p = reverse(p,j+1)
				ans +=1
			p = reverse(p,i)
			ans +=1
		i += 1
	return ans


def reverse(p,i):

	r = p[i:]
	r.reverse()
	a = p[0:i]
	for c in r:
		cs = '+'
		if c == '+':
			cs = '-'
		a.append(cs)
	return a


"""
a
b
-++-
+()
1 -> 5
5 s4
7 s2
(--------)
-()
-------
------+---
+--+

-... 1 + 
-++
--- 
+--+ 
+-++
+---
++++
"""

f = open("B-large.in")
T = int(f.readline())
for case in range(1,T+1):
	p = [a for a in f.readline()]
	if p[-1] == '\n':
		p = p[:-1]
	print  "Case #{0}: {1}".format(case,solve(p))







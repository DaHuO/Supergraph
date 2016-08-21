import sys

sys.stdin = open("a.in", 'r')
sys.stdout = open("a.out", 'w')

def f(n):
	d = {}
	v = 0
	while True:
		v = v + n
		s = str(v)
		for c in s:
			d[c] = True
		if len(d) == 10:
			return v
	return None


T = int(raw_input())
for t in range(1, T+1):
	n = int(raw_input())
	if n == 0:
		res = "INSOMNIA"
	else:
		res = str(f(n))
	print "Case #%d: %s" % (t, res)

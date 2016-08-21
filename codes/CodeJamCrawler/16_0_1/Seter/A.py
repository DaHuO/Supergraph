T = int(raw_input())

def solve():
	n = int(raw_input())
	l = {}
	for j in range(1, 101):
		m = str(j * n)
		for k in m:
			l[k] = True
		if len(l) == 10:
			print m
			return
	print "INSOMNIA"

for i in range(1, T + 1):
	print "Case #%d:" % i,
	solve()
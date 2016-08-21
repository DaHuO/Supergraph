import sys

def solve(n):
	ini = n
	if n == 0:
		return "INSOMNIA"
	mp = [False]*10
	while True:
		cont = False
		i = [int(x) for x in str(n)]
		for j in range(0,10):
			if not mp[j]:
				if j in i:
					mp[j] = True
				else:
					cont = True
		if not cont:
			ans = n
			break
		else:
			n = n + ini
	return n


with open('in.txt') as f:
	sys.stdout = file('out.txt', 'w')
	t = int(f.readline())
	for nT in range(1,t+1):
		n = int(f.readline())
		print "Case #%d:"%nT,solve(n)


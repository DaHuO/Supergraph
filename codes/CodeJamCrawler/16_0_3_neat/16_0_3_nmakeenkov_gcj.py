import math

n = 16
j = 50

def check(s):
	ans = []
	for base in range(2, 11):
		x = 0
		for i in s:
			x = base * x + int(i)
		ok = False
		for i in range(2, min(x, int(math.sqrt(x)) + 5)):
			if x % i == 0:
				ans.append(i)
				ok = True
				break
		if (not ok):
			return 0
	print x,
	for i in ans:
		print i, 
	print 
	return 1

def solve(s, j):
	if j == 0:
		return 0
	if (len(s) == n - 1):
		return check("1" + s)
	else:
		jj = j
		for i in ["0", "1"]:
			jj -= solve(i + s, jj)
			if jj == 0:
				break
	return (j - jj)

print "Case #1:"
solve("1", j)

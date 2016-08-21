import sys
def win(a,b):
	if a == b: return -1
	if a == 'r':
		if b == 's':
			return 0
		elif b == 'p':
			return 1
	if a == 'p':
		if b == 's':
			return 1
		elif b == 'r':
			return 0
	if a == 's':
		if b == 'p':
			return 0
		elif b == 'r':
			return 1

def test(s):
	while len(s) > 1:
		sp = ""
		for i in range(0, len(s), 2):
			ww = win(s[i], s[i+1])
			if ww == -1: return False
			sp += s[i:i+2][ww]
		s = sp
	return True

def b3(n,t):
	y = "rps"
	s = ""
	for i in range(t):
		s += y[n%3]
		n /= 3
	return s


def solve(r,p,s):
	f = "z"
	t = r+p+s
	for i in range(3**t):
		q = b3(i,t)

		if q.count("r") == r and q.count("p") == p and q.count("s") == s:
			if test(q) and q < f:
				f = q
	if f == "z": return "IMPOSSIBLE"
	return f
	

CASES = int(raw_input())

case = 1
for i in range(CASES):
	n,r,p,s = [int(i) for i in raw_input().split()]
	print "Case #" + str(case) + ": " + solve(r,p,s).upper()
	case += 1

def maketree(x, n):
	if n == 0: return x
	if x == 'P': a,b = maketree('P',n-1),maketree('R',n-1)
	if x == 'R': a,b = maketree('R',n-1),maketree('S',n-1)
	if x == 'S': a,b = maketree('P',n-1),maketree('S',n-1)
	if a < b: return a + b
	else: return b + a

def solve(n,r,p,s):
	if r == s:
		if (n % 2 == 1):
			if p != r-1:
				return "IMPOSSIBLE"
		if (n % 2 == 0):
			if p != r+1:
				return "IMPOSSIBLE"
		tmp = 2
	elif s == p:
		if (n % 2 == 1):
			if r != s-1:
				return "IMPOSSIBLE"
		if (n % 2 == 0):
			if r != s+1:
				return "IMPOSSIBLE"
		tmp = 0
	elif p == r:
		if (n % 2 == 1):
			if s != p-1:
				return "IMPOSSIBLE"
		if (n % 2 == 0):
			if s != p+1:
				return "IMPOSSIBLE"
		tmp = 1
	else:
		return "IMPOSSIBLE"
	
	winners = ["R","S","P"]
	winner = winners[ (tmp + n)%3 ]
		
	return maketree(winner, n)

f = open('A-large.in','r')
out = open('out.txt','w')

cases = int(f.readline())

for case in range(1,cases+1):
	n,r,p,s = [int(x) for x in f.readline().split()]
	res = solve(n,r,p,s)
	output = 'Case #{0}: '.format(case) + " " + res + "\n"
	print(output)
	out.write(output)

out.close()	
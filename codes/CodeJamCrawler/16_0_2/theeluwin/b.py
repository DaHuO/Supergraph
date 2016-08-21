infile = open('b.in')
outfile = open('b.out', 'w')
indata = infile.read().split('\n')
T = int(indata[0])

def solve(s):
	s = s[::-1]
	if len(s):
		r = 0
		c = s[0]
		if c == '-':
			r += 1
		for i in range(1, len(s)):
			if s[i] != c:
				r += 1
			c = s[i]
		return r
	else:
		return 0

def main():
	for t in range(1, T + 1):
		r = solve(indata[t])
		outfile.write("Case #{}: {}\n".format(t, r))

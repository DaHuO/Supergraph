from itertools import groupby

def normalize(s):
	return ''.join([c for c, it in groupby(s)])

def negate(c):
	if c == "+":
		return "-"
	return "+"

def solve(s):
	if s == "+":
		return 0	

	counter = 0
	while len(s) > 1:
		s = normalize(negate(s[0]) + s[1:])
		counter += 1

	if s == "-":
		counter += 1
	
	return counter

if __name__ == "__main__":
	t = int(input())
	for cc in range(t):
		print("Case #{}: {}".format(cc+1, solve(normalize(input()))))

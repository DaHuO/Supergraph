n = int(input())

def answer(s):
	s += "+"
	return sum(int(c1 != c2) for (c1, c2) in zip(s[:-1], s[1:]))

for i in range(n):
	print(("Case #%d: " % (i+1)) + str(answer(input())))
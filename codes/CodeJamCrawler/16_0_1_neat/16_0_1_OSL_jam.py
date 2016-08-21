def solve(n):
	dig = [0] * 10
	c = 0
	
	if n == 0:
		return "INSOMNIA"

	for i in range(1, 1000):
		s = str(n * i)
		for t in s:
			if dig[int(t)] == 0:
				dig[int(t)] += 1
				c += 1
		if c == 10:
			return(i * n)


f = open("intput.txt", "r")

t = int(f.readline())

for i in range(t):
	n = int(f.readline())
	print("Case #" + str(i+1) + ": " + str(solve(n)));
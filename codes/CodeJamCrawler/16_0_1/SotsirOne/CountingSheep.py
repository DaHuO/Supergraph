def solve(n):
	cycle = set()
	digits = set()
	multiplier = 0
	while True:
		multiplier += 1
		x = n * multiplier
		if x in cycle:
			return "INSOMNIA"
		else:
			cycle.add(x)
		for c in str(x):
			digits.add(c)

		if len(digits) >= 10:
			return x
		
		#print("cycle: {}, digits: {}".format(cycle, digits))
		#print("n: {}, multiplier: {}".format(n, multiplier))


t = int(input().strip())
for x in range(t):
	n = int(input().strip()) 
	print ("Case #{0}: {1}".format(x+1, solve(n)))

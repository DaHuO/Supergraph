from sys import stdin
cin = lambda: [int(n) for n in stdin.readline().strip('\n\r ').split(' ')]

t = cin()[0]
for i in range(t):
	n = cin()[0]
	count = [0] * 2501
	leftovers = []
	
	data = [cin() for j in range(n * 2 - 1)]
	
	for row in data:
		for num in row:
			count[num] += 1
	
	for j in range(2500):
		if count[j] % 2 != 0:
			leftovers.append(j)
	
	leftovers.sort()
	
	print "Case #%i:" % (i + 1), " ".join([str(n) for n in leftovers])
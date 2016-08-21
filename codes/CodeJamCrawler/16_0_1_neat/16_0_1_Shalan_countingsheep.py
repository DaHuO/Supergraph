def readFile(name):
	with open(name) as file:
		for line in file:
			yield int(line)

def solve():
	lines = iter(readFile('countingsheep.in'))
	numCases = next(lines)
	for i in range(1,numCases+1):
		digitsSeen = set([])
		start = next(lines)
		if start == 0:
			print("Case #" + str(i) + ": INSOMNIA")
		else:
			n = start
			while True:
				m = n
				while m > 0:
					digitsSeen.add(m%10)
					m = m//10
				if (len(digitsSeen) == 10):
					print("Case #" + str(i) + ": " + str(n))
					break
				n += start

solve()
			


		
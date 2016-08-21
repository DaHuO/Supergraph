import math
import random


def solve(j, p, s, k):

	results = []
	jpmap = [[0 for x in range(10)] for x in range(10)]
	psmap = [[0 for x in range(10)] for x in range(10)]
	jsmap = [[0 for x in range(10)] for x in range(10)]
	for jind in range(j):
		prange = range(p)[(jind+1) % p:]
		prange.extend(range(p)[:(jind+1) % p])
		for pind in prange:
			srange = range(s)[(jind+pind+1) % s:]
			srange.extend(range(s)[:(jind+pind+1) % s])
			for sind in srange:
				if jpmap[jind][pind] < k and psmap[pind][sind] < k and jsmap[jind][sind] < k:
					results.append(str(jind+1) + " " + str(pind+1) + " " + str(sind+1))
					jpmap[jind][pind] += 1
					psmap[pind][sind] += 1
					jsmap[jind][sind] += 1

	return results


name = "C-large"#"C-small-attempt1"
fi = open(name + ".in", "r")

fout = open(name + ".out", "w")

numTestCases = int(fi.readline())
print "#TestCases: ", numTestCases

for i in range(0, numTestCases):
	line = fi.readline().strip().split(" ")
	line = map(int, line)
	j = line[0]
	p = line[1]
	s = line[2]
	k = line[3]

	result = solve(j, p, s, k)
	fout.write("Case #" + str(i + 1) + ": " + str(len(result)) + "\n")
	for row in result:
		fout.write(row + "\n")
	print "Case #" + str(i + 1) + ": " + str(len(result))
	for row in result:
		print row

fi.close()
fout.close()
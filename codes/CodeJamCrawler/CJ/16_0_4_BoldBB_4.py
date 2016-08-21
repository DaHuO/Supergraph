import itertools
import random

def isG(base, position, depth):
	for i in range(1, depth+1):
		if "1" == base[(position % (len(base) ** (depth-i+1))) // (len(base) ** (depth - i))]:
			return True
	return False


def getCollumnCounts(K, positions, C):
	total = 0
	i = 0
	while i < 2**K:
		base = "{0:b}".format(i)
		base = (K - len(base)) * "0" + base
		if sum(int(isG(base, pos, C)) for pos in positions) > 0:
			total += 1
		i += 1
	return total

with open("input4_1.txt", "r") as f:
	for linenr, line in enumerate(f.read().split("\n")[1:]):
		# S == # tiles you can clean
		# C == combination depth
		# K == tile pattern width
		K,C,S = [int(i) for i in line.split(" ")]
		stopat = (2**K) - 1

		if S > 1:
			print "Case #{}:".format(str(linenr+1)),
			colls = [(K**C) - i*((K**(C-1))) - 1 for i in range(S)]
			print " ".join(str(c+1) for c in colls)
			#if K < 15:
			#	print stopat, "colltotal", getCollumnCounts(K, colls, C)
			#if K < 8:
			#	print 2**K, "col c:", getCollumnCounts(K, ((2**K) - 1, (2**K) - (2**(K-1)) - 1), C)
		else:
			found = False
			for i in range(1, S+1):
				j = 0
				while j < 10**3:
					subset = [int(random.random() * K**C) for _ in range(i)]
					if getCollumnCounts(K, subset, C) >= stopat:
						print "Case #{}:".format(linenr+1),
						for col in subset:
							print col + 1,
						print ""
						found = True
						break
					j += 1
				if found:
					break
			else:
				print "Case #{}: IMPOSSIBLE".format(str(linenr+1))
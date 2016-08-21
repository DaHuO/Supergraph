#!/usr/bin/python3
import sys

def solver(file):

	def solve(n):
		if (n == 0): return "Case #{:d}: INSOMNIA\n".format(c)
		res = set()
		k = 1
		while (len(res) != 10):
			res = res.union(set(str(k * n)))
			k += 1
		return "Case #{:d}: {:d}\n".format(c, (k - 1) * n)
	with open(file, 'r') as f:
		f.readline()
		c = 1
		with open("out.txt", 'w') as w:
			for line in f:
				w.write(solve(int(line.split()[0])))
				c += 1

if __name__ == "__main__":
	if (len(sys.argv) == 2): solver(sys.argv[1])
	else: raise IndexError("Not enough arguments.")

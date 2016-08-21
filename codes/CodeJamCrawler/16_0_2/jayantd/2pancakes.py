#!/usr/bin/env python

def is_complete(N, digmap):
	dlist = [int(x) for x in list(str(N))]

	for d in dlist:
		if not digmap[d]:
			digmap[d] = 1

	for d in digmap:
		if d == 0:
			return False

	return True

def main():

	filename = "B-large.in"
	f = open(filename, 'r')
	o = open(filename + "_out", 'w')

	T = int(f.readline())

	for t in range(T):
		S = f.readline().split("\n")[0]
		o.write("Case #" + str(t + 1) + ": ")

		minuses = 0
		pluses = 0
		flips = 0
		for i, s in enumerate(S):
			if minuses and s == '+':
				# Do a flip of all prev -es here
				flips += 1
				minuses = 0
				pluses = 1
			elif s == '+':
				pluses += 1
			elif pluses and s == '-':
				# Do a flip of all prev +es here
				flips += 1
				pluses = 0
				minuses = 1
			elif s == '-':
				minuses += 1

		if s == '-':
			flips += 1

		o.write(str(flips) + "\n")

if __name__ == "__main__":
	main()

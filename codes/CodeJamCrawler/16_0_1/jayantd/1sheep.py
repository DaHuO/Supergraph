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

	filename = "A-large.in"
	f = open(filename, 'r')
	o = open(filename + "_out", 'w')

	T = int(f.readline())

	for t in range(T):
		N = int(f.readline())
		o.write("Case #" + str(t + 1) + ": ")

		if N == 0:
			o.write("INSOMNIA\n")
			continue

		n = N
		digmap = [0,0,0,0,0,0,0,0,0,0]
		while True:
			if is_complete(n, digmap):
				o.write(str(n) + "\n")
				break
			n += N

if __name__ == "__main__":
	main()

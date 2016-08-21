#!/usr/bin/env python
__author__ = "Thomas Kargul"

def countSheep():
	numOfInput = int(raw_input()) # 1 <= T <= 100
	inputN = [] #list of ints
	for i in range(numOfInput):
		inp = int(raw_input()) #small: 0 <= n <= 200, large: ..<= 10^6
		inputN.append(inp)

	for it, N in enumerate(inputN):
		if N == 0:
			print("Case #{}: INSOMNIA".format(it+1))

		else:
			seen = []
			for d in str(N):
				if d not in seen:
					seen.append(d)

			i = 0
			last = 0
			while(len(seen) < 10):
				nextN = (i+1) * N
				last = nextN
				i += 1
				for d in str(nextN):
					if d not in seen:
						seen.append(d)

			print("Case #{}: {}".format(it+1, last))

if __name__ == '__main__':
	countSheep()
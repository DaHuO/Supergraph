#!/usr/bin/env python



def main():


	names = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
	unique1 = {'Z' : 0, 'W' : 2, 'U' : 4, 'X' : 6, 'G' : 8}
	unique2 = {'O' : 1, 'S' : 7, 'T' : 3}
	unique3 = {'N' : 9, 'V' : 5}
	occur = {}

	filename = "A-large.in"
	f = open(filename, 'r')
	o = open(filename + "_out", 'w')

	T = int(f.readline())

	for t in range(T):
		S = f.readline()[:-1]
		o.write("Case #" + str(t + 1) + ": ")

		for c in S:
			if c in occur:
				occur[c] += 1
			else:
				occur[c] = 1
		
		number = []
		for u in unique1:
			if u not in occur:
				continue
			while occur[u]:
				n = unique1[u]
				for c in names[n]:
					occur[c] -= 1
				number.append(n)

		for u in unique2:
			if u not in occur:
				continue
			while occur[u]:
				n = unique2[u]
				for c in names[n]:
					occur[c] -= 1
				number.append(n)

		for u in unique3:
			if u not in occur:
				continue
			while occur[u]:
				n = unique3[u]
				for c in names[n]:
					occur[c] -= 1
				number.append(n)


		o.write(''.join([str(x) for x in sorted(number)]) + "\n")


if __name__ == "__main__":
	main()

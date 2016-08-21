#!/usr/bin/env python

def main():
	testcase_nb = long(raw_input().strip())
	i = 1

	with open('counting_sheep.out', 'w') as outfile:
		while i <= testcase_nb:
			N = raw_input().strip()
			number_count = {str(c): False for c in range(0,10)}
			factor = 1

			if N == "0":
				outfile.write("Case #%d: %s\n" % (i, "INSOMNIA"))
				i += 1
				continue
			while not all(number_count.itervalues()):
				for c in str(long(N)*factor):
					number_count[c] = True
				factor += 1
			outfile.write("Case #%d: %s\n" % (i, str(long(N)*(factor-1))))
			i += 1

if __name__ == '__main__':
	main()

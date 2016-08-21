#!usr/bin/python2
import sys


def main():
	output = "Case #{}: {}"
	cases = int(raw_input())
	for case, line in enumerate(sys.stdin):
		n = int(line)
		if n == 0:
			print output.format(case + 1,  "INSOMNIA")
		else:
			found = set()
			iterations = 0
			while len(found) < 10:
				iterations += 1
				found |= set(str(n * iterations))
			print output.format(case + 1, iterations * n)

if __name__ == "__main__":
	main()

#!usr/bin/python2
import sys

def main():
	output = "Case #{}: {}"
	cases = int(raw_input())
	for case, line in enumerate(sys.stdin):
		changes = 0
		current = line[0]
		line = line.strip()
		if len(line) > 1:
			for c in line[1:]:
				if current != c:
					changes += 1
					current = c
		if line[-1] != "+":
			changes += 1
		print output.format(case + 1, changes)
		
if __name__ == "__main__":
	main()

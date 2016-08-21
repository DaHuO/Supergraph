#!/usr/bin/python
import sys

def pancake_revenge(cakes):
	times = 0
	for i in range(0, len(cakes)):
		#print(cakes)
		j = len(cakes) - i - 1
		if cakes[j] == '-':
			times += 1
			for t in range(0, j):
				if cakes[t] == '+':
					cakes[t] = '-'
				else:
					cakes[t] = '+'

	return times

if __name__ == '__main__':
	with open(sys.argv[1]) as f:
		content = f.read().split()
		for i in range(1, len(content)):
			res = pancake_revenge(list(content[i]))
			print 'Case #' + str(i) + ': ' + str(res)



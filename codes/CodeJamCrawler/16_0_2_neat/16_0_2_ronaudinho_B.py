import sys

fileout = sys.stdout
cases = int(raw_input())

for case in range (0, cases):
	data = raw_input()
	pancakes = []
	for x in data:
		pancakes.append(x)
	flip = 0
	
	while pancakes.count('+') < len(pancakes):
		i = 0
		while i < len(pancakes):
			if pancakes[0] == '+':
				if pancakes[i] == '-':
					break
			else:
				if pancakes[i] == '+':
					break
			i += 1
		for j in range (0, i):
			if pancakes[j] == '+':
				pancakes[j] = '-'
			else:
				pancakes[j] = '+'
		flip += 1
			
	print ("Case #{}: {}".format(case + 1, flip))
from __future__ import division

def turn(pcakes, i):
	for c in range(0, i):
		if pcakes[c] == '+':
			pcakes[c] = '-'
		else:
			pcakes[c] = '+'

def flip(pcakes):
	print pcakes
	result = 0
	if '+' not in pcakes:
		turn(pcakes, len(pcakes)) 
		return 1
	elif '-' in pcakes:
		for i in range(len(pcakes)):
			if pcakes[i] != pcakes[0]:
				break			
		turn(pcakes, i)
		result = 1 + flip(pcakes)
		return result
	else: 
		return 0

f = open("B-large.in", 'r')
g = open("output.out", 'w')
cases = int(f.readline())
i = 0

for i in range(cases):
	result = 0
	pcakes = list(f.readline())
	result = flip(pcakes)
	print result

	g.write("Case #" + str(i + 1) + ": " + str(result) +  "\n")

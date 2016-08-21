input_file = open("B-large.in", 'r')
from time import sleep

wasted = input_file.readline()

for ix, pancakes in enumerate(input_file):
	print "Case #" + str(ix + 1) + ": ",
	pancakes = pancakes.strip() + '+'

	flips = 0
	for i in range(len(pancakes) - 1):
		if pancakes[i] != pancakes[i + 1]:
			flips += 1

	print str(flips)





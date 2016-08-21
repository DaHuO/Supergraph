from string import *
import math
import numpy

def read_words(filename):
    '''
    converts a file to a list
    '''
    words = []
    for line in filename:
            words.append(line.strip())
    return words

filename = open("in3.txt", 'r')
numcases = int(filename.readline().split()[0])

for case in range(numcases):
	things = filename.readline().split()
	k = int(things[0])
	c = int(things[1])
	s = int(things[2])

	if s < k:
		pass
		#CAN'T HANDLE THIS... YET!

	num_tiles = k**c
	last_it = k**(c-1)

	investigate_tiles = []
	cur_i = 1
	while cur_i <= num_tiles:
		investigate_tiles.append(cur_i)
		cur_i += last_it

	print "Case #" + str(case+1) + ":",
	for tile in investigate_tiles:
		print tile,
	print 

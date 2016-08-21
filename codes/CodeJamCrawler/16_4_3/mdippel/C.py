#! /usr/bin/env python

import sys, getopt
from collections import defaultdict as dd

#######################
## I/O functions begin
def processInput():
	# yields test cases
	T = int(raw_input())
	for i in range(T):
		R, C = map(int, raw_input().split())
		pairs = map(int, raw_input().split())
		yield (R, C, pairs)
	return


def writeOutput(results):
	for result in results:
		print result
	return
## I/O functions begin
#######################

next_dir = {}
next_dir[('/', 'E')] = 'N'
next_dir[('/', 'S')] = 'W'
next_dir[('/', 'N')] = 'E'
next_dir[('/', 'W')] = 'S'

next_dir[('\\', 'E')] = 'S'
next_dir[('\\', 'N')] = 'W'
next_dir[('\\', 'S')] = 'E'
next_dir[('\\', 'W')] = 'N'

def next_direction(assignments, entered, came_from):
	#print entered
	wall = assignments[entered]
	#print wall
	return next_dir[(wall, came_from)]

def next_square(assignments, entered, came_from):
	d = next_direction(assignments, entered, came_from)
	x, y = entered
	if d == "N":
		return (x-1, y), d
	elif d == "S":
		return (x + 1, y), d
	elif d == "W":
		return (x, y-1), d
	elif d == "E":
		return (x, y+1), d
	raise ValueError

def bin_string_to_dict(S, R, C):
	assert len(S) == R*C
	x = 0
	placement = {}
	for i in range(1, R + 1):
		for j in range(1, C + 1):
			symb = int(S[x])*'/' + (1 - int(S[x]))*'\\'
			placement[(i,j)] = symb
			x += 1
	curr_court = 1
	court_locations = {}
	for i in range(1, C+1):
		placement[(0, i)] = curr_court
		court_locations[curr_court] = (0,i)
		curr_court += 1

	for j in range(1, R+1):
		placement[(j, C+1)] = curr_court
		court_locations[curr_court] = (j,C+1)
		curr_court += 1

	for i in range(C, 0, -1):
		placement[(R+1, i)] = curr_court
		court_locations[curr_court] = (R+1,i)
		curr_court += 1

	for j in range(R, 0, -1):
		placement[(j, 0)] = curr_court
		court_locations[curr_court] = (j, 0)
		curr_court += 1

	return placement, court_locations

def placement_to_str(placement, R, C):
	s = ""
	def row_to_str(r):
		return "".join([placement[r, i] for i in range(1, C+1)])
	s = "\n" + "\n".join([row_to_str(r) for r in range(1, R+1)])
	if s[-1] == '\n':
		return s[:-1]
	return s

flip = {}
flip['N'] = 'S'
flip['E'] = 'W'
flip['S'] = 'N'
flip['W'] = 'E'

def partner(placement, R, C, court_locations, i):
	start = court_locations[i]
	r, c = start
	if start[0] == 0:
		start_dir = 'S'
		r = r + 1
	elif start[0] == R+1:
		start_dir = 'N'
		r = r - 1
	elif start[1] == 0:
		start_dir = 'E'
		c = c + 1
	elif start[1] == C+1:
		start_dir = 'W'
		c = c - 1
	else:
		raise ValueError

	next_sq, next_d = next_square(placement, (r, c), start_dir)
	count = 0
	while placement[next_sq] in ['/', '\\']:
		#print next_sq

		next_sq, next_d = next_square(placement, next_sq, next_d)
		#print placement[next_sq], next_d
		#print next_sq, next_d
		#next_d = flip[next_d]
#	print "we are ret " + str(placement[next_sq])
	return placement[next_sq]


def ALGORITHM(test_case):
	R, C, pairs = test_case
	#print pairs
	for i in range(0, 2**(R*C)):
		#print i
		bin_str = bin(i)[2:].zfill(R*C)
		placement, court_loc = bin_string_to_dict(bin_str, R , C)
		#print placement_to_str(placement, R, C)
		works = True
		for i in range(len(pairs) / 2):
			if not works:
				break
			a, b = pairs[2*i], pairs[2*i + 1]
			c = partner(placement, R, C, court_loc, a)
			#print (a,b)
			#print (a,c)
			#print a, c
			if c != b:
				works = False
				continue
			else:
				assert partner(placement, R, C, court_loc, b) == a
		if works:
			return placement_to_str(placement, R, C)
			return
	return "\n" + "IMPOSSIBLE"
	
def basic_test():
	pass

def runAlgorithm():
	results = []
	i = 1
	for test_case in processInput():
		results.append(ALGORITHM(test_case))
		#print i
		#i = i + 1

	for i in range(len(results)):
		results[i] = "Case #" + str(i+1) + ": " + results[i] + "\n"

	writeOutput(results)

if __name__ == "__main__":
	basic_test()
	runAlgorithm()

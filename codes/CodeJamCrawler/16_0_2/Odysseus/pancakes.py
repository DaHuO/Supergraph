#!/usr/bin/python

import sys
import fileinput

#the minimum number of maneuvers is equal to the number of alternate pancake sides
#+ 1 if the bottom pancake has a blank side up

def compute_flips(pancake_pile):
	current_side = pancake_pile[0]
	alternate_sides=0
	for i in pancake_pile:
		if not (current_side == i):
			alternate_sides = alternate_sides+1
			current_side = i
	if current_side=='-':
		return alternate_sides+1
	else:
		return alternate_sides

line_cnt=0
test_cases=1

for line in fileinput.input():
	if(line_cnt > (test_cases)):
		#print 'error'
		break;
	if(line_cnt == 0):
		test_cases=int(line);
	else:
		pancake_pile=line.rstrip()
		flips = compute_flips(pancake_pile)
		print('Case #'+str(line_cnt)+': '+ str(flips))
	line_cnt+=1;

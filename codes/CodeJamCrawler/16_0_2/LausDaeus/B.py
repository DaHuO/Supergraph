import os
import sys
current = os.getcwd()
outer = os.path.dirname(os.getcwd())
sys.path.append(current)
sys.path.append(outer)

from utils.io import *

def main():
	start = time_in_ms()
	info = parse_data()
	raw_tests = info[0]
	output_file = info[1]
	results = []

	for r_test in raw_tests:
		test = r_test[0]
		#test.append([int(g) for g in r_test[1]])
		results.append(solve(test))
		#print ""

	data_output(results, output_file)
	print "Time taken:",str(time_in_ms() - start)+"ms"

def solve(test):
	flips = 0
	pancakes = list(test)[::-1]

	for idx, p in enumerate(pancakes):
		if p == '-':
			flip(pancakes, idx)
			flips += 1

	#print ''.join(pancakes)
	return flips

def flip(pan, start):
	for i in xrange(start, len(pan)):
		if pan[i] == '-':
			pan[i] = '+'
		elif pan[i] == '+':
			pan[i] = '-'

if __name__ == '__main__':
	main()
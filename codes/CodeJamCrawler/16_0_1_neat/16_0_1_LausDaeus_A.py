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
		test = int(r_test[0])
		#test.append([int(g) for g in r_test[1]])
		results.append(solve(test))

	data_output(results, output_file)
	print "Time taken:",str(time_in_ms() - start)+"ms"

def solve(test):
	digits = [False] * 10
	if test == 0:
		return "INSOMNIA"

	counter = 1
	amount = ""
	while False in digits:
		amount = str(test*counter)
		counter += 1
		for d in amount:
			digits[int(d)] = True

	return amount

if __name__ == '__main__':
	main()
#!/usr/bin/env python3.2
#coding=UTF-8

'''

Google Code Jam 2016
Round qualification
Problem a
Counting Sheep

Instructions:
	chmod u+x process.py
	./process.py <input_file >output_file
	# stderr output is intended to display on a console

Notes:
	* simplest approach will be to follow Bleatrix's procedure and just check off the digits, won't it?
	* are we guaranteed to finish in a fixed number (eg. 10) of steps?
		* if so, the INSOMNIA requirement is a red herring
		* if not, then we must do more clever analysis in order to detect INSOMNIA without actually performing the steps
	* 0 won't generate any digits other than 0
		* 0 could be considered a special case
	* 2 will generate all digits, as 10 is a multiple of 2
	* any power of 10 will generate all digits in 10 steps
	* any factor of a power of 10 will generate all digits eventually
		0 INSOMNIA
		1 2 3 4 5 6 7 8 9 10
		2 4 6 8 10 12 14 16 ... 30 ... 50 ... 70 ... 90
		3 6 9 12 15 18 21 24 27 30
		4 8 12 16 20 24 28 32
	* I'm going to take a guess that 0 is the only possible input that produces INSOMNIA


'''

################################################################################


def read_case(id, input):
	N = int(input.readline())
	return N

def solution(case):
	N = case
	if N == 0: return 'INSOMNIA'
	target = set('0123456789')
	seen = set()
	value = N
	while True:
		seen.update(str(value))
		if seen == target: return value
		value = value + N

def solve_case(id, case):
	return "Case #{}: {}\n".format(id, solution(case))


def prepare():
	def prepare_data():
		return None
	
	global prepared_data
	prepared_data = prepare_cached(prepare_data, 'prepared_data.cached')


################################################################################


from sys import stdin, stdout, stderr
import time
import math
import pickle
import io

execution_timer = time.time
#execution_timer = time.clock
debugging = 1


################################################################################


def debug(message):
	if debugging:
		stderr.write(message() if hasattr(message, '__call__') else message)

def report(message):
	stderr.write(message)

def prepare_cached(prepare_data, pickle_path='data.pickle'):
	try:
		data = pickle.load(io.open(pickle_path, 'rb'))
		report("Loaded {}.\n".format(pickle_path))
	except IOError:
		data = prepare_data()
		report("Prepared {}.\n".format(pickle_path))
		pickle.dump(data, io.open(pickle_path, 'wb'))
	return data

def main():
	t0 = execution_timer()
	#prepare()
	t1 = execution_timer()
	report("Completed preparation in {:.6f} seconds.\n".format(t1 - t0))
	
	T = int(stdin.readline())
	for case_id in range(1,T+1):
		report("Processing test case {} of {} (output {}). {:.0f} seconds elapsed.".format(case_id, T, case_id-1, execution_timer() - t1))
		report("\n" if debugging else "\r")
		stderr.flush()
		stdout.write(solve_case(case_id, read_case(case_id, stdin)))
		stdout.flush()
	
	t2 = execution_timer()
	report("Processed {} test cases in {:.6f} seconds.                           \n".format(T, t2 - t1))
	report("Total time: {:.6f} seconds.\n".format(t2 - t0))

if __name__ == '__main__':
	main()


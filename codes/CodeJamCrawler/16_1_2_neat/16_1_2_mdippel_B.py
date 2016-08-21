#! /usr/bin/env python

import sys, getopt
from collections import defaultdict as dd

#######################
## I/O functions begin
def processInput():
	# yields test cases
	T = int(raw_input())
	for i in range(T):
		N = int(raw_input())
		lists = []
		for _ in range(2*N - 1):
			curr_list = map(int, raw_input().split())
			assert len(curr_list) == N
			lists.append(curr_list)
		yield N, lists
	return


def writeOutput(results):
	for result in results:
		print result
	return
## I/O functions begin
#######################

def brute_force(types, N, rows, cols, lists):
	if len(lists) == 0:
		missing = (None, None)
		for i in range(N):
			if rows[i] == None:
				missing = ("R", i)
				continue
			for j in range(N):
				if cols[j] == None:
					missing = ("C", j)
					continue
				if rows[i][j] != cols[j][i]:
					return None
		if missing[0] == "R":
			row = map(lambda l: l[missing[1]], cols)
			return row
		else:
			col = map(lambda l: l[missing[1]], rows)
			return col
	else:
		l = lists[0]
		for i in range(N):
			if cols[types][i] == l[types] and rows[i] is None:
				rows[i] = l
				fin = brute_force(types, N, rows, cols, lists[1:])
				if fin is not None:
					return fin
				rows[i] = None
			if rows[types][i] == l[types] and cols[i] is None:
				cols[i] = l
				fin = brute_force(types, N, rows, cols, lists[1:])
				if fin is not None:
					return fin
				cols[i] = None
	#print len(lists)
	return None



def ALGORITHM(test_case):
	N, lists = test_case
	#print lists
	abs_min = min(map(min, lists))
	firsts = filter(lambda l: l[0] == abs_min, lists)
	abs_max = max(map(max, lists))
	lasts = filter(lambda l: l[-1] == abs_max, lists)
	if len(firsts) == 2:
		rows = [None] * N
		cols = [None] * N
		rows[0] = firsts[0]
		cols[0] = firsts[1]
		remaining = filter(lambda l: l not in firsts, lists)
		assert len(remaining) == len(lists) - 2
		fin = brute_force(0, N, rows, cols, remaining)
		return " ".join(map(str, fin))

	else:
		rows = [None] * N
		cols = [None] * N
		rows[-1] = lasts[0]
		cols[-1] = lasts[1]
		remaining = filter(lambda l: l not in lasts, lists)
		fin = brute_force(N-1, N, rows, cols, remaining)
		return " ".join(map(str, fin))






	
def basic_test():
	N = 7
	lists = [[23, 25, 27, 29, 30, 33, 34],
[22, 24, 26, 28, 31, 32, 34],
[1, 2, 3, 4, 5, 6, 22],
[5, 10, 14, 17, 19, 20, 30],
[6, 11, 15, 18, 20, 21, 33],
[2, 7, 8, 9, 10, 11, 25],
[2, 7, 8, 9, 10, 11, 24],
[6, 11, 15, 18, 20, 21, 32],
[4, 9, 13, 16, 17, 18, 28],
[3, 8, 12, 13, 14, 15, 27],
[1, 2, 3, 4, 5, 6, 23],
[5, 10, 14, 17, 19, 20, 31],
[4, 9, 13, 16, 17, 18, 29]]
	#print ALGORITHM((N, lists))

def runAlgorithm():
	results = []
	for test_case in processInput():
		results.append(ALGORITHM(test_case))

	for i in range(len(results)):
		results[i] = "Case #" + str(i+1) + ": " + results[i] + "\n"

	writeOutput(results)

if __name__ == "__main__":
	basic_test()
	runAlgorithm()

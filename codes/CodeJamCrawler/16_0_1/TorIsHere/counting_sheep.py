#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solve(cipher):
	LIMIT = 100
	SUM   = 45 # 0 + 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9
	counting = [True] * 10
	for n in xrange(1, LIMIT + 1):
		num_str = str(int(n) * int(cipher))
		for digit in num_str:
			if counting[int(digit)]:
				counting[int(digit)] = False
				SUM = SUM - int(digit)
				if SUM == 0 and not counting[0]:
					return num_str
	return "INSOMNIA"

if __name__ == "__main__":
	testcases = input()
	 
	for caseNr in xrange(1, testcases+1):
		cipher = raw_input()
		print("Case #%i: %s" % (caseNr, solve(cipher)))

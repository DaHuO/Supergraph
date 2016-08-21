#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solve(case):
	c = case[0]
	if c == '+':
		moves = 0
		prev = "+"
	else:
		moves = 1
		prev = "-"
	for i in xrange(1, len(case)):
		if prev == "+" and case[i] == "-":
			moves = moves + 2
		prev = case[i]
	return moves


if __name__ == "__main__":
	testcases = input()
	 
	for caseNr in xrange(1, testcases+1):
		case = raw_input()
		print("Case #%i: %s" % (caseNr, solve(case)))
#!/usr/bin/env python
# -*- coding: utf-8 -*-



def solve(case):
	seen = {}
	st = 0
	i = 1
	case = int(case)
	if case == 0:
		return "INSOMNIA"
	while True:
		b = i*case
		for e in str(b):
			if e not in seen:
				seen[e] = 1
				st = st + int(e)
		if st >= 45 and '0' in seen:
			return b
		i = i+1


if __name__ == "__main__":
	testcases = input()
	 
	for caseNr in xrange(1, testcases+1):
		case = raw_input()
		print("Case #%i: %s" % (caseNr, solve(case)))

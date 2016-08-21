

#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solve(s):
	l = len(s)
	d = 0
	t = s[0]
	for i in range(1, l):
		if t != s[i]:
			d = d + 1
			t = s[i]
	if s[-1] == '+':
		return d
	else:
		return d+1

if __name__ == "__main__":
	testcases = input()

	for caseNr in xrange(1, testcases+1):
		cipher = raw_input()
		print("Case #%i: %s" % (caseNr, solve(cipher)))

#!/usr/bin/env python
# -*- coding: utf-8 -*-


def solve(cipher):
	K, C, S = map(int, cipher.split(" "))
	return " ".join([str(i*(K**(C-1)) + 1) for i in range(0, S)])

if __name__ == "__main__":
	testcases = int(input().strip())
	 
	for caseNr in iter(range(1, testcases+1)):
		cipher = input()
		print("Case #%i: %s" % (caseNr, solve(cipher)))

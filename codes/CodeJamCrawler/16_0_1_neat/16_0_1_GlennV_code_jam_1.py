#!/usr/bin/env python
# -*- coding: utf-8 -*-


def solve(cipher):
	if cipher == "0":
		return "INSOMNIA"

	found_hash = [i for i in range(0,10)]

	N = int(cipher)

	i = 1
	while True:
		n = i*N
		for char in str(n):
			if int(char) in found_hash:
				found_hash.remove(int(char))

		if not len(found_hash):
			break

		i += 1

	return n

if __name__ == "__main__":
	testcases = int(input().strip())
	 
	for caseNr in iter(range(1, testcases+1)):
		cipher = input()
		print("Case #%i: %s" % (caseNr, solve(cipher)))

#!/usr/bin/env python
# -*- coding: utf-8 -*-


def solve(cipher):
	lista = range(10)
	i=1
	while len(lista)!=0 and i<1000000:
		n=i*cipher
		for number in str(n):
			if int(number) in lista:
				lista.remove(int(number))
		i=i+1
	return n if len(lista)==0 else "INSOMNIA"

if __name__ == "__main__":
	testcases = input()
	 
	for caseNr in xrange(1, testcases+1):
		cipher = raw_input()
		print("Case #%i: %s" % (caseNr, solve(int(cipher))))

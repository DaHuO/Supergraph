#!/usr/bin/env python
# -*- coding: utf-8 -*-

if __name__ == "__main__":
	testcases = input()
	 
	for caseNr in xrange(1, testcases+1):
		cipher = raw_input()
		digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
		i = 1
		while(True):
			result = i * int(cipher)
			for character in '%s' % result:
				if character in digits:
					digits.remove(character)
			if len(digits) == 0:
				print("Case #%i: %s" % (caseNr, (result)))
				break
			elif result == 0:
				print("Case #%i: INSOMNIA" % (caseNr))
				break
			else:
				i += 1
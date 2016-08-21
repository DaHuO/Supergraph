#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solve(cipher):
	# Greedy solution
	flip_count = 0
	pancake_stack = cipher
	pancake_stack = pancake_stack[:pancake_stack.rfind('-') + 1]
	while (len(pancake_stack) > 0):
		new_pancake_stack = ""
		for pancake in pancake_stack:
			new_pancake_stack = new_pancake_stack+ "-"  if pancake == "+" else new_pancake_stack + "+" 
		pancake_stack = new_pancake_stack
		flip_count = flip_count + 1
		pancake_stack = pancake_stack[:pancake_stack.rfind('-') + 1]
	return flip_count

if __name__ == "__main__":
	testcases = input()
	 
	for caseNr in xrange(1, testcases+1):
		cipher = raw_input()
		print("Case #%i: %s" % (caseNr, solve(cipher)))

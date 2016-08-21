#!/usr/bin/python

import math

def hasPattern(freq, pattern):
	return all(x >= y for x, y in zip(freq, pattern))

def addPattern(freq, pattern):
	for i in range(len(freq)):
		freq[i] += pattern[i]

def removePattern(freq, pattern):
	for i in range(len(freq)):
		freq[i] -= pattern[i]

def find(freq):
	if all(x == 0 for x in freq):
		return '', True

	for i, pattern in enumerate(patterns):
		if hasPattern(freq, pattern):
			removePattern(freq, pattern)
			found, isOK = find(freq)
			if isOK:
				return str(i) + found, True
			addPattern(freq, pattern)

	return '', False


numbers = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
patterns = []
for number in numbers:
	pattern = [0] * 26
	for c in number:
		pattern[ord(c) - ord('A')] += 1
	patterns.append(pattern)


T = input()
for t in range(1, T + 1):
	S = raw_input()

	freq = [0] * 26
	for c in S:
		freq[ord(c) - ord('A')] += 1
		
	result, isOK = find(freq)

	print "Case #%d: %s" % (t, ''.join(sorted(result)))

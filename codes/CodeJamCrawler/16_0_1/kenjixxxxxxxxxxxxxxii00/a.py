#!/usr/bin/env python

import sys

def main1():
	for i in range(1000000+1):
		x = i
		if x == 0:
			print "Case #%d: INSOMNIA" % (i+1)
			continue
		b = []
		j = 1
		while 1:
			for c in str(x * j):
				if c not in b:
					b.append(c)
			if len(b) == 10:
				print "Case #%d: %d" % (i+1, x * j)
				break
			j += 1

def main():
	N = int(raw_input())
	for i in range(N):
		x = int(raw_input())
		if x == 0:
			print "Case #%d: INSOMNIA" % (i+1)
			continue
		b = []
		j = 1
		while 1:
			for c in str(x * j):
				if c not in b:
					b.append(c)
			if len(b) == 10:
				print "Case #%d: %d" % (i+1, x * j)
				break
			j += 1

if __name__ == '__main__':
	main()

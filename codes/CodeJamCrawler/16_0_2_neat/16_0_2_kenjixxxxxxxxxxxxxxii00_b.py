#!/usr/bin/env python

import sys

def main():
	N = int(raw_input())
	for i in range(N):
		s = raw_input()
		if len(s) == 1:
			if s[0] == "-":
				print "Case #%d: 1" % (i+1)
			else:
				print "Case #%d: 0" % (i+1)
			continue
		b = s[0]
		Flag = False
		if b == "-":
			Flag = False
		else:
			Flag = True
		cnt = 0
		for c in s[1:]:
			if b != c:
				cnt += 1
				if Flag == False:
					Flag = True
				else:
					Flag = False
			b = c
		if Flag == False:
			cnt += 1
		print "Case #%d: %d" % (i+1, cnt)
		
if __name__ == '__main__':
	main()

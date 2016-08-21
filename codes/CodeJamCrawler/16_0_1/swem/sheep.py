#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from itertools import *
#from sets import *
import math
import sys

def numbers(input):
	s = set()
	while input != 0:
		s.add(input % 10)
		input = (input - input%10)/10
	return s

if __name__ == "__main__":
	t = int(input())
	for caseIdx in range(1,t+1):
		sys.stdout.flush()
		d = int(input())
		if d == 0:
			ans = "INSOMNIA"
		else:
			s = set()
			target = 0
			while len(s) != 10:
				target += d
				s |= numbers(target)
			ans = str(target)

		print("Case #%d: %s" % (caseIdx, ans))

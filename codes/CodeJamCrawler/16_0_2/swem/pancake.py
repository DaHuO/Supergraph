#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from itertools import *
#from sets import *
import math
import sys

if __name__ == "__main__":
	t = int(input())
	for caseIdx in range(1,t+1):
		sys.stdout.flush()
		stack = input()
		ans = 0
		last = '+'
		for idx, c in enumerate(reversed(stack)):
			if c != last :
				ans += 1
			last = c

		print("Case #%d: %d" % (caseIdx, ans))

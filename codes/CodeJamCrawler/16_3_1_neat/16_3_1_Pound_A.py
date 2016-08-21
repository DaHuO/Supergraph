"""
E:\python27\python_nopause.bat "$(FULL_CURRENT_PATH)" < "A-test.in" > "A-test-out.txt" 2>&1
E:\python27\python_nopause.bat "$(FULL_CURRENT_PATH)" < "A-small-attempt0.in" > "A-small-out.txt" 2>&1
E:\python27\python_nopause.bat "$(FULL_CURRENT_PATH)" < "A-large.in" > "A-large-out.txt" 2>&1
"""

# Index of duplicates items in a python list
def duplicates(lst, item):
	return [i for i, x in enumerate(lst) if x == item]

import os
from sys import *

inputfile = os.path.realpath("A-test.in")
fid = open(inputfile, 'r')					

# T = int(fid.readline())
T = int(stdin.readline())
for t in xrange(T):
	# N = int(fid.readline())
	# P = map(int, fid.readline().split())
	N = int(stdin.readline())
	P = map(int, stdin.readline().split())
	# print N, P, sum(P)
	
	temp = [float(i) for i in P]
	res = []
	while sum(P) > 0:
		dup = duplicates(P,max(P))	# index of duplication
		if len(dup) > 2:
			if P[dup[0]]!=1:
				P[dup[0]] = P[dup[0]] - 1
				P[dup[1]] = P[dup[1]] - 1
				temp[dup[0]] = temp[dup[0]] - 1
				temp[dup[1]] = temp[dup[1]] - 1
				ans = [chr(65+dup[0]), chr(65+dup[1])]
			elif P[dup[0]] == 1:
				if len(dup)%2 == 0:
					P[dup[0]] = P[dup[0]] - 1
					P[dup[1]] = P[dup[1]] - 1
					temp[dup[0]] = temp[dup[0]] - 1
					temp[dup[1]] = temp[dup[1]] - 1
					ans = [chr(65+dup[0]), chr(65+dup[1])]
				elif len(dup)%2 == 1:
					P[dup[0]] = P[dup[0]] - 1
					temp[dup[0]] = temp[dup[0]] - 1
					ans = [chr(65+dup[0])]
		elif len(dup) == 2:
			P[dup[0]] = P[dup[0]] - 1
			P[dup[1]] = P[dup[1]] - 1
			temp[dup[0]] = temp[dup[0]] - 1
			temp[dup[1]] = temp[dup[1]] - 1
			ans = [chr(65+dup[0]), chr(65+dup[1])]
		elif len(dup) == 1:
			P[dup[0]] = P[dup[0]] - 1
			temp[dup[0]] = temp[dup[0]] - 1
			ans = [chr(65+dup[0])]
		res.append("".join(str(x) for x in ans))
		
	print "Case #%d:" %(t+1), " ".join(str(x) for x in res)

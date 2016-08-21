#!/usr/bin/python
def check(L):
	return reduce(lambda x, y: x and y, L)

fin = open('A-large.in')
T = int(fin.readline())
for i in range(T):
	N = int(fin.readline())
	result = 0
	lis = [False] * 10
	if N == 0:
		result = "INSOMNIA"
	else:
		KN = N
		while True:
			for c in str(KN):
				lis[int(c)] = True
			if check(lis):
				result = KN
				break
			KN += N
	print "Case #%s: %s" % (i + 1, result)
fin.close()
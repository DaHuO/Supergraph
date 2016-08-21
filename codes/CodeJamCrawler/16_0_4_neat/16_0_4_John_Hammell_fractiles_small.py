#!/usr/bin/python2

test_cases = []

f = open('D-small-attempt0.in', 'r')
T = int(f.readline().rstrip()) # Number of test cases.
for i in range(T):
	test_cases.append(map(int, f.readline().split()))
f.close()

for i in range(len(test_cases)):
	K = test_cases[i][0]
	C = test_cases[i][1]
	S = test_cases[i][2]

	result = "Case #%s:" % (i+1)

	for n in range(1, K+1):
		result += " " + str(n)

	print result

import sys

n = int(raw_input())

for j in range(n):
	st = raw_input()[::-1]

	i = 0
	while i < len(st) and st[i] == '+':
		i += 1

	flips = 0
	if i == 0:
		i = 1
		flips = 1

	while i < len(st):
		if st[i] != st[i-1]:
			flips = flips + 1
		i += 1

	print "Case #" + str(j+1) + ":" + " " + str(flips)
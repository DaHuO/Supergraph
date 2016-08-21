#!/usr/bin/python3
f = open('B-large.in', 'r')
T = int(f.readline().rstrip())
#T = int(input())
prefix = "Case #"

for t in range(1,T+1):
	#arr = list(input())
	arr = list(f.readline().rstrip())
	changes = list()
	last = arr[0]
	count = 0
	i = 1

	while len(arr) > 0 and i < len(arr):
		if arr[i] != last:
			last = arr[i]
			arr = arr[i:]
			i = 0
			count += 1
		else:
			i += 1

	if arr[0] == '-':
		count += 1

	print(prefix + str(t) + ": " + str(count))

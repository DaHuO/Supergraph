#!/usr/bin/python3
f = open('A-large.in', 'r')
T = int(f.readline())
#T = int(input())

for t in range(1,T+1):
	N = int(f.readline())
	#N = int(input())
	if N == 0:
		print("Case #" + str(t) + ": INSOMNIA")
		continue

	arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
	x = 0
	while len(arr) > 0:
		x += 1
		numbs = list(map(int, list(str(N * x))))
		for numb in numbs:
			if numb in arr:
				arr.remove(numb)

	print("Case #" + str(t) + ": " + str(x * N))
#!/usr/bin/python3
for t in range(int(input())):
	K, C, S = map(int, input().split())
	result = [i * (K ** (C - 1)) + 1 for i in range(K)]
	print('Case #{}: {}'.format(t + 1, ' '.join(map(str, result))))

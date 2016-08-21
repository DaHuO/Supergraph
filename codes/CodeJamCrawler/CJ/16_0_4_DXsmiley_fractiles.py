T = int(input())

for t in range(1, T + 1):
	K, C, S = map(int, input().split())
	o = (str(K ** (C - 1) * i + 1) for i in range(K))
	print('Case #{}: {}'.format(t, ' '.join(o)))

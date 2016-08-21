T = int(input())
for cc in range(1, T + 1):
	k, c, s = (int(_) for _ in input().split())
	print('Case #%d: ' % cc, end='')
	print(' '.join([str(1 + i * k ** (c - 1)) for i in range(s)]))

#!/usr/bin/python3	

t = int(input())


for t in range(1, t+1):
	n = int(input())
	if n == 0:
		print('Case #{}: {}'.format(t, 'INSOMNIA'))
		continue
	
	x = 0
	vis = [1 for x in range(10)]
	while any(vis):
		x += n
		for d in str(x):
			vis[ord(d) - ord('0')] = 0

	print('Case #{}: {}'.format(t, x))

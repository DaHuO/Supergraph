import numpy as np

n = int(raw_input())
xs = [raw_input() for _ in range(n)]


def solve(x):
	x_n = np.array([int(c=='+') for c in x])

	def rec_solve(arr):
		if len(arr)==0:
			return 0
		if len(arr)==1:
			return int(arr[0]!=1)

		tail = arr[-1]
		ptail = len(arr)-1
		while ptail>=0 and arr[ptail]==tail:
			ptail-=1
		if tail==0:
			return rec_solve(1-arr[:ptail+1]) + 1
		else:
			return rec_solve(arr[:ptail+1])

	return rec_solve(x_n)




for i,x in enumerate(xs):
	print 'Case #{}: {}'.format(i+1,solve(x))
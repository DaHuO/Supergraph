import itertools

te = input()
for qe in range(1, te+1):

	n, k = map(int, raw_input().split())
	p = map(float, raw_input().split())
	
	AAA = 0
	cnt =0
	for xx in itertools.combinations(p, k):
		# print cnt
		# cnt +=1
		# print p
		v = [ [ 0 for j in range(k+1) ]for i in range(2*k+2)]

		v[k+0][k] = 1.0

		for b in range(k-1, -1, -1):
			for a in range(-k, k+1):
				# print a, b
				v[k+a][b] = xx[b] * v[k+a-1][b+1] + (1.0-xx[b]) * v[k+a+1][b+1]

		AAA = max(AAA, v[k+0][0])
	# print AAA, k
	print 'Case #%d: %.10f'%(qe, AAA)
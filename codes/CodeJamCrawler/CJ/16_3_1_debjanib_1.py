from collections import defaultdict

T = int(raw_input())

for t in range(T):
	N = input()
	heap = map(int, raw_input().split())
	for i in range(N):
		heap[i] = (-heap[i], chr(ord('A')+i))
	import heapq
	heapq.heapify(heap)
	res = []
	while len(heap) > 0:
		A,B = heapq.heappop(heap), None
		if len(heap) > 0:
			B = heapq.heappop(heap)
			if A[0] == B[0]:
				res+= [A[1]+B[1]]
				A = ( A[0]+1, A[1])
				B = ( B[0]+1, B[1])
			else:
				if A[0] == -1:
					res+= [A[1]]
					A = ( A[0]+1, A[1])
				else:
					res+=[A[1]+A[1]]
					A = ( A[0]+2, A[1])

		else:
			if A[0] == -1:
				res+= [A[1]]
				A = ( A[0]+1, A[1])
			else:
				res+=[A[1]+A[1]]
				A = ( A[0]+2, A[1])

		if A and A[0] < 0:
			heapq.heappush(heap, A)

		if B and B[0] < 0:
			heapq.heappush(heap, B)

	if len(res[-1]) == 1 and len(res) > 1:
		res[-1], res[-2] = res[-2], res[-1] 

	res = " ".join(res)
	print( "Case #%d: %s" % (t+1, res) )
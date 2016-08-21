T = input()
for i in range(T):
	A = list(raw_input())
	l = 0
	flips  = 0
	while '-' in A:
		r = 1
		while r < len(A) and A[r] == A[l]:
			r += 1			
		temp =['+' if A[j] == '-' else '-' for j in reversed(range(l, r , 1))] 
		flips += 1
		A = temp + A[r:]

	print 'Case #' + str(i+1) + ': '+ str(flips)

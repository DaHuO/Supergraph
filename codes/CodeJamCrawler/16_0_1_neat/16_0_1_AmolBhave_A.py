N = int(raw_input())
for i in range(1, N+1):
	n0 = int(raw_input())
	if n0 == 0:
		print 'Case #' + str(i) + ': ' + 'INSOMNIA'
		continue
	n = n0
	j = 0
	digits = set()
	while len(digits) != 10:
		j+=1
		n = n0*j
		digits = digits.union(set(list(str(n))))
	print 'Case #' + str(i) + ': ' + str(n)

filename = "in.01"
filename = "B-small-attempt1.in"
# filename = "B-large.in.txt"

f = open(filename)
test = 0
for test in xrange(int(f.readline())):
	print "Case #%d:" % (test+1),
	n = int(f.readline())
	ls = []
	for i in range(2*n-1):
		ls.append([int(x) for x in f.readline().strip().split()])
	pairs = []
	for i in range(n):
		min_h = min(map(lambda x:x[i],ls))
		# print min_h
		pairs.append(filter(lambda x:x[i] == min_h, ls))
		ls = filter(lambda x:x[i] != min_h, ls)
	a = []
	b = []
	# print pairs
	col = lambda k:lambda row: row[k] 
	finished = False
	def visit(k):
		global a,finished
		# print a, b
		if k >= n:
			finished = True
		if finished:
			return
		if len(pairs[k]) == 1:
			p = pairs[k][0]
			ok = True
			for i in xrange(k):
				# print b[i][k], p[i]
				if len(b[i])>0 and b[i][k] != p[i]:
					ok = False
					break
			if ok:
				a.append(p)
				b.append([])
				visit(k + 1)
				if finished: return
				a.pop()
				b.pop()
		else:
			for t in xrange(2):
				p = pairs[k][t]
				p1 = pairs[k][1-t]
				ok = True
				# print p
				for i in xrange(n):
					if map(col(k), a) != p[:k]:
						# print map(col(k), a), p[:k]
						ok = False
						break
				for i in xrange(k):
					if len(b[i])>0 and b[i][k] != p1[i]:
						# print b[i][k], p1[i]
						ok = False
						break
				# print ok
				if ok:
					# print pairs[k], t
					a.append(pairs[k][1-t])
					b.append(pairs[k][t])
					visit(k+1)
					if finished: return
					a.pop()
					b.pop()

	for p in xrange(n):
		if len(pairs[p]) == 1:
			miss = p
			break
	# print pairs
	visit(0)
	if not finished:
		print '-----------'
	# print a
	else:
		print ' '.join([str(x) for x in map(col(miss),a)])
	# print pairs, miss






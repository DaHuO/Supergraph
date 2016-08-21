f = open("b.in")
o = open("b.out", "w")

def valid(before, after):
	for i in xrange(len(before)):
		if before[i] >= after[i]: return False
	return True

def valid_all(l1, l2):
	for i in xrange(len(l1)-1):
		if not valid(l1[i], l1[i+1]):
			return False
			#print "ERROR 1"
			#exit()
	for i in xrange(len(l2)-1):
		if not valid(l2[i], l2[i+1]):
			return False
			#print "ERROR 2"
			#exit()
	
	if len(l1) < len(l2): l1, l2 = l2, l1
	"""
	# l1 is complete
	print "L1 ="
	for e in l1:
		print e
	print "L2 ="
	for e in l2:
		print e
	"""
	i = 0
	while i < N-1 and l2[i] == [e[i] for e in l1]:
		i += 1
	
	missing = [e[i] for e in l1]
	"""
	print "missing index", i
	print "missing list", missing
	"""
	l2 = l2[:i] + [missing] + l2[i:]
	
	l3 = [[e[j] for e in l2] for j in xrange(len(l2))]
	"""
	print "L3 (=l2) ="
	for e in l3:
		print e
	"""
	if l1 != l3:
		return False
		#print "ERROR"
		#exit()
	return True

def l1l2_rec(N, ls, l1, l2, i):
	global L1, L2
	if i == len(ls):
		L1, L2 = l1, l2
		return valid_all(l1, l2)
	if l1 == [] or (valid(l1[-1], ls[i]) and len(l1) < N):
		if l1l2_rec(N, ls, l1 + [ls[i]], l2, i + 1):
			return True
	if l2 == [] or (valid(l2[-1], ls[i]) and len(l2) < N):
		if l1l2_rec(N, ls, l1, l2 + [ls[i]], i + 1):
			return True
	return False

L1, L2 = [], []
def l1l2(N, ls):
	global L1, L2
	L1, L2 = [], []
	l1, l2 = [], []
	l1l2_rec(N, ls, l1, l2, 0)
	return L1, L2

T = int(f.readline().strip())
print T
for t in xrange(T):
	N = int(f.readline().strip())
	ls = []
	for l in xrange(2*N-1):
		ls.append(map(int, f.readline().strip().split(" ")))
	ls.sort()
	
	l1, l2 = l1l2(N, ls)
	
	for i in xrange(len(l1)-1):
		if not valid(l1[i], l1[i+1]):
			print "ERROR 1"
			exit()
	for i in xrange(len(l2)-1):
		if not valid(l2[i], l2[i+1]):
			print "ERROR 2"
			exit()
	
	if len(l1) < len(l2): l1, l2 = l2, l1
	
	# l1 is complete
	print "L1 ="
	for e in l1:
		print e
	print "L2 ="
	for e in l2:
		print e
	i = 0
	while i < N-1 and l2[i] == [e[i] for e in l1]:
		i += 1
	
	missing = [e[i] for e in l1]
	print "missing index", i
	print "missing list", missing
	
	l2 = l2[:i] + [missing] + l2[i:]
	
	l3 = [[e[j] for e in l2] for j in xrange(len(l2))]
	print "L3 (=l2) ="
	for e in l3:
		print e
	
	if l1 != l3:
		print "ERROR"
		exit()
	
	ln = "Case #%d: %s" % (t+1, " ".join(map(str, missing)))
	print ln
	o.write(ln + "\n")


o.close()
f.close()

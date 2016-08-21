T = int(raw_input())
counter = 1 
while(T > 0):
	seen = set()
	N = int(raw_input())
	m = 1
	if (N == 0):
		print "Case #"+str(counter)+": INSOMNIA"
	else:
		while(len(seen) != 10):
			uniq = set(str(N*m))
			seen = seen.union(uniq)
			# print seen,N*m
			m+=1
		print "Case #"+str(counter)+": "+str(N*(m-1))
	counter+=1
	T-=1

# counter = 1
# for N in range(10 ** 6):
# 	seen = set()
# 	# N = int(raw_input())
# 	m = 1
# 	if (N == 0):
# 		print "Case #"+str(counter)+": INSOMNIA"
# 	else:
# 		while(len(seen) != 10):
# 			uniq = set(str(N*m))
# 			seen = seen.union(uniq)
# 			# print seen,N*m
# 			m+=1
# 		print "Case #"+str(counter)+": "+str(N*(m-1))
# 	counter+=1
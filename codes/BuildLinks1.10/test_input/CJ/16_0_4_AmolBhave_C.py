# for s in ['LLLL', 'LLLG', 'LLGL', 'LLGG', 'LGLL', 'LGLG', 'LGGL', 'LGGG', 'GLLL', 'GLLG', 'GLGL', 'GLGG', 'GGLL', 'GGLG', 'GGGL', 'GGGG']:
# 	s0 = s# = 'LLLL'
# 	for i in range(0,1):
# 		S = ''
# 		for c in s:
# 			if c == 'L':
# 				S += s0
# 			else:
# 				S += 'G' * len(s0)
# 		s = S
# 	print s

def partition(i, j, n, idx):
	x = i + (idx-1)*(j-i)/n
	return x, x+(j-i)/n

T = int(raw_input())
for t in range(1, T+1):
	K, C, S = map(int, raw_input().split())
	#print K,C,S
	if K > C*S:
		print 'Case #' + str(t) + ': IMPOSSIBLE'
		continue

	idxs = []
	b = 1
	cnt = 0
	while cnt*C < K:
		i, j = 0, K**C
		c = 1
		while c <= C and b <= K:
			i, j = partition(i, j, K, b)
			#print b, c, i, j
			b += 1
			c += 1
		idxs.append(i+1)
		cnt += 1
	# b = 0
	# cnt = 0
	# while cnt*C < K:
	# 	idx = 1
	# 	for c in range(1, C+1):
	# 		idx += b*K**(C-c)
	# 		print idx
	# 		b+=1
	# 		print idx, b, K, C-c
	# 	idxs.append(idx)
	# 	if K > C:
	# 		b -= 1
	# 	cnt += 1

	print 'Case #' + str(t) + ': ' + ' '.join(map(str, idxs))

# L L L = L1 L2 L3 L1 L2 L1 L1 L2 L1 = L L L L L L L L L L L L L L L L L L L L L L L L L L L
# L L G = L1 L2 G3 L1 L2 G3 G3 G3 G3 = L L G L L G G G G L L G L L G G G G G G G G G G G G G
# L G L = L1 G2 L3 G2 G2 G2 L1 G2 L3 = L G L G G G L G L G G G G G G G G G L G L G G G L G L
# L G G = L1 G2 G3 G2 G2 G2 G3 G3 G3 = L G G G G G G G G G G G G G G G G G G G G G G G G G G
# G L L = G1 G1 G1 G1 L2 L3 G1 L2 L3 = G G G G G G G G G G G G G L L G L L G G G G L L G L L
# G L G = G1 G1 G1 G1 L2 G3 G3 G3 G3 = G G G G G G G G G G G G G L G G G G G G G G G G G G G
# G G L = G1 G1 G1 G2 G2 G2 G1 G2 L3 = G G G G G G G G G G G G G G G G G G G G G G G G G G L
# G G G = G1 G1 G1 G2 G2 G2 G3 G3 G3 = G G G G G G G G G G G G G G G G G G G G G G G G G G G

# C >= K

# XXXX XXXX XXXX XXXX  XXXX XXXX XXXX XXXX  XXXX XXXX XXXX XXXX  XXXX XXXX XXXX XXXX

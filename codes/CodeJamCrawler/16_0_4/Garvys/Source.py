# def genAllArtwork(K):
# 	if K == 0:
# 		return ['']
# 	l = genAllArtwork(K-1)
# 	l1 = [('L' + e) for e in l]
# 	l2 = [('G' + e) for e in l]
# 	return l1 + l2

# def genFutureArtwork(originalSequence,K,art,C):
# 	if C = 1:
# 		return art
# 	s = ''
# 	for e in art:
# 		if e == 'L':
# 			s += originalSequence
# 		elif e == 'G':
# 			s += 'G'*K
# 	return genFutureArtwork(originalSequence,K,s,C-1)

T = int(input())
for t in range(T):
	K,C,S = list(map(int,input().split()))
	A = pow(K,C-1)
	l = []
	for i in range(K):
		l.append(1+i*A)
	print('Case #{}: {}'.format(t+1,' '.join(list(map(str,l)))))


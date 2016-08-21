T = int(raw_input())
for t in range(T):
	S = raw_input() + '+'
	n_boundaries = S.count('-+') + S.count('+-')
	print 'Case #%d: %d' %(t+1, n_boundaries)

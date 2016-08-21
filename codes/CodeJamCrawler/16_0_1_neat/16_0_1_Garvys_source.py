T = int(input())
for t in range(T):
	N = int(input())
	if N == 0:
		print('Case #{}: {}'.format(t+1,'INSOMNIA'))
		continue
	s = set(str(N))
	i = 1
	while len(s) != 10:
		i += 1
		s = s | set(str(N*i))
	print('Case #{}: {}'.format(t+1,N*i))
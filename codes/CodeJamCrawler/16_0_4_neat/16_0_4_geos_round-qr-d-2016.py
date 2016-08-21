fin = open('D-small.in', 'r')
T = fin.readline().strip()
T = int(T)
fout = open('D-small-qr.out', 'w')


for t in range(1, T + 1):
	K, C, S = fin.readline().split()
	K = int(K)
	C = int(C)
	S = int(S)
	if K == S:
		pos = ' '.join(map(str, list(range(1, S + 1))))
		fout.write('Case #{0}: {1}\n'.format(t, pos))

fin.close()
fout.close()

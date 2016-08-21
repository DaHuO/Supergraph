# coding=utf-8

import os, sys, ljqpy, time
time.clock()


def Compute(pps):
	k = len(pps)
	f = [[0 for y in range(k+1)] for x in range(k+1)]
	f[0][0] = 1.0
	for i in range(1, k+1):
		for j in range(0, i+1):
			if j > 0:
				f[i][j] += f[i-1][j-1] * pps[i-1]
			f[i][j] += f[i-1][j] * (1-pps[i-1])
	return f[k][k//2]
	
def Run(p1, p2):
	n, k = map(int, p1.split())
	plst = list(map(float, p2.split()))
	ret = 0.0
	for v in range(2**n):
		pps = [plst[u] for u in range(n) if (v&(1<<u)) != 0]
		if len(pps) != k: continue
		ret = max(ret, Compute(pps))
	return '%.8f' % ret

lst = ljqpy.LoadList('B-small-attempt2.in')
outf = 'B-small-attempt2.out'

with open(outf, 'w') as fout:
	N = int(lst[0])
	for k in range(N):
		fout.write('Case #%d: %s\n' % (1+k,Run(lst[k*2+1], lst[k*2+2])))
		fout.flush()

os.system('emeditor.exe ' + outf)
print('completed')
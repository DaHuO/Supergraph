# coding=utf-8

import os, sys, ljqpy, time
time.clock()

nlst = [(1,0,0), (1,1,0)]
for ii in range(2, 14):
	z = nlst[-1]
	zz = (z[0] + z[2], z[1] + z[0], z[2] + z[1])
	nlst.append(zz)

ee = 'PRS'
def Make(N, t):
	if N == 0: return ee[t]
	z1 = Make(N-1, t)
	z2 = Make(N-1, (t+1)%3)
	if z1 < z2: return z1+z2
	return z2+z1

def Run(ss):
	N, R, P, S = map(int, ss.split())
	lst = [P, R, S]
	for ii in range(3):
		z = (lst[ii%3], lst[(ii+1)%3], lst[(ii+2)%3])
		if z == nlst[N]:
			return Make(N, ii)
	return 'IMPOSSIBLE'

lst = ljqpy.LoadList('A-large.in')
outf = 'A-large.out'

with open(outf, 'w') as fout:
	for k, v in enumerate(lst[1:]):
		fout.write('Case #%d: %s\n' % (1+k,Run(v)))

os.system('emeditor.exe ' + outf)
print('completed')
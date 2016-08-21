#coding: utf8


s = '''\
3
2 2
0.50 0.50
4 2
0.00 0.00 1.00 1.00
3 2
0.75 1.00 0.50
'''



filename = ''
filename = 'B-small-attempt0.in'
#filename = 'B-large-practice.in'
if filename:
	import glob
	no = 0
	for s in glob.glob(filename[:-3] + '-*.out'):
		no = max(no, int(s[len(filename[:-3])+1:-4])+1)
	outname = filename[:-3] + '-%d.out'%no
else:	
	outname = ''
#outname = ''
#new = defaultdict(lambda:float('inf'))	
	
import sys
#set_trace()
input = iter(s.splitlines(keepends=True))
out = sys.stdout
if filename:
	input = open(filename)
if outname and len(sys.argv) != 2:
	print('out', outname)
	out = open(outname, 'w')
elif outname and len(sys.argv) == 2:
	out = sys.stderr

from pdb import set_trace
from itertools import combinations, permutations, combinations_with_replacement, product
from collections import defaultdict
from copy import deepcopy
from math import sin,cos,tan,log,atan2,pi as PI



def solve():
	ans = 0.0
	for p in combinations(range(N), K):
		DP = [[0.0]*(K+1) for i in range(K)]
		
		DP[0][1] = D[p[0]]
		DP[0][0] = 1.0 - D[p[0]]
		for i in range(K-1):
			for k in range(K):
				DP[i+1][k]   += DP[i][k]*(1-D[p[i+1]])
				DP[i+1][k+1] += DP[i][k]*D[p[i+1]]
			#DP[i+1][K-1] += DP[i][K-1]*(1-D[i+1])
		#print(DP[K-1])
		ans = max(ans, DP[K-1][K//2])
	return ans
	
CaseCnt = int(next(input))

import time
start0 = time.time()

#if len(sys.argv) == 2:
if 1:
	for case in range(1,CaseCnt+1):
		N,K = map(int,next(input).split())
		*D, = map(float,next(input).split())
		#for i in range(N):
		#	d,l = map(int,next(input).split())
		#	V += [(d,l)]
		#D, = map(int,next(input).split())
		if len(sys.argv) == 2 and case != int(sys.argv[1]): continue
		#if case != 29: continue
		start = time.time()
		ans = solve()
		print(case, time.time()-start)
		print('Case #%d:'%case, ans, file=out)
		
else:	
	import subprocess
	import threading
	import sys
	ProcNo = 0
	lock_output = threading.Lock()
	
	result = ['']*CaseCnt
	
	def SubProc(threadNo):
		global CaseNo
		while CaseNo <= CaseCnt:
			case = CaseNo
			CaseNo += 1
			p = subprocess.Popen([sys.executable, __file__, str(case)]
				, stdout=subprocess.PIPE
				, stderr=subprocess.PIPE)
			#p.wait()
			while p.poll() is None:
				time.sleep(0.01)
			#elapsed = p.stdout.readline().decode().strip()
			print(p.stdout.read().decode()[:-1], threadNo)
			result[case-1] = p.stderr.read().decode().strip()
			#with lock_output:
			#	print(case, elapsed)
				#print(result[case-1])
	
	CaseNo = 1
	ts = [threading.Thread(target=SubProc, args=(no,)) for no in range(min(6,CaseCnt))]
	for t in ts:
		t.start()
	for t in ts:
		t.join()
		
	for s in result:
		print(s, file=out)

if len(sys.argv) != 2:
	print(time.time()-start0)
import re
import sys
import itertools as it
import functools as fn
redtext = sys.stderr.write

@fn.lru_cache(None)
def ty(d,r):
	if d==0:
		if r=='r':
			return r,[1,0,0]
		elif r=='s':
			return r,[0,1,0]
		elif r=='p':
			return r,[0,0,1]
	if r=='p':
		o,x=ty(d-1,'p')
		o2,x2=ty(d-1,'r')
	elif r=='s':
		o,x=ty(d-1,'p')
		o2,x2=ty(d-1,'s')
	elif r=='r':
		o,x=ty(d-1,'r')
		o2,x2=ty(d-1,'s')
	if o2<o:
		o,x,o2,x2=o2,x2,o,x
	return o+o2,[x[i]+x2[i] for i in range(3)]


def calc(n,*ix):
	ix = list(ix)
	ix[1],ix[2] = ix[2],ix[1]
	if sum(ix) != (1<<n):
		red('what')
	for i in 'rsp':
		s,out = ty(n,i)
		if all(out[i] == ix[i] for i in range(3)):
			return s.upper()
	else:
		return 'IMPOSSIBLE'


def scanit():
	while True:
		inbuf = (i.strip() for i in input().split(' '))
		yield from (i for i in inbuf if i)
scangen = scanit()
def scans(): return next(scangen)
def scan(): return int(next(scangen))

red = sys.stderr.write
testcase = 1
output = 1
if testcase:
	sys.stdin = open('input.txt')
with open('output.txt','w') if output else sys.stdout as sys.stdout:
	for t in range(scan()):
		red('Case #%d\n'%(t+1))
		print('Case #%d: %s'%(t+1,calc(scan(),scan(),scan(),scan())))

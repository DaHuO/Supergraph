import re
import sys
import itertools as it

def calc():
	n = scan()
	dcta,dctb = {},{}
	data = []
	for i in range(n):
		a,b = scans(),scans()
		if a not in dcta:
			dcta[a] = len(dcta)
		a = dcta[a]
		if b not in dctb:
			dctb[b] = len(dctb)
		b = dctb[b]
		data += [(a,b)]
	out = 0
	for i in it.product([False,True],repeat=n):
		realda,realdb = [],[]
		for k,j in enumerate(i):
			if not j:
				realda+=[data[k][0]]
				realdb+=[data[k][1]]
		realda,realdb = set(realda),set(realdb)
		# print(i)
		# print(realda,realdb)
		for k,j in enumerate(i):
			if j:
				if data[k][0] not in realda:
					break
				if data[k][1] not in realdb:
					break
		else:
			out = max(out, sum(i))
	return out

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
		print('Case #%d: %d'%(t+1,calc()))
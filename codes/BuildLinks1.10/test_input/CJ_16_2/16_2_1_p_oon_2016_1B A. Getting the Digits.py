import re
import sys
import itertools as it

decomp = "EFGHINORSTUVWXZ"
tem = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
tem_buck = [{j:sum(j==k for k in i) for j in decomp} for i in tem]
orz = [0,6,8,2,4,5,7,3,1,9]
"""
Z for zero
X for six
G for eight
W for two
U for four
f for five (four)
S for seven (six)
R for three
O for one
then nine
"""
def try_dec(a,b):
	a=a.copy()
	for i in a:
		a[i]-=b[i]
		if a[i] < 0:
			return None
	return a

def calc(st):
	bk = {j:sum(j==k for k in st) for j in decomp}
	oo = [0]*10
	for i in orz:
		while True:
			out = try_dec(bk,tem_buck[i])
			if out:
				bk=out
				oo[i]+=1
			else:
				break
	return ''.join(str(i) for i in (sum(([i]*oo[i] for i in range(10)),[])))

def scanit():
	while True:
		inbuf = (i.strip() for i in input().split(' '))
		yield from (i for i in inbuf if i)
scangen = scanit()
def scans(): return next(scangen)
def scan(): return int(next(scangen))
testcase = 1
output = 1
if testcase:
	sys.stdin = open('A-large.in')
with open('output.txt','w') if output else sys.stdout as sys.stdout:
	for t in range(scan()):
		print('Case #%d: %s'%(t+1,calc(scans())))
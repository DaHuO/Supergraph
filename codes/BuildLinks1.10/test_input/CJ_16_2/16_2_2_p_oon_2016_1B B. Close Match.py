import re
import sys
import itertools as it

def calc3(x,cond):
	if cond == 1: # getmax
		return ''.join(('9' if i == "?" else i) for i in x)
	if cond == 0: # getmax
		return ''.join(('0' if i == "?" else i) for i in x)
	raise Exception
def calc2(a,b,cond):
	if not a:
		return "",""
	az,bz = a[0],b[0]
	la,lb = az,bz
	a,b = a[1:],b[1:]
	if cond==0: #eq
		if az!='?' and bz!='?':
			a,b = calc2(a,b,(0 if az==bz else (-1 if az<bz else 1)))
			return az+a,bz+b
		if az=='?':
			if bz=='?':
				bz='0'
			az=bz
		bz=az
		#try eq
		if not a:
			return az,bz
		aaa,bbb = calc2(a,b,0)
		choice = (az+aaa,bz+bbb)
		lla,llb = az,bz
		if int(az)>0 and la=="?":
			az = str(int(az)-1)
			azz,bzz = calc2(a,b,(0 if az==bz else (-1 if az<bz else 1)))
			choice = cmp(*choice,az+azz,bz+bzz)
			az=lla
		if int(bz)>0 and lb=="?":
			bz = str(int(bz)-1)
			azz,bzz = calc2(a,b,(0 if az==bz else (-1 if az<bz else 1)))
			choice = cmp(*choice,az+azz,bz+bzz)
			bz=llb
		if int(az)<9 and la=="?":
			az = str(int(az)+1)
			azz,bzz = calc2(a,b,(0 if az==bz else (-1 if az<bz else 1)))
			choice = cmp(*choice,az+azz,bz+bzz)
			az=lla
		if int(bz)<9 and lb=="?":
			bz = str(int(bz)+1)
			azz,bzz = calc2(a,b,(0 if az==bz else (-1 if az<bz else 1)))
			choice = cmp(*choice,az+azz,bz+bzz)
			bz=llb
		return choice
	elif cond == 1: # a grt
		if az=="?":
			az='0'
		if bz=="?":
			bz='9'
		a,b = calc2(a,b,1)
		return az+a,bz+b
	elif cond == -1: # b grt
		if az=="?":
			az='9'
		if bz=="?":
			bz='0'
		a,b = calc2(a,b,-1)
		return az+a,bz+b
	raise Exception

def cmp(a,b,a2,b2):
	d1=abs(int(a)-int(b))
	d2=abs(int(a2)-int(b2))
	if d1!=d2:
		return (a,b) if d1 < d2 else (a2,b2)
	if b!=b2:
		return (a,b) if b<b2 else (a2,b2)
	return (a,b) if a<a2 else (a2,b2)

def try_all_b(a,b,d):
	if d == len(a):
		return ''.join(a),''.join(b)
	if b[d]!='?':
		return try_all_b(a,b,d+1)
	o=0,0
	for i in range(10):
		b[d] = str(i)
		oo=try_all_b(a,b,d+1)
		if i==0:
			o=oo
		else:
			o=cmp(*o,*oo)
		b[d] = '?'
	return o
def try_all_a(a,b,d):
	if d == len(a):
		return try_all_b(a,b,0)
	if a[d]!='?':
		return try_all_a(a,b,d+1)
	o=0,0
	for i in range(10):
		a[d] = str(i)
		oo=try_all_a(a,b,d+1)
		if i==0:
			o=oo
		else:
			o=cmp(*o,*oo)
		a[d] = '?'
	return o

def calc(a,b):
	az,bz=calc2(a,b,0)
	# a,b = try_all_a(list(a),list(b),0)
	# if a!=az or b!=bz:
	# 	print("!!!!! %s %s"%(a,b))
	return "%s %s"%(az,bz)

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
	sys.stdin = open('input.txt')
with open('output.txt','w') if output else sys.stdout as sys.stdout:
	for t in range(scan()):
		print('Case #%d: %s'%(t+1,calc(scans(),scans())))
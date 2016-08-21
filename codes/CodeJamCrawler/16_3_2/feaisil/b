#!/usr/bin/env python3

import sys,time, math
cin=sys.stdin
cerr=sys.stderr
cout=sys.stdout

def rl(cin):
	"""readline and remove \n"""
	return cin.readline()[:-1]
cin.rl=lambda:rl(cin)
def rs(cin):
	return cin.rl().split()
cin.rs=lambda:rs(cin)
def ri(cin):
	return int(cin.rl())
cin.ri=lambda:ri(cin)
def riv(cin):
	return [int(x) for x in rs(cin)]
cin.riv=lambda:riv(cin)
def rf(cin):
	return float(cin.rl())
cin.rf=lambda:rf(cin)
def rfv(cin):
	return [float(x) for x in rs(cin)]
cin.rfv=lambda:rfv(cin)
def rev(i):
	o=[]	
	for x in range(1,1+len(i)): o+=[i[-x]]
	return o
def revs(s):
	return ''.join(rev(s))	
def isPrime(n):
	for i in range(2, int(math.sqrt(n))):
		if not i%n:
			return true
		
def printr(*args):
	cerr.write(', '.join([repr(x) for x in args])+'\n')
		
class bin_base:
	def __init__(self):
		pass
	def up(self):
		pass
	def lo(self):
		pass
	def cont(self):
		pass
class bin_int:
	def __init__(self, m=0, M=10):
		self.m=m-1
		self.M=M+1
		self.c=int((self.M+self.m)/2)
	def up(self):
		self.m=self.c+1
		self.c=int((self.M+self.m)/2)
		return self.c
	def lo(self):
		self.M=self.c
		self.c=int((self.m+self.M)/2)
		return self.c
	def cont(self):
		return self.m < self.M

def search(r, k, pred):
	while r.cont():
		pre=pred(r.c)
		if pre < k:
			r.up()
		else:
			r.lo()
	return r.m

def parse(cin):
	return cin.riv()

def do(l):
	b=l[0]
	m=l[1]
	n=[['0' for k in range(b)] for j in range(b)]
	mink=b
	for k in range(b):
		for j in range(b):
			if k>j and j > 0:
				n[j][k]='1'
	k=1
	while m>0 and k < b-1:
		c=pow(2,b-k-2)
		printr(k, b-k+1,c, m)
		if c <= m:
			mink = min(k, mink)
			n[0][k]='1'
			m-= c
		k+=1
	if m==1:
		mink=min(b-1, mink)
		n[0][b-1]='1'
		m=0
	for k in range(1,b):
		for j in range(1,b):
			if k < mink or j<mink:
				n[j][k]='0'
	# k=1
	# i1=0
	# i2=b-1
	# printr(b,m)
	# j=1
	# for i in range(1,m):
	# 	if k==i2:
	# 		i1+=1
	# 		k=i1+1
	# 	printr(k,i1,i2,j)
	# 	if k<i2:
	# 		n[i1][k]='1'
	# 		n[k][i2]='1'
	# 		k+=1
	# 		j+=1
	# printr(j)
	if m>0:
	 	return "IMPOSSIBLE"
	return 'POSSIBLE\n'+'\n'.join([''.join(x) for x in n])

def main():
	start = time.time()
	T=cin.ri()
	cerr.write("Going to process {} cases\n".format(T))
	k=0
	for Ti in range(1,T+1):
		if math.log(100*Ti/T) > k:
			cerr.write("case {}...".format(Ti))
		print("case #{0}: {1}".format(Ti, do(parse(sys.stdin))))
		if math.log(100*Ti/T) > k:
			k+=1
			cerr.write("duration {}\n".format(time.time()-start))
	cerr.write("duration {0}\n".format(time.time()-start))

if __name__=="__main__":
	main()


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
	l=cin.rl()
	return l

a=[
	"ZERO",
	"ONE",
	"TWO",
	"THREE",
	"FOUR",
	"FIVE",
	"SIX", "SEVEN", "EIGHT", "NINE"]

def do(l):
	l = [x for x in l]
	i=0
	r=[]
	o=[0,2,8,4,1,6,5,7,9,3]
	for i in o:
		bl=[x for x in l]
		valid = True
		while valid:
			for k in a[i]:
				if k in l:
					l.remove(k)
				else:
					valid = False
					l = [x for x in bl]
					break
			if valid:
				bl = [x for x in l]
				r+=[i]
	# while len(l) > 0:
	# 	i = l.pop(0)
	# 	for v in range(10):
	# 		bl=[x for x in l]
	# 		val=[x for x in a[v]]
	# 		valid = True
	# 		if i in val:
	# 			val.remove(i)
	# 			for j in val:
	# 				printr(l, val, j, i)
	# 				if j in l:
	# 					l.remove(j)
	# 				else:
	# 					valid = False
	# 					l = [x for x in bl]
	# 					break
	# 			if valid:
	# 				r+=[v]
	r.sort()
	return ''.join([str(i) for i in r])

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


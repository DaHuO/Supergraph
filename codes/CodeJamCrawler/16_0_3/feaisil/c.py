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
	for i in range(2, int(math.sqrt(n))+1):
		if not n%i:
			return (i,False)
	return (1,True)


def parse(cin):
	l=cin.riv()
	return l

def isValid(s):
	st=''.join(s)
	r=[]
	for i in range(2,11):
		p,v = isPrime(int(st,i))
		if v:
			return False,[]
		r+=[p]
	return True, r 
def inc(a):
	for i in range(2, len(a)):
		if a[-i] == '1':
			a[-i] = '0'
		else:
			a[-i] = '1'
			break	
	return a
def do(l):
	N=l[0]
	J=l[1]
	print("Case #1:")
	p=[]
	k=["1"]+["0" for x in range(N-2)] + ["1"]
	for i in range(J):
		valid = False
		while not valid:
			valid,p = isValid(k)
			if not valid: inc(k)
		print(''.join(k), *p)	
		inc(k)

	return l

def main():
	start = time.time()
	T=cin.ri()
	cerr.write("Going to process {} cases\n".format(T))
	k=0
	for Ti in range(1,T+1):
		if math.log(100*Ti/T) > k:
			cerr.write("case {}...".format(Ti))
		do(parse(cin))
		#print("case #{0}: {1}".format(Ti, do(parse(sys.stdin))))
		if math.log(100*Ti/T) > k:
			k+=1
			cerr.write("duration {}\n".format(time.time()-start))
	cerr.write("duration {0}\n".format(time.time()-start))

if __name__=="__main__":
	main()


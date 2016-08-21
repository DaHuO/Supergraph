#!/usr/bin/python

import sys,random
def insom(a):
	N = 999999999
	x = a;
	if ( a == 0 ) :
		return "INSOMNIA"
	A = [ 0 for y in range(0,10)]
	f = 0
	
	while x < N :
		st = str(x)
		for i in st:
			A[ord(i)-48] = 1
		if sum(A) == 10:
			f = 1
			break
		x += a
	if ( f == 0 ):
		print ("INSOMNIA")
	return x
def main():
	t = int(sys.stdin.readline())
	for i in range(1,t+1):
		print("Case #"+str(i)+": "+str(insom(int(sys.stdin.readline()))))

if __name__=='__main__':
	main()

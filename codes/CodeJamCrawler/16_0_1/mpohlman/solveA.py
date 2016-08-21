#!/usr/bin/env python

debug=0

def compute(N):
	if N == 0:
		return 'INSOMNIA'
	count = 0
	number = N
	d={}
	for digit in list(str(number)):
		d[digit]=1
	while len(d) < 10:
		number = number + N
		count = count + 1
		for digit in list(str(number)):
			d[digit]=1
	return number
	

def solve(infilename):
	infile=open(infilename,'r')
	line=infile.readline()
	T=int(line)
	if debug > 0:
		print 'T:',T
	#iterate
	for index in range(T):
		[N]=[int(i) for i in infile.readline().split()]
		if debug > 0:
			print 
			print 'N:',N
		answer = compute(N)
		print 'Case #%(index)d: %(answer)s' % {"index":index+1,"answer":answer}
	infile.close()
	return

if __name__ == "__main__":
	import sys
	if len(sys.argv) > 1:
		solve(sys.argv[1])
	else:
		solve('A-example')

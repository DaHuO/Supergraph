#!/usr/bin/env python

debug=0

def compute(S):
	count = 0
	while len(S) > sum(1 for i in S if i == '+'):
		new = list(S)
		if S[0] == '+':
			iflip = S.index('-')
		else:
			if sum(1 for i in S if i == '+') == 0:
				iflip = len(S)
			else:
				iflip = S.index('+')
		for i in range(iflip):
			if S[iflip-i-1] == '+':
				new[i]='-'
			else:
				new[i]='+'
		S=new
		count = count + 1
	return count 
	

def solve(infilename):
	infile=open(infilename,'r')
	line=infile.readline()
	T=int(line)
	if debug > 0:
		print 'T:',T
	#iterate
	for index in range(T):
		S=list(infile.readline().rstrip())
		if debug > 0:
			print 
			print 'S:',S
		answer = compute(S)
		print 'Case #%(index)d: %(answer)s' % {"index":index+1,"answer":answer}
	infile.close()
	return

if __name__ == "__main__":
	import sys
	if len(sys.argv) > 1:
		solve(sys.argv[1])
	else:
		solve('B-example.in')

#!/usr/bin/env python

debug=0

def compute(S):
	answer=S[0:1]
	for letter in S[1:]:
		if letter < answer[0]:
			answer.append(letter)
		else:
			answer[:0]=[letter]
	return ''.join(answer)
	

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
		solve('A-example')

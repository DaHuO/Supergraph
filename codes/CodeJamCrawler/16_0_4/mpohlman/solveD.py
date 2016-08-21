#!/usr/bin/env python

debug=0

def optimalSolution(K,C):
	if K == 1 or C == 1:
		solution = range(1,K+1)
	else:
		solution = []
		for index in range((K+1)/2):
			itile = (K-index)+index*K
			solution.append(itile)
	return solution	

def compute(K,C,S):
	solution = optimalSolution(K,C)
	if len(solution) <= S:
		answer = repr(solution).replace(",","").replace("[","").replace("]","")
	else:
		answer = "IMPOSSIBLE"
	return answer

def generate(K,C):
	canon=[]
	for index in range(K+1):
		seed = [int(i==index) for i in range(K)]
		block = [1 for i in range(K)]
		#print 'index,K:',index,K
		#print 'seed:',seed 
		iter = seed[:]
		for cindex in range(C-1):
			new=[]
			for x in iter:
				if x == 1:
					new.extend(block)
				else:
					new.extend(seed)
			iter = new[:]
			#print 'cindex:',cindex
			#print 'iter:',iter
		canon.append(iter)
	solution = optimalSolution(K,C)
	print 'optimal_solution:',solution
	print 'canon:'
	for x in canon:
		print repr(x).replace(" ","").replace(",",",")
	print 'tiles:'
	for x in canon:
		print [x[i-1] for i in solution]
	return

def solve(infilename):
	infile=open(infilename,'r')
	line=infile.readline()
	T=int(line)
	if debug > 0:
		print 'T:',T
	#iterate
	for index in range(T):
		[K,C,S]=[int(i) for i in infile.readline().split()]
		if debug > 0:
			print 
			print 'K,C,S:',K,C,S
		if debug > 0:
			generate(K,C)
		answer = compute(K,C,S)
		print 'Case #%(index)d: %(answer)s' % {"index":index+1,"answer":answer}
	infile.close()
	return

if __name__ == "__main__":
	import sys
	if len(sys.argv) > 1:
		solve(sys.argv[1])
	else:
		solve('D-example.in')

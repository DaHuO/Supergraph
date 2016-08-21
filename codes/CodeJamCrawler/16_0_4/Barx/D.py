import math


"""def solve(K, C, S):

	if C == 1:
		result = range(1,K+1)
	else:
		if C > K: # we can solve for C items at a time, if we only have K, limit to that
			C=K

		end = math.pow(K,C)
		
		start = sum([math.pow(K,c) for c in xrange(2,C-2)])+C
		inc = C * (math.pow(K,C-1)) + 1
		result = [start]
		while result[-1] + inc <= end:
			result.append(result[-1]+inc)

	result = [str(int(r)) for r in result]
	return ' '.join(result) if len(result) <= S else "IMPOSSIBLE"
"""

# just for small set,
def solve(K,C,S):
	if C == 1:
		result = range(1,K+1)
	else:
		m = int(math.pow(K,C-1))

		result = [a*(m+1)-m for a in xrange(1,K+1)]
	result = [str(r) for r in result]
	return ' '.join(result) if len(result) <= S else "IMPOSSIBLE"

def main(source, dest):
    with open(source, 'r') as fd, open(dest, 'w') as fo:
    	T = int(fd.readline())
    	for i in range(1,T+1):
        	K, C, S = fd.readline().rstrip().split(' ')
        	result = solve(int(K), int(C), int(S))
	
        	print 'Case #' + str(i) + ': ' + result + '\n',
        	fo.write('Case #' + str(i) + ': ' + result + '\n')


if __name__ == "__main__":
	filename = os.path.basename(sys.argv[1])
	source = sys.argv[1]
	dest = os.path.join(sys.argv[2], filename.replace(".in.txt",".out.txt"))
	main(source, dest)
# Yash Mittal (yashmittal2009@gmail.com)

def findResult(n):
	if n == 0:
		return 'INSOMNIA'
	digits = set([int(i) for i in str(n)])
	temp = n
	while len(digits) < 10:
		digits = digits.union(set([int(i) for i in str(n)]))
		n += temp
	return n-temp


with open('A-large.in','r') as fin:
	with open('output.out','w') as fout:
		num = int(fin.readline())
		for i in range(1, num+1):
			N = int(fin.readline())
			result = findResult(N)
			fout.write('Case #' + str(i) + ': ' + str(result) + '\n')
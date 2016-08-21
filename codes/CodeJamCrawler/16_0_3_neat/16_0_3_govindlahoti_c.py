NN = 32
JJ = 500

print 'Case #1:'

def conv(s):
	return '11' + ''.join([i+i for i in s]) + '11'

def print_ans(s):
	print conv(s) + ' 3 4 5 6 7 8 9 10 11'


digs = (NN-4)/2
for i in xrange(JJ):
	x = bin(i)[2:].zfill(digs)
	print_ans(x)


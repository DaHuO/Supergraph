infile = open('D-small-attempt0.in', 'r')
outfile = open('fractiles.out', 'w')

def fractile(K, C, S):
	queue = []

T = int(infile.readline().strip())

for t in xrange(T):
	K, C, S = map(int, infile.readline().strip().split(' '))
	outfile.write('Case #' + str(t+1) + ': ' + ' '.join([str(i) for i in xrange(1, S+1)]) + '\n')
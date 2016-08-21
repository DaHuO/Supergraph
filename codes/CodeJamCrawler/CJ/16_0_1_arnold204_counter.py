import sys

def get_last_multiple(n):
	allints = set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
	seen = set()
	for ii in range(1, 100):
		m = n * ii
		seen |= set([int(i) for i in str(m)])
		if seen == allints:
			return m
	return 'INSOMNIA'


fpath = sys.argv[1]

f = open(fpath, 'r')
with open(fpath, 'r') as f:
	content = f.read()

content = content.split('\n')

t = int(content[0]) #no. of test cases


for jj in range(1, t+1):
	print 'Case #{}: {}'.format(jj, get_last_multiple(int(content[jj])))

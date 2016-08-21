infile = open('A-large.in', 'r')
outfile = open('sheep.out', 'w')

def sheep(N):
	lst = [1,2,3,4,5,6,7,8,9,0]
	i = 1
	while lst != []:
		tmp = str(N*i)
		for x in xrange(len(tmp)):
			if int(tmp[x]) in lst:
				lst.remove(int(tmp[x]))
		i += 1
	return N*(i-1)

T = int(infile.readline())
for t in xrange(T):
	N = int(infile.readline().strip())
	ans = 0
	if N == 0:
		ans = 'INSOMNIA'
	else:
		ans = sheep(N)
	outfile.write('Case #' + str(t+1) + ': ' + str(ans) + '\n')
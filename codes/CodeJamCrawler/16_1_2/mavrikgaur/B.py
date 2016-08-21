ip = open('B-small.in')
op = open('B-small.out','w')
t = int(ip.readline())
for case in range(t):
	numdict = dict()
	n = int(ip.readline())
	for _ in range(1,2*n):
		lister = map(int, ip.readline().strip().split())
		for i in lister:
			try:
				numdict[i] += 1
			except:
				numdict[i] = 1
	possible = []
	for i in numdict.keys():
		if(numdict[i]%2!=0):
			possible += [i]
	possible.sort()
	possible = ' '.join(map(str, possible))
	op.write('Case #'+str(case+1)+': '+possible+'\n')
op.close()
ip.close()

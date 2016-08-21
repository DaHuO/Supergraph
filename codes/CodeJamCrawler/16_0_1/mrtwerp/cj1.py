def check(d):
	for i in range(10):
		if d[i]==0:
			return False
	return True

ans = []
ans.append("INSOMNIA")
for n in range(1,10**6+1):
	d = {}
	for i in range(10):
		d[i] = 0
	x = n
	while not check(d):
		for t in str(x):
			d[int(t)] += 1
		x += n
	ans.append(x-n)

for i in range(input()):
	print "Case #" + str(i+1) + ": " + str(ans[input()])


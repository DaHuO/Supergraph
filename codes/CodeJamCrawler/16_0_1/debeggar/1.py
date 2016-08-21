def noSteps(N):
	if N == 0:
		return "INSOMNIA"
	visited = {}
	last = 0
	temp = N
	while len(visited) != 10:
		last += N
		temp = last
		while temp > 0:
			visited[temp%10] = 1
			temp /= 10
	return str(last)
t = input()
for i in range(1, t+1):
	n = input()
	res = noSteps(n)
	print "Case #{0}: {1}".format(i, res)
	#print "Case #{0}: {1}, {2}".format(i, res, int(res)/n)

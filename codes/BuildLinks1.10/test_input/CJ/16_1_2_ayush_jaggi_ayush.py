for tcas in xrange(int(raw_input())):
	n = int(raw_input())
	array = [0]*(2501)
	for i in range(2*n-1):
		l = map(int, raw_input().split())
		for j in l:
			array[j] = (array[j]+1)%2
	ans = "Case #"+str(tcas+1)+":"
	for i in range(2501):
		if (array[i]==1):
			ans+=(" "+str(i))
	print ans
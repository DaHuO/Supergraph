def addToList(listOfNum,n):
	if n < 10:
		listOfNum[n] = 1
		return listOfNum
	else:
		temp = n % 10
		listOfNum[temp] = 1
		return addToList(listOfNum,n/10)

t = int(raw_input())
for j in xrange(1,t+1):
	listOfNum = [0 for x in xrange(10)]
	n = int(raw_input())
	done = False
	i = 1
	while not done:
		if n==0:
			print "Case #{}: INSOMNIA".format(j)
			done = True
		else:
			addToList(listOfNum, n*i)
			if sum(listOfNum) == 10:
				print "Case #{}: {}".format(j,n*i)
				done = True
		i+=1



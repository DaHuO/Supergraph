testC = int(input())

for tc in range(1, testC+1):
	n = int(input())
	start = n
	if n == 0:
		print("Case #"+str(tc)+":", "INSOMNIA")
	
	else:
		toSee = set([i for i in range(0,10)])
	
		count = 1
		while len(toSee) > 0:
			toSee = toSee - set(map(int, list(str(n))))
			#print(toSee)
			n += start
			count += 1
		print("Case #"+str(tc)+":", n - start)

T = int(input())
for t in range(T):
	print("Case #" + str(t+1) + ": ",end="")
	N = int(input())
	Ntmp = N
	if (N==0):
		print("INSOMNIA")
	else:
		l = []
		for i in range(10):
			l.append(0)
		while(True):
			s = str(Ntmp)
			for i in s:
				# print(i)
				digit = int(i)
				l[digit]+=1
			if (l.count(0)==0):
				print(s)
				break
			# print(l)
			Ntmp+=N
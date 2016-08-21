t = int(input())
for x in range(t):
	flag=0
	l = set([])
	n = int(input())
	if n != 0:
		for j in range(n,10000,n):
			for k in str(j):
				l.add(k)
				if len(l) == 10:
					print("Case #",x+1,": ",j,sep="")
					flag = 1
					break
			if flag == 1:
				break
	if len(l) != 10:
		print("Case #",x+1,": INSOMNIA",sep="")

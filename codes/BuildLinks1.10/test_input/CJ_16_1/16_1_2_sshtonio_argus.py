
nb_entry = int(input())

for entry in range(1,nb_entry+1):
	n = int(input())
	l=[]
	out = "Case #"+str(entry)+': '
	for i in range(2*n-1):
		l.append(list(map(int,input().split() )))

	#print(*l)
	num = 0
	minima = 0
	theLine = []
	lprime = l
	bigL =[]
	for i in range(n):
		l2=[]
		for j in range(len(lprime)):
			l2.append(l[j][i])
		#print(*l2)
		l3 = []
		mini = min(l2)
		#print("minimum")
		#print(mini)
		topop = []
		for j in range(len(lprime)):
			if l[j][i] == mini:
				l3.append(l[j])
				topop.append(j)
		for j in reversed(topop):
			lprime.pop(j)
		#print("LEs l3")
		#print(*l3)
		bigL.append(l3)
		if len(l3)==1:
			#found = True
			num = i
			minima = mini
			theLine = l3[0]
			#break
	res = []
	#print("theLine")
	#print(*theLine)
	for i in range(n):
		if i==num:
			res.append(minima)
			continue	
		#print("bigL")
		#print(*bigL[i])
		if (bigL[i][0][num] == theLine[i]):
			res.append(bigL[i][1][num])
		else:
			res.append(bigL[i][0][num])

	print(out, end='')		
	print(*res, sep=' ')	

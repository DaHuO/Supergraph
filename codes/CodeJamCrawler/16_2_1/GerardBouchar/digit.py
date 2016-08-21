


digits=[
	(0,{'Z':1,'E':1,'R':1,'O':1}),
	(2,{'T':1,'W':1,'O':1}),
	(6, {'S':1,'I':1,'X':1}),
	(8, {'E':1,'I':1,'G':1,'H':1,'T':1}),
	(4, {'F':1,'O':1,'U':1,'R':1}),
	(5,{'F':1,'I':1,'V':1,'E':1}),
	(7, {'S':1,'E':2,'V':1,'N':1}),
	(1, {'O':1,'N':1,'E':1}),
	(3, {'T':1,'H':1,'R':1,'E':2}),
	(9, {'N':2,'I':1,'E':1})]


for  N in range(int(input())) :
	s = input()
	count={}
	for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" :
		count[c]=0
	for c in s :
		count[c]=count[c]+1
	res=[]
	# print(count)
	for t in digits :
		num=t[0]
		l=t[1]
		m=10000000000000000000
		for c in list(l.keys()):
			if count[c]//l[c]<m : 
				m=count[c]//l[c]
		res+=[num]*m
		for c in list(l.keys()):
			count[c]-=l[c]*m
		# print(count)
		num+=1
	if sum(list(count.values()))!=0 : 
			print("!!!!!!!!!!!!!!!!!!!!!!!erreur : "+str(N+1))
		

	res.sort()
	print("Case #"+str(N+1)+": "+str(res)[1:-1].replace(', ',''))



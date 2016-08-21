test=int(raw_input())

for i in range(test):
	num=int(raw_input())
	if num==0:
		print "Case #"+str(i+1)+": INSOMNIA"
	else:
		lst = [int(j) for j in str(num)]
		lst = list(set(lst))
		nam = num
		k=2
		while len(lst)!=10:
			nam =num*k
			k+=1
			lst += [int(j) for j in str(nam)]
			lst = list(set(lst))
		print "Case #"+str(i+1)+": "+str(nam)
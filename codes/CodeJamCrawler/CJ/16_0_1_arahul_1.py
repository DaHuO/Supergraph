t=int(raw_input())
case=1
for _ in range(t):
	n=int(raw_input())
	if(n==0):
		print("Case #"+str(case)+": INSOMNIA")
		case+=1
		continue
	arr=[0 for x in range(10)]
	count=1
	while(True):
		flag=0
		temp=count*n
		st = str(temp)
		for i in st:
			#print(st[i],end=" ")
			arr[int(i)]=1
		for i in range(0,10):
			if(arr[i]==0):
				flag=1
				break
		if(flag==0):
			break
		count+=1
	print("Case #"+str(case)+": "+str(count*n))
	case+=1

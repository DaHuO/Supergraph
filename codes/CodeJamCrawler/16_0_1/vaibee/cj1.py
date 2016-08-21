with open("ip.txt","r") as fo:
	t=fo.readline()
	p=1
	with open("op.txt","a") as output:
		for line in fo.read().split():
			num= int(line)
			arr=[]
			j=1
			n=num*j
			if num==0:
				output.write("Case #%d: INSOMNIA\n"%p)
			else:
				while(len(arr)<10):
					n=str(n)
					for i in n:
						if i not in arr:
							arr.append(i)
					k=0
					while(k<=9):
						if k in arr:
							k=k+1
						else:
							n=num*j
							j=j+1
							break
				output.write("Case #%d: %d\n" %(p,n-num))
			p=p+1





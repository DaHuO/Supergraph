n=input()
for i in range(n):
	x=input()
	print "Case #%s:"%(i+1),
	if x==0:
		print 'INSOMNIA'
	else:
		visit = [0] * 10
		j=1	
		while True:
			value = j*x
			value = str(value)
			for m in range(len(value)):
				visit[int(value[m])]=1
			flag=1
			for y in range(10):
				if(visit[y]==0):
					flag=0
					break
			if flag==1:
				print int(value)
				break
			j=j+1


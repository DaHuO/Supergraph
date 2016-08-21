n = int(raw_input())
abc = 0
for i in range(n):
	abc+=1
	r = int(raw_input())
	if(r==0):
		print("Case #"+str(abc)+": ""INSOMNIA")
	else:
		d = [0 for i in range(10)]
		visited = 0
		k = 0
		count = 1
		while(k==0):
			temp = r*count
			while(temp!=0):
				if(d[temp%10]==0):
					d[temp%10]=1
					visited+=1
					if(visited==10):
						k=1
						break
				temp/=10
			count+=1
		print("Case #"+str(abc)+": "+str(r*(count-1)))


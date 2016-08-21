
d= dict()
def check():
	count=0
	for i in d.keys():
		if d[i]==1:
			count+=1
	if count==10:
		return 1
	else:
		return 0



n = int(input())
x = list()
for i in range(n):
	x.append(int(input()))


index = 1
for i in x:
	if i==0:
		print("Case #" +str(index)+": INSOMNIA")
		index+=1
		continue
	flag1=0
	p=1
	for j in range(11):
		d[j]=0
	
	#print("soome")
	while 1:
		#print(" while")
		flag=0
		s = str(p*i)
		for j in s:
			k = int(j)
			if d[k]==0:
				d[k]=1
				if check():
					flag=1
					print("Case #" +str(index)+":" , int(s))
					break
		if flag==1:
			break
		p+=1
	index+=1

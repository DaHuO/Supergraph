def sleepsheep(j,b,count):
	if j=='':
		quit()
		
	elif int(j)==0:

		return("INSOMNIA")
	else:
		for k in range(0, len(j)):
			if j[k] not in b:
				b.append(int(j[k]))
			

		c=True
		for l in range(10):
			if l not in b:
				c=False
				break
				

		if c==True:
			return(j)
		else:
			count=count+1
			j=str(round(int(j)*(count/(count-1))))
			#print('count', count, 'j', j)
			return(sleepsheep(j,b,count))

f=open('A-large.in','r')
g=open('codejam1.txt','w')

x='sheep'
count2=1
simple=f.readline()
while x!='':
	num=f.readline()
	q=''
	for s in range(len(num)-1):
		q=q+num[s]
	
	num=q
	b=[]
	count=1
	ans=sleepsheep(num,b,count)
	ans2='Case #{0}: {1}'.format(count2,ans)
	g.write(ans2)
	g.write('\n')
	x=num
	count2+=1

f.close()
g.close()

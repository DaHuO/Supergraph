f=open("input.txt")
t=int(f.readline())
f2 = open('out.txt', 'w')

for i in range(t):
	n=int(f.readline())
	if n==0:
		f2.write("Case #"+str(i+1)+": "+"INSOMNIA"+"\n")
	else:
		j=1
		d={}
		m=0
		while(True):
			m=n*j
			s = str(m)
			for k in s:
				try:
					d[k]+=1
				except:
					d[k]=1
			if len(d)==10:
				break
			j+=1
		f2.write("Case #"+str(i+1)+": "+str(m)+"\n")
f.close()
f2.close()
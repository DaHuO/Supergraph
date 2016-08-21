file_in=open("A-large.in")
file_out=open("A-lar.out",'w')

T=int(file_in.readline())
print T
for t in range(1,T+1):
	go=1
	num=1
	cur=set([])
	i=int(file_in.readline())
	while(go==1):
		if(i==0):
			file_out.write("Case #"+str(t)+": INSOMNIA\n")
			break
		x=i*num
		x=set(str(x))
		cur=cur|x
		#print cur
		if len(cur)==10:
			file_out.write("Case #"+str(t)+": "+str(i*num)+'\n')
			break

		num=num+1
file_out.close()
file_in.close()

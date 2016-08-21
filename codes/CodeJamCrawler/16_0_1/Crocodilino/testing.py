fr = open('/home/rafail/Desktop/input1.in', 'r')
fw = open ('/home/rafail/Desktop/output1.out', 'w')

t=fr.readline().rstrip()


count=1

for i in range(int(t)):
	times=[0,0,0,0,0,0,0,0,0,0]
	check=1
	n=int(fr.readline().rstrip())
	N=n
	if (n == 0):
			fw.write("Case #"+str(count)+": " + "INSOMNIA\n")
			count+=1
	else:		
		while(check==1):
			
			l=map(int,str(int(N)))
			for j in l:
				if (times[int(j)]==0):
					times[int(j)]=1
					
			if (sum(times)==10):
				check=0
				fw.write("Case #"+str(count)+": " + str(N) + "\n")
				count+=1
			N+=n
fw.close()
fr.close()
				
		
		

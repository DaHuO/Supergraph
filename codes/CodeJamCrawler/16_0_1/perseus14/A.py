T=input()
for _ in xrange(T):
	N=input()
	Z=['0','1','2','3','4','5','6','7','8','9']
	i=1
	num=N
	print "Case #%d: "%(_+1),
	while(True):
		if(num==0):
			print "INSOMNIA"
			break;
		else:
			for x in str(num):
				try:
					Z.remove(x)	
				except:
					continue;
			if(Z==[]):
				print num
				break;
			i+=1
			num=i*N
			

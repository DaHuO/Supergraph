t = range(int(raw_input()))
for i in t:
	a = [0,0,0,0,0,0,0,0,0,0];
	s = raw_input()
	ss = s
	if(int(s)==0):
		print "Case #"+str(i+1)+": "+"INSOMNIA"
	else:
		mult = 1
		sum = 0
		while(sum!=10):
			s = str(int(ss)*mult)
			for x in s:
				if(a[int(x)]==0):
					##print s,"(",mult,") ",x
					a[int(x)]=1
					sum+=1

			if(sum==10):
				print "Case #"+str(i+1)+": "+s
				mult = 0
			mult+=1
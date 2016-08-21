for k in xrange(int(raw_input())):
	s = raw_input()
	dict={'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0,'0':0}
	count=0	
	if int(s)==0:
		print 'Case #'+str(k+1)+':','INSOMNIA'
		#iter+=1
	else:
		i=1
		while 1 :
			num=i*int(s)
			for j in str(num):
				if dict[j] ==0:
					dict[j]=1
					count+=1	
				else:	
					pass
			if count==10:
				break
			else:
				i+=1
		print 'Case #'+str(k+1)+':',num

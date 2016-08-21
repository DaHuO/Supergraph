test=int(input());

def retrive (i):
	if i==0:
		#global s;
		#s.add(0);
		return 0;
	else:
		global s;
		#l=[];
		#l.append(i%10);
		s.add(i%10);
		i=int(i/10);
		return retrive(i);

org={0,1,2,3,4,5,6,7,8,9}	
j=1;	
while test:
	
	s=set();
	n=int(input());
	i=1;
	while s!=org and i!=1000000:
		(retrive(i*n))
		i+=1;
	s.add(0);
	if  i!=1000000:
		print("Case #"+str(j)+": "+str((i-1)*n));


	else:
		print("Case #"+str(j)+": ""INSOMNIA");
	j+=1;
	test-=1;

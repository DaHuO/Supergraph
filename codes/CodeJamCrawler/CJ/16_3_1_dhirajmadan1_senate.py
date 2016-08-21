T=input();
P=[[]]*T;
def computeMaxIndex(l):
	max1=l[0];
	ind=0;
	#max2=l[1];
	#if(max2>max1):
	#	max2=max1;
	#	ind1=1;
	#	ind2=0;
	#else:
	#	ind1=0;
	#	ind2=1;	
	for i in range(1,len(l)):
		if(l[i]>max1):
		#	max2=max1;
		#	ind2=ind1;
			max1=l[i];
			ind=i;
	l[ind]-=1;
	return ind;

def ctr(l):
	ret=[];
	for i in range(len(l)):
		if(l[i]>0):
			while(l[i]):
				ret.append(i);
				l[i]-=1;
	return ret;			







for i in range(T):
	N=input();
	P[i]=map(lambda x:int(x),raw_input().split());

for i in range(T):
	print("case #"+str(i+1)+":"),
	cursum=sum(P[i]);
	while(cursum>3):
		ind1=computeMaxIndex(P[i]);
		ind2=computeMaxIndex(P[i]);
		cursum-=2;
		print(chr(97+ind1)+chr(97+ind2)),
	ret=ctr(P[i]);
	if(len(ret)==3):
		if(not(ret[0]==ret[1]) and (not(ret[1]==ret[2]))):
			print(chr(97+ret[0])),
			print(chr(97+ret[1])+chr(97+ret[2])),
		elif(ret[0]==ret[1]):
			print(chr(97+ret[0])),
			print(chr(97+ret[1])+chr(97+ret[2])),
		else:
			print(chr(97+ret[2])),
			print(chr(97+ret[1])+chr(97+ret[0])),
	else:#len(ret)==2
		print(chr(97+ret[1])+chr(97+ret[0])),
				
	print('');
		













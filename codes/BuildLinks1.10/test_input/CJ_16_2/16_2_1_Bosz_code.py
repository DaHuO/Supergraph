T =int(input())
digit = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]

def delS(s,p):
	for c in p:
		s=s.replace(c,'',1)
	return s
		
	


for case in range(1,T+1):
	s = raw_input()
	count={}
	for i in range(0,10):
		count[i]=0
	s2= s[:]
	cz=0;cw=0;cu=0;cx=0;cg=0
	for c in s:
		if(c=='Z'):
			count[0]+=1
			s2=delS(s2,'ZERO')
		elif(c=='W'):
			count[2]+=1
			s2=delS(s2,'TWO')
		elif(c=='U'):
			count[4]+=1
			s2=delS(s2,'FOUR')
		elif(c=='X'):
			count[6]+=1
			s2=delS(s2,'SIX')
		elif(c=='G'):
			count[8]+=1
			s2=delS(s2,'EIGHT')
	s3=s2[:]
	for c in s2:
		if(c=='O'):
			count[1]+=1
			s3=delS(s3,'ONE')
		if(c=='T'):
			count[3]+=1
			s3=delS(s3,'THREE')
		if(c=='F'):
			count[5]+=1
			s3=delS(s3,'FIVE')
		if(c=='S'):
			count[7]+=1
			s3=delS(s3,'SEVEN')

	s4=s3[:]
	for c in s3:
		if(c=='I'):
			count[9]+=1
			s4=delS(s4,'NINE')
	ans=''
	for i in range(0,10):
		for j in range(count[i]):
			ans+=str(i)
	print 'Case #{}: {}'.format(case,ans)
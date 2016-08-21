from math import sqrt
k=(1<<31)+1

def chkprime(temp):
	if(temp%6==1 or temp%6==5):
		return 0;
	else:
		return 1
def two():
	if(chkprime(k)==0):
		return 0;
	else:
		return 1
		
def three():
	temp=0
	for i in range(32):
		if((k>>i)&1!=0):
			temp=temp+3**i	
	
	if(chkprime(temp)==0):
		return 0;
	else:
		return 1
def four():
	temp=0
	for i in range(32):
		if((k>>i)&1!=0):
			temp=temp+4**i	
	
	if(chkprime(temp)==0):
		return 0;
	else:
		return 1

def five():
	temp=0
	for i in range(32):
		if((k>>i)&1!=0):
			temp=temp+5**i	
	
	if(chkprime(temp)==0):
		return 0;
	else:
		return 1
def six():
	temp=0
	for i in range(32):
		if((k>>i)&1!=0):
			temp=temp+6**i	
	#print temp
	if(temp%6 ==5):
		return 0;
	else:
		return 1
def seven():
	temp=0
	for i in range(32):
		if((k>>i)&1!=0):
			temp=temp+7**i	
	
	if(chkprime(temp)==0):
		return 0;
	else:
		return 1

def eight():
	temp=0
	for i in range(32):
		if((k>>i)&1!=0):
			temp=temp+8**i
		#	print temp	
	#print temp
	if(chkprime(temp)==0):
		return 0;
	else:
		return 1

def nine():
	temp=0
	for i in range(32):
		if((k>>i)&1!=0):
			temp=temp+9**i	
	
	if(chkprime(temp)==0):
		return 0;
	else:
		return 1

def ten():
	temp=0
	for i in range(32):
		if((k>>i)&1!=0):
			temp=temp+10**i	
	
	if(chkprime(temp)==0):
		return 0;
	else:
		return 1
def ppten():
	temp=0
	for i in range(32):
		if((k>>i)&1!=0):
			temp=temp+10**i
	print temp,
	
cnt=0
def fact(num):
	gg=int(sqrt(num))
	
	i=2;
	while i<gg:
		i=i+1
		if num%i==0:
			print i,
			return
	print "-1"
		

def ppfacts():
	fact(k)
	
	temp=0
	for i in range(32):
		if((k>>i)&1!=0):
			temp=temp+3**i
	fact(temp)
	
	temp=0
	for i in range(32):
		if((k>>i)&1!=0):
			temp=temp+4**i
	fact(temp)
			
	temp=0
	for i in range(32):
		if((k>>i)&1!=0):
			temp=temp+5**i
	fact(temp)
	
	temp=0
	for i in range(32):
		if((k>>i)&1!=0):
			temp=temp+6**i
	fact(temp)
	
	temp=0
	for i in range(32):
		if((k>>i)&1!=0):
			temp=temp+7**i
	fact(temp)
	
	temp=0
	for i in range(32):
		if((k>>i)&1!=0):
			temp=temp+8**i
	fact(temp)
	
	temp=0
	for i in range(32):
		if((k>>i)&1!=0):
			temp=temp+9**i
	fact(temp)

	temp=0
	for i in range(32):
		if((k>>i)&1!=0):
			temp=temp+10**i
	fact(temp)
print "Case #1:"
while cnt<500:
	#print six()
	if(two()==1 and three()==1 and four()==1 and five()==1 and six()==1 and seven()==1 and eight()==1 and nine()==1 and ten()==1):
		ppten()
		ppfacts()
		print " "
		cnt=cnt+1
	k=k+2




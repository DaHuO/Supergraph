test=input()
w=test

def flip(order,indd):
	i=0
	while (i<=indd):
		if(order[i]=='-'):
			order[i]="+"
		else:
			order[i]="-"
		i+=1

def find_indd(order):
	ind =0
	indd=0
	for i in order:
		if (i=='-'):
			indd=ind
		ind+=1
	return indd	
while test:
	order=raw_input()
	order=list(order)
	
	m=list(set(order))
	number =0
	while m!=['+']:
			
			ad=find_indd(order)
			flip(order,ad)
			m=list(set(order))
			number+=1
	print "Case #"+str(w-test + 1)+":",number
	test-=1

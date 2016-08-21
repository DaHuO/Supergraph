'''
	1st if: only one just flip
	2nd elif: all -- but only one + at last
	3rd else
		flip
		get index of last occurance of first
		flip the bits till that occurance
		

'''
def flip(end):
	global l;
	i=0;
	while end:
		if l[i]=='+':
			l[i]='-'
		else:
			l[i]='+'
		i+=1;
		end-=1;			
test=int(input())
j=1;
while test:
	ip=(input())
	tt=len(ip)
	l=[]
	check_p=[]
	check_m=[]
	r_val=0;
	while tt:
		check_p.append('+');
		check_m.append('-');
		
		tt-=1;
	l=list(ip);
	'''
	if len(ip)==1:
		if ip=='-':
			flip(len(ip)-1)
		r_val+=1
	elif l.index('+')==len(l)-1:
		flip(len(ip)-2)	
	'''

	if check_m==l:
		r_val=1
	elif l.index('+')==len(l)-1 and check_p!=l:
		r_val+=1
	
	else:
		while check_p!=l:
			r_val+=1;
			
			k=l.copy();
			k.reverse();
			kk=k.index('-');
			temp=len(k)-kk;
		#	print(l)
			flip(temp)
	print("Case #"+str(j)+": "+str(r_val));
	j+=1;
	test-=1

from math import sqrt;
a = int(input());
inputs = 0;
def check(a,disp):
	iterator = 0;
	flag = 0;
	factors = [];
	factors.append(disp);
	while (iterator<len(a)):
		factor = 2;		
		flag = 0;
		while(factor<=int(sqrt(a[iterator]))):
			if(a[iterator]%factor == 0):
				flag = 1;
				factors.append(factor);
				break;
			if(factor>2):
				factor+=2;
			else:
				factor+=1;
		if(flag==0):
			return 0;
		iterator+=1;
	for element in factors:
		print(element,end=" ");
	return 1;
while(inputs<a):	
	b = input().split();
	N = int(b[0]);
	J = int(b[1]);
	i = 0;
	print("Case #"+str(inputs+1)+":");
	start = pow(2,N-1)+1;
	while(start<pow(2,N)):
		bi = int(bin(start)[2:]);
		disp = bi;
		base = [0,0,0,0,0,0,0,0,0];
		temp = 0;
		while(bi>0):
			pos = 0;
			while(pos<len(base)):
				base[pos]+=(bi%10)*pow(pos+2,temp);
				pos+=1;
			temp+=1;
			bi = int(bi/10);
		if(check(base,disp)):
			i+=1;
			if(i<J):
				print("");			
		if(i==J):
			break;
		start+=2;
	a-=1;
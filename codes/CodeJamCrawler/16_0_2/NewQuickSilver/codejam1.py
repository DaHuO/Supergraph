a = int(input());
i = 0;
flag = 0;
count = 0;
while(i<a):
	ip = input();
	j = 0;
	count =0;
	while(j<len(ip)):
		flag = 0;
		if(j<len(ip)):
			while(ip[j]=='+'):
				j+=1;
				flag = 1;
				if(j==len(ip)):
					count-=1;
					break;				
		if(flag == 1):
			count+=1;
		if(j<len(ip)):
			while(ip[j] == '-'):
				j+=1;								
				flag = 2;
				if(j == len(ip)):
					count+=1;
					flag = 0;
					break;
		if(flag == 2):
			count+=1;
	print("Case #"+str(i+1)+": "+str(count));
	i+=1;

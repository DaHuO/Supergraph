T = input();
tempT = T;
result = [];
while(T!=0):
	n = input();
	i = 1;
	List = [];
	while(1):
		k = i*n;
		if(k == 0):
			break;	
		while(k):
			r = k%10;
			if(r not in List):
				List.append(r);
			k = k/10;
		if(len(List) == 10):
			break;
		i = i+1;
	if(i*n == 0):
		result.append("INSOMNIA");
	else:
		result.append(i*n);
	T=T-1

i=0
while(i<tempT):   
    print "case #"+str(i+1)+":",result[i]
    i = i+1
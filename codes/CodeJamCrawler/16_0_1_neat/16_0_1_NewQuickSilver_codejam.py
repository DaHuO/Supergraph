a = int(input());
i = 0;
while(i<a):
	num = set([]);
	n = int(input());
	j = 1;
	while(len(num)<10 and n > 0):
		b = n * j;
		while(b>0):
			num.add(b%10);
			b = int(b/10);
		j+=1;
	if(n>0):
		print("Case #"+str(i+1)+": "+str(n*(j-1)));
	else:
		print("Case #"+str(i+1)+": INSOMNIA");
	i+=1;
n = int(input());
i = 0;
while(i<n):
	ip = input().split(" ");
	k = int(ip[0]);
	c = int(ip[1]);
	s = int(ip[2]);
	print("Case #"+str(i+1)+": ",end = "");
	if(s<k):
		print("IMPOSSIBLE");
	else:
		j = 0
		while(j<k):
			print(j+1,end = " ");
			j+=1;
		print("")
	i+=1;
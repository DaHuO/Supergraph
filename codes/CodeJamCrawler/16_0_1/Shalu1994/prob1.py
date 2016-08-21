file = open('A-large.in', 'r')
ip=file.readlines()

T=int(ip[0])
k=1
while k<=T:
	N=int(ip[k])
	seen_num=[]
	first=N
	first=str(first)
	dump=list(first)
	for i in dump:
		if (i not in seen_num):
			seen_num.append(i)
	i=2;
	while (N != (N*i)):
		#print i, seen_num
		if (len(seen_num) != 10):
			first=N*i
			first=str(first)
			dump=list(first)
			for j in dump:
				if (j not in seen_num):
					seen_num.append(j)
			i=i+1;
		else:
			break;
	if (len(seen_num)==10):
		print "Case #"+str(k)+":",N*(i-1)
	else:
		print "Case #"+str(k)+":","INSOMNIA"
	k+=1

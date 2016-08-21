import sys
for t in range(input()):
	a = input()
	l = []
	flag =True
	p = list(str(a).strip())
	for x in p:
		if x not in l:
			l.append(x)
	i=2
	while(len(l) != 10):
		if(a==0):
			print "Case ",
			sys.stdout.write("#"),
			print t+1,
			sys.stdout.write(":"),
			print "","INSOMNIA"
			flag = False
			break
		b = a*i
		k = list(str(b).strip())
		for j in k:
			if j not in l:
				l.append(j)
		i += 1
	if(flag == True):
		print "Case ",
		sys.stdout.write("#"),
		print t+1,
		sys.stdout.write(":"),
		print "",b


	

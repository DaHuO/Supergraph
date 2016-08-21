for i in range(input()):
	d={}
	t=n=input()
	print 'Case #'+str(i+1)+':',
	if n==0:
		print 'INSOMNIA'
	else:
		no=0
		while no<10:
			for dig in str(n):
				if dig not in d:
					d[dig]=1
					no+=1
			n+=t
		print n-t
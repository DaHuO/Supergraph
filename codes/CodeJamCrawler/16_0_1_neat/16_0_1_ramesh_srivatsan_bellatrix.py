t = int(raw_input())
for i in range(t):
	a = set([])
	x = int(raw_input())
	if x==0:
		print('Case #'+str(i+1)+': INSOMNIA')
	k=1
	n = x
	while n!=0:
		s = str(n)
		a = a | set(s)
		if len(a)==10:
			print('Case #'+str(i+1)+': '+ str(n))
			k=-1
		k+=1
		n=x*k

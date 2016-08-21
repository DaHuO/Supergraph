fo = open("foo.txt", "wb")
t = input()
f = 1
while t:
	n = input()
	l = set()
	i = 2
	if n == 0:
		print 'INSOMNIA'
		fo.write('Case #'+str(f) + ': INSOMNIA\n');
	ans = 0
	j = n
	if n != 0:
		while(len(l)!=10):
			k = n
			while (k!=0):
				a = k%10
				l.add(a)
				k= k/10
			if(len(l)==10):
				ans = n
			n = i*j;
			i += 1
		print ans
		fo.write('Case #'+str(f) + ': '+str(ans)+'\n');
	t = t-1	
	f = f+1
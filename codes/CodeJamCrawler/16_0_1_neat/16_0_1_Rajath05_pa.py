fo = open("biga.in" , "r")
fo1=open("output.txt" , "w")
i = int(fo.readline())
n = 1
while True:
	m = int(fo.readline())
	fo1.write("Case #")
	fo1.write('%s'%n)
	fo1.write(": ")
	if m == 0:
		fo1.write("INSOMNIA\n")
		n=n+1
		continue
	a = { }
	k = 1
	while 1:
		c = 0
		t = m*k;
		temp = t 
		while t != 0:
			rem = t%10
			a[rem] = 1
			t = t/10;
		c = len(a)
		if c==10:
			break
		k = k+1
	fo1.write('%s'%temp)
	fo1.write('\n')
	n=n+1
	i=i-1
fo.close()
fo1.close()
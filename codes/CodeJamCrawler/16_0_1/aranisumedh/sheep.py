tc = int(input())
i=1
while tc:
	num =input()
	tnum = int(num)
	inum = int(num)
	digs = set(' '.join(num).split())
	if num!='0':
		while len(digs)!=10:
			inum = inum+tnum
			num=str(inum)
			temp = set(' '.join(num).split())
			digs= digs|temp
		print("Case #"+str(i)+": "+num)
	else:
		print("Case #"+str(i)+": "+"INSOMNIA")
	tc=tc-1
	i=i+1
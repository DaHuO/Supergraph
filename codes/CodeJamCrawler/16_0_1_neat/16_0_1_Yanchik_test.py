file = open('A-large.in', 'r')
t = file.readline()
t = int(t)
print(t)
digits=[0,1,2,3,4,5,6,7,8,9]
mydigits=[]
f = open('workfile.txt', 'w')
i = 1
for i in range(t):
	flag = True
	n = file.readline()
	print(i, n)
	n = int(n)
	mydigits=[]
	j = 1
	if (n==0):
		f.write("Case #"+str((i+1))+": INSOMNIA"+"\n")
		continue
	while(flag):
		mul = n*j
		while(mul != 0):
			d = mul%10
			if d not in mydigits:
				mydigits.append(d)
			mul = mul//10

		mydigits.sort()
		if (mydigits==digits):
			f.write("Case #"+str((i+1))+": "+str(n*(j))+"\n")
			flag = False
		j+=1


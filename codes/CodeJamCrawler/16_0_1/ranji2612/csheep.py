def retNum2Sleep(n):
	h={}
	flag = False
	x = 0
	while(1):
		x += n
		if  flag and x==n:
			return "INSOMNIA"
		for i in str(x):
			h[i] = 1
		if len(h)==10:
			return str(x)
		flag = True

f = open('A-small-attempt0.in') #input.out')
s = f.readlines()
f.close()

f = open('output.out','w')

t = s[0]
ipList = s[1:]

for i in range(int(t)):
	res = retNum2Sleep(int(ipList[i][:-1]))
	f.write('Case #'+str(i+1)+': '+str(res)+'\n')


f = open('test.txt','r')
a = open('ans.txt','w')
for i in range(1,int(f.readline())+1):
	c = 1
	digit = set()
	num = int(f.readline())
	while(num!=0):
		digit = digit | set(list(str(num*c)))
		if len(digit)==10:
			break
		c+=1
	if num==0:
		a.write('Case #%d: INSOMNIA\n'%(i))
	else:
		a.write('Case #%d: %d\n'%(i,num*c))


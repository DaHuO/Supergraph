
num = [0,1,2,3,4,5,6,7,8,9]


def rem(n):
	s = str(n)
	for sd in s:
		d = int(sd)
		if d in num:
			num.remove(d)
	if not num:
		return n
	else:
		return 0

def outrem(n):
	inop = rem(n)
	ind = 1
	while inop==0:
		inop = rem(n*ind)
		ind+=1
	return inop


ob = open('A-large.in','r')
wob = open('output.txt','w')
t = int(ob.readline())
for i in range(1,t+1):
	num = [0,1,2,3,4,5,6,7,8,9]
	n = int(ob.readline())
	if n<1:
		wob.write("Case #"+str(i)+": INSOMNIA\n")
	else:
		op = outrem(n)
		wob.write("Case #"+str(i)+": "+str(op)+"\n")
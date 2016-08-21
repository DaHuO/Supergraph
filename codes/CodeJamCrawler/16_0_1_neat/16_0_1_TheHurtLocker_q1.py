from sets import Set
a=Set()
def check():
	for i in range(10):
		if str(i) not in a:
			return False
	return True
def fun(s):
	k=str(s)
	for i in range(len(k)):
		a.add(k[i])
t=int(raw_input())
for xx in range(1,(t+1)):
	a.clear()
	n=int(raw_input())
	if n==0:
		print "Case #%d: INSOMNIA" %xx
	else:
		i=1
		while(check()==False):
			fun(n*i)
			#print a
			i+=1
		print "Case #%d: %d" %(xx,n*(i-1))
from random import randint

T=input()


for t in range(0,T):
	n=input()
	if n==0:
		print "Case #%d: INSOMNIA" % (t+1)
	else:
		i=0
		s=set([])
		while True:
			i+=1
			s|=set(str(n*i))
			if s==set(list('0123456789')):
				break
		
		print "Case #%d: %d" % (t+1,n*i)

def res(m,n):
	if n==0:
		print 'Case #'+str(m)+':'+' INSOMNIA'
		return
	d={}	
	for i in range(10):
		d[str(i)]=0
	s=0
	c=0
	while True:
		s=s+n
		st=str(s)
		for num in st:
			if not d.get(num):
				d[num]=1
				c+=1
				if c==10:
					print 'Case #'+str(m)+': '+st
					return

def main():
	t=int(raw_input())
	for i in range(1,t+1):
		n=int(raw_input())
		res(i,n)

main()		



import sys
if __name__ == '__main__':
	t=int(sys.stdin.readline())
	i=1
	while i<=t:
		ans=0
		line=sys.stdin.readline()
		n=int(line)
		if n is 0:
			print 'Case #%d: INSOMNIA'%(i)
			i+=1
			continue
		j=n
		d={}
		ins=False
		while len(d)<10:
			for s in str(j):
				d[s]=True
			j+=n
			# if j>2e8:
				# ins=True
				# break
		ans=j-n
		if ins is True:
			print 'Case #%d: INSOMNIA'%(i)
		else:
			print 'Case #%d: %d'%(i,ans)
		i+=1

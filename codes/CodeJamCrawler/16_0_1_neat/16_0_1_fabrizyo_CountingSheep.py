T=int(input())

for t in range(1,T+1):
	N=int(input())
	seen=set()
	count=0
	while N!=0 and len(seen)<10:
		count+=1
		n=count*N
		s=str(n)
		for c in s:
			seen.add(c)
	res="INSOMNIA" if len(seen)<10 else str(count*N)
	print("Case #%s: %s"%(t,res))
T=int(input())

for t in range(1,T+1):
	s=input()
	l=list(s)
	res=0
	while '-' in l:
		end=0
		curr=l[end]
		while end+1<len(l) and l[end+1]==l[end]:
			end+=1
		#reverse
		l[0:end+1]='+'*(end+1) if curr=='-' else  '-'*(end+1)
		res+=1
	print("Case #%s: %s"%(t,res))
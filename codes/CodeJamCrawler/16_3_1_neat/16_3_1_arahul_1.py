t=int(raw_input())
ans=""
case=0
for _ in range(t):
	case+=1
	n=int(raw_input())
	l=list(map(int, raw_input().split()))
	total=0
	ansl="Case #"+str(case)+": "
	for i in range(len(l)):
		total+=l[i]
	while(total>0):
		mx=max(l)
		ind=-1
		for i in range(n):
			if l[i]==mx:
				l[i]-=1
				total-=1
				ind=i
				break
		mx=max(l)
		ansl=ansl+chr(65+ind)
		for i in range(n):
			if l[i]==mx:
				if 2*l[i]>total:
					ansl=ansl+chr(65+i)+" "
					l[i]-=1
					total-=1
				else:
					ansl=ansl+" "
				break
	ans=ans+ansl+"\n"
print ans

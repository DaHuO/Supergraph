t=int(raw_input())
jj=1
while t>0:
    k,c,s=[int(x) for x in raw_input().split()]
    r=0
    p=pow(k,c)
    o=[]
    for i in range(k/2):
        o.append(i+1)
        o.append(p-i)
    if k%2==1:    
        o.append((k/2)+1)
    r=""
    for i in o:
        r+=str(i)+" "
    if k==1:
        r="1 "
    print("Case #"+str(jj)+": "+r[:-1])
    jj+=1
    t-=1

"""
def abc(n,m):
	s=[]
	pp=0
	for i in range(2**n):
		p=""
		x=i
		for j in range(n):
			if x%2==0:
				p+="G"
			else:
				p+="L"
			x=x/2
		q=""
		l=p
		#print(p)
		for k in range(m-1):
			q=""
			for j in p:
				if j=="L":
					q+=l
				else:
					q+=("G"*n)
			p=q
		o=[]
		for i in range(n/2):
			o.append(i+1)
			o.append(len(p)-i-2)
		r=0
		for i in o:
			if p[i]=="G":
				r=1
		if r==1:
			qq=1
		else:
			pp+=1
	print(o)
	if pp==1:
		print("Yes")
"""	

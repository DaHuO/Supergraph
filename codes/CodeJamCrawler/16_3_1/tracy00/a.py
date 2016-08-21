tc=int(raw_input())
for i in range(tc):
	p=[]
	alpha=[]
	tp=0
	n=int(raw_input())
	
	pp=raw_input().split()
	for j in range(n):
		pp[j]=int(pp[j])
	
	while 1:
		
		jj= pp.index(max(pp))
		
		if  max(pp)==0:
			break
		t=max(pp)
		
		b = [int(l != 0) for l in pp]
		
		if b.count(1)==2:
			if jj==0:
				alpha.append("A")
			if jj==1:
				alpha.append("B")
			if jj==2:
				alpha.append("C")	
			pp[jj]=pp[jj]-1
			k=max(pp)
			
			kk= pp.index(max(pp))
			if k==t:
				if kk==0:
					alpha.append("A")
				if kk==1:
					alpha.append("B")
				if kk==2:
					alpha.append("C")	
				pp[kk]=pp[kk]-1
			alpha.append(" ")
			
			continue
			
		
		
		
		if jj==0:
			alpha.append("A")
		if jj==1:
			alpha.append("B")
		if jj==2:
			alpha.append("C")
		alpha.append(" ")
		pp[jj]=pp[jj]-1
		if  max(pp)<=0:
			break
		
		
		
			
	alpha=''.join(alpha)	
	print "Case #%d: %s" %(i+1,alpha)
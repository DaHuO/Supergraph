def flipnum(pan):
	plen=len(pan)
	if plen==1:
		if pan[0]==1:
			return 0
		else:
			return 1
	else:
		p=plen-1
		while p>=0 and pan[p]==1:
			p=p-1
		if p<0:
			return 0
		elif p==0:
			return 1
		else:
			for i in range(p):
				pan[i]=1-pan[i]
			return flipnum(pan[:p])+1
def pancake(inputfile,outputfile):
	with open(inputfile,'r') as f:
		T=int(f.readline())
		print(T)
		case=[]
		for i in range(T):
			s=f.readline()
			case.append([])
			for ch in s:
				if ch=='+':
					case[i].append(1)
				elif ch=='-':
					case[i].append(0)
	print(case[i])
	print('Data reading finished.')
	f=open(outputfile,'w')
	for i in range(T):
		pan=case[i]
		result=flipnum(pan)
		s='Case #'+str(i+1)+': '+str(result)+'\n'
		f.write(s)
		print(s)
	f.close
	return

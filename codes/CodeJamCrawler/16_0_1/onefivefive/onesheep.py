nputfile,outputfile):
	with open(inputfile,'r') as f:
		T=int(f.readline())
		print(T)
		N=[]
		for i in range(T):
			N.append(int(f.readline()))
			print(N[i])
		print('data read finished.')
		result=[]
		for i in range(T):
			if N[i]==0:
				s='Case #'+str(i+1)+': '+'INSOMNIA'+'\n'
				result.append(s)
				print(s)
				continue
			miss={j for j in range(10)}
			msn=10
			x=0
			while msn>0:
				x=x+N[i]
				d=x
				while d>0:
					if d%10 in miss:
						miss=miss-{d%10}
						msn=msn-1
					d=d//10
			s='Case #'+str(i+1)+': '+str(x)+'\n'
			result.append(s)
			print(s)
		f=open(outputfile,'w')
		for i in range(T):
			f.write(result[i])
		f.close
		return


with open('A-small.in','r') as f:
	t=int(f.readline())
	
	for i in range(t):
		st=f.readline()
		st.rstrip()
		d=dict()
		l=list()
		for j in range(len(st)):
			d[st[j]]=d.get(st[j],0)+1
		while d.get('Z',0)>0:
			l.append(0)
			d['Z']=d.get('Z',0)-1
			d['E']=d.get('E',0)-1
			d['R']=d.get('R',0)-1
			d['O']=d.get('O',0)-1
		while d.get('W',0)>0:
			l.append(2)
			d['W']=d.get('W',0)-1
			d['T']=d.get('T',0)-1
			d['O']=d.get('O',0)-1
		while d.get('U',0)>0:
			l.append(4)
			d['F']=d['F']-1
			d['O']-=1
			d['U']-=1
			d['R']-=1
		while d.get('X',0)>0:
			l.append(6)
			d['S']-=1
			d['I']-=1
			d['X']-=1
		while d.get('G',0)>0:
			l.append(8)
			d['E']-=1
			d['I']-=1
			d['G']-=1
			d['H']-=1
			d['T']-=1
		while d.get('T',0)>0:
			l.append(3)
			d['T']-=1
			d['H']-=1
			d['R']-=1
			d['E']-=2
		while d.get('F',0)>0:
			l.append(5)
			d['F']-=1
			d['I']-=1
			d['V']-=1
			d['E']-=1
		while d.get('S',0)>0:
			l.append(7)
			d['S']-=1
			d['E']-=2
			d['V']-=1
			d['N']-=1
		while d.get('I',0)>0:
			l.append(9)
			d['N']-=2
			d['I']-=1
			d['E']-=1
		while d.get('O',0)>0:
			l.append(1)
			d['O']-=1
			d['N']-=1
			d['E']-=1
		l.sort()
		print("Case #"+str(i+1)+": ",end="")
		for k in range(len(l)):
			print(l[k],end="")
		print()





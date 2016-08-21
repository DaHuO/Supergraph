t=int(raw_input())
case=0
for _ in range(t):
	case+=1
	ans=[]
	s=raw_input()
	dica=dict()
	for c in s:
		if c in dica.keys():
			dica[c]+=1
		else:
			dica[c]=1
	#Remove zero
	if 'Z' in dica.keys() and dica['Z']!=0:
		c=dica['Z']
		for i in range(c):
			ans.append(0)
		dica['Z']-=c
		dica['E']-=c
		dica['R']-=c
		dica['O']-=c
	#Remove two
	if 'W' in dica.keys() and dica['W']!=0:
		c=dica['W']
		for i in range(c):
			ans.append(2)
		dica['T']-=c
		dica['W']-=c
		dica['O']-=c
	#Remove four
	if 'U' in dica.keys() and dica['U']!=0:
		c=dica['U']
		for i in range(c):
			ans.append(4)
		dica['F']-=c
		dica['O']-=c
		dica['U']-=c
		dica['R']-=c
	#Remove six
	if 'X' in dica.keys() and dica['X']!=0:
		c=dica['X']
		for i in range(c):
			ans.append(6)
		dica['S']-=c
		dica['I']-=c
		dica['X']-=c
	#Remove eight
	if 'G' in dica.keys() and dica['G']!=0:
		c=dica['G']
		for i in range(c):
			ans.append(8)
		dica['E']-=c
		dica['I']-=c
		dica['G']-=c
		dica['H']-=c
		dica['T']-=c
	#Remove seven
	if 'S' in dica.keys() and dica['S']!=0:
		c=dica['S']
		for i in range(c):
			ans.append(7)
		dica['S']-=c
		dica['E']-=c
		dica['V']-=c
		dica['E']-=c
		dica['N']-=c
	#Remove Three
	if 'T' in dica.keys() and dica['T']!=0:
		c=dica['T']
		for i in range(c):
			ans.append(3)
		dica['T']-=c
		dica['H']-=c
		dica['R']-=c
		dica['E']-=c
		dica['E']-=c
	if 'V' in dica.keys() and dica['V']!=0:
		c=dica['V']
		for i in range(c):
			ans.append(5)
		dica['F']-=c
		dica['I']-=c
		dica['V']-=c	
		dica['E']-=c	
	#Remove One
	if 'O' in dica.keys() and dica['O']!=0:
		c=dica['O']
		for i in range(c):
			ans.append(1)
		dica['O']-=c
		dica['N']-=c
		dica['E']-=c
	#Remove nine
	#print dica
	if 'I' in dica.keys() and dica['I']!=0:
		c=dica['I']
		for i in range(c):
			ans.append(9)
		dica['N']-=c
		dica['I']-=c
		#dica['N']-=c
		dica['E']-=c
	ans.sort()
	s=""
	for i in range(len(ans)):
		s+=str(ans[i])
	print "Case #"+str(case)+": "+s	

for _ in range(int(input())):
	st=input()
	s=list(st)
	arr=[]
	dict2={'O':1,'R':3,'F':5,'S':7,'I':9}
	dict1={'Z':0,'W':2,'U':4,'X':6,'G':8}
	for i in dict1:
		while i in s:
			if i=='Z':
				s.remove('Z')
				s.remove('E')
				s.remove('R')
				s.remove('O')
				arr.append(dict1[i])
			elif i=='W':
				s.remove('T')
				s.remove('W')
				s.remove('O')
				arr.append(dict1[i])
			elif i=='U':
				s.remove('F')
				s.remove('O')
				s.remove('U')
				s.remove('R')
				arr.append(dict1[i])
			elif i=='X':
				s.remove('S')
				s.remove('I')
				s.remove('X')
				arr.append(dict1[i])
			elif i=='G':
				s.remove('E')
				s.remove('I')
				s.remove('G')
				s.remove('H')
				s.remove('T')
				arr.append(dict1[i])
	for i in dict2:
		while i in s:
			if i=='O':#1
				s.remove('O')
				s.remove('N')
				s.remove('E')
				arr.append(dict2[i])
			elif i=='R':#3
				s.remove('T')
				s.remove('H')
				s.remove('R')
				s.remove('E')
				s.remove('E')
				arr.append(dict2[i])
			elif i=='F':#5
				s.remove('F')
				s.remove('I')
				s.remove('V')
				s.remove('E')
				arr.append(dict2[i])
			elif i=='S':#7
				s.remove('S')
				s.remove('E')
				s.remove('V')
				s.remove('E')
				s.remove('N')
				arr.append(dict2[i])
			elif i=='I' and 'N' in s and 'E' in s:#9
				s.remove('N')
				s.remove('I')
				s.remove('N')
				s.remove('E')
				arr.append(dict2[i])
	tmp=''
	arr.sort()
	for i in arr:
		tmp+=str(i)
	print('Case #{}: {}'.format(_+1,tmp))
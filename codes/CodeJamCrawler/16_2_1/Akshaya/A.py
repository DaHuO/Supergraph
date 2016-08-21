def remove(s,c):
	i=s.index(c)
	return s[:i]+s[i+1:]


f = open('A.out','w')
fin = open('A.in','r')
t=int(fin.readline().strip())
for i in range(t):
	s=fin.readline().strip()
	
	num=""
	while ('Z' in s):
		s=remove(s,'Z')
		s=remove(s,'E')
		s=remove(s,'R')
		s=remove(s,'O')
		num=num+'0'

	while ('U' in s):
		s=remove(s,'F')
		s=remove(s,'O')
		s=remove(s,'R')
		s=remove(s,'U')
		num=num+'4'


	while ('G' in s):
		s=remove(s,'E')
		s=remove(s,'I')
		s=remove(s,'G')
		s=remove(s,'H')
		s=remove(s,'T')
		num=num+'8'


	while ('W' in s):
		s=remove(s,'T')
		s=remove(s,'W')
		s=remove(s,'O')
		
		num=num+'2'


	while ('X' in s):
		s=remove(s,'S')
		s=remove(s,'I')
		s=remove(s,'X')
		num=num+'6'


	while ('R' in s):
		s=remove(s,'T')
		s=remove(s,'H')
		s=remove(s,'R')
		s=remove(s,'E')
		s=remove(s,'E')
		num=num+'3'


	while ('F' in s):
		s=remove(s,'F')
		s=remove(s,'I')
		s=remove(s,'V')
		s=remove(s,'E')
		num=num+'5'


	while ('O' in s):
		s=remove(s,'O')
		s=remove(s,'N')
		s=remove(s,'E')
		
		num=num+'1'


	while ('V' in s):
		s=remove(s,'S')
		s=remove(s,'E')
		s=remove(s,'E')
		s=remove(s,'N')
		s=remove(s,'V')
		num=num+'7'

	while ('I' in s):
		s=remove(s,'I')
		s=remove(s,'N')
		s=remove(s,'E')
		s=remove(s,'N')
		num=num+'9'








	result = "Case #"+str(i+1)+": "+''.join(sorted(num))
	print result
	f.write(result+'\n')


fin.close()
f.close()

t=int(raw_input())
for i in range(t):
	
	str=raw_input()
	str=list(str)
	res=[]
	if 'Z' in str:
		cnt=int(str.count('Z'))
		for j in range(cnt):
			res.append('0')
			str.remove('O')
			#print str
	#print "Hey1"		
	if 'W' in str:
		#print "Hey2"
		cnt=int(str.count('W'))
		for j in range(cnt):
			res.append('2')
			str.remove('W')
			str.remove('T')
			str.remove('O')
			#print str

	if 'U' in str:
		cnt=int(str.count('U'))
		for j in range(cnt):
			res.append('4')
			str.remove('U')
			str.remove('O')
			str.remove('F')
			#print str

	if 'X' in str:
		cnt=int(str.count('X'))
		for j in range(cnt):
			res.append('6')
			str.remove('X')
			str.remove('I')
			#print str

	if 'G' in str:
		cnt=int(str.count('G'))
		for j in range(cnt):
			res.append('8')
			str.remove('I')
			
			str.remove('T')
			#print str

	if 'T' in str:
		cnt=int(str.count('T'))
		for j in range(cnt):
			res.append('3')
			
			#print str

	if 'O' in str:
		cnt=int(str.count('O'))
		for j in range(cnt):
			res.append('1')
			#print str

	if 'F' in str:
		cnt=int(str.count('F'))
		for j in range(cnt):
			res.append('5')
			str.remove('I')
			str.remove('V')
			#print str


	if 'V' in str:
		cnt=int(str.count('V'))
		for j in range(cnt):
			res.append('7')
			#print str	

	if 'I' in str:
		cnt=int(str.count('I'))
		for j in range(cnt):
			res.append('9')
			#print str	

	res.sort()
	#print res
	hel="".join(res)
	#print hel
	print "Case #%d: %s"%(i+1,hel)



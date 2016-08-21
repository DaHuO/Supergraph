for z in range(int(input())):
	a=list(input())
	d=[0]*26
	for i in a:
		d[ord(i)-ord('A')]+=1
	l=[]
	while d[ord('Z')-ord('A')]!=0:
		l.append(0)
		# print('0')
		d[ord('Z')-ord('A')]-=1
		d[ord('E')-ord('A')]-=1
		d[ord('R')-ord('A')]-=1
		d[ord('O')-ord('A')]-=1
	while d[ord('W')-ord('A')]!=0:
		l.append(2)
		# print('2')
		d[ord('T')-ord('A')]-=1
		d[ord('W')-ord('A')]-=1
		d[ord('O')-ord('A')]-=1
	while d[ord('U')-ord('A')]!=0:
		l.append(4)
		# print('4')
		d[ord('F')-ord('A')]-=1
		d[ord('O')-ord('A')]-=1
		d[ord('U')-ord('A')]-=1
		d[ord('R')-ord('A')]-=1
	while d[ord('X')-ord('A')]!=0:
		l.append(6)
		# print('6')
		d[ord('S')-ord('A')]-=1
		d[ord('I')-ord('A')]-=1
		d[ord('X')-ord('A')]-=1
	while d[ord('S')-ord('A')]!=0:
		l.append(7)
		# print('7')
		d[ord('S')-ord('A')]-=1
		d[ord('E')-ord('A')]-=1
		d[ord('V')-ord('A')]-=1
		d[ord('E')-ord('A')]-=1
		d[ord('N')-ord('A')]-=1
	while d[ord('G')-ord('A')]!=0:
		l.append(8)
		# print('8')
		d[ord('E')-ord('A')]-=1
		d[ord('I')-ord('A')]-=1
		d[ord('G')-ord('A')]-=1
		d[ord('H')-ord('A')]-=1
		d[ord('T')-ord('A')]-=1
	while d[ord('H')-ord('A')]!=0:
		l.append(3)
		# print('3')
		d[ord('T')-ord('A')]-=1
		d[ord('H')-ord('A')]-=1
		d[ord('R')-ord('A')]-=1
		d[ord('E')-ord('A')]-=1
		d[ord('E')-ord('A')]-=1
	# while d[ord('S')-ord('A')]!=0:
	# 	l.append(7)
	# 	print('7')
	# 	d[ord('S')-ord('A')]-=1
	# 	d[ord('E')-ord('A')]-=1
	# 	d[ord('V')-ord('A')]-=1
	# 	d[ord('E')-ord('A')]-=1
	# 	d[ord('N')-ord('A')]-=1
	while d[ord('O')-ord('A')]!=0:
		l.append(1)
		# print('1')
		d[ord('O')-ord('A')]-=1
		d[ord('N')-ord('A')]-=1
		d[ord('E')-ord('A')]-=1
	while d[ord('F')-ord('A')]!=0:
		l.append(5)
		# print('5')
		d[ord('F')-ord('A')]-=1
		d[ord('I')-ord('A')]-=1
		d[ord('V')-ord('A')]-=1
		d[ord('E')-ord('A')]-=1
	while d[ord('N')-ord('A')]!=0:
		l.append(9)
		# print('9')
		d[ord('N')-ord('A')]-=1
		d[ord('I')-ord('A')]-=1
		d[ord('N')-ord('A')]-=1
		d[ord('E')-ord('A')]-=1
	l.sort()
	print("Case #{}: ".format(z+1),end="")
	for i in l:
		print(i,end="")
	print()
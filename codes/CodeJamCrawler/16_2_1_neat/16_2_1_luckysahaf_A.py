T = int(raw_input())

for t in range(0,T):
	dict1 = {}
	unique = {0:'Z',2:'W',4:'U',6:'X',8:'G'}
	unique1 = {'Z':'ERO', 'W':'TO', 'U':'FOR', 'X':'SI', 'G':'EIHT'}
	unique2 = {1:'O' ,3:'T' ,5:'F',7:'S' }
	un2 = {'O':'NE', 'T':'HREE','F':'IVE','S':'EVEN'}
	S = raw_input()
	# print S
	for k,u in unique.items():
		count = S.count(u)
		dict1[k] = count
		S = S.replace(u,'',count)
		rep = unique1[u]
		for ch in rep:
			S = S.replace(ch,'',count)

	# print dict1
	for k,u in unique2.items():
		count = S.count(u)
		dict1[k] = count
		S = S.replace(u,'',count)
		rep = un2[u]
		for ch in rep:
			S= S.replace(ch,'',count)
	dict1[9] = S.count('E')
	# print dict1
	res = ''
	for i in range(0,10):
		for j in range (0,dict1[i]):
			res = res + str(i)

	print "Case #" + str(t+1) + ": " + res

def stringToList(s):
	l = []
	for e in s:
		if e == '+':
			l.append(True)
		elif e == '-':
			l.append(False)
	return l

def removePlusAtTheEnd(l):
	while len(l) > 0 and l[-1] == True:
		l = l[:len(l)-1]
	return l

def reverseCookies(l,iFinal):
	lbis = []
	for i in range(len(l)):
		if i <= iFinal:
			lbis.append(not l[iFinal-i])
		else:
			lbis.append(l[i])
	return lbis

T = int(input())
for t in range(T):
	s = str(input())

	l = stringToList(s)
	#print(l)

	res = 0

	while len(l) > 0:
		l = removePlusAtTheEnd(l)
		if len(l) > 0:
			top = l[0]
			iFinal = -1
			for i in range(len(l)):
				if l[i] == top:
					iFinal += 1
				else:
					break
			#sprint(iFinal)
			l = reverseCookies(l,iFinal)
			res += 1

	print("Case #{}: {}".format(t+1,res))

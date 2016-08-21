

def check(S,A):
	for i in A:
		if i/S > 0.5:
			return False
	return True

def evacuate(A):
	Res = []
	S = sum(A)
	#while S != 0:
	while S != 0:
		m1 = A.index(max(A))
		A[m1] -= 1
		m2 = A.index(max(A))
		A[m2] -= 1
		#print(S)
		S = sum(A)
		#print(S)
		if S != 0 and not check(S,A):
			#print('here')
			A[m2] += 1
			Res.append(chr(m1+ord('A')));
		else:
			l1 = chr(m1+ord('A'))
			l2 = chr(m2+ord('A'))
			Res.append(l1+l2)
	return Res


if __name__ == '__main__':
	A = [2,3,1]
	Ans = []
	Ans = evacuate(A)


	f = open('A-large.in', 'r')
	lineList = f.readlines()
	n = int(lineList[0])
	fOut = open('A-result-large.txt','w')

	i=1
	for a in range(1,(n)*2, 2):
		line = lineList[a].replace('\n','')
		A = [int(x) for x in lineList[a+1].split()]
		Ans = evacuate(A)
		#print(Ans)
		fOut.write('Case #'+str(i)+': '+(' '.join([str(i) for i in Ans]))+'\n')
		i += 1


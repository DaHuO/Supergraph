from sys import stdin

def sup1(liste,chaine):
	for c in chaine:
		i=0
		while liste[i]!=c:
			i=i+1
		del liste[i]
	return liste

def answer(chaine):
	result=[]
	L=list(chaine)
	while 'Z' in L:
		result.append(0)
		L=sup1(L,'ZERO')
	while 'W' in L:
		r=result.append(2)
		L=sup1(L,'TWO')
	while 'G' in L:
		result.append(8)
		L=sup1(L,'EIGHT')
	while 'U' in L:
		result.append(4)
		L=sup1(L,'FOUR')
	while 'H' in L:
		result.append(3)
		L=sup1(L,'THREE')
	while 'F' in L:
		result.append(5)
		L=sup1(L,'FIVE')
	while 'V' in L:
		result.append(7)
		L=sup1(L,'SEVEN')
	while 'S' in L:
		result.append(6)
		L=sup1(L,'SIX')
	while 'I' in L:
		result.append(9)
		L=sup1(L,'NINE')
	while 'O' in L:
		result.append(1)
		L=sup1(L,'ONE')
	A=sorted(result)
	r=''
	for c in A:
		r=r+str(c)
	return r


	
	
	
	
	
	
	



T=int(stdin.readline())
for case in range(1,T+1):
	chaine=stdin.readline()[:-1]
	result=answer(chaine)
	print('Case #%i: %s' % (case,result))

from sys import stdin




def answer(chaine):
	if int(chaine)==0:
		return 'INSOMNIA'
	else:
		S=set(chaine)-set('\n')
		N=int(chaine)
		n=N
		while len(S)<10:
			n=n+N
			S=S|set(str(n))
		return str(n)

T=int(stdin.readline())
for case in range(1,T+1):
	chaine=stdin.readline()
	print('Case #%i: %s' % (case,answer(chaine)))

#print(answer('11'))
#print(set(str(1692)))

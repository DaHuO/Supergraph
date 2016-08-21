from sys import stdin


def answer(chaine):
	N=len(chaine)
	if chaine[0]=='+':
		c=0
	else:
		c=1
	for i in range(N-1):
		if chaine[i]!=chaine[i+1] and chaine[i+1]=='-':
			c=c+2
	return c


T=int(stdin.readline())
for case in range(1,T+1):
	c=stdin.readline()
	print('Case #%i: %i' % (case,answer(c)))


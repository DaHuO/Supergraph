X = {(0,'R'):'R', (0,'S'):'S', (0,'P'):'P'}

P = {'P':'PR' , 'R':'RS', 'S':'SP'}

for i in range(1,13):
	
	for c in 'PSR':
		X[(i,c)] = min(X[(i-1,P[c][1])]+X[(i-1,P[c][0])],X[(i-1,P[c][0])]+X[(i-1,P[c][1])])



n = int(raw_input())

for i in range(1,n+1):
	I = map(int,raw_input().split())
	
	n,a,b,c = I

	pri = True

	for l in 'SRP':
		if a == X[(n,l)].count('R') and b == X[(n,l)].count('P') and c == X[(n,l)].count('S'):
			pri = False
			print 'Case #%d:'%i,X[(n,l)]
			break

	if pri:
		print 'Case #%d: IMPOSSIBLE'%i



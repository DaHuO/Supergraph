from template import * 

readFile('r31')

T = readInt()
for t in range(T):
	s = readLn()
	# print s
	d = {}
	for c in s:
		if not c in d:
			d[c] =0 
		d[c]+=1
	# print d
	k = (
		('Z', 'ZERO',0),
		('W','TWO',2),
		('X','SIX',6),
		('G', 'EIGHT',8),
		('H', 'THREE',3),
		('R', 'FOUR',4),
		('F', 'FIVE',5),
		('V', 'SEVEN',7),
		('O','ONE',1),
		('E', 'NINE',9))
	ou=""
	o = [0 for i in range(10)]
	for ch, wo, nu in k:
		if ch in d:
			num = d[ch]
		else:
			num =0
		# print wo,nu, num
		for i in wo:
			if i in d:
				d[i]-=num
		o[nu] = num
	# print o
	for i in range(10):
		ou+=str(i)*o[i]
	# print d
	answerLn("Case #"+str(t+1)+": "+ou)


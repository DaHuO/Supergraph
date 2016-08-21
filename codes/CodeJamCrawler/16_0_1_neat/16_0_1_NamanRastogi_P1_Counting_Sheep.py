T = int( input().strip() )
O = list()
for t in range(T) :
	I = int( input().strip() )
	x = [0 for x in range(10)]
	if I == 0 :
		O.append('INSOMNIA')
	else :
		to = 0
		while sum(x) != 10 :
			to = to + I
			i = to
			while i > 0 :
				x[ int(i % 10) ] = 1
				i //= 10
		O.append(to)

for i,o in enumerate(O):
	print('Case #', i+1, ': ', o, sep='')
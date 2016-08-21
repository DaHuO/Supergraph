f = open('i.txt', 'r')
f = f.readlines()

for i in f:
	i = list(i)
	print i
	if i[0] == '-':
		z = 0
		while z < len(i) and i[z] == '-':
			i[z] = '+'
			z += 1
	
	else:
		
	print i
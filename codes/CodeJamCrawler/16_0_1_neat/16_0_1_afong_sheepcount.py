from sys import argv

numberinos = set([0,1,2,3,4,5,6,7,8,9])

with open(argv[1], 'r') as of:
	cases = int(of.next())
	for n, x in enumerate(of):
		sheep = int(x)
		if sheep == 0:
			print('Case #' + str(n+1) +': '+ 'INSOMNIA')
			continue
			
		lastsheep = 0
		count = 0
		sheepset = set([])
		while(not sheepset.issuperset(numberinos)):
			count += 1
			lastsheep = count * sheep
			for char in str(lastsheep):
				if int(char) not in sheepset:
					sheepset.add(int(char))
		print('Case #' + str(n+1) + ': ' + str(lastsheep))
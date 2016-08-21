f = open('A-large.in', 'r')
g = open('A-large.out', 'w')

for cases in range(int(f.readline())):
	lines = int(f.readline())
	array = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
	multiplier = 1
	while((sum(array) != 10) and (lines != 0)):
		n = lines*multiplier
		#print(lines, multiplier, n, array)
		nstr = str(n)
		#print(nstr)
		for letters in nstr:
			#print(letters)
			array[int(letters)] = 1
		
		multiplier = multiplier + 1
	
	if(sum(array) == 10):
		g.write("Case #"+str(cases+1)+": "+str(n)+"\n")
	else:
		g.write("Case #"+str(cases+1)+": INSOMNIA\n")

g.close()
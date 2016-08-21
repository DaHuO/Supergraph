file = open("enter.txt", "r")
fo = open("output.txt", "w")
t = file.readline()
g = 1
while 1:	
	
	inpu = file.readline().strip()
	if not inpu:
		break
	array = [0]*10
	count = 0
	if int(inpu) == 0:
		fo.write("Case #" + str(g) + ": " + "INSOMNIA \n")
		g += 1
		continue
	print inpu

	i = 2
	check = str(inpu)
	while count != 10:
		for x in xrange(0,len(check)):
			if array[int(check[x])] == 0:
				array[int(check[x])] = 1
				count += 1
		check = int(inpu) * i
		i += 1
		check = str(check)
	fo.write("Case #" + str(g) + ": " + str(int(check) - int(inpu)) + "\n")
	g = g + 1
fo.close()
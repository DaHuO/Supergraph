out = ''
f = open("A-large.in",'r')
o = open("outfile.txt",'w')
i = eval(f.readline())


for n in range(i):
	N = eval(f.readline())
	
	if(N == 0):
		out += 'Case #' +str(n+1) +': INSOMNIA\n'
		continue

	poss = list(range(10))
	# print(poss)
	temp = 0;
	while (poss[:1]):
		remlist = []
		temp += N
		# print(temp)
		Nlist = [int(x) for x in str(temp)]
		for i in poss:
			# print(i)
			if(i in Nlist):
				remlist.append(i)
				
		for i in remlist:
			poss.remove(i)	

	out += 'Case #' +str(n+1) +': ' + str(temp) +'\n'
	# print(out)

o.write(out[:-1])


o.close()
f.close()
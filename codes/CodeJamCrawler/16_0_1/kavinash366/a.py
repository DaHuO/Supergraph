test = raw_input()
test = int(test)


for t in range(1,test+1):
	error = 1
	n = raw_input()
	nint = int(n)
	numbers = {}
	for i in range(0,10):
		numbers[i] = 0
	# print numbers
	if(nint==0):
		print "Case #"+str(t)+": INSOMNIA"
	else:
		k = 1
		while(1):
			error = 0
			for c in n:
				numbers[int(c)] = numbers[int(c)] + 1
			for key in numbers.keys():
				if(numbers[key]<1):
					error = 1
			if(error == 0):
				print "Case #"+str(t)+": "+str(n)
				break
			else:
				k = k + 1
				n = str(nint * k)
				# print n
			# print numbers
			
	

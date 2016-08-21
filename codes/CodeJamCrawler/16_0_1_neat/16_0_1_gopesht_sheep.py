with open("A-large.in",'r') as f:
	o = open('A-large.txt','a')
	test_cases = []
	for line in f:
		line = line.replace("\n","")
		test_cases.append(line)
	for t in xrange(1,int(test_cases[0])+1):
		n = int(test_cases[t])
		if n == 0:
			o.write("Case #"+str(t)+": "+"INSOMNIA"+"\n")
		else:
			counter = 1
			numbers = {}
			for i in xrange(0,10):
				numbers[str(i)] = 0
			while True:
				s = str(n*counter)
				y = list(s)
				# print numbers
				for i in y:
					numbers[i] = 1
				flag = 0
				for k,v in numbers.iteritems():
					if v==0:
						flag =1
				if flag == 0:
					break
				else:
					counter+=1
			o.write("Case #"+str(t)+": "+s+"\n")
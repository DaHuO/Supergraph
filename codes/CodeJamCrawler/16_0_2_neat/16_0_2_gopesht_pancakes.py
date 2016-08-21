def pancakes(s):
	if s=="--" or s == "-" or s=="-+":
		return 1
	elif s == "++" or s=="+" or s=="":
		return 0
	elif s== "+-":
		return 2
	else:
		s = list(s)
		s = s[::-1]
		index = 0
		flag = 0
		for i in s:
			if i == "-":
				flag = 1
				index = s.index(i)
				while index < len(s):
					if s[index]=="-":
						index+=1
					else:
						break
				break
		if flag == 1:
			q = []
			for i in s[index:]:
				if i=="+":
					q.append("-")
				else:
					q.append("+")
			q="".join(q[::-1])
			return pancakes(q)+1
		else:
			return 0
with open("B-large.in",'r') as f:
	o = open('B-large.txt','a')
	test_cases = []
	for line in f:
		line = line.replace("\n","")
		test_cases.append(line)
	for t in xrange(1,int(test_cases[0])+1):
		s = test_cases[t]
		o.write("Case #"+str(t)+": "+str(pancakes(s))+"\n")

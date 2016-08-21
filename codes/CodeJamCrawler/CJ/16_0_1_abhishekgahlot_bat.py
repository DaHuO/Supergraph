def result(x,j):
	a = set(['0','1','2','3','4','5','6','7','8','9'])
	tmp = set([])
	for i in range(1,1000000):
		tmp |= set(list(str(x*i)))
		if tmp == a:
			return "CASE #"+str(j)+": "+ str(x*i)
			break
	return "CASE #"+str(j)+": "+"INSOMNIA"
			
i=1
for _ in range(int(raw_input())):
	print result(int(raw_input()),i)
	i+=1
	
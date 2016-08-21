t = input()
for case in range(0,t):
	num = int(raw_input())
	if num == 0:
		print "Case #%d: INSOMNIA"%(case+1)
	else:
		num2 = str(num)
		appear = [0] * 10
		flag = 0
		temp = num
		while(flag == 0):
			for z in num2:
				x = int(z)
				if appear[x] == 0:
					appear[x] = 1
			flag = 1
			for i in range(0,10):
				if appear[i] == 0:
					flag = 0
			if flag == 0:
				num = num + temp
				num2 = str(num)
		print "Case #%d: %d"%(case+1,num)

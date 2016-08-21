def foo(num):
	i = 1
	flag = [False for x in range(10)]
	while(1):
		temp = num * i
		while(temp != 0):
			flag[temp % 10] = True
			temp /= 10
		if all(flag):
			return num * i
		else:
			i+=1
		if(i > 50000):
			break
	return -1

with open("A-large.in") as readfile:
	with open ("output.txt", "w") as writefile:
		N  = int(readfile.readline())
		for x in range(N):
			num = int(readfile.readline())
			if num == 0:
				writefile.write("Case #" + str(x+1) + ": INSOMNIA\n")	
			else:
				res = foo(num)
				writefile.write("Case #" + str(x+1) + ": " + str(res) + "\n")
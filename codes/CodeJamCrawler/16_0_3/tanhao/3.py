prime_list = range(2, 100)
f = open("3.in")
n = int(f.readline()[:-1])
x, y = [int(x) for x in f.readline().split()]

count = 0
kernel = 0
base = (1 << (x-1)) + 1
print "Case #1:"
while True:
	now = (kernel << 1) + base
	#print bin(now)
	s = bin(now)[2:]

	flag = True
	ans = []
	for i in xrange(2, 11):
		tmp = int(s, i)
		number = 1
		for number in prime_list:
			if tmp % number == 0:
				break
		else:
			flag = False
			break
		ans.append(number)
		
	
	#print s
	kernel += 1
	
	
	if flag:
		print s,
		for x in ans:
			print x,
		print
		count += 1
		if count == y:
			break

	
		

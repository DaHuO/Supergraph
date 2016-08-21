#code jam

n = int(raw_input())

for i in range(n):
	new = 0
	nums = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 0:0}
	num = raw_input()
	num2 = str(num)
	t = 1
	
	if num == '0':
		print "Case #%d: INSOMNIA" % (i + 1)
	
	else:
		while new < 10:
			for k in num2:
				if nums[int(k)] == 0:
					new += 1
					nums[int(k)] += 1
				
				if new == 10:
					print "Case #%d: %s" %(i + 1, num2)
					break
				
				else:
					nums[int(k)] += 1
			t += 1
			num2 = str(int(num) * t)

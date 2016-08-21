cases = raw_input()
case = int(cases)
	
def getAll(l):
	for i in l:
		if i == 0:
			return False
	return True


for i  in range(case):
	listt = [0]*10
	nb = raw_input()
	number = int(nb)
	
	if number == 0:
		aa = i+1
		print "Case #"+str(aa)+": INSOMNIA"
	else:
		mul = 1
		while(True):
			numstr = str(number*mul)
			for n in range(len(numstr)):
				listt[int(numstr[n])] += 1
			
			# print listt
			# print number*mul
			if getAll(listt):
				aa = i+1
				print "Case #"+str(aa)+":",number*mul
				break
			else:
				mul += 1



# f = open('out', 'w')
# f.write('0123456789abcdef')
# f.close()
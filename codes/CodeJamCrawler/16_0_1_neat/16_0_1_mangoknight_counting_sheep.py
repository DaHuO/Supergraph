n = int(raw_input())

total = '0123456789'

def check(done):
	for i in total:
		if i not in done:
			return 0
	return 1

for T in range(1, n + 1):
	number = int(raw_input())
	flag = 0
	done = []
	for i in range(1, 100):
		multiple = str(number * i)
		for mul in multiple:
			if mul not in done:
				done.append(mul)
				if check(done):
					print "Case #" + str(T) + ": " + str(multiple)
					flag = 1
					break
	if not flag: print "Case #" + str(T) + ": INSOMNIA"


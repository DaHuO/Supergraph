import sys

file = open(sys.argv[1])
cases = file.readline()
caseNum = 1

for line in file.read().split("\n"):
	if caseNum <= int(cases):
		sys.stdout.write("Case #" + str(caseNum) + ": ")
	num = int(line)
	if num == 0:
		print ("INSOMNIA")
	else:
		currNum = num
		digits = [False]*10
		found = False
		while found == False:
			for c in str(currNum):
				digits[int(c)] = True
			found = True
			for i in digits:
				if i == False:
					found = False
			if found == False:
				currNum += num
		print(currNum)
	caseNum += 1
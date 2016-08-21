f = open("A-large.in", 'r')
f1 = open("output.txt", 'w')
noTestcases = int(f.readline())
inputs = []
ans = []
flag = False
for i in range(noTestcases):
	inputs.append(int(f.readline()))
j = 1
for input1 in inputs:
	flag = False
	i = 2
	numDone = []
	num = set(list(str(input1)))
	numDone += num
	while(len(numDone) < 10):
		#print numDone
		prevNum = num
		num = list(str(i * input1))
		if prevNum == num:
			print "Case #" + str(j) + ": INSOMNIA"
			f1.write("Case #" + str(j) + ": INSOMNIA" + "\n")
			flag = True
			break
		for n in num:
			if n not in numDone:
				numDone.append(n)
		i += 1
	if not flag:
		#print numDone
		print "Case #" + str(j) + ": " + ''.join(num)
		f1.write("Case #" + str(j) + ": " + ''.join(num) + "\n")
	j += 1
	
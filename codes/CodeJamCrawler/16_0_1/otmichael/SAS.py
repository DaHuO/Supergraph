caseCount = int(input())
outfile = open("outSAS.txt", "w")
for x in range(caseCount):
	num = int(input())
	if num == 0:
		outfile.write("Case #{}: INSOMNIA\n".format(x+1))
		continue
	digits = set([])
	counter = 1
	while True:
		digs = list(str(counter * num))
		print(digits)
		for dig in digs:
			try:
				digits.add(dig)
			except:
				pass
		if len(digits) == 10:
			outfile.write("Case #{}: {}\n".format(x+1, counter*num))
			print("Case #{}: {}".format(x+1, counter*num))
			print(digits)
			break
		counter += 1
outfile.close()

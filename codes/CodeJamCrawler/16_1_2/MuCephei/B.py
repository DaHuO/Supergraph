def TenHut():
	bigList = []
	result = ""
	n = input()
	for x in range((2*n) - 1):
		stub = raw_input()
		for height in stub.split():
			bigList.append(height)

	bigList.sort()

	setList = set(bigList)
	smallList = []
	for item in setList:
		if bigList.count(item) % 2 == 1:
			smallList.append(int(item))

	smallList.sort()

	for i in smallList:
		result = result + str(i) + ' '

	return result


times = input()

for x in range(times):
    print ("Case #" + str(x+1) + ": " + TenHut())
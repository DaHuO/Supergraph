import sys

numCases = int(input())

for i in range(numCases):
	n = int(input())
	total = 0
	output = ""
	numbersSeen = set()
	if n == 0:	
		output = "INSOMNIA"
	else:
		while len(numbersSeen) < 10:
			total += n
			listN = list(str(total))
			for item in listN:
				numbersSeen.add(item)
		output = str(total)
	print("Case #" + str(i+1) + ": " + output)			
testC = int(input())

for tc in range(1, testC+1):
	line = list(input())
	count = 0
	while len(set(line)) > 1:
		count += 1
		currentSym = line[0]
		endRange = 0
		for j in range(len(line)):
			if line[j] == currentSym:
				endRange = j
			else:
				break
		endRange += 1
		line[0:endRange] = ['-' if i == '+' else '+' for i in line[0:endRange][::-1]]
	if line[0] == '-':
		count += 1
	print("Case #"+str(tc)+":", count)

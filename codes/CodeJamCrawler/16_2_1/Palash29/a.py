T=int(input())
for i in range(1, T+1):
	num=str(input())
	numbers=[0,0,0,0,0,0,0,0,0,0]
	for j in range(0, len(num)):
		if num[j] == 'Z':
			numbers[0] = numbers[0]+1
		if num[j] == 'O':
			numbers[1] = numbers[1]+1
		if num[j] == 'W':
			numbers[2] = numbers[2]+1
		if num[j] == 'R':
			numbers[3] = numbers[3]+1
		if num[j] == 'U':
			numbers[4] = numbers[4]+1
		if num[j] == 'F':
			numbers[5] = numbers[5]+1
		if num[j] == 'X':
			numbers[6] = numbers[6]+1
		if num[j] == 'S':
			numbers[7] = numbers[7]+1
		if num[j] == 'G':
			numbers[8] = numbers[8]+1
		if num[j] == 'I':
			numbers[9] = numbers[9]+1
	if numbers[1] > (numbers[0]+numbers[2]+numbers[4]):
		numbers[1] = numbers[1] - (numbers[0]+numbers[2]+numbers[4])
	else:
		numbers[1] = 0
	if numbers[3] > (numbers[0]+numbers[4]):
		numbers[3] = numbers[3] - (numbers[0]+numbers[4])
	else:
		numbers[3] = 0
	if numbers[5] > (numbers[4]):
		numbers[5] = numbers[5] - (numbers[4])
	else:
		numbers[5] = 0
	if numbers[7] > (numbers[6]):
		numbers[7] = numbers[7] - (numbers[6])
	else:
		numbers[7] = 0
	if numbers[9] > (numbers[8]+numbers[6]+numbers[5]):
		numbers[9] = numbers[9] - (numbers[8]+numbers[6]+numbers[5])
	else:
		numbers[9] = 0
	print("Case #{}: ".format(i),end='')
	for j in range(0,10):
		for k in range(0,numbers[j]):
			print("{}".format(j),end='')
	print("")
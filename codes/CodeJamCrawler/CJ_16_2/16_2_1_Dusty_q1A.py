fileout = open('output.out', 'w')
filein = open('A-large.in', 'r')

T = int(filein.readline()) #Number of cases
numbers = ['ZERO', 'TWO', '  ', 'FOUR', 'SIX', 'EIGHT']
numbers2 = ['ONE', 'THREE']
numbers3 = ['SEVEN']
numbers4 = ['FIVE']
numbers5 = ['NINE']
for t in range(T):
	S = list(filein.readline())
	print(S)
	
	endNumbers = []

	for x in range(len(numbers)):
		cont = True
		while(cont):
			count = 0
			temp = []
			cont = True
			for l in numbers[x]:
				for number in range(len(S)):
					if(S[number] == l):
						count += 1
						temp.append(number)
						break
			if(count == len(numbers[x])):
				if(x == 0):
					endNumbers.append(0)
				if(x == 1):
					endNumbers.append(2)
				if(x == 2):
					endNumbers.append(3)
				if(x == 3):
					endNumbers.append(4)
				if(x==4):
					endNumbers.append(6)
				if(x==5):
					endNumbers.append(8)
				for i in temp:
					S[i] = ''
			else:
				cont = False
				break
	print(endNumbers)

	for x in range(len(numbers2)):
		cont = True
		while(cont):
			count = 0
			temp = []
			cont = True
			for l in numbers2[x]:
				for number in range(len(S)):
					if(S[number] == l):
						count += 1
						temp.append(number)
						break
			if(count == len(numbers2[x])):
				if(x == 0):
					endNumbers.append(1)
				if(x == 1):
					endNumbers.append(3)
				for i in temp:
					S[i] = ''
			else:
				cont = False
				break
	print(endNumbers)
	for x in range(len(numbers3)):
		cont = True
		while(cont):
			count = 0
			temp = []
			cont = True
			for l in numbers3[x]:
				for number in range(len(S)):
					if(S[number] == l):
						count += 1
						temp.append(number)
						break
			if(count == len(numbers3[x])):
				endNumbers.append(7)
				for i in temp:
					S[i] = ''
			else:
				cont = False
				break

	for x in range(len(numbers4)):
		cont = True
		while(cont):
			count = 0
			temp = []
			cont = True
			for l in numbers4[x]:
				for number in range(len(S)):
					if(S[number] == l):
						count += 1
						temp.append(number)
						break
			if(count == len(numbers4[x])):
				endNumbers.append(5)
				for i in temp:
					S[i] = ''
			else:
				cont = False
				break

	for x in range(len(numbers5)):
		cont = True
		while(cont):
			count = 0
			temp = []
			cont = True
			for l in numbers5[x]:
				for number in range(len(S)):
					if(S[number] == l):
						count += 1
						temp.append(number)
						break
			if(count == len(numbers5[x])):
				endNumbers.append(9)
				for i in temp:
					S[i] = ''
			else:
				cont = False
				break
	endNumbers.sort()
	print(endNumbers)
	print(S)
	result = ''
	for x in endNumbers:
		result += str(x)


	fileout.write('Case #'+str(t+1)+': '+str(result)+'\n')




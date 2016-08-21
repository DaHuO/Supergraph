
fileout = open('output.out', 'w')
filein = open('A-large.in', 'r')

N = int(filein.readline()) #Number of cases
for i in range(N):
	T = int(filein.readline())
	result = ''
	if(T == 0):
		result = 'INSOMNIA'
	numbersSeen = []
	count = 1
	if(not result):
		while(len(numbersSeen)<10):
			temp = T*count
			stringT = str(temp)
			for letter in stringT:
				if(letter not in numbersSeen):
					numbersSeen.append(letter)
			result = stringT
			count += 1

	fileout.write('Case #'+str(i+1)+': '+result+'\n')




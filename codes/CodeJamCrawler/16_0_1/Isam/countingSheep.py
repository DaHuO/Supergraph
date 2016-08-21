import time

digits = [i for i in range(10)]


def countSheep(N):
	myDigits = [9999 for i in range(10)]
	i = 1
	l = len(N)
	s = N
	N = int(N)
	num = N

	if num == 0:
		return 'INSOMNIA'

	while myDigits != digits:
		num = i * N
		s = str(num)
		for ele in s:
			if int(ele) not in myDigits:
				myDigits[int(ele)] = int(ele)
				check = True
		i += 1
		if len(s) > l+1:
			return 'INSOMNIA'
	return num


if __name__ == '__main__':
	#print(digits)
	#print(countSheep(0))
	start_time = time.time()

	f = open('A-large.in', 'r')
	lineList = f.readlines()
	n = int(lineList[0])
	fOut = open('A-result-large.txt','w')

	for a in range(1,n+1):
		s = lineList[a].replace('\n','')
		dig = countSheep(s)
		fOut.write('Case #'+str(a)+': '+str(dig)+'\n')

	print("--- %s seconds ---" % (time.time() - start_time))

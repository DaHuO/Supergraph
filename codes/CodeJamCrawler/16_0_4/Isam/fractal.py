import time


if __name__ == '__main__':
	#print(digits)
	#print(countSheep(0))
	start_time = time.time()

	f = open('D-small-attempt0.in', 'r')
	lineList = f.readlines()
	n = int(lineList[0])
	fOut = open('D-result-small.txt','w')

	for a in range(1,n+1):
		line = lineList[a].replace('\n','')
		k,c,s = lineList[a].split()
		print(k,c,s)
		fOut.write('Case #'+str(a)+': '+(' '.join([str(i) for i in range(1,int(s)+1)]))+'\n')

	print("--- %s seconds ---" % (time.time() - start_time))
def mapNum(num,numHash) :
	flag = True
	while flag :
		lsn = num % 10
		next = num/10
		numHash[lsn] = True
		num = next
		if next == 0 :
			flag = False	
	return 

def sheep(num,fdOut,case) :
	numList = {}
	numHash = {}
	for x in xrange(1,1000000000):
		inputNum = num * x
		mapNum(inputNum,numHash)
		#print inputNum #debug
		#print numHash#debug
		if len(numHash) == 10 :
			#print inputNum
			fdOut.write('Case #'+case+': '+str(inputNum)+'\n')
			break
		if numList.get(inputNum) == True :
			#print 'INSOMNIA'
			fdOut.write('Case #'+case+': '+'INSOMNIA'+'\n')
			break;
			
		numList[inputNum] = True
		
	
fdInput=open("input","r")
fdOut = open("outSmall","rw+") #outBig comes later
iterator = iter(fdInput)
line = iterator.next()
numTestCases = line

case = 1
for line in fdInput :
	num = int(line)
	sheep(num,fdOut,str(case))
	case+=1


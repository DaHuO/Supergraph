import sys
def readInt():
	return int(raw_input())

def retrieveEachNumber(number):
	eachNumberList = []
	rem = 0
	while number > 0:
		rem = number % 10
		number = number/10
		eachNumberList.append(rem)
	return eachNumberList


fileout = open('log.txt', 'w')
needList = [0,1,2,3,4,5,6,7,8,9]
trueval = []

T = readInt()

for cases in range(1,T+1):
	#print "Enter N: "
	N = readInt()
	val = 0
	i = 1
	arr = []
	while i<1000000:
	#	print "i is :",i
		val = N*i
	#	print "val = ",val
		arr += retrieveEachNumber(val)  
	#	print arr
		i = i+1
		arr = list(set(sorted(arr)))
		if arr == needList:
			flag = 1
			break
		else:
			flag = 0
			continue
	if flag == 1:
		print >> fileout,"Case #"+str(cases)+": ",val
	else:
		print >> fileout,"Case #"+str(cases)+": INSOMNIA"
fileout.close()

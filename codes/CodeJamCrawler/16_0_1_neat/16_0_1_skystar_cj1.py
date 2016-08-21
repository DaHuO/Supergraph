def Insomnia(num):
	if num == 0:
		return -1
	CheckArr = [0,0,0,0,0,0,0,0,0,0]
	i=1
	tmpNum = num
	while i>-1:
		tmpNum = num * i
		i=i+1
		for j in range(len(str(tmpNum))):
			CheckArr[int(str(tmpNum)[j])] = 1
		if 0 in CheckArr:
			continue
		else:
			return tmpNum
#	return -1

fd = open("input.txt","r")
tmp = fd.read()
fd.close()
inputArray=tmp.split("\n")
result = ""
ResultTmp = 0

for i in range(1,int(inputArray[0])+1):
	ResultTmp = Insomnia(int(inputArray[i]))
	if ResultTmp == -1:
		result = result + "\n" + "Case #" + str(i) + ": INSOMNIA"
	else:
		result = result + "\n" + "Case #" + str(i) + ": " + str(ResultTmp)
	
print(result)

fd = open("output.txt","w")
fd.write(result)
fd.close()
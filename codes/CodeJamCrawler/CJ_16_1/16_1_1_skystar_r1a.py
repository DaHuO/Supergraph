def Sorting(string):
	cur = string[0]
	allstr = cur
	for i in range(1,len(string)):
		if ord(cur) <= ord(string[i]):
			allstr = string[i] + allstr
			cur = string[i]
		else:
			allstr = allstr + string[i]
	return allstr

teststr = "ZXCASDQWE"

fd = open("input.txt","r")
tmp = fd.read()
fd.close()
inputArray=tmp.split("\n")
result = ""
ResultTmp = ""

for i in range(1,int(inputArray[0])+1):
	ResultTmp = Sorting(inputArray[i])
	result = result + "\n" + "Case #" + str(i) + ": " + ResultTmp

fd = open("output.txt","w")
fd.write(result)
fd.close()
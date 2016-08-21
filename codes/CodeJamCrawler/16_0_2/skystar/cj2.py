
def CountFlip(inputText):
	currentStatus = 0
	flipCount = 0
	for i in range(len(inputText)):
		if currentStatus == 0 and inputText[len(inputText)-1-i] == "-" :
			flipCount = flipCount + 1
			currentStatus = 1
		elif currentStatus == 1 and inputText[len(inputText)-1-i] == "+" :
			flipCount = flipCount + 1
			currentStatus = 0
	return flipCount
			
fd = open("input.txt","r")
tmp = fd.read()
fd.close()
inputArray=tmp.split("\n")
result = ""

for i in range(1,int(inputArray[0])+1):
	result = result + "\n" + "Case #" + str(i) + ": " + str(CountFlip(inputArray[i]))
	
print(result)

fd = open("output.txt","w")
fd.write(result)
fd.close()
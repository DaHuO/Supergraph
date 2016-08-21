a=open('digits-large-in.txt','r')
b=a.readlines()
for i in range(len(b)):
	b[i]=b[i].rstrip('\n')
a.close()

c=open('digits-large-out.txt','w')

def checkNumTimes(key,tempDict):
	if key in tempDict.keys():
		return tempDict[key]
	return 0


for i in range(1,len(b)):
	numList=[]
	freq={}
	for letter in b[i]:
		if letter in freq.keys():
			freq[letter]+=1
		else:
			freq[letter]=1
	for j in range(checkNumTimes("Z",freq)): #ZERO
		numList.append(0)
		freq["E"]-=1
		freq["R"]-=1
		freq["O"]-=1
	for j in range(checkNumTimes("W",freq)): #TWO
		numList.append(2)
		freq['T']-=1
		freq['O']-=1
	for j in range(checkNumTimes("U",freq)): #FOUR
		numList.append(4)
		freq['F']-=1
		freq['O']-=1
		freq['R']-=1
	for j in range(checkNumTimes("F",freq)): #FIVE
		numList.append(5)
		freq["I"]-=1
		freq["V"]-=1
		freq["E"]-=1
	for j in range(checkNumTimes("X",freq)): #SIX
		numList.append(6)
		freq['S']-=1
		freq['I']-=1
	for j in range(checkNumTimes("V",freq)): #SEVEN
		numList.append(7)
		freq['S']-=1
		freq['E']-=2
		freq['N']-=1
	for j in range(checkNumTimes("G",freq)): #EIGHT
		numList.append(8)
		freq['E']-=1
		freq['I']-=1
		freq['H']-=1
		freq['T']-=1
	for j in range(checkNumTimes("I",freq)): #NINE
		numList.append(9)
		freq['N']-=2
		freq['E']-=1
	for j in range(checkNumTimes("H",freq)): #THREE
		numList.append(3)
		freq['T']-=1
		freq['R']-=1
		freq['E']-=2
	for j in range(checkNumTimes("O",freq)): #ONE
		numList.append(1)
		freq['N']-=1
		freq['E']-=1
	numList.sort()
	result=""
	for num in numList:
		result+=str(num)
	c.write("Case #"+str(i)+": "+result+"\n")
c.close()

t = raw_input()

inputList = []

# Get input list
for i in range(int(t)):
	temp = raw_input()
	temp = int(temp)
	inputList.extend([temp])

# Number of Inputs
if type(t[0] == str):
	n = int(t[0])

# Get the set of digits
def getDigits(inputNumber):
	tray = str(inputNumber)
	traySet = set(tray)
	return traySet

# Get the size of the set
def checkSize(traySet):
	flag = False
	if len(traySet) == 10:
		flag = True
	return flag

# Get Sheep Name
def getSheepName(n):
	ret = n
	p = n
	tray = getDigits(n)
	flag = checkSize(tray)
	i=2
	if n==0:
		flag = True
		ret = "INSOMNIA"
	while(not(flag)):
		p = n*i
		tempTray = getDigits(p)
		tray = tray.union(tempTray)
		flag = checkSize(tray)
		ret = p
		i = i+1
	return ret

# print getSheepName(9)
case = 1
f = open('out.txt', 'w')

for i in inputList:
	text = "Case #"+str(case)+': '+str(getSheepName(i))
	print >> f, text  # or f.write('...\n')
	case = case + 1

f.close()

def checkDict():
	global digitsDict
	for digit in digitsDict:
		if digitsDict[digit] == False:
			return False
	return True

def main():
	global digitsDict
	global INPUT_NO
	global VAR_NO
	if INPUT_NO == 0:
		return "INSOMNIA"
	while 1:
		for digit in str(VAR_NO):
			digitsDict[int(digit)] = True
		if checkDict():
			break
		VAR_NO +=  INPUT_NO
	return str(VAR_NO)

f = open('A-large.in', 'r')
lineCounter = 1
results = ""
init = True
for line in f:
	if init == True:
		init = False
		continue
	INPUT_NO = int(line[:-1])
	VAR_NO = INPUT_NO
	digitsDict = {1:False,2:False,3:False,4:False,5:False,6:False,7:False,8:False,9:False,0:False}
	results += "Case #" + str(lineCounter) + ": " + main() + "\n"
	lineCounter += 1
f.close()
w = open('results.txt','w')
w.write(results)
w.close()



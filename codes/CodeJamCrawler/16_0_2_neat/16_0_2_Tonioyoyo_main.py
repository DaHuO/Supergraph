changes = 0

def flip(stringStack,end):
	global changes
	newStack = stringStack[end::-1]
	stackToReturn = list(newStack)

	for i in range(end+1):
		if stackToReturn[i] == '+':
			stackToReturn[i] = '-'
		else:
			stackToReturn[i] = '+'

	changes += 1
	return "".join(stackToReturn) + "".join(stringStack[end+1:])

def arrangeTop(stringStack):
	end = 0
	listStack = list(stringStack)

	for i in range(len(listStack)):
		if listStack[i] == '-':
			break
		else:
			end = i

	return flip(stringStack,end)

def adjustEndIndex(stringStack):
	start = 0
	end = len(stringStack) - 1

	listStack = list(stringStack)

	for i in range(len(stringStack)-1,start-1,-1):
		if listStack[i] == '-':
			break
		else:
			end -= 1

	if end < 0:
		end = 0

	return end

def pancakeStackIsOK(stringStack):
	if '-' in stringStack:
		return False
	else:
		return True


def main():
	f = open('B-large.in', 'r')
	fout = open('outputLarge', 'w')

	numberTestCase = int(f.readline())

	for n in range(numberTestCase):
		global changes
		changes = 0
		fout.write('Case #%d: ' % (n + 1))

		strLine = f.readline().strip('\n')

		#TODO
		print(strLine)

		while not pancakeStackIsOK(strLine):
			end = adjustEndIndex(strLine)

			if strLine.startswith('-'):
				strLine = flip(strLine,end)
			else:
				strLine = arrangeTop(strLine)

		# TODO
		print(strLine,changes)
		print('------------------')

		fout.write('%d\n' % changes)


if __name__ == "__main__":
    # execute only if run as a script
    main()


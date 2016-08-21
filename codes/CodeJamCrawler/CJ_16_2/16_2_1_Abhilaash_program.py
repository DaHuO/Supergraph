import copy
def inputvars():
	f = open('input.txt')
	num = int(f.readline())
	numlist = f.read().splitlines()
	return num, numlist

def outputvars(num, output):
	f = open('output.txt', 'w')
	for x in range(num):
		f.write(str('Case #' + str(x + 1) + ': ' + str(output[x]) + '\n'))
	f.close()
	
def checkNum(s, letters):
	temp = copy.copy(letters)
	for letter in s:
		if(not letter in temp):
			return False
		temp.remove(letter)
	return True

def removeLetter(s, letters):
	# print(letters)
	for letter in s:
		letters.remove(letter)
		# print('removed: ', letter, letters)
	# print(letters)
	return letters

def main():
	num, numlist = inputvars()
	output = []
	for x in range(num):
		letters = list(numlist[x])
		curnum = []
		while(len(letters) > 0):
			while(checkNum('SIX', letters)):
				letters = removeLetter('SIX', letters)
				curnum.append('6')
			while(checkNum('SEVEN', letters)):
				letters = removeLetter('SEVEN', letters)
				curnum.append('7')
			while(checkNum('FIVE', letters)):
				letters = removeLetter('FIVE', letters)
				curnum.append('5')
			while(checkNum('FOUR', letters)):
				letters = removeLetter('FOUR', letters)
				curnum.append('4')
			while(checkNum('EIGHT', letters)):
				letters = removeLetter('EIGHT', letters)
				curnum.append('8')
			while(checkNum('ZERO', letters)):
				letters = removeLetter('ZERO', letters)
				curnum.append('0')
			while(checkNum('NINE', letters)):
				letters = removeLetter('NINE', letters)
				curnum.append('9')
			if(checkNum('THREE', letters)):
				letters = removeLetter('THREE', letters)
				curnum.append('3')
			if(checkNum('ONE', letters)):
				letters = removeLetter('ONE', letters)
				curnum.append('1')
			if(checkNum('TWO', letters)):
				letters = removeLetter('TWO', letters)
				curnum.append('2')
		curnum.sort()
		# print(curnum)
		output.append(''.join(curnum))
	outputvars(num, output)

main()
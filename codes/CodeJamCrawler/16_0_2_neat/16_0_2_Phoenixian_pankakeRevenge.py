def flip(pancakes, number):
	#first reverse the first number pancakes
	pancakes[:number] = reversed(pancakes[:number])
	#next change all - to + and + to minus
	for index in range(number):
		if pancakes[index] == '-':
			pancakes[index] = '+'
		else:
			pancakes[index] = '-'

def countInversions(pancakes):
	inversions = 0
	currentCharacter = '+'
	for index in range(len(pancakes) - 1, -1, -1):
		if pancakes[index] != currentCharacter:
			inversions += 1
			currentCharacter = pancakes[index]
	return inversions
	
def answer(inversions, number):
	print("Case #" + str(number) + ": " + str(inversions))
	
numCases = int(input())
for case in range(1, numCases + 1):
	pancakes = input()
	answer(countInversions(pancakes), case)
ALL_NUMBERS = ['ZERO', 'ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE']
NUMBER_LETTERS = [list(number) for number in ALL_NUMBERS]

def main():
	T = int(input())
	for x in range(1, T + 1):
		S = input()
		y = ''.join([str(num) for num in solve(S)])
		print('Case #{0}: {1}'.format(x, y))

def solve(string, number=0):
	if len(string) == 0:
		return []
	if number >= len(NUMBER_LETTERS):
		return None
	nextString = reduceString(string, NUMBER_LETTERS[number])
	if nextString == string:
		return solve(string, number + 1)
	nextNumbers = solve(nextString, number)
	if nextNumbers is None:
		return solve(string, number + 1)
	return [number] + nextNumbers

def reduceString(string, numberLetters):
	stringLetters = list(string)
	for letter in numberLetters:
		if letter not in stringLetters:
			return string
		else:
			stringLetters.remove(letter)
	return ''.join(stringLetters)

main()

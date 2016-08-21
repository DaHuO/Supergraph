#0: Z-k száma a nullások száma
#1: O - 0-ás - 2-es - 4-es
#2: W
#3: R - 4-es - 0-ás
#4: U
#5: V - 7-es
#6: X
#7: S - 6-osok száma
#8: G
#9: I - 5-ös - 6-os - 8-as

def doit(row):
	numbers = [0]*10
	letters = {
		'Z': 0,
		'O': 0,
		'W': 0,
		'R': 0,
		'U': 0,
		'V': 0,
		'X': 0,
		'S': 0,
		'G': 0,
		'I': 0,
	}

	for c in row:
		if (c in letters):
			letters[c] += 1

	numbers[0] = letters['Z']
	numbers[2] = letters['W']
	numbers[4] = letters['U']
	numbers[6] = letters['X']
	numbers[8] = letters['G']

	numbers[3] = letters['R'] - numbers[4] - numbers[0]
	numbers[7] = letters['S'] - numbers[6]
	numbers[5] = letters['V'] - numbers[7]
	numbers[9] = letters['I'] - numbers[5] - numbers[6] - numbers[8]	
	numbers[1] = letters['O'] - numbers[0] - numbers[2] - numbers[4]

	result = ""
	for i in range(10):
		result += str(i) * numbers[i]

	return result


test_cases = int(input())
current_case = 0

while (test_cases):
	test_cases -= 1
	current_case += 1
	print("Case #%d: %s" % (current_case, doit(input())))
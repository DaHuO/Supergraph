import sys
# Insert your import here.

def solve(stream):
	# Implement your solving method here.
	# N = int(stream.readline().strip())
	#for i in range(N):
	number = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
	letters = stream.readline().strip()
	numbers = []
	count = 0
	while len(letters) > 0:
		if 'Z' in letters:
			numbers += [0]
			for i in (number[0]):
				letters = letters.replace(i, "", 1)
		elif 'W' in letters:
			numbers += [2]
			for i in (number[2]):
				letters = letters.replace(i, "", 1)
		elif 'X' in letters:
			numbers += [6]
			for i in (number[6]):
				letters = letters.replace(i, "", 1)
		elif 'U' in letters:
			numbers += [4]
			for i in (number[4]):
				letters = letters.replace(i, "", 1)
		elif 'R' in letters:
			numbers += [3]
			for i in (number[3]):
				letters = letters.replace(i, "", 1)
		elif 'O' in letters:
			numbers += [1]
			for i in (number[1]):
				letters = letters.replace(i, "", 1)
		elif 'F' in letters:
			numbers += [5]
			for i in (number[5]):
				letters = letters.replace(i, "", 1)
		elif 'V' in letters:
			numbers += [7]
			for i in (number[7]):
				letters = letters.replace(i, "", 1)
		elif 'G' in letters:
			numbers += [8]
			for i in (number[8]):
				letters = letters.replace(i, "", 1)
		elif 'N' in letters:
			numbers += [9]
			for i in (number[9]):
				letters = letters.replace(i, "", 1)
		count += 1
		if count > 50:
			break
	numbers = sorted(numbers)
	return ''.join(map(str,numbers))

# Script entry point, read the file
# given in the parameter and execute
# solve method for each test case.
# DO NOT MODIFY THIS PART UNLESS YOU KNOW WHAT YOU ARE DOING !
if __name__ == "__main__":
	input = sys.argv[1]
	file = open(input, "r")
	T = int(file.readline().strip())
	for t in range(T):
		result = solve(file)
		print("Case #%d: %s" % (t + 1, result))
	file.close()
def get_digits(str):

	letters = {}

	digits = ""

	for c in str:
		if c in letters:
			letters[c] += 1
		else:
			letters[c] = 1

	# Zero
	if "Z" in letters:
		digits += "0" * letters["Z"]
		letters["E"] -= letters["Z"]
		letters["R"] -= letters["Z"]
		letters["O"] -= letters["Z"]
		letters["Z"] = 0
	
	letters = clean_dict(letters)

	# Two
	if "W" in letters:
		digits += "2" * letters["W"]
		letters["T"] -= letters["W"]
		letters["O"] -= letters["W"]
		letters["W"] = 0
	
	letters = clean_dict(letters)
	
	# Four
	if "U" in letters:
		digits += "4" * letters["U"]
		letters["O"] -= letters["U"]
		letters["F"] -= letters["U"]
		letters["R"] -= letters["U"]
		letters["U"] = 0
	
	letters = clean_dict(letters)
	
	#Five
	if "F" in letters:
		digits += "5" * letters["F"]
		letters["V"] -= letters["F"]
		letters["I"] -= letters["F"]
		letters["E"] -= letters["F"]
		letters["F"] = 0
	
	letters = clean_dict(letters)
	
	# One
	if "O" in letters:
		digits += "1" * letters["O"]
		letters["N"] -= letters["O"]
		letters["E"] -= letters["O"]
		letters["O"] = 0
	
	letters = clean_dict(letters)

	# Three
	if "R" in letters:
		digits += "3" * letters["R"]
		letters["T"] -= letters["R"]
		letters["H"] -= letters["R"]
		letters["E"] -= 2 * letters["R"]
		letters["R"] = 0
	
	letters = clean_dict(letters)

	# Six
	if "X" in letters:
		digits += "6" * letters["X"]
		letters["I"] -= letters["X"]
		letters["S"] -= letters["X"]
		letters["X"] = 0
	
	letters = clean_dict(letters)

	# Seven
	if "V" in letters:
		digits += "7" * letters["V"]
		letters["E"] -= letters["V"]
		letters["E"] -= letters["V"]
		letters["N"] -= letters["V"]
		letters["S"] -= letters["V"]
		letters["V"] = 0
	
	letters = clean_dict(letters)

	# Eight
	if "G" in letters:
		digits += "8" * letters["G"]

	# Nine
	if "N" in letters:
		digits += "9" * int(letters["N"] / 2)

	return ''.join(sorted(digits))

def clean_dict(d):

	to_delete = []
	for i in d:
		if d[i] == 0:
			to_delete.append(i)

	for i in to_delete:
		del d[i]

	return d

# Read line with the number of cases
t = int(input())
for i in range(1,t+1):
	n = input()
	print("Case #{}: {}".format(i, get_digits(n)))
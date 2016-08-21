inputs = []
with open("A-large.in") as f:
    lines = f.readlines()
    inputs = [int(w[:-1]) for w in lines[1:]]

limit = 10000
for i in range(len(inputs)):
	n = inputs[i]
	print("Case #" + str(i + 1) + ": ", end="")
	digits = [0] * 10
	found = False
	for x in range(1, limit):
		test = x * n
		str_test = str(test)
		for c in str_test:
			digits[int(c)] = 1
		if sum(digits) == 10:
			found = True
			print(test)
			break
	if not found:
		print("INSOMNIA")
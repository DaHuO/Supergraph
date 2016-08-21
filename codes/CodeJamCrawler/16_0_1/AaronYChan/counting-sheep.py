with open("A-large.in") as f:
	lines = f.readlines()

numTests = int(lines[0])
output = ""

for i in range(0, numTests):
	n = int(lines[i + 1])
	if n == 0:
		output += "Case #" + str(i + 1) + ": INSOMNIA\n"
		continue
	digits = set()
	count = 1
	while len(digits) < 10:
		for c in str(count * n):
			digits.add(c)
		count += 1
	output += "Case #" + str(i + 1) + ": " + str((count - 1) * n) + "\n"

with open("sheep-ans-large.out", "w") as f:
	f.write(output)
def check(numbers):
	for n in numbers:
		if n == False:
			return False
	return True

file_in = open("input.txt", "r")
file_out = open("output.txt", "w")
file_out.truncate()
lines = []
lines_out = []

for line in file_in:
	lines.append(line)

i = -1
for line in lines:
	k = False
	if i == -1:
		i = 0
		k = True
	if k == True :
		continue
	else :
		n = int(line)
		ma = len(line) + 3
		maximum = pow(10, ma)
		numbers = [False, False, False, False, False, False, False, False, False, False]
		count = 1
		ready = False
		while ready == False:
			temp = n * count
			s = str(temp)
			for t in s:
				numbers[int(t)] = True
			if check(numbers) == True:
				lines_out.append(str(temp))
				ready = True
			if count > maximum:
				lines_out.append("INSOMNIA")
				ready = True
			count += 1

for i in range(int(lines[0])):
	file_out.write("Case #" + str(i + 1) + ": " + lines_out[i] + "\n")

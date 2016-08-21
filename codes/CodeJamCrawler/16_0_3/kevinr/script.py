def increment(jamcoin):
	for i in range(1, len(jamcoin) - 1):
		if jamcoin[i] == 1:
			jamcoin[i] = 0
		else:
			jamcoin[i] = 1
			break
	return jamcoin

def ending(jamcoin):
	for i in range(1, len(jamcoin) - 1):
		if jamcoin[i] == 0:
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
		ready = False
		l = line.split(" ")
		results = []
		length = int(l[0])
		number = int(l[1])
		number_temp = 0
		jamcoin = []
		jamcoin.append(1)
		for c in range(length - 2):
			jamcoin.append(0)
		jamcoin.append(1)
		border = 2

		while ready == False:
			divisors = [0, 0, 0, 0, 0, 0, 0, 0, 0]
			prime = False
			for b in range(2, 11):
				msb = pow(b, length - 1)
				actual_number = 0
				for counter in range(0, len(jamcoin)):
					actual_number += (jamcoin[counter] * msb)
					msb /= b
				for d in range(border, border * 10):
					if d >= actual_number:
						break
					if (actual_number % d) == 0:
						divisors[b - 2] = d
						break
				if divisors[b - 2] == 0:
					prime = True
					break

			if prime == False:
				results.append([jamcoin[:], divisors[:]])
				number_temp += 1

			if ending(jamcoin) == True:
				border *= 10

			jamcoin = increment(jamcoin)

			if number_temp == number:
				lines_out.append(results)
				ready = True

for i in range(int(lines[0])):
	file_out.write("Case #" + str(i + 1) + ":" + "\n")
	for o in lines_out[i]:
		for c in o[0]:
			file_out.write(str(c))
		for c in o[1]:
			file_out.write(" ")
			file_out.write(str(c))
		file_out.write("\n")

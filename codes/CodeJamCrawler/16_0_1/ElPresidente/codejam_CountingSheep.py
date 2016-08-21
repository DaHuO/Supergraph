#Henry Wang
#Problem A
#Counting Sheep
#4/8/16

#infile = open('A-small-attempt1.in.txt', 'r')
infile = open('A-large.in.txt', 'r')
numT = infile.readline()

fileout = open('codejam0_output_large.txt', 'w')
count = 1
list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


for line in infile:
	input = int(line)
	if input == 0: #
		result = 'INSOMNIA'
		fileout.write('Case #' + str(count) + ': ' + result + '\n')
	else:
		i = 1
		while list:
			input = i * int(line)
			for digit in str(input):
				if int(digit) in list:
					list.remove(int(digit))
			i += 1
		lastN = (i-1) * int(line)
		fileout.write('Case #' + str(count) + ': ' + str(lastN) + '\n')
	list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
	count += 1


infile.close()
fileout.close()
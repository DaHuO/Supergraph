inFile = open('/Users/Michael/Desktop/D-small-attempt1.in', 'r')
outFile = open('/Users/Michael/Desktop/output', 'w')

line = inFile.readline()
data = line.split()
T = int(data[0])

for i in range(0, T):
	line = inFile.readline()
	data = line.split()
	K = int(data[0])
	C = int(data[1])
	S = int(data[2])

	outFile.write('Case #' + str(i + 1) + ': ')

	X = K ** C
	Y = int(X / K)

	while (X > 0):
		outFile.write(str(X) + ' ')
		X -= Y

	outFile.write('\n')


inFile.close()
outFile.close()
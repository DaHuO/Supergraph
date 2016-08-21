import fileinput as FileIn
import sys

def ReadData(File, Data):
	for line in FileIn.input(File):
		line = line.replace( "\n", "" )
		Data.append(int(line))

def counting_sheep(N):
	digits = []
	count = 1
	while True:

		if len(digits) == 10:
			break
		else:
			tmp = N * count
			if count > 1 and tmp == N:
				return 'INSOMNIA'
			count += 1

		while tmp != 0:
			digit = tmp % 10
			if digit not in digits:
				digits.append(digit)
			tmp /= 10

	return N * (count - 1)



if __name__ == '__main__':
	File = 'A-large.in.txt'
	Data = []
	ReadData(File, Data)
	#print Data
	#print counting_sheep(96)
	#print len(Data)
	#for idx in range(1, len(Data)):
	#	print "Case #" + str(idx) + ':', counting_sheep(Data[idx])
	print counting_sheep(6)
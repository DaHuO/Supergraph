import fileinput as FileIn
import sys

def ReadData(File, Data):
	for line in FileIn.input(File):
		line = line.replace( "\n", "" )
		Data.append(line)

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

def is_all_smile(cakes):
	times = 0
	for cake in cakes:
		if cake == '+':
			times += 1
	if times == len(cakes):
		return True
	else:
		return False



def maneuver(cakes):
	Result = 0
	times = 0
	counter = 0
	bottom = len(cakes) - 1
	top = 0
	tmp = [cakes[i] for i in range(0, len(cakes))]

	while not is_all_smile(tmp):

		top = 0
		bottom = len(cakes) - 1

		# move "bottom" to the first '-'
		while tmp[bottom] == '+':
			bottom -= 1

		# move "top" to the front of first '-'
		while tmp[top] == '+':
			top += 1
		top -= 1

		#print 'top:', top, 'bottom:', bottom

		# the top is '-'
		if top < 0:
			for idx in range(0, bottom + 1):
				if tmp[idx] == '+':
					tmp[idx] = '-'
				else:
					tmp[idx] = '+'
		# the top is '+'
		else:
			for idx in range(0, top + 1):
				if tmp[idx] == '+':
					tmp[idx] = '-'
				else:
					tmp[idx] = '+'
		counter += 1
		#print tmp

	return counter








if __name__ == '__main__':
	File_1 = 'A-large.in.txt'
	Data_1 = []
	# problem1
	ReadData(File_1, Data_1)
	#print Data
	#print counting_sheep(96)
	#print len(Data)
	#for idx in range(1, len(Data)):
	#	print "Case #" + str(idx) + ':', counting_sheep(Data[idx])
	#print counting_sheep(6)

	# problem2
	File_2 = 'test.txt'
	Data_2 = []
	ReadData(File_2, Data_2)

	for idx in range(1, len(Data_2)):
		print "Case #" + str(idx) + ':', maneuver(Data_2[idx])

	#tmp = [cakes[i] for i in range(0, len(cakes))]
	#print tmp
	#print maneuver(cakes)

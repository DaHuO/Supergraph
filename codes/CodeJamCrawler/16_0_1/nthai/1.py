def getResult(num):
	allnums = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
	counter = 0
	if num == 0:
		return 'INSOMNIA'
	while allnums and counter < 10000:
		counter += 1
		digits = set(map(int, str(num * counter)))
		allnums = allnums - digits
	if counter == 10000:
		print('-----------------ERROR--------------------')
	return counter * num

def printResult(num):
	print('Case #{0}: {1}'.format(num, getResult(num)))

if __name__ == '__main__':
	with open('A-large.in') as infile, open('A-large-out.txt', 'w') as outfile:
		case = 0
		for line in infile:
			if case == 0:
				case = 1
			else:
				res = getResult(int(line.strip()))
				outfile.write('Case #{0}: {1}\n'.format(case, res))
				case += 1
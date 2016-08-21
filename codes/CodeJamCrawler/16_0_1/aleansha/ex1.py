import numpy as np

def get_data(exnr):
	filename = "A-small-attempt0.in"
	data = np.genfromtxt(filename, delimiter=',', dtype=int, skip_header=1)
	process_data(data)

def process_data(data):
	index = 1
	for number in data:
		result = process_number(number)
		print('Case #%d: %s' %(index, result))
		index += 1
		

def process_number(number):
	if number == 0:
		return 'INSOMNIA'
	digits = []
	for i in range(1, 201):
		nr = str(number*i)
		for digit in nr:
			if not digit in digits:
				digits.append(digit)
		if len(digits) == 10:
			return nr
	if len(digits) == 10:
		return nr
	else:
		return 'INSOMNIA'

if __name__ == '__main__':
	data = get_data(1)
# Counting sheep

def main_func(num):
	org_number = num
	i = 1

	digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

	while digits:
		number = str(int(org_number) * i)
		for value in number:
			try:
				digits.pop(digits.index(value))
			except ValueError:
				pass
		i += 1
		if i > int(number) and org_number != '1':
			return 'INSOMNIA'

	return number

fhi = open('large_input.in')
fho = open('large_output.txt', 'w')

t = int(fhi.readline().strip())

for i in range(1, t + 1):
	number = fhi.readline().strip()
	text = 'Case #' + str(i) + ': ' + main_func(number) + '\n'
	fho.write(text)
	fho.flush()

fhi.close()
fho.close()

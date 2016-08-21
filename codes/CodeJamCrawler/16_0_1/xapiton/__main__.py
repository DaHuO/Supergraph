f = open('A-large.in', 'r')

s = f.read()

splitted = s.split('\n')

number_cases = int(splitted[0])

out_s = ''

for num in range(0, number_cases):

	d = []

	start_number = int(splitted[num + 1])

	if start_number == 0:
		out_s += 'Case #%d: %s\n' % (num + 1, 'INSOMNIA') 

	else:

		is_end = False

		fin_number = 0

		cur_number = start_number

		index = 2

		while not is_end:

			for char in str(cur_number):
				if char not in d:
					d.append(char)

			if len(d) >= 10:
				fin_number = cur_number
				is_end = True
			else:
				cur_number = start_number * index

			index += 1

		out_s += 'Case #%d: %d\n' % (num + 1, fin_number)

		
with open('output.txt', 'w') as f:
	f.write(out_s)
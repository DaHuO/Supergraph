def last_number(n): 
	if n == 0:  
		return 'INSOMNIA'

	s = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
	s2 = set()
	count = 0

	while s != s2: 
		count += 1
		num = n * count 
		lst = list(str(num))
		s2.update(lst)

	return num

if __name__ == '__main__': 
	f2 = open('output2.txt', 'w')

	with open('A-large.in', 'r') as f: 
		count = 0 

		for line in f: 
			if count == 0: 
				pass 
			else: 
				n = int(line)
				f2.write('Case #{}: {}\n'.format(count, last_number(n)))

			count += 1
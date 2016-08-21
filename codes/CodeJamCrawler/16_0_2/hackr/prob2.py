def num_flips(chars): 
	count = 0 
	is_pos = all(c == '+' for c in chars)

	if not chars or is_pos: 
		return count 

	i = 0 

	while not is_pos: 
		while i < len(chars) and chars[i] != '+': 
			i += 1

		if i != 0: 
			for j in range(i): 
				if chars[j] == '-': 
					chars[j] = '+'
				else: 
					chars[j] = '-'
			
			count += 1

		is_pos = all(c == '+' for c in chars)

		if is_pos: 
			break

		while i < len(chars) and chars[i] == '+': 
			i += 1		

		if i != 0: 
			for j in range(i): 
				if chars[j] == '-': 
					chars[j] = '+'
				else: 
					chars[j] = '-'
			
			count += 1			

		is_pos = all(c == '+' for c in chars)

	return count 

if __name__ == '__main__': 
	f2 = open('output2.txt', 'w')

	with open('B-large.in', 'r') as f: 
		count = 0 

		for line in f: 
			if count == 0: 
				pass 
			else: 
				chars = list(line.strip())
				f2.write('Case #{}: {}\n'.format(count, num_flips(chars)))

			count += 1
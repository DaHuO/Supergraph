with open('sheep.in') as f:
	data = f.read().split('\n')

with open('sheep.out', 'w') as f:
	for i in range(1, len(data)):
		x = int(data[i])
		if x == 0:
			f.write('Case #{}: INSOMNIA\n'.format(i))
			continue
		digits = set()
		mult = 1
		while len(digits) != 10:
			temp = x * mult
			while temp > 0:
				digits.add(temp % 10)
				temp /= 10
			mult += 1
		f.write('Case #{}: {}\n'.format(i, (mult-1) * x))

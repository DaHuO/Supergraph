with open('fractiles.in') as f:
	data = f.read().split('\n')

with open('fractiles.out', 'w') as f:
	for i in range(1, len(data)):
		row = [int(x) for x in data[i].split(' ')]
		k, c, s = row
		f.write('Case #{}: '.format(i))
		f.write(' '.join(str(x) for x in range(1, k+1)))
		f.write('\n')

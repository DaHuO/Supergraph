def count(N):
	if N == 0:
		return 'INSOMNIA'
	seen = []
	count = 0;
	last = 0;
	while len(seen) < 10:
		count += 1
		temp = count * N
		while temp != 0:
			digit = temp % 10
			if not digit in seen:
				seen.append(digit)
			temp = temp // 10
	return count * N

case = 1
inputs = []
with open('A-large.in') as f:  
    for line in f:
        line = line.split() # to deal with blank 
        if line:            # lines (ie skip them)
            line = [int(i) for i in line]
            inputs += line
inputs = inputs[1:]
for i in range(0, len(inputs)):
	print('Case #' + str(case) + ': ' + str(count(inputs[i])))
	case += 1

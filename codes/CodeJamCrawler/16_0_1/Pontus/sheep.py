fname = 'A-large.in'
f = open(fname, 'r')
fout = open('out.txt', 'w')
T = int(f.readline().strip())
case = 1
for l in f:
	N = int(l.strip())
	digits_left = [0,1,2,3,4,5,6,7,8,9]
	num = 0
	if N == 0:
		fout.write('Case #' + str(case) + ': INSOMNIA\n')
		case += 1
		continue

	while len(digits_left) > 0:
		num += N
		digits = [int(d) for d in str(num)]
		digits_left = [d for d in digits_left if d not in digits]	
	fout.write('Case #' + str(case) + ': ' + str(num) + '\n')
	case += 1
fout.close()

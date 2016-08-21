used = [0]*10

N = int(raw_input())
case = 1

def count(num):
	
	while num:
		used[num%10] = 1
		num //= 10
	
	for i in used:
		if not i:
			return False
	
	return True

for _ in xrange(N):
	
	num = int(raw_input())
	tmp = num
	
	if num == 0:
		print 'Case #' + str(case) + ': INSOMNIA'
		case += 1
		continue
	
	while not count(num):
		num += tmp
	
	print 'Case #' + str(case) + ':', num
	case += 1
	used = [0]*10
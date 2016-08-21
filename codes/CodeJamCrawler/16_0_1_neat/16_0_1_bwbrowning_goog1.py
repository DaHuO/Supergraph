import sys

lines = sys.stdin.readlines()

def get_digits(num):
	str_num = str(num)
	return list(str_num)

case_num = 1
for line in lines[1:]:
	line = line.rstrip()
	digits_seen = set()
	#print "%r" % line
	if line == '0':
		print "Case #%d: INSOMNIA" % case_num
		case_num = case_num + 1
		continue

	n = int(line)
	count = 1
	while True:
		#print n
		digits_seen.update(get_digits(count*n))
	#	print digits_seen
		if(len(digits_seen) == 10):
			break

		count = count+1

	print "Case #%d: %d" % (case_num, count*n)
	case_num = case_num+1

f = open('A-large.in')
num_cases = int(f.readline())


def process(line):
	num = int(line)
	if num == 0:
		return 'INSOMNIA'
	seen = set()
	num_seen = 0
	
	for i in range(num, 100*num, num):
		str_num = str(i)
		for c in str_num:
			if c not in seen:
				num_seen += 1
				seen.add(c)
				if num_seen == 10:
					return str_num

for i in range(num_cases):
	print "Case #%d: %s" % (i+1, process(f.readline()))




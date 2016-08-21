# Problem A. Counting Sheep

def run():
	i = 0
	with open('input.txt', 'rt') as src, open('output.txt', 'wt') as tgt:
		for line in src:
			if i > 0:
				tgt.write(processItem(i, int(line)) + '\n')
			i = i + 1


def processItem(lineNo, item):
	if item == 0:
		return 'Case #%d: %s' % (lineNo, 'INSOMNIA')
	else:
		i = 1
		digits = list()
		while True:
			for c in str(item * i):
				if not c in digits:
					digits.append(c)
			if len(digits) == 10:
				return 'Case #%d: %s' % (lineNo, item * i)
			i = i + 1

run()

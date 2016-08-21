txt = ''
with open('A-large.in', 'r') as f:
# with open('input.in', 'r') as f:
	txt = f.read()
	txt = txt.split('\n')
output_list = []
for test_case in xrange(int(txt.pop(0))):
	num_base = int(txt.pop(0))
	num = num_base
	digit_set = set()
	inf = False
	if num == 0:
		inf = True
	else:
		for x in str(num_base):
			digit_set.add(x)
		while len(digit_set) < 10:
			num += num_base
			for x in str(num):
				digit_set.add(x)
	if num == 0:
		num = 'INSOMNIA'
	output_list.append(num)
with open('out.out', 'w') as f:
	for i, x in enumerate(output_list, 1):
		f.write('Case #%d: %s\n'%(i, str(x)))
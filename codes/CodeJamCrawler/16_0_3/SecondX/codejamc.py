def get_nums(bits):
	for n in xrange(2,11):
		yield int(bits, n)

def get_big_factor(n):
	if n%2 == 0:
		return n/2
	# for x in xrange(3,int(n**0.5)+1,2):
	for x in xrange(3,65536,2):
		if n % x == 0:
			return n/x
	return None
def get_bits(n):
	for x in xrange(0, 2**(n-2)):
		yield '1{0}1'.format('{0:b}'.format(x).zfill(n-2))

def run(N, J):
	output = []
	catch = 0
	for bits in get_bits(N):
		numbers = list(get_nums(bits))
		record = []
		invalid = False
		for number in numbers:
			factor = get_big_factor(number)
			if not factor:
				invalid = True
				break
			record.append(factor)
		if invalid:
			invalid = False
			continue
		output.append('%s %s'%(bits, ' '.join(map(str,record))))
		catch += 1
		if catch == J:
			return output
	return output
txt = ''
with open('C-large.in', 'r') as f:
# with open('input.in', 'r') as f:
	txt = f.read()
	txt = txt.split('\n')
output_list = []
for test_case in xrange(1, int(txt.pop(0))+1):
	N, J = map(int, txt.pop(0).split())
	with open('Clarge.out', 'w') as f:
		f.write('Case #%d:\n%s'%(test_case, '\n'.join(run(N, J))))

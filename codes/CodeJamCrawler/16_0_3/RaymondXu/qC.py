import math

n = 16
j = 50
i = 2 ** (n - 1)


def next_bitstring():
	global i
	s = format(i, 'b')

	if len(s) > n:
		return None

	if s[len(s) - 1] == '0':
		i += 1
		return next_bitstring()
	return s


def make_proof(bits):
	proof = []
	for base in range(2, 11):
		factor = verify(bits, base)
		if factor:
			proof.append(factor)
		else:
			return None
	return proof


def verify(bits, base):
	# convert to base
	num = convert_base(bits, base)

	if num % 2 == 0:
		return 2
	if num % 3 == 0:
		return 3

	# return divisor
	for div in range(5, int(math.ceil(math.sqrt(int(num))))):
		if num % div == 0:
			return div

	# prime
	return None


def convert_base(bits, base):
	ans = 0
	power = 0

	for bit in bits[::-1]:
		ans += int(bit) * (base ** power)
		power += 1

	return ans


def main():
	w = open('output_file.txt', 'w')

	w.write('Case #1:\n')
	global i
	global j
	while j > 0:
		s = next_bitstring()
		if not s:
			print 'NO MORE'
			return
		proof = make_proof(s)
		if proof:
			generator = (str(x) for x in proof)
			log = '{} {}'.format(s, ' '.join(generator))
			w.write(log + '\n')
			j -= 1
		i += 1

main()
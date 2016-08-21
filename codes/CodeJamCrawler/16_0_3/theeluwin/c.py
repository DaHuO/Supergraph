import math
import collections

infile = open('c.in')
outfile = open('c.out', 'w')
indata = infile.read().split('\n')
T = int(indata[0])
is_prime = collections.defaultdict(lambda: False)

def generate_some_prime(P):
	for i in range(2, P):
		is_prime[i] = True
		pythagoras = int(math.sqrt(i))
		for j in range(2, pythagoras + 1):
			if i % j == 0:
				is_prime[i] = False
				break


def get_nontrivial_divisor(k):
	if is_prime[k]:
		return None
	pythagoras = int(math.sqrt(k))
	for i in range(2, pythagoras + 1):
		if k % i == 0:
			is_prime[k] = False
			return i
	is_prime[k] = True
	return None


def solve(s):
	N, J = [int(ss) for ss in s.split(' ')]
	r = ""
	n = 0
	j = 0
	template = '1{:0' + str(N - 2) + 'b}1'
	while j < J:
		coin = template.format(n)
		divisors = []
		for base in range(2, 11):
			interpretation = int(coin, base)
			divisor = get_nontrivial_divisor(interpretation)
			if divisor:
				divisors.append(divisor)
			else:
				break
		if len(divisors) == 9:
			r += coin + ' ' + ' '.join([str(divisor) for divisor in divisors]) + '\n'
			j += 1
		n += 1
	return r


if __name__ == '__main__':
	generate_some_prime(1000000)
	for t in range(1, T + 1):
		r = solve(indata[t])
		outfile.write("Case #{}:\n{}\n".format(t, r))

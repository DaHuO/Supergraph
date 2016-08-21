from math import sqrt, ceil
from random import choice

def is_prime(n):
	for i in range(2, ceil(sqrt(n))+1):
		if n%i == 0:
			return i
	return 1

factors = {}

def is_special_prime(n):
	"""
	It's faster to write than some fancy, tried-and-tested, well-known probabilistic algorithm
	"""
	if n in factors:
		return factors[n]
	for i in range(2, min(ceil(sqrt(n))+1, 1000000)):
		if n%i == 0:
			factors[n] = i
			return i
	factors[n] = 1
	return 1

def interpret(case, base):
	num = 0
	for exp, i in enumerate(case[::-1]):
		if i=='1':
			num += base**exp
	return num

class JamcoinFactory():
	def __init__(self):
		self.checked = []

	def is_jamcoin(self, n):
		if n[0] == '0' or n[-1] == '0':
			return False
		proof = []
		for base in range(2, 11):
			div = is_special_prime(interpret(n, base))
			if div == 1:
				return False
			else:
				proof.append(div)
		return proof

	def generate_jamcoin(self, N):
		assert N >= 6
		ready = False
		while len(self.checked) < 2**(N-4):
			p = '100' + ''.join(choice('01') for _ in range(N-4)) + '1'
			if p not in self.checked:
				self.checked.append(p)
				proof = self.is_jamcoin(p)
				if proof:
					return [p] + proof


def main():
	fname = input()
	with open(fname, 'r') as fh:
		with open(fname+'.out', 'w') as fout:
			T = int(fh.readline())
			for i in range(T):
				fout.write("Case #{0}:\n".format(i+1))
				f = JamcoinFactory()
				N, J = fh.readline().split()
				for j in range(int(J)):
					fout.write(' '.join(str(x) for x in f.generate_jamcoin(int(N))))
					fout.write('\n')

if __name__ == '__main__':
	main()
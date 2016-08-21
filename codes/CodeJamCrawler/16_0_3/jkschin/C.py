import pyprimes
from pyprimes import factors
from numba import jit
import signal
import warnings

def handler(signum, frame):
	raise Exception

def write(out, case, answer):
	out.write("Case #%d: \n" %(case))
	out.write(str(answer))

def parse(f):
	f = open(f, "r").read().split("\n")
	n = f[0]
	return n, f[1:]

def check_jam_coin(n):
	for base in range(2,10+1):
		new_n = int(n, base)
		warnings.simplefilter('error',RuntimeWarning)
		try:
			if pyprimes.is_prime(new_n):
				return False
		except RuntimeWarning:
			print "Warned", new_n
			return False
	return True

def get_all_divisors(n):
	l = []
	for base in range(2,10+1):
		new_n = int(n, base)
		divisor = factors.factors(new_n).next()[0]
		l.append(divisor)
	return l

def combined(N, J):
	count = 0
	ans = ""
	for i in xrange(2**(N-1),2**(N)):
		binary = bin(i)[2:].zfill(N)
		if binary[0]=="1" and binary[-1]=="1":
			if check_jam_coin(binary):
				print count
				signal.signal(signal.SIGALRM, handler)
				signal.alarm(1)
				try:
					divisors = get_all_divisors(binary)
				except Exception:
					continue
				divisors.insert(0, binary)
				count += 1
				ans += " ".join(str(x) for x in divisors)
				ans +="\n"
			if count == J:
				break
	return ans

# combined(6, 3)
# print get_one_divisor(470184985873, sieve)
# print (2**16)

# get_binary_representations(6)

def main():
	out = open("test_ans.txt", "w")
	cases, l = parse("test.txt")
	cases = int(cases)
	for i in range(cases):
		N, J = l[i].split()
		N, J = int(N), int(J)
		write(out, i+1, combined(N,J))

main()

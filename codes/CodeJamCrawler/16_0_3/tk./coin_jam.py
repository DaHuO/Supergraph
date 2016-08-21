import sys
import sympy.ntheory

# WARNING: Assumes all input is squeaky clean.

def main():
	T = int(sys.stdin.readline())

	for case_num in range(1,T+1):
		input_line = sys.stdin.readline()
		args = input_line.split(' ')
		N = int(args[0])
		J = int(args[1])

		num_results = 0
		coins = coin_generator(N)

		print("Case #{0}:".format(case_num))
		for j in range(J):
			coin = coins.next()
			print coin['coin'],
			for divisor in coin['divisors']:
				print divisor,
			print ''

def interpret_in_base(string_representation, base):
	num = 0
	for i,c in enumerate(string_representation[::-1]):
		num += int(c)*(base**(i))
	return num

def candidates_generator(N):
	# count down instead of up, larger numbers means less chances of a prime
	for i in xrange(2**(N-2)-1, -1, -1):
		candidate = "1"+format(i,'b').zfill(N-2)+"1"
		yield candidate


def coin_generator(N):
	candidates = candidates_generator(N)
	for candidate in candidates:
		divisor_list = []
		for base in xrange(2,11):
			interpretation = interpret_in_base(candidate, base)
			divisible = False
			# no need to check all factors, just need these (there are enough
			# possible candidates that we don't need to pick out all of them).
			for divisor in [2, 3, 5, 7, 11, 13]:
				divisible = (interpretation % divisor) == 0
				if divisible:
					divisor_list.append(divisor)
					break
			if not divisible:
				break
		if len(divisor_list) == 9:
			yield {'coin': candidate, 'divisors': divisor_list}



if __name__ == "__main__":
	main()
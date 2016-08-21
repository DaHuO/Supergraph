import itertools
import pickle

# with open("c.pickle", "wb") as handle:
# 	result = {}

# 	def check_prime(n):
# 		if n <= 3:
# 			return True, None
# 		elif n %2 ==0:
# 			return False, 2
# 		elif n%3 ==0:
# 			return False, 3
# 		i = 5
# 		while  i * i * i *i <= n:
# 			if n % i ==0:
# 				return False, i
# 			if n % (i + 2) == 0:
# 				return False, i+2
# 			i += 6
# 		return True, None

# 	each_size = 32
# 	length = each_size - 2
# 	result[each_size] = {}
# 	for each_number in itertools.product(["0", "1"], repeat=length):
# 		# print each_size, len(result[each_size]) 
# 		if len(result[each_size]) > 500:
# 			break

# 		print each_number, len(result[each_size])

# 		N = "1" + ''.join(each_number) + "1"
# 		result[each_size][N] = []

# 		for each_base in xrange(2, 10+1):
# 			n = int(N, each_base)
			
# 			# print each_size, N, each_base, n
# 			is_prime, divisible_number = check_prime(n)
# 			if is_prime:
# 				"prime found"
# 				result[each_size].pop(N) 
# 				break
# 			result[each_size][N].append(divisible_number)

# 	# print result
# 	pickle.dump(result, handle)


with open('c.pickle', 'rb') as handle:
  	result = pickle.load(handle)

  	# print result
	T = int(raw_input())

	for t in range(T):
		N, J = tuple(map(int, raw_input().split()))
		# print N,J

		jamcoins = result[N].keys()[:J]
		print "Case #%d:"%(t+1)
		for jamcoin in jamcoins:
			print "%s %s" % (jamcoin , ' '.join( map(str, result[N][jamcoin]) ))


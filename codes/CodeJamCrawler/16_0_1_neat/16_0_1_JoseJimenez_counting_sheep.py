def solution(N):
	if (N == 0):
		return "INSOMNIA"
	
	all_known_digits = ""	
	i=1
	while True:
		digit = N * i
		all_known_digits += str(digit)
		
		if (len(set(all_known_digits)) == 10):
			return digit		
		i += 1
	return time

if __name__ == "__main__":
	test_cases = input()
	for case in xrange(1, test_cases + 1):
		N = int(raw_input()) 
		print "Case #%i: %s" %  (case, solution(N))

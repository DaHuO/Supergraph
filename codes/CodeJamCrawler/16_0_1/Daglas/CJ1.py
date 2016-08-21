def main():
	cases = []
	number_of_cases = int(raw_input())
	for i in range(number_of_cases):
		cases.append(int(raw_input()))
	
	for i,c in enumerate(cases):
		print "Case #%s: %s" % (i+1, naive_solution(c))

def naive_solution(n):
	if n == 0:
		return "INSOMNIA"
	needed_digits = range(0,10)
	i = 1
	while needed_digits:
		number = n * i
		digits = [int(j) for j in str(number)]
		for d in digits:
			needed_digits = list(set(needed_digits) - set(digits))
		i = i + 1
	return number
		
if __name__ == "__main__":
	main()
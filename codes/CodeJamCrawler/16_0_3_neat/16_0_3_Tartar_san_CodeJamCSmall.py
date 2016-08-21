num_cases = int(input())
num = [True] * 10000000
num[0] = False
num[1] = False
prime_numbers = []
for i in range(2, 10000000):
	if num[i] == True:
		prime_numbers.append(i)
		for j in range(i*2, 10000000, i):
			num[j] = False

def generate(lst, n, current):
	"""Generate strings in format "1(0,1)^(n-2)1" and save it in lst"""
	if len(current) == 0:
		current += "1"
		generate(lst, n, current)
	elif len(current) == n-1:
		current += "1"
		numbers.append(current)
	else:
		generate(lst, n, current+"1")
		generate(lst, n, current+"0")

for case in range(num_cases):
	line = input()
	n = int(line.split()[0])
	j = int(line.split()[1])
	
	numbers = []
	results = []
	generate(numbers, n, "")
	
	for number in numbers:
		prime = False
		for system in range(2,11):
			prime_in_system = True
			number_in_system = int(number, system)
			if number_in_system in prime_numbers:
				prime = True
				break
			for prime_number in prime_numbers:
				if number_in_system % prime_number == 0:
					prime_in_system = False
					break
			if prime_in_system:
				prime = True
				break
		if not prime:
			results.append(number)
			if len(results) == j:
				break
	answerline = "Case #1:\n"
	for number in results:
		answerline += number
		for system in range(2,11):
			number_in_system = int(number, system)
			for prime_number in prime_numbers:
				if number_in_system % prime_number == 0:
					answerline += " " + str(prime_number)
					break
		answerline += "\n"
print(answerline, end = "")
		
		
	

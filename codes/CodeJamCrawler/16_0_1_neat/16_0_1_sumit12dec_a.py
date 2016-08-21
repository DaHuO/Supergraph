N = input()

test_cases = []
results = []
for i in range(0, N):
	test_cases.append(input())



def get_output(number):
	bit_check = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
	number_use = number
	for i in range(1,1000000):
		for each in str(number_use):
			bit_check[int(each)] = 1
		if bit_check == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]:
			return number_use
		else:
			number_use = number*(i+1)
	return "INSOMNIA"

for each_no in test_cases:
	results.append(get_output(each_no))

for i in range(0, len(results)):
	print "Case #{0}: {1}".format(i+1, results[i])

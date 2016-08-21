num_cases = int(input())
results = []
for i in range(num_cases):
	n = int(input())
	
	if n == 0:
		results.append("INSOMNIA")
	else:
		numbers = set()
		coefficient = 0
		while len(numbers) != 10:
			coefficient += 1
			for number in str(n*coefficient):
				numbers.add(number)
		results.append(coefficient*n)

for i in range(len(results)):
	print("Case #" + str(i + 1) + ": " + str(results[i]))
				
		

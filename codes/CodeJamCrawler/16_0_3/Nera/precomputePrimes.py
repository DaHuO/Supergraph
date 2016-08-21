max = 10**8 + 3
#max = 20
numbers = [True] * max

for i in range(2, max):
	if i % 10000 == 0:
		print i
	if (numbers[i]):
		for j in range(2*i, max, i):
			numbers[j] = False


output = open("primes", "w")
for i in range(2, max):
	if numbers[i]:
		output.write("%d\n" % i)
output.close()
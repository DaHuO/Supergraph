def count(n):
	numbers = []
	if n==0:
		return "INSOMNIA"

	b = str(n)
	while len(numbers)<10:
		for x in b:
			if x not in numbers:
				numbers.append(x)
		else:
			b = str(int(b)+ n)	
	return int(b)-n

a = open('A-large.in')
b = open('prob_a_output.txt', 'w')

test_cases = map(int, a)
i = 1
for x in test_cases[1:]:
	b.write('Case #'+ str(i)+ ': ' +  str(count(x))+'\n')
	i += 1
a.close()
b.close()



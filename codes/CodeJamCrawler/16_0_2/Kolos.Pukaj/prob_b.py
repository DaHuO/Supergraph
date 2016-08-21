def remove_plus(s):
	a = s
	b = a[len(a)-1]
	while b == '+':
		a = a[:len(a)-1]
		b = a[len(a)-1]
	return a

def maneuvers(s):
	for x in s:
		if x != '+':
			break
	else:
		return str(0)

	new_string = remove_plus(s)

	result = 0
	first_pancake = 0

	for x in new_string:
		if x != first_pancake:
			first_pancake = x
			result += 1

	return str(result)

a = open('B-large.in')
b = open('output.txt', 'w')

t = a.readline()
t = t[:len(t)-1]

for i in range(0,int(t)):
	test_case = a.readline()
	test_case = test_case[:len(test_case)-1]
	b.write("Case #" + str(i+1) + ": " + maneuvers(test_case)+ '\n')

a.close()
b.close()

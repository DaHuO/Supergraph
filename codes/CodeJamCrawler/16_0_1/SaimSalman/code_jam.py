import sys
from sets import Set

f = open('A-large.in', 'r')
number_of_test_cases = f.readline()

for i in range(0,int(number_of_test_cases)):
	current = f.readline()

	sys.stdout.write("Case #")
	sys.stdout.write(str(i+1))
	sys.stdout.write(": ")

	current_set = Set()
	value = -1
	for j in range(1,1000):
		for k in str(int(current) * j):
			current_set.add(k)
			if (len (current_set) == 10):
				value = int(current) * j
				break
		if (value != -1):
			break

	# print current_set
	# current_set.clear()
	if (value != -1):
		print(str(value))
	else:
		print("INSOMNIA")







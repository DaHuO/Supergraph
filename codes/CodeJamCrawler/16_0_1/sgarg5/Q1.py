import sys
from sets import Set

t = input()

def print_result(i):
	value = input()
	if value == 0:
		print "Case #%d: INSOMNIA" %(i+1)
	else:
		unique_digits = Set([])
		counter = 1
		old_value = value
		while True:
			value = old_value * counter
			counter = counter + 1
			digits = [ int(j) for j in str(value) ]
			for digit in digits:
				unique_digits.add(digit)
				if len(unique_digits) == 10:
					print "Case #%d: %d" %(i+1, value)
					return;

for i in range(t):
	print_result(i)
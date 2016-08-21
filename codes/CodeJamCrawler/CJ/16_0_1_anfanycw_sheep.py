#!/usr/bin/python
from __future__ import print_function

digits = dict.fromkeys([0,1,2,3,4,5,6,7,8,9])
outfile = None

def run():
	global outfile
	outfile = open("output.txt", "w")

	with open("input.txt", "r") as f:
		lines = []
		for line in f:
			lines.append(line.strip("\n"))

		lines = lines[1:]

		for i,l in enumerate(lines):
			count_sheep(i+1, int(l))

def check_digits():
	global digits
	for key, value in digits.iteritems():
		if value is None:
			return False
	return True

def update_digits(num):
	global digits
	for o in map(int,str(num)):
		digits[o] = True

def clear_dict():
	global digits
	digits = dict.fromkeys([0,1,2,3,4,5,6,7,8,9])

def count_sheep(case, l):
	global digits
	update_digits(l)
	i = 2
	while True:
		num = i*l

		# update dict for every digit of num
		update_digits(num)

		# if num is ever 0, must be insomnia
		if num == 0:
			print("Case #%d: %s" % (case, 'INSOMNIA'), file=outfile)
			clear_dict()
			break

		# check if all keys in dict have a value
		if check_digits():
			print("Case #%d: %d" % (case, num), file=outfile)
			clear_dict()
			break

		# increment
		i += 1

# start script
run()
import random as r

def count(n):
	nums = set(str(n))
	if n == 0:
		return "INSOMNIA"
	if len(nums) == 10:
		return n
	for i in range(1, 100):
		nums.update(set(str(i * n)))
		if len(nums) == 10:
			return i * n

f = open('input_large.txt')
for i, line in enumerate(f):
	if not i: 
		continue
	n = int(line)
	print("Case #%i: %s" % (i, count(n)))

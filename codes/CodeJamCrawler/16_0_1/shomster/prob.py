input_file = open("A-large.in", 'r')
from time import sleep

l = input_file.readline()

for ix, num in enumerate(input_file):
	print "Case #" + str(ix + 1) + ": ",
	num = num.strip()

	if num == '0':
		print "INSOMNIA"
		continue

	i = 1
	cur = num
	seen = dict()

	# print "the number is", cur

	while True:
		for d in list(cur): 
			seen[d] = True
		# print seen

		if len(seen) == 10:
			print cur
			break

		i = i + 1
		cur = str(int(num) * i)
		# sleep(0.2)






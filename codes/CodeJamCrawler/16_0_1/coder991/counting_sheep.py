with open('input', 'r') as input:
	with open('output', 'w+') as output:
		input_size = int(input.readline())
		for i in xrange(1,input_size+1):
			num = int(input.readline())
			if num == 0:
				output.write("Case #%s: %s\n" % (i, "INSOMNIA"))
			else:
				seen = set()
				multiplier = 1
				while(len(seen) < 10):
					print seen
					seen.update(list(str(multiplier*num)))
					multiplier += 1
				output.write("Case #%s: %s\n" % (i, (multiplier-1)*num))

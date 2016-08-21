for tc in range(input()):
	num = int(raw_input())
	if num == 0:
		print "Case #" + str(tc + 1) + ": INSOMNIA"
	seen_digits = []
	for mult in range(1,460):
		for i in str(mult * num):
			if i not in seen_digits:
				seen_digits = seen_digits + [i]
		if len(seen_digits) == 10:
			print "Case #" + str(tc + 1) + ": " + str(mult * num)
			break
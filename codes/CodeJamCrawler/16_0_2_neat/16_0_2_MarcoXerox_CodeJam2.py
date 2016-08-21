for i in range(int(input())):
	cont, ch, s = 0, '\0', input()
	for x in s:
		if x != ch:
			ch = x
			cont += 1
	print("Case #%d: %d" % (i+1, cont-s.endswith('+')))

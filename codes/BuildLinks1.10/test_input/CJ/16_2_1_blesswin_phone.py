for c in range(int(input())):
	s = input()
	n = []

	while 'Z' in s:
		s = s.replace("Z", "", 1)
		s = s.replace("E", "", 1)
		s = s.replace("R", "", 1)
		s = s.replace("O", "", 1)
		n.append(0)
	while 'U' in s:
		s = s.replace("F", "", 1)
		s = s.replace("O", "", 1)
		s = s.replace("U", "", 1)
		s = s.replace("R", "", 1)
		n.append(4)
	while 'X' in s:
		s = s.replace("S", "", 1)
		s = s.replace("I", "", 1)
		s = s.replace("X", "", 1)
		n.append(6)
	while 'S' in s:
		s = s.replace("S", "", 1)
		s = s.replace("E", "", 1)
		s = s.replace("V", "", 1)
		s = s.replace("E", "", 1)
		s = s.replace("N", "", 1)
		n.append(7)
	while 'V' in s:
		s = s.replace("F", "", 1)
		s = s.replace("I", "", 1)
		s = s.replace("V", "", 1)
		s = s.replace("E", "", 1)
		n.append(5)
	while 'G' in s:
		s = s.replace("E", "", 1)
		s = s.replace("I", "", 1)
		s = s.replace("G", "", 1)
		s = s.replace("H", "", 1)
		s = s.replace("T", "", 1)
		n.append(8)
	while 'I' in s:
		s = s.replace("N", "", 1)
		s = s.replace("I", "", 1)
		s = s.replace("N", "", 1)
		s = s.replace("E", "", 1)
		n.append(9)
	while 'R' in s:
		s = s.replace("T", "", 1)
		s = s.replace("H", "", 1)
		s = s.replace("R", "", 1)
		s = s.replace("E", "", 1)
		s = s.replace("E", "", 1)
		n.append(3)
	while 'W' in s:
		s = s.replace("T", "", 1)
		s = s.replace("W", "", 1)
		s = s.replace("O", "", 1)
		n.append(2)
	while 'O' in s:
		s = s.replace("O", "", 1)
		s = s.replace("N", "", 1)
		s = s.replace("E", "", 1)
		n.append(1)

	print("Case #{}: ".format(c + 1) + "".join(map(str, sorted(n))))

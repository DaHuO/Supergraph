
read = open('in.in', 'r')
write = open('out.out', 'w')

cases = int(read.readline())

for case in range(cases):
	
	line = read.readline()[:-1]
	fields = line.split(" ")
	n = int(fields[0])
	r = int(fields[1])
	p = int(fields[2])
	s = int(fields[3])

	# counts = []
	# counts += [(r, p, s)]
	imposs = False
	for i in range(n):
		rp = (r + s - p) // 2
		pp = (r + p - s) // 2
		sp = (s + p - r) // 2
		if rp < 0 or pp < 0 or sp < 0:
			imposs = True
			break
		r = rp
		p = pp
		s = sp
		# counts = [(r, p, s)] + [counts]

	if imposs:
		write.write("Case #{0}: {1}\n".format(case+1, "IMPOSSIBLE"))
		continue
	
	# print(counts)

	string = ''

	if r == 1:
		string = 'R'
	if p == 1:
		string = 'P'
	if s == 1:
		string = 'S'
	for i in range(n):
		stringp = ''
		for j in string:
			if i == n - 1 and j == 'R':
				stringp += 'RS'
			elif j == 'R':
				stringp += 'SR'
			if j == 'P':
				stringp += 'PR'
			if i < n - 2 and j == 'S':
				stringp += 'SP'
			elif j == 'S':
				stringp += 'PS'
		string = stringp
	
	# print(string)
	write.write("Case #{0}: {1}\n".format(case+1, string))

read.close()
write.close()



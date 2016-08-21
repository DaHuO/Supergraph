fin = open('input', 'r')
fout = open('output', 'w')
tests = int(fin.readline())
for i in range(tests):
	s = fin.readline()
	values = s.split()
	
	for j in range(len(values)):
		values[j] = int(values[j])

	s = "Case #"+str(i+1)+": "
	if values[2] >= values[0]:
		for j in range(values[2]):
			s = s + " " + str(j+1)
	elif values[2] + 1>= values[0] and values[1] != 1:
		for j in range(values[2]):
			s = s + " " + str(j+2)
	else:
		s = s + "IMPOSIBLE"

	fout.write(s+"\n")

fin.close()
fout.close()
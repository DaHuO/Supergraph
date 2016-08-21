input_file = "A-large (1).in"
output_file = "A-large.out"

f_in = open(input_file, "r")
f_out = open(output_file, "w")

test_cases = int(f_in.readline()[:-1])

alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

for case in range(test_cases):
	f_out.write("Case #" + str(case+1) + ": ")
	
	p = int(f_in.readline())
	s = f_in.readline().split()
	s_sum = 0
	for i in range(p):
		s[i] = int(s[i])
		s_sum += s[i]

	queue = ""

	while s_sum > 0 and max(s) > 2:
		m = max(s)
		p_max = s.index(m)
		queue += alphabet[p_max]
		s[p_max] = s[p_max] - 1
		s_sum -= 1
		if m in s:
			p_max = s.index(m)
			queue += alphabet[p_max] + " "
			s[p_max] = s[p_max] - 1
			s_sum -= 1
		else: 
			queue += " "

	while max(s) == 2:
		if s.count(2) % 2 == 0:
			p_max = s.index(2)
			queue += alphabet[p_max]
			s[p_max] = s[p_max] - 1
			s_sum -= 1
			p_max = s.index(2)
			queue += alphabet[p_max]
			s[p_max] = s[p_max] - 1
			s_sum -= 1
			queue += " "
		else:
			p_max = s.index(2)
			queue += alphabet[p_max] + " "
			s[p_max] = s[p_max] - 1
			s_sum -= 1
	
	while s_sum > 2:
		p_max = s.index(1)
		queue += alphabet[p_max] + " "
		s[p_max] = s[p_max] - 1
		s_sum -= 1

	if s_sum == 2:
		p_max = s.index(1)
		queue += alphabet[p_max]
		s[p_max] = s[p_max] - 1
		s_sum -= 1
		p_max = s.index(1)
		queue += alphabet[p_max] + " "
		s[p_max] = s[p_max] - 1
		s_sum -= 1

	f_out.write(queue + "\n")


f_in.close()
f_out.close()
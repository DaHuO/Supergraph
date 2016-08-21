

def get_ans(cl):

	cl = [ int(d) for d in cl ]

	plan_l = []

	while True:
		
		if sum(cl) <= 0:
			break
		m = max(cl)

		if cl.count(m) == 1:
			i = cl.index(m)

			if cl[i] == 1:

				cl[i] = 0
				plan_l.append(chr(65+i))
			else:
				cl[i] = cl[i] - 2

				if cl[i] < 0:
					cl[i] = 0

				plan_l.append(chr(65+i)+chr(65+i))

		else:

			if m == 1 and cl.count(m) % 2 == 1:

				s = ''
				i2 = cl.index(m)
				cl[i2] = cl[i2] - 1

				if cl[i2] < 0:
					cl[i2] = 0
				else:
					s += chr(65+i2)
				plan_l.append(s)


			else:
				s = ''
				i1 = cl.index(m)
				cl[i1] = cl[i1] - 1
				if cl[i1] < 0:
					cl[i1] = 0
				else:
					s += chr(65+i1)
				
				i2 = cl.index(m)
				cl[i2] = cl[i2] - 1

				if cl[i2] < 0:
					cl[i2] = 0
				else:
					s += chr(65+i2)
				plan_l.append(s)


	return ' '.join(plan_l)



f = open("A-large.in" , "r")

lines = f.readlines()

N = int(lines[0])

for i in range(N):
	T = lines[2*i+1].split("\n")[0]
	cnt_l = lines[2*i+2].split("\n")[0].split(" ")
	# print s

	# print cnt_l

	ans = get_ans(cnt_l)

	ans = "Case #"+str(i+1)+": "+str(ans)
	print ans
	# print 
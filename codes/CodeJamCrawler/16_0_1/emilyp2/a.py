fi = open('A-large.in', 'r')
fo = open('aL.out', 'w')

T = fi.readline()
T = int(T)

for x in range(1,T+1):
	numb = fi.readline()
	N = int(numb)

	nums = ['0','1','2','3','4','5','6','7','8','9']

	fo.write('Case #'+str(x)+': ')
	if N == 0:
		fo.write('INSOMNIA\n')
		continue
	else:
		for t in range(1, 500):
			Nn = N*t
			Ns = str(Nn)
			for c in Ns:
				try:
					nums.remove(c)
				except:
					pass
			if len(nums) < 1:
				fo.write(Ns + '\n')
				break

fi.close()
fo.close()


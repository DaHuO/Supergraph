file = open("/Users/daviddai/Desktop/A-large.in", "r")
data = file.read()
file.close()

data = data.split()[1:]
opt = ''

for i, j in enumerate(data):
	hs = set()
	N = 1
	full = set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
	numStr = j
	if j == '0':
		opt += "Case #" + str(i + 1) + ": " + "INSOMNIA" + '\n'
	else:
		while hs != full:
			for dgt in str(int(j) * N): 
				if int(dgt) not in hs:
					hs.add(int(dgt))
			N += 1
		opt += "Case #" + str(i + 1) + ": " + str(int(j) * (N - 1)) + '\n'


file = open('result.txt', 'w')
file.write(opt)
file.close()





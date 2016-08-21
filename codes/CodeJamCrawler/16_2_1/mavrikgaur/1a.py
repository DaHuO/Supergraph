ip = open('A-small.in')
op = open('A-small.out', 'w')
t = int(ip.readline())
for case in range(t):
	x = ip.readline().strip()
	dictionary = dict()
	for i in 'qwertyuiopasdfghjklzxcvbnm'.upper():
		dictionary[i] = 0
	for i in x:
		dictionary[i] += 1
	count = [0]*10
	count[0] = dictionary['Z']
	count[2] = dictionary['W']
	count[4] = dictionary['U']
	count[6] = dictionary['X']
	count[8] = dictionary['G']
	dictionary['Z'] -= count[0]
	dictionary['E'] -= count[0]
	dictionary['R'] -= count[0]
	dictionary['O'] -= count[0]
	dictionary['T'] -= count[2]
	dictionary['W'] -= count[2]
	dictionary['O'] -= count[2]
	dictionary['F'] -= count[4]
	dictionary['O'] -= count[4]
	dictionary['U'] -= count[4]
	dictionary['R'] -= count[4]
	dictionary['S'] -= count[6]
	dictionary['I'] -= count[6]
	dictionary['X'] -= count[6]
	dictionary['E'] -= count[8]
	dictionary['I'] -= count[8]
	dictionary['G'] -= count[8]
	dictionary['H'] -= count[8]
	dictionary['T'] -= count[8]
	count[5] = dictionary['F']
	dictionary['F'] -= count[5]
	dictionary['I'] -= count[5]
	dictionary['V'] -= count[5]
	dictionary['E'] -= count[5]
	count[7] = dictionary['V']
	dictionary['S'] -= count[7]
	dictionary['E'] -= count[7]
	dictionary['V'] -= count[7]
	dictionary['E'] -= count[7]
	dictionary['N'] -= count[7]
	count[3] = dictionary['T']
	dictionary['T'] -= count[3]
	dictionary['H'] -= count[3]
	dictionary['R'] -= count[3]
	dictionary['E'] -= count[3]
	dictionary['E'] -= count[3]
	count[1] = dictionary['O']
	dictionary['O'] -= count[1]
	dictionary['N'] -= count[1]
	dictionary['E'] -= count[1]
	count[9] = dictionary['I']
	print count
	answer = ''
	for i in range(10):
		answer += str(i)*count[i]
	op.write('Case #'+str(case+1)+': '+answer+'\n')
ip.close()
op.close()

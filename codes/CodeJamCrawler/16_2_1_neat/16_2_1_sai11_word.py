fin=open('A-large.in','r')
# fin=open('test.in','r')
T=int(fin.readline())

file('A-large.out','w')
f=open('A-large.out','w')

def remove(spell, check, num):
	phone = []
	while check in h:
		# print h
		phone.append(num)
		for c in list(spell):
			h[c] -= 1
			if h[c] == 0:
				del h[c]

	return phone

for t in xrange(T):
	S = list(fin.readline().strip())
	
	h = {}
	for c in S:
		if c in h:
			h[c] += 1
		else:
			h[c] = 1

	num = []
	num += remove('ZERO', 'Z', 0)
	num += remove('TWO', 'W', 2)
	num += remove('FOUR', 'U', 4)
	num += remove('SIX', 'X', 6)
	num += remove('EIGHT', 'G', 8)
	num += remove('ONE', 'O', 1)
	num += remove('THREE', 'H', 3)
	num += remove('FIVE', 'F', 5)
	num += remove('SEVEN', 'S', 7)
	num += remove('NINE', 'N', 9)

	num.sort()
	
	f.write('Case #'+str(t+1)+': '+''.join(map(str,num))+'\n')

f.close()
def counting(n):
	a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
	if (n == 0):
		return "INSOMNIA"
	for i in range(1, 100):
		for dig in str(n*i):
			if(int(dig) in a):
				a.remove(int(dig))
		if(len(a) == 0):
			return n*i
	return "INSOMNIA"

f = open('A-large.in.txt', 'r')
f2 = open('outputLarge.txt', 'w')
final = ''

for i in range(1, int(f.readline().strip())+1):
	s = int(f.readline())
	final += 'Case #{}: {}\n'.format(i, counting(s))

f2.write(final)
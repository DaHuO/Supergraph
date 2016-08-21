def numb_to_dig(n):
	c = []
	while n:
		c.append(n%10)
		n /= 10
	return c

digits = set([1,2,3,4,5,6,7,8,9,0])
fout = open('o_large.txt', 'w')
with open('A-large.in') as f:
	t = int(f.readline())
	for i in range(int(t)):
		n = int(f.readline())
		if n == 0:
			fout.write('CASE #'+str(i+1)+': INSOMNIA\n')
		else:
			z = set(numb_to_dig(n))
			count = 2
			while z != digits:
				last_num = n*count
				z.update(numb_to_dig(last_num))
				count+=1
			fout.write('CASE #'+str(i+1)+': '+str(last_num)+'\n')


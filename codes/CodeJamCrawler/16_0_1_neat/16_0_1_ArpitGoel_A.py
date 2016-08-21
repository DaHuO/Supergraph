f = open('input', 'r')
g = open('output', 'a')
T = int(f.readline())
for i in range(T):
	num = int(f.readline())
	t = list('0000000000')
	if num == 0:
		g.write("Case #{0}: {1}\n".format(i+1, 'INSOMNIA'))
	else:
		j = 1
		while int("".join(t), 2) ^ 0b1111111111 != 0:
			temp = int(num * j)
			while temp > 0:
				t[int(temp%10)] = '1'
				temp = int(temp / 10)
			j = j + 1
		#print(j)
		g.write("Case #{0}: {1}\n".format(i+1, num * (j-1)))
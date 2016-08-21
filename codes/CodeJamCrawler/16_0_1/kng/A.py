def update(a, i, n):
	#print a
	m = i*n
	while(m>0):
		a[m%10] = 1
		m = m/10
	return a

input_file = open('A-large.in', 'r+')
output_file = open('A-large.out', 'w+')
t = int(input_file.readline())
c = 0
while(c<t):
	c += 1
	line = input_file.readline().strip()
	#print line
	n = int(line)
	if(n==0):
		output_file.write('Case #'+str(c)+': INSOMNIA\n')
		continue
	a = [0 for _ in xrange(10)]
	i = 0
	while(sum(a)!=10):
		i = i+1
		a = update(a, i, n)
	print n, i
	output_file.write('Case #'+str(c)+': '+str(i*n)+'\n')

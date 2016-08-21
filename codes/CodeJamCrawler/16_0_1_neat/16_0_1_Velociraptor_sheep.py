def sleep(n):
	print n
	m = n
	j = 1
	if (n == '0'):
		return 'INSOMNIA'
	digits = {'0':0,'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0}
	totes = 0
	n = int(n)
	while (totes < 10):
		m = n*j
		j += 1
		for char in str(m):
			if digits[char] == 0:
				totes += 1
				digits[char] = 1
	return m

inputt = open('sheep.txt','r')
outfile = open('output.txt', 'w')
totals = inputt.readline()

i = 1
for line in inputt:
	outputt = sleep(line.strip())
	outfile.write('Case #%s: %s\n' %(i, outputt))
	i += 1

# sleep(1)
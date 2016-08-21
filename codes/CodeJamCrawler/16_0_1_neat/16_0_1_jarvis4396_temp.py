text_file = open("output.txt", "w")
lines = [line.rstrip('\n') for line in open('input.txt')]
t = int(lines[0])
for k in range(1,t+1):
	a = [0 for i in range(0,10)]
	n = int(lines[k])
	if(n == 0):
		text_file.write('Case #' + str(k) + ': INSOMNIA\n')
		continue
	i = 1
	while(1):
		b = str(i*n)
		for j in range(0,len(b)):
			a[ord(b[j])-48] = 1
		if(sum(a) == 10):
			text_file.write('Case #' + str(k) + ': ' + str(i*n) + '\n')
			break
		i = i + 1
text_file.close()
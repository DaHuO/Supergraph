t = input()
for j in range(1, t+1):
	n = input()
	if n == 0:
		print 'Case #'+str(j)+': INSOMNIA'
		continue
	fd = [0]*10
	i = 1
	while 1:
		if sum(fd) == 10:
			print 'Case #'+str(j)+': '+str((i-1)*n)
			break
		s = str(i*n)
		for x in s:
			val = int(x)
			if fd[val] == 0:
				fd[val] = 1
		i = i + 1
	t = t - 1
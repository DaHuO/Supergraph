t = int(raw_input())
for i in range(t):
	n = int(raw_input())
	if n == 0:
		print 'Case #' + str(i+1) + ': INSOMNIA'
		continue;
	var=set()
	z=1
	while True:
		n1 = n * z
		nstr = str(n1)
		var = var | set(nstr)
		var_list=list(var)
		if len(var_list)==10:
			print 'Case #' + str(i+1) + ': ' + nstr
			break
		elif z>500:
			print 'Case #' + str(i+1) + ': INSOMNIA'
			break
		z=z+1

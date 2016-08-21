t = int(raw_input())
for i in range(1,t+1):
	str1 = "Case #"+str(i)+": "
	n = int(raw_input())
	if n == 0:
		str1+="INSOMNIA"
		print str1
		continue
	else:
		j = 1
		d = {}
		while True:
			tmp = n*j
			tmp_s = str(tmp)
			for i in tmp_s:
				d[i] = True
			if len(d) == 10:
				str1+=tmp_s
				print str1
				break
			j+=1

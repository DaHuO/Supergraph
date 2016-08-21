T = long(raw_input())
for re in range (1, T+1):
	n = long(raw_input());
	mark = [False] * 10
	n_mark = 0;
	print "Case #" + str(re) + ": ",

	if n == 0:
		print "INSOMNIA";
	else:
		m = n
		while n_mark < 10:
			sn = str(n)
			for c in sn:
				if not mark[int(c)]:
					mark[int(c)] = True
					n_mark += 1
					if n_mark == 10:
						print n
						break
			n += m
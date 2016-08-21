for cases in range(1, int(input()) + 1):
	n = int(input())
	cur = n
	ans = 'INSOMNIA'
	s = {c for c in str(n)}
	if(s == {'0'}):
		pass
	else:
		while(len(s) < 10):
			cur += n
			s = s.union({c for c in str(cur)})
		else:
			ans = cur
	print('Case #%d:' % (cases,), ans)


t = int(input())
for cc in range(t):
	s = input()
	out = ''

	for x in s:
		if out == '':
			out = x
			continue
		
		if ord(out[0])>ord(x):
			out = out+x
		else:
			out = x+out
	
	print("Case #{}: {}".format(cc+1, out))

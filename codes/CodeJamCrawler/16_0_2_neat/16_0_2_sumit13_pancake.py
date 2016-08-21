t = int(raw_input())

for z in range(t):
	l = raw_input()

	prev = l[0]
	count = 0
	for i in range(1, len(l)):
		if(l[i]!=prev):
			prev = l[i]
			count += 1
	if(l[len(l)-1]=='-'):
		count += 1
	print("Case #{}: {}".format(z+1, count))
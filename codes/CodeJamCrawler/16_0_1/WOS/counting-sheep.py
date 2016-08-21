test = int(input())

for i in range(test):
	n = input()
	l = set(n)
	if int(n) == 0:
		print("Case #{}:".format(i+1),"INSOMNIA")
	else:
		c = 2
		while len(l) < 10:
			t = int(n) * c
			l = l.union(set(str(t)))
			c+=1
		print("Case #{}:".format(i+1),t)
			

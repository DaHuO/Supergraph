with open("input.txt", 'r') as f:
	with open('output.txt', 'w') as o:
		t = int(f.readline())
		for x in range(t):
			a = f.readline()
			a = a.rstrip()
			count = 0
			for i in range(1,len(a)):
				if a[i] == a[i-1]:
					continue
				count += 1
			if a[len(a)-1] == '-':
				count += 1
			o.write("Case #"+str(x+1)+": " + str(count) + "\n")
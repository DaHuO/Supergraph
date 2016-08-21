with open("input.txt", 'r') as f:
	with open('output.txt', 'w') as o:
		t = int(f.readline())
		for x in range(t):
			n = int(f.readline())
			if n==0:
				o.write("Case #"+str(x+1)+": INSOMNIA\n")
			else:
				a = [0]*10
				count = 0
				p = n
				while 1:
					i = str(p)
					for j in i:
						if a[int(j)] == 0:
							# print n
							a[int(j)] = 1
							count += 1
					if count==10:
						break
					p += n
				o.write("Case #"+str(x+1)+": " + str(p) + "\n")
f = open('A-small-attempt2.in', 'r')
o = open("o.txt", "w")
f = f.readlines()[1:]

for t, i in enumerate(f):
	i = int(i)
	A = [1,2,3,4,5,6,7,8,9,0]
	z = 1
	while len(A) > 0 and i != 0:
		j = i*z
		for x in list(str(j)):
			if int(x) in A:
				A.remove(int(x))
			if len(A) == 0:
				o.write("Case #" + str(t+1) + ": " + str(j) + "\n")
				break				
		z += 1
	
	if len(A) > 0:
		o.write("Case #" + str(t+1) + ": INSOMNIA\n")
		
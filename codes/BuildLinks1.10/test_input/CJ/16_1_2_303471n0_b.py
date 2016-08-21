f = open('B-large.in', 'r')
o = open('ob.txt', 'w')
t = f.readline()

for x in range(int(t)):
	n = f.readline()
	arr1 = []
	arr2 = []
	ans = ''
	for y in range((2*int(n)) - 1):
		a = f.readline().rstrip("\n").split(" ")
		for h in a:
			if int(h) not in arr1:				
				arr1.append(int(h))
				arr2.append(1)
			else:
				arr2[arr1.index(int(h))] += 1
	fin = []
	for i, z in enumerate(arr2):
		if z%2 == 1:
			fin.append(arr1[i])
			
	for a in sorted(fin):
		ans = ans + str(a) + " "
		
	o.write("Case #" + str(x+1) + ": " + ans + "\n")
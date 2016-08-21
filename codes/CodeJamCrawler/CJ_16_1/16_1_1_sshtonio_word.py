
nb_entry = int(input())

for i in range(1,nb_entry+1):
	a = raw_input()
	out = "Case #"+str(i)+': '

	 #= a[0]
	bigger = ord(a[0])
	s = a[0]
	for i in a[1:]:
		if ord(i) >= bigger:
			s = i+s
			bigger = ord(i)
		else:
			s += i
	out += s
	print(out)
	
		

	

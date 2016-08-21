
nb_entry = int(input())
for i in range(1,nb_entry+1):
	a = int(input())
	s = "Case #"+str(i)+': '
	if a==0:
		s+="INSOMNIA"
		print(s)
		continue
	l=[]
	n = a
	j=1
	while len(l)<10:
		n = j*a
		for c in str(n):
			if l.count(c)==0:
				l.append(c)
		j +=1
	s += str(n)
	print(s)


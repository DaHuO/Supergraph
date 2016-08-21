
f = open('A-large.in',"r")
g = open("outA.txt","w")
lines = f.readlines()
t = int(lines[0])
for q in range(1,t+1):

	n = int(lines[q])
	arr = ["0","1","2","3","4","5","6","7","8","9"]
	arr2 = []
	res = ""
	if n == 0:
		res = "INSOMNIA"
	else:
		i = 1
		while arr:
			a = n * i
			s = str(a)
			for el in arr:
				if el in s:
					arr2.append(el)
			for el in arr2:
				arr.remove(el)
			arr2 = []	
			i += 1
		res = str(a)			
	s = ("Case #%i: " + res) % (q)
	g.write(s + "\n")
f.close()
g.close()	
			


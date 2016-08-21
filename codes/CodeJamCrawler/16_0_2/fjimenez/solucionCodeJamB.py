archivo = open("B-large.in", "Ur")
num_lines = archivo.readline()
line=0
f = open("resultado.txt", "w")
for dato in archivo.readlines():
	line=line+1
	dato=dato.rstrip('\n')
	i=len(dato)
	c=0
	while(i > 0):
		if dato[i-1]=="-":
			dato=dato[:i].replace("-",'p')
			dato=dato[:i].replace("+",'-')
			dato=dato[:i].replace("p",'+')
			c=c+1
		i=i-1
	#print("Case #%d: %s" % (line,c))	
	f.write("Case #%d: %s" % (line,c)+"\n")
f.close()
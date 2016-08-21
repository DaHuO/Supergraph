archivo = open("A-large.in", "Ur")
num_lines = archivo.readline()
line=0
f = open("resultado.txt", "w")
for dato in archivo.readlines():
	line=line+1
	if dato.rstrip('\n') =='0':
		f.write("Case #%d: %s" % (line,"INSOMNIA")+"\n")	
	else:
		c=0
		vector=[0,0,0,0,0,0,0,0,0,0]
		i=1
		while( c < 10 ):
			dato1=str(int(dato)*i)
			for e in dato1: 
				if vector[int(e)] != 1 : 
					vector[int(e)]=1
					c=c+1		
			i=i+1			
		f.write("Case #%d: %s" % (line,dato1)+"\n")
f.close()
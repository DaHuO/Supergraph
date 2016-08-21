fr = open('/home/rafail/Desktop/code_jam/input4.in', 'r')
fw = open ('/home/rafail/Desktop/code_jam/output4.out', 'w')

t=fr.readline().rstrip()
t = int(t)
for j in range(t):
	line=(fr.readline().rstrip()).split()
	k=int(line[0])
	c=int(line[1])
	s=int(line[2])
	fw.write("Case #"+str(j+1)+": ")
	for i in range(0,s-1):
		fw.write(str(i+1) +" ")
	fw.write(str(s) + "\n")
		
			
fw.close()
fr.close()	

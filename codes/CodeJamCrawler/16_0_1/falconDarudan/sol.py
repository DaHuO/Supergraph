











filer = open("A-large.in","r")
inp = filer.readline()
noc = int(inp)

filwrite = open("output.txt","w")

op = ""
for i in range (1,noc+1):
	inp = int(filer.readline())
	digitcounter = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
	if inp == 0:
		sol = "INSOMNIA"
	else:
		ctr = 0
		mult = 1
		while ctr == 0:
			numstr = str(mult * inp)
			#print numstr
			for p in numstr:
				#print p
				digitcounter[int(p)] += 1
			ctr2 = 0
			#print digitcounter
			for k in range(0,10):
				if digitcounter[k] == 0:
					ctr2+=1
			if ctr2 == 0:
				ctr = 1
			mult+=1
		sol = numstr

	op = op + ("Case #%d: " % i)
	op = op +  sol
	op = op + "\n"

filwrite.write(op)
filer.close()
filwrite.close()

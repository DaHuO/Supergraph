def conversion(strc):
	cvtable=[(0,'ZERO','Z'),(8,'EIGHT','G'),(6,'SIX','X'),(2,'TWO','W'),(4,'FOUR','U'),(1,'ONE','O'),(3,'THREE','H'),(5,'FIVE','F'),(7,'SEVEN','V'),(9,'NINE','I')]
	rst=[]
	slen=len(strc)
	data=[]
	for i in range(slen):
		data.append(strc[i])
	for cvitem in cvtable:
		count=data.count(cvitem[2])
		for i in range(count):
			rst.append(str(cvitem[0]))
		for i in range(count):
			templen=len(cvitem[1])
			for j in range(templen):
				ix=data.index(cvitem[1][j])
				data[ix]='-'
	rst.sort()
	result=''.join(rst)
	return result

def phonenum(inputfile, outputfile):
	fr=open(inputfile,'r')
	T=int(fr.readline())
	print(T,' cases.')
	fw=open(outputfile,'w')
	for j in range(T):
		strc=fr.readline()
		strd=conversion(strc)
		s='Case #'+str(j+1)+': '+strd+'\n'
		fw.write(s)
	fw.close()
	fr.close()
	return

import string

def solveCase(str):
	#print(str)
	if(str == ""):
		return ""
	ret = list()
	#try to find zero
	while(str.find("Z") != -1):
		str = str.replace("Z", "", 1)
		str = str.replace("E", "", 1)
		str = str.replace("R", "", 1)
		str = str.replace("O", "", 1)
		ret.append("0")
		#print (str)
		#print (ret)
	while(str.find("W") != -1):
		str = str.replace("T", "", 1)
		str = str.replace("W", "", 1)
		str = str.replace("O", "", 1)
		ret.append("2")
		#print (str)
		#print (ret)
	while(str.find("U") != -1):
		str = str.replace("F", "", 1)
		str = str.replace("O", "", 1)
		str = str.replace("U", "", 1)
		str = str.replace("R", "", 1)
		ret.append("4")
		#print (str)
		#print (ret)
	while(str.find("F") != -1):
		str = str.replace("F", "", 1)
		str = str.replace("I", "", 1)
		str = str.replace("V", "", 1)
		str = str.replace("E", "", 1)
		ret.append("5")
		#print (str)
		#print (ret)
	while(str.find("X") != -1):
		str = str.replace("S", "", 1)
		str = str.replace("I", "", 1)
		str = str.replace("X", "", 1)
		ret.append("6")
		#print (str)
		#print (ret)
	while(str.find("O") != -1):
		str = str.replace("O", "", 1)
		str = str.replace("N", "", 1)
		str = str.replace("E", "", 1)
		ret.append("1")
		#print (str)
		#print (ret)
	while(str.find("G") != -1):
		str = str.replace("E", "", 1)
		str = str.replace("I", "", 1)
		str = str.replace("G", "", 1)
		str = str.replace("H", "", 1)
		str = str.replace("T", "", 1)
		ret.append("8")
		#print (str)
		#print (ret)
	while(str.find("H") != -1):
		str = str.replace("T", "", 1)
		str = str.replace("H", "", 1)
		str = str.replace("R", "", 1)
		str = str.replace("E", "", 1)
		str = str.replace("E", "", 1)
		ret.append("3")
		#print (str)
		#print (ret)
	while(str.find("V") != -1):
		str = str.replace("S", "", 1)
		str = str.replace("E", "", 1)
		str = str.replace("V", "", 1)
		str = str.replace("E", "", 1)
		str = str.replace("N", "", 1)
		ret.append("7")
		#print (str)
		#print (ret)
	while(str.find("N") != -1):
		str = str.replace("N", "", 1)
		str = str.replace("I", "", 1)
		str = str.replace("N", "", 1)
		str = str.replace("E", "", 1)
		ret.append("9")
		#print (str)
		#print (ret)
	ret.sort()
	#print(ret)
	fout.write("".join(ret) + "\n")

#print("Start")
fin = open('input.txt')
fout = open('output.txt', 'w+')
cases = int(fin.readline())
i = 0
for case in range(0, cases):
	i+=1
	fout.write("Case #" + str(i) + ": ")
	solveCase(fin.readline())
fin.close()
fout.close()
def improveArr(n_str, n_Arr, b_Arr):
	for s in n_str:
		s = int(s)
		if(b_Arr[n_Arr.index(s)] == 0):
			b_Arr[n_Arr.index(s)] = 1
	return b_Arr


def Sheep():
	inFile = open("problemAinp.txt", 'r')
	outFile = open('problemAout.txt','w')
	flag = 0
	i = 0
	for line in inFile:
		numArr = [0,1,2,3,4,5,6,7,8,9]
		boolArr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
		# mult = 1
		line_int = int(line.rstrip())
		if (flag == 0):
			flag = 1
			numInp = line_int
		else:
			if (line_int < 0):
				print "Negative value encountered in input file...\nExiting Program..."
				break;
			if(numInp < i):
				break
			elif(line_int == 0):
				outStr = 'Case #' + str(i) + ': INSOMNIA\n'
				outFile.write(outStr)
			else:	
				mult = 1
				ans_str = ''
				while(True):
					if (0 not in boolArr):
						break;
					ans_str = str(line_int*mult)
					boolArr = improveArr(ans_str, numArr, boolArr)
					mult += 1
				finalAns = ans_str
				outStr = 'Case #' + str(i) + ': '+ ans_str+ '\n'
				outFile.write(outStr)
		i += 1
	outFile.close()
	newOut = open('problemAout_edit.txt', 'w')
	with open('problemAout.txt', 'r') as newIn:
		data = newIn.read()
	newOut.write(data.rstrip())


def main():
	Sheep()


if __name__ == '__main__':
    main();
